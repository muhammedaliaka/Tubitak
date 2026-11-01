"""Işık + radyo: aynı uydu geçişinde telefon açıları ve Doppler -- SENTETİK test.

İki soru, tek ISS benzeri geçiş (Kağıthane):
  S1 (yörünge belirleme, konum biliniyor):  Gauss (3 fotoğraf noktası) -> açı EKK -> açı + Doppler
  S2 (konum belirleme, yörünge biliniyor):  yalnız Doppler / yalnız açı / birleşik
Ek: kameranın saat hatası (deklanşör ofseti) bilinmiyorsa radyo bunu düzeltebilir mi? (S1b, S2b)
    aynı akşam iki geçiş yörüngeyi ne kadar iyileştirir? (S1c)
    konumu bilinen bir istasyon (okul) TLE hatasını ölçüp ikinci istasyona verirse? (S3, diferansiyel)

Model (BASİTLEŞTİRİLMİŞ; gerçek ölçüm DEĞİLDİR):
  - Küresel Dünya (R = 6371 km), dönme dahil, iki cisim. Gerçek yörünge dairesel,
    420 km / 51,6° (ISS benzeri). Hava sürtünmesi, J2, ışık zamanı, sapınç, kırılma YOK.
  - Gözlem: yükselim > 15° (kentsel ufuk). Uydunun gölgeye girmesi modellenmedi
    (geçişin tamamı görünür kabul edildi; gerçekte çoğu geçişin bir kısmı görünür).
  - Optik: N_FRAME uzun pozlama, her biri 2 iz ucu (açılış/kapanış anı). Her uç için
    açısal gürültü SIG_TH (iki eksen) ve zaman gürültüsü SIG_T. İsteğe bağlı ortak
    kamera saati ofseti (bütün fotoğraflara aynı).
  - Radyo: f0 = 437,8 MHz (ISS'in Ekim 2026 indirme frekansı), geçiş boyunca N_DOP
    rastgele anda frekans ölçümü, gürültü SIG_F; verici + alıcı ofseti b bilinmiyor.
    Radyo zaman damgası dizüstünün (NTP) saatinden; hatası ihmal edildi.
SINIRLAR: Veriyi üreten ve çözen model aynıdır ("inverse crime"); sonuçlar yalnızca
"ilke olarak işe yarar mı ve hangi hata baskın?" sorusunu yanıtlar.
Çalıştırma: numpy ve scipy gerekir. Süre: birkaç dakika.
"""
import numpy as np
from scipy.optimize import least_squares

MU = 398600.4418            # km^3/s^2
R_E = 6371.0                # km
OMEGA_E = 7.2921159e-5      # rad/s
C_KMS = 299792.458          # km/s
F0 = 437.8e6                # Hz
H_SAT, INC = 420.0, np.radians(51.6)
A_SAT = R_E + H_SAT
N_MOT = np.sqrt(MU / A_SAT**3)
V_SAT = np.sqrt(MU / A_SAT)
T_ORB = 2 * np.pi / N_MOT
LAT0, LON0, ALT0 = np.radians(41.08), np.radians(28.97), 0.08   # Kağıthane (yaklaşık)
MASK = np.radians(15.0)
N_FRAME, T_EXP = 10, 4.0    # 10 fotoğraf x 4 s pozlama -> 20 iz ucu
N_DOP = 30                  # geçiş başına frekans ölçümü (aralıklı ses/paket)
B_SIG = 500.0               # Hz, verici + alıcı frekans ofseti (bilinmiyor)


# ---------------------------------------------------------------- geometri
def ecef(lat, lon, alt=ALT0):
    r = R_E + alt
    return np.array([r * np.cos(lat) * np.cos(lon), r * np.cos(lat) * np.sin(lon), r * np.sin(lat)])


def obs_eci(t, lat=LAT0, lon=LON0):
    """Gözlemcinin ECI konumu ve hızı (t=0'da ECI ile ECEF çakışık)."""
    p = ecef(lat, lon)
    th = OMEGA_E * np.atleast_1d(t)
    c, s = np.cos(th), np.sin(th)
    r = np.stack([c * p[0] - s * p[1], s * p[0] + c * p[1], np.full_like(th, p[2])], axis=-1)
    v = np.stack([-OMEGA_E * r[:, 1], OMEGA_E * r[:, 0], np.zeros_like(th)], axis=-1)
    return r, v


def sat_true(t, raan, u0):
    """Gerçek (dairesel) yörünge, ECI konum ve hız."""
    t = np.atleast_1d(t)
    u = u0 + N_MOT * t
    P = np.array([np.cos(raan), np.sin(raan), 0.0])
    Q = np.array([-np.sin(raan) * np.cos(INC), np.cos(raan) * np.cos(INC), np.sin(INC)])
    r = A_SAT * (np.cos(u)[:, None] * P + np.sin(u)[:, None] * Q)
    v = V_SAT * (-np.sin(u)[:, None] * P + np.cos(u)[:, None] * Q)
    return r, v


def elevation(rs, ro):
    d = rs - ro
    up = ro / np.linalg.norm(ro, axis=-1, keepdims=True)
    return np.arcsin(np.sum(d * up, axis=-1) / np.linalg.norm(d, axis=-1))


# ---------------------------------------------------------------- iki cisim yayılımı
def _stumpff(z):
    C = np.empty_like(z)
    S = np.empty_like(z)
    p, n, o = z > 1e-8, z < -1e-8, np.abs(z) <= 1e-8
    sp, sn = np.sqrt(z[p]), np.sqrt(-z[n])
    C[p], S[p] = (1 - np.cos(sp)) / z[p], (sp - np.sin(sp)) / sp**3
    C[n], S[n] = (np.cosh(sn) - 1) / (-z[n]), (np.sinh(sn) - sn) / sn**3
    C[o], S[o] = 0.5, 1.0 / 6.0
    return C, S


def propagate(R0, V0, dt):
    """Evrensel değişkenle Kepler yayılımı (Curtis, Alg. 3.3–3.4), dt dizisi için."""
    dt = np.atleast_1d(np.asarray(dt, float))
    r0, v0 = np.linalg.norm(R0), np.linalg.norm(V0)
    vr0 = R0 @ V0 / r0
    alpha = 2 / r0 - v0**2 / MU
    sm = np.sqrt(MU)
    x = sm * abs(alpha) * dt
    for _ in range(30):
        z = alpha * x**2
        C, S = _stumpff(z)
        F = r0 * vr0 / sm * x**2 * C + (1 - alpha * r0) * x**3 * S + r0 * x - sm * dt
        dF = r0 * vr0 / sm * x * (1 - alpha * x**2 * S) + (1 - alpha * r0) * x**2 * C + r0
        step = F / dF
        x = x - step
        if np.max(np.abs(step)) < 1e-10:
            break
    z = alpha * x**2
    C, S = _stumpff(z)
    f = 1 - x**2 / r0 * C
    g = dt - x**3 * S / sm
    R = f[:, None] * R0 + g[:, None] * V0
    r = np.linalg.norm(R, axis=-1)
    fd = sm / (r * r0) * (alpha * x**3 * S - x)
    gd = 1 - x**2 / r * C
    V = fd[:, None] * R0 + gd[:, None] * V0
    return R, V


# ---------------------------------------------------------------- ölçüm modelleri
def los(rs, ro):
    d = rs - ro
    return d / np.linalg.norm(d, axis=-1, keepdims=True)


def doppler(rs, vs, ro, vo):
    d, dv = rs - ro, vs - vo
    rdot = np.sum(d * dv, axis=-1) / np.linalg.norm(d, axis=-1)
    return -(F0 / C_KMS) * rdot


def perp_basis(L):
    ref = np.where(np.abs(L[:, 2:3]) < 0.9, np.array([[0, 0, 1.0]]), np.array([[1.0, 0, 0]]))
    e1 = np.cross(L, ref)
    e1 /= np.linalg.norm(e1, axis=-1, keepdims=True)
    return e1, np.cross(L, e1)


def find_pass(rng, min_len=150.0):
    while True:
        raan, u0 = rng.uniform(0, 2 * np.pi, 2)
        tc = np.arange(0, 86400, 10.0)
        el = elevation(sat_true(tc, raan, u0)[0], obs_eci(tc)[0])
        idx = np.where(el > MASK)[0]
        if idx.size < 3:
            continue
        brk = np.where(np.diff(idx) > 1)[0]
        blk = idx[: brk[0] + 1] if brk.size else idx
        t = np.arange(tc[blk[0]] - 10, tc[blk[-1]] + 10, 0.5)
        e = elevation(sat_true(t, raan, u0)[0], obs_eci(t)[0])
        t = t[e > MASK]
        if t[-1] - t[0] >= min_len:
            return raan, u0, t[0], t[-1]


def make_obs(rng, raan, u0, t_a, t_b, sig_th, sig_t, clock_bias=0.0, sig_f=10.0, lat=LAT0, lon=LON0):
    """Sentetik optik ve radyo ölçümleri (gerçek yörüngeden), (lat, lon) gözlemcisi için."""
    starts = np.linspace(t_a, t_b - T_EXP, N_FRAME)
    t_nom = np.sort(np.concatenate([starts, starts + T_EXP]))
    t_tru = t_nom + clock_bias + rng.normal(0, sig_t, t_nom.size)   # gerçek çekim anı
    L = los(sat_true(t_tru, raan, u0)[0], obs_eci(t_tru, lat, lon)[0])
    e1, e2 = perp_basis(L)
    n = rng.normal(0, np.radians(sig_th), (t_nom.size, 2))
    Lm = L + n[:, :1] * e1 + n[:, 1:] * e2
    Lm /= np.linalg.norm(Lm, axis=-1, keepdims=True)
    # açısal hız (yalnız ölçümden) -> zaman gürültüsünün açı karşılığı, ağırlık için
    ang = np.arccos(np.clip(np.sum(Lm[1:] * Lm[:-1], axis=-1), -1, 1)) / np.diff(t_nom)
    rate = np.concatenate([ang[:1], 0.5 * (ang[1:] + ang[:-1]), ang[-1:]])
    sig_eff = np.sqrt(np.radians(sig_th)**2 + (rate * sig_t)**2)
    t_d = np.sort(rng.uniform(t_a, t_b, N_DOP))
    rs, vs = sat_true(t_d, raan, u0)
    ro, vo = obs_eci(t_d, lat, lon)
    b = rng.normal(0, B_SIG)
    f_m = doppler(rs, vs, ro, vo) + b + rng.normal(0, sig_f, t_d.size)
    return dict(t_nom=t_nom, Lm=Lm, sig_eff=sig_eff, t_d=t_d, f_m=f_m, sig_f=sig_f,
                grp=np.zeros(t_d.size, int))   # grp: Doppler ölçümünün geçiş numarası (her geçişe ayrı b)


def ang_res(L_model, Lm, sig):
    e1, e2 = perp_basis(Lm)
    d = L_model - Lm
    return np.concatenate([np.sum(d * e1, -1) / sig, np.sum(d * e2, -1) / sig])


# ---------------------------------------------------------------- Gauss yöntemi
def gauss_iod(t, Lhat, R):
    """Curtis Alg. 5.5 (f, g serisiyle). t: 3 an, Lhat/R: 3x3. Dönüş: [(r2, v2), ...]."""
    tau1, tau3 = t[0] - t[1], t[2] - t[1]
    tau = tau3 - tau1
    p1, p2, p3 = np.cross(Lhat[1], Lhat[2]), np.cross(Lhat[0], Lhat[2]), np.cross(Lhat[0], Lhat[1])
    D0 = Lhat[0] @ p1
    D = np.array([[R[i] @ p for p in (p1, p2, p3)] for i in range(3)])
    A = (-D[0, 1] * tau3 / tau + D[1, 1] + D[2, 1] * tau1 / tau) / D0
    B = (D[0, 1] * (tau3**2 - tau**2) * tau3 / tau + D[2, 1] * (tau**2 - tau1**2) * tau1 / tau) / (6 * D0)
    E = R[1] @ Lhat[1]
    a = -(A**2 + 2 * A * E + R[1] @ R[1])
    b = -2 * MU * B * (A + E)
    c = -MU**2 * B**2
    roots = np.roots([1, 0, a, 0, 0, b, 0, 0, c])
    out = []
    for x in roots:
        if abs(x.imag) > 1e-6 or not (6500.0 < x.real < 8000.0):
            continue
        r2 = x.real
        rho1 = ((6 * (D[2, 0] * tau1 / tau3 + D[1, 0] * tau / tau3) * r2**3
                 + MU * D[2, 0] * (tau**2 - tau1**2) * tau1 / tau3)
                / (6 * r2**3 + MU * (tau**2 - tau3**2)) - D[0, 0]) / D0
        rho2 = A + MU * B / r2**3
        rho3 = ((6 * (D[0, 2] * tau3 / tau1 - D[1, 2] * tau / tau1) * r2**3
                 + MU * D[0, 2] * (tau**2 - tau3**2) * tau3 / tau1)
                / (6 * r2**3 + MU * (tau**2 - tau1**2)) - D[2, 2]) / D0
        r1v, r2v, r3v = R[0] + rho1 * Lhat[0], R[1] + rho2 * Lhat[1], R[2] + rho3 * Lhat[2]
        f1, f3 = 1 - MU * tau1**2 / (2 * r2**3), 1 - MU * tau3**2 / (2 * r2**3)
        g1, g3 = tau1 - MU * tau1**3 / (6 * r2**3), tau3 - MU * tau3**3 / (6 * r2**3)
        v2 = (-f3 * r1v + f1 * r3v) / (f1 * g3 - f3 * g1)
        out.append((r2v, v2))
    return out


# ---------------------------------------------------------------- S1: yörünge belirleme
def od_fit(ob, t_ep, x0, use_ang=True, use_dop=False, est_clock=False):
    ro_a = obs_eci(ob["t_nom"])[0]
    ro_d, vo_d = obs_eci(ob["t_d"])

    nb = int(ob["grp"].max()) + 1 if use_dop else 0

    def res(p):
        R0, V0 = p[:3], p[3:6]
        b = p[6:6 + nb][ob["grp"]] if use_dop else 0.0
        cb = p[6 + nb] if est_clock else 0.0
        out = []
        if use_ang:
            t_a = ob["t_nom"] + cb
            ro = obs_eci(t_a)[0] if est_clock else ro_a
            out.append(ang_res(los(propagate(R0, V0, t_a - t_ep)[0], ro), ob["Lm"], ob["sig_eff"]))
        if use_dop:
            rs, vs = propagate(R0, V0, ob["t_d"] - t_ep)
            out.append((doppler(rs, vs, ro_d, vo_d) + b - ob["f_m"]) / ob["sig_f"])
        return np.concatenate(out)

    p0 = list(x0) + [np.median(ob["f_m"])] * nb + ([0.0] if est_clock else [])
    scale = [1.0] * 3 + [1e-3] * 3 + [10.0] * nb + ([0.01] if est_clock else [])
    r = least_squares(res, p0, x_scale=scale, method="lm", max_nfev=4000)
    return r.x[:3], r.x[3:6], r.x[6:]


def od_errors(R0, V0, t_ep, raan, u0):
    """Epokta konum hatası (km) ve bir tur sonraki yörünge boyu zaman hatası (s)."""
    rt, vt = sat_true(np.array([t_ep, t_ep + T_ORB]), raan, u0)
    Re, _ = propagate(R0, V0, np.array([0.0, T_ORB]))
    e_ep = np.linalg.norm(Re[0] - rt[0])
    along = (Re[1] - rt[1]) @ (vt[1] / np.linalg.norm(vt[1]))
    return e_ep, abs(along) / V_SAT


def sub_obs(ob, idx):
    """Yalnız seçili iz uçlarını içeren ölçüm kümesi (Doppler aynen kalır)."""
    o = dict(ob)
    for k in ("t_nom", "Lm", "sig_eff"):
        o[k] = ob[k][idx]
    return o


def merge_obs(o1, o2):
    o = {k: (np.concatenate([o1[k], o2[k]]) if k != "sig_f" else o1[k]) for k in o1}
    o["grp"] = np.concatenate([o1["grp"], o2["grp"] + o1["grp"].max() + 1])
    return o


def gauss_init(ob):
    """Üç iz ucuyla (ilk, orta, son) Gauss; birden çok kök varsa bütün açılara en iyi uyan."""
    n = ob["t_nom"].size
    i3 = np.array([0, n // 2, n - 1])
    t3 = ob["t_nom"][i3]
    sols = gauss_iod(t3, ob["Lm"][i3], obs_eci(t3)[0])
    if not sols:
        return None
    t_ep = t3[1]
    ro_a = obs_eci(ob["t_nom"])[0]
    cost = [np.sum(ang_res(los(propagate(r2, v2, ob["t_nom"] - t_ep)[0], ro_a), ob["Lm"], ob["sig_eff"])**2)
            for r2, v2 in sols]
    r2, v2 = sols[int(np.argmin(cost))]
    return r2, v2, t_ep, i3


def run_od(rng, n_trials, sig_th, sig_t, sig_f, clock_sig=0.0):
    keys = ("gauss", "3nokta", "aci", "aci+dop") + (("aci+dop+saat",) if clock_sig > 0 else ())
    res = {k: [] for k in keys}
    clk = []
    fail = 0
    for _ in range(n_trials):
        raan, u0, t_a, t_b = find_pass(rng)
        cb = rng.normal(0, clock_sig) if clock_sig > 0 else 0.0
        ob = make_obs(rng, raan, u0, t_a, t_b, sig_th, sig_t, cb, sig_f)
        g = gauss_init(ob)
        if g is None:
            fail += 1
            continue
        r2, v2, t_ep, i3 = g
        x0 = np.concatenate([r2, v2])
        try:
            out = {"gauss": od_errors(r2, v2, t_ep, raan, u0),
                   "3nokta": od_errors(*od_fit(sub_obs(ob, i3), t_ep, x0)[:2], t_ep, raan, u0),
                   "aci": od_errors(*od_fit(ob, t_ep, x0)[:2], t_ep, raan, u0),
                   "aci+dop": od_errors(*od_fit(ob, t_ep, x0, use_dop=True)[:2], t_ep, raan, u0)}
            if clock_sig > 0:
                R0, V0, ex = od_fit(ob, t_ep, x0, use_dop=True, est_clock=True)
                out["aci+dop+saat"] = od_errors(R0, V0, t_ep, raan, u0)
                clk.append(abs(ex[-1] - cb) * 1000)   # ms
        except Exception:
            fail += 1
            continue
        for k, v in out.items():
            res[k].append(v)
    return res, fail, clk


def find_two_passes(rng, min_len=120.0):
    """Ardışık iki geçiş (yaklaşık bir tur arayla), ikisi de maskenin üstünde >= min_len s."""
    while True:
        raan, u0, t_a, t_b = find_pass(rng, min_len)
        tc = np.arange(t_b + 0.5 * T_ORB, t_b + 1.5 * T_ORB, 5.0)
        el = elevation(sat_true(tc, raan, u0)[0], obs_eci(tc)[0])
        idx = np.where(el > MASK)[0]
        if idx.size and tc[idx[-1]] - tc[idx[0]] >= min_len and np.all(np.diff(idx) == 1):
            return raan, u0, (t_a, t_b), (tc[idx[0]], tc[idx[-1]])


def run_od_two(rng, n_trials, sig_th, sig_t, sig_f):
    """Aynı akşam iki geçiş: ölçümler birleştirilir; öngörü ikinci geçişten bir tur sonrası için."""
    res = {k: [] for k in ("tek_aci", "iki_aci", "iki_aci+dop")}
    for _ in range(n_trials):
        raan, u0, p1, p2 = find_two_passes(rng)
        o1 = make_obs(rng, raan, u0, *p1, sig_th, sig_t, 0.0, sig_f)
        o2 = make_obs(rng, raan, u0, *p2, sig_th, sig_t, 0.0, sig_f)
        g = gauss_init(o1)
        if g is None:
            continue
        r2, v2, t_ep, _ = g
        x0 = np.concatenate([r2, v2])
        both = merge_obs(o1, o2)
        t_pred = 0.5 * (p2[0] + p2[1]) + T_ORB - t_ep     # ikinci geçişten bir tur sonra
        try:
            for k, ob, ud in (("tek_aci", o1, False), ("iki_aci", both, False), ("iki_aci+dop", both, True)):
                R1, V1, _ = od_fit(o1, t_ep, x0, use_dop=ud)              # önce ilk geçiş
                R0, V0, _ = od_fit(ob, t_ep, np.concatenate([R1, V1]), use_dop=ud)
                rt, vt = sat_true(np.array([t_ep + t_pred]), raan, u0)
                Re, _ = propagate(R0, V0, np.array([t_pred]))
                res[k].append(abs((Re[0] - rt[0]) @ (vt[0] / V_SAT)) / V_SAT)
        except Exception:
            continue
    return res


# ---------------------------------------------------------------- S2: konum belirleme
def hdist_m(la, lo, la0, lo0):
    return 1000 * R_E * np.arccos(np.clip(np.sin(la) * np.sin(la0) + np.cos(la) * np.cos(la0)
                                          * np.cos(lo - lo0), -1, 1))


def pos_fit(ob, raan, u0, dt_eph, rng, use_ang, use_dop, est_clock=False, lat_t=LAT0, lon_t=LON0):
    """Yörünge modeli: sat_true(t + dt_eph) (dt_eph = TLE'nin yörünge boyu zaman hatası)."""
    ang0 = rng.uniform(0, 2 * np.pi)
    x0 = [lat_t + 20 / R_E * np.cos(ang0), lon_t + 20 / (R_E * np.cos(lat_t)) * np.sin(ang0)]

    def res(p):
        k = 2
        b = 0.0
        if use_dop:
            b = p[k]
            k += 1
        cb = p[k] if est_clock else 0.0
        out = []
        if use_ang:
            t_a = ob["t_nom"] + cb
            ro = obs_eci(t_a, p[0], p[1])[0]
            out.append(ang_res(los(sat_true(t_a + dt_eph, raan, u0)[0], ro), ob["Lm"], ob["sig_eff"]))
        if use_dop:
            rs, vs = sat_true(ob["t_d"] + dt_eph, raan, u0)
            ro, vo = obs_eci(ob["t_d"], p[0], p[1])
            out.append((doppler(rs, vs, ro, vo) + b - ob["f_m"]) / ob["sig_f"])
        return np.concatenate(out)

    p0 = x0 + ([np.median(ob["f_m"])] if use_dop else []) + ([0.0] if est_clock else [])
    scale = [1e-5, 1e-5] + ([10.0] if use_dop else []) + ([0.01] if est_clock else [])
    r = least_squares(res, p0, x_scale=scale, method="lm", max_nfev=4000)
    return hdist_m(r.x[0], r.x[1], lat_t, lon_t)


def eph_fit(ob, raan, u0, dt_eph, est_clock=True):
    """Konumu bilinen istasyon: TLE'nin yörünge boyu zaman hatasını (δ), b'yi ve (istenirse) kamera saatini kestirir."""
    ro_d, vo_d = obs_eci(ob["t_d"])

    def res(p):
        d, b = p[0], p[1]
        cb = p[2] if est_clock else 0.0
        t_a = ob["t_nom"] + cb
        a = ang_res(los(sat_true(t_a + dt_eph - d, raan, u0)[0], obs_eci(t_a)[0]), ob["Lm"], ob["sig_eff"])
        rs, vs = sat_true(ob["t_d"] + dt_eph - d, raan, u0)
        return np.concatenate([a, (doppler(rs, vs, ro_d, vo_d) + b - ob["f_m"]) / ob["sig_f"]])

    p0 = [0.0, np.median(ob["f_m"])] + ([0.0] if est_clock else [])
    r = least_squares(res, p0, x_scale=[0.01, 10.0] + ([0.01] if est_clock else []), method="lm")
    return r.x[0]


def run_pos(rng, n_trials, sig_th, sig_t, sig_f, sig_al_km, clock_sig=0.0):
    keys = ("dop", "aci", "birlesik") + (("birlesik+saat",) if clock_sig > 0 else ())
    res = {k: [] for k in keys}
    for _ in range(n_trials):
        raan, u0, t_a, t_b = find_pass(rng)
        cb = rng.normal(0, clock_sig) if clock_sig > 0 else 0.0
        ob = make_obs(rng, raan, u0, t_a, t_b, sig_th, sig_t, cb, sig_f)
        dte = rng.normal(0, sig_al_km / V_SAT) if sig_al_km > 0 else 0.0   # TLE yörünge boyu hatası
        try:
            out = {"dop": pos_fit(ob, raan, u0, dte, rng, False, True),
                   "aci": pos_fit(ob, raan, u0, dte, rng, True, False),
                   "birlesik": pos_fit(ob, raan, u0, dte, rng, True, True)}
            if clock_sig > 0:
                out["birlesik+saat"] = pos_fit(ob, raan, u0, dte, rng, True, True, est_clock=True)
        except Exception:
            continue
        for k, v in out.items():
            res[k].append(v)
    return res


def run_diff(rng, n_trials, sig_th, sig_t, sig_f, sig_al_km, clock_sig, base_km):
    """Diferansiyel: A (okul, konumu biliniyor) TLE hatasını ölçer; B (base_km uzakta) düzeltilmiş yörüngeyle konum bulur."""
    res = {"B_tle": [], "B_duzeltilmis": [], "delta_hata_ms": []}
    for _ in range(n_trials):
        raan, u0, t_a, t_b = find_pass(rng)
        az = rng.uniform(0, 2 * np.pi)
        latB = LAT0 + base_km / R_E * np.cos(az)
        lonB = LON0 + base_km / (R_E * np.cos(LAT0)) * np.sin(az)
        dte = rng.normal(0, sig_al_km / V_SAT)
        ec = clock_sig > 0
        oA = make_obs(rng, raan, u0, t_a, t_b, sig_th, sig_t, rng.normal(0, clock_sig) if ec else 0.0, sig_f)
        oB = make_obs(rng, raan, u0, t_a, t_b, sig_th, sig_t, rng.normal(0, clock_sig) if ec else 0.0, sig_f,
                      latB, lonB)
        try:
            d_est = eph_fit(oA, raan, u0, dte, ec)
            res["B_tle"].append(pos_fit(oB, raan, u0, dte, rng, True, True, ec, latB, lonB))
            res["B_duzeltilmis"].append(pos_fit(oB, raan, u0, dte - d_est, rng, True, True, ec, latB, lonB))
            res["delta_hata_ms"].append(abs(d_est - dte) * 1000)
        except Exception:
            continue
    return res


def q(v, fmt="{:.1f}"):
    v = np.asarray(v)
    return (fmt + " / " + fmt).format(np.median(v), np.percentile(v, 90)) if v.size else "-"


def main(n_trials=150, seed=7):
    rng = np.random.default_rng(seed)
    print(f"ISS benzeri yörünge {H_SAT:.0f} km / {np.degrees(INC):.1f}°, f0 = {F0/1e6:.1f} MHz, maske "
          f"{np.degrees(MASK):.0f}°, {N_FRAME} fotoğraf x {T_EXP:.0f} s ({2*N_FRAME} iz ucu), "
          f"{N_DOP} Doppler ölçümü, {n_trials} rastgele geçiş. Değerler: medyan / P90.")

    print("\nS1 — YÖRÜNGE BELİRLEME (gözlemci konumu biliniyor)")
    print("Hücre: epok konum hatası (km) ; bir tur (~93 dk) sonraki zamanlama hatası (s)")
    cols = ("gauss", "3nokta", "aci", "aci+dop")
    print("açı / zaman | Doppler | " + " | ".join(("Gauss ham (3 nokta)", "3 nokta iyileştirilmiş",
                                                     "açı EKK (20 nokta)", "açı + Doppler")))
    for sig_th, sig_t in ((0.02, 0.02), (0.05, 0.05), (0.1, 0.1)):
        for sig_f in (10.0, 50.0):
            r, fail, _ = run_od(rng, n_trials, sig_th, sig_t, sig_f)
            cells = [f"{q(np.array(r[k])[:, 0])} ; {q(np.array(r[k])[:, 1], '{:.0f}')}" for k in cols]
            print(f"{sig_th:.2f}° / {sig_t:.2f} s | {sig_f:.0f} Hz | " + " | ".join(cells)
                  + (f"  (başarısız {fail})" if fail else ""))

    print("\nS1b — KAMERA SAATİ OFSETİ bilinmiyor (σ = 0,3 s), açı 0,05° / 0,05 s, Doppler 10 Hz")
    r, fail, clk = run_od(rng, n_trials, 0.05, 0.05, 10.0, clock_sig=0.3)
    for k in ("gauss", "3nokta", "aci", "aci+dop", "aci+dop+saat"):
        a = np.array(r[k])
        print(f"  {k:>14s}: epok {q(a[:, 0])} km ; bir tur sonra {q(a[:, 1], '{:.0f}')} s")
    print(f"  kamera saati ofsetinin kestirim hatası (açı + Doppler): {q(clk, '{:.0f}')} ms")

    print("\nS1c — AYNI AKŞAM İKİ GEÇİŞ (~93 dk arayla); ikinci geçişten bir tur sonraki zamanlama hatası (s)")
    for sig_th, sig_t in ((0.05, 0.05), (0.1, 0.1)):
        r = run_od_two(rng, n_trials, sig_th, sig_t, 10.0)
        bad = {k: np.mean(np.array(v) > 60) * 100 for k, v in r.items()}
        print(f"  açı {sig_th:.2f}° / {sig_t:.2f} s, Doppler 10 Hz: tek geçiş açı {q(r['tek_aci'], '{:.1f}')} | "
              f"iki geçiş açı {q(r['iki_aci'], '{:.2f}')} (>60 s: %{bad['iki_aci']:.0f}) | "
              f"iki geçiş açı + Doppler {q(r['iki_aci+dop'], '{:.2f}')} (>60 s: %{bad['iki_aci+dop']:.0f})")

    print("\nS2 — KONUM BELİRLEME (yörünge TLE'den biliniyor, kamera saati kalibre), yatay hata (m)")
    print("TLE hatası | açı/zaman | Doppler | yalnız Doppler | yalnız açı | birleşik")
    for sig_al in (0.0, 1.0):
        for sig_th, sig_t in ((0.02, 0.02), (0.1, 0.1)):
            for sig_f in (10.0, 50.0):
                r = run_pos(rng, n_trials, sig_th, sig_t, sig_f, sig_al)
                print(f"{sig_al:.0f} km | {sig_th:.2f}°/{sig_t:.2f} s | {sig_f:.0f} Hz | "
                      + " | ".join(q(r[k], '{:.0f}') for k in ("dop", "aci", "birlesik")))

    print("\nS2b — KAMERA SAATİ OFSETİ bilinmiyor (σ = 0,3 s), TLE hatası 1 km, açı 0,05°/0,05 s, Doppler 10 Hz")
    r = run_pos(rng, n_trials, 0.05, 0.05, 10.0, 1.0, clock_sig=0.3)
    for k in ("dop", "aci", "birlesik", "birlesik+saat"):
        print(f"  {k:>14s}: {q(r[k], '{:.0f}')} m")

    print("\nS3 — DİFERANSİYEL: A (konumu bilinen okul) TLE hatasını ölçer, B aynı geçişte konum bulur")
    print("     (TLE hatası 1 km, Doppler 10 Hz, her iki istasyonda birleşik çözüm)")
    for clk_sig in (0.0, 0.3):
        print(f"  kamera saati: {'kalibre (ofset yok)' if clk_sig == 0 else 'ofset σ 0,3 s, kestiriliyor'}")
        for base, sig_th, sig_t in ((3.0, 0.05, 0.05), (3.0, 0.1, 0.1), (10.0, 0.05, 0.05)):
            r = run_diff(rng, n_trials, sig_th, sig_t, 10.0, 1.0, clk_sig, base)
            print(f"  A–B {base:4.0f} km, açı {sig_th:.2f}°/{sig_t:.2f} s: B, TLE ile {q(r['B_tle'], '{:.0f}')} m | "
                  f"B, A'nın düzeltmesiyle {q(r['B_duzeltilmis'], '{:.0f}')} m | "
                  f"A'nın TLE zaman hatası kestirimi {q(r['delta_hata_ms'], '{:.0f}')} ms")


if __name__ == "__main__":
    main()
