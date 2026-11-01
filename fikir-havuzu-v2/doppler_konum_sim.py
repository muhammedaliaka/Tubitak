"""Uydu Doppler'i ile konum (TRANSIT ilkesi) -- SENTETİK uygulanabilirlik testi.

Soru: Kağıthane'den tek bir ucuz alıcıyla (RTL-SDR) alçak yörünge uydusunun Doppler
eğrisi ölçülürse, alıcının konumu ne doğrulukla bulunabilir? Hata bütçesinde
(1) frekans ölçüm gürültüsü, (2) yörünge (TLE) hatası ne kadar pay alır?

Model (BASİTLEŞTİRİLMİŞ; gerçek ölçüm DEĞİLDİR):
  - Küresel Dünya (R = 6371 km), dönme dahil; dairesel yörünge, yükseklik 750 km,
    eğim 45° (Orbcomm benzeri; değerler örnek amaçlı, doğrulanmadı).
  - Ölçüm: Δf(t) = -(f0/c)·dρ/dt + b + d·t + gürültü   (b, d: alıcı osilatör ofseti/kayması)
  - Bilinmeyenler: enlem, boylam, b, d (yükseklik biliniyor kabul edilir).
  - Yörünge hatası: tahmin modeli uyduyu δt kadar ileri/geri konumda sanır
    (yörünge boyu hata ≈ v·δt; TLE hatasının baskın bileşeni olduğu varsayımı).
  - Ölçüm, uydu yükselimi > 15° iken saniyede bir (kentsel ufuk kabulü).
SINIRLAR: İyonosfer, troposfer, Dünya basıklığı, uydu verici frekans kayması,
çok yollu yayılma ve "ayna" belirsizliği (yer izinin hangi tarafındayız) modellenmedi;
ilk tahmin doğru tarafta, gerçeğe ~20 km uzaklıkta başlatıldı.
Çalıştırma: numpy ve scipy gerekir.
"""
import numpy as np
from scipy.optimize import least_squares

R_E = 6371e3
MU = 3.986004418e14
OMEGA_E = 7.2921159e-5
C = 299792458.0
F0 = 137.5e6
H_SAT = 750e3
INC = np.radians(45.0)
LAT0, LON0 = np.radians(41.08), np.radians(28.97)  # Kağıthane (yaklaşık)
ALT0 = 50.0
MASK = np.radians(15.0)
A = R_E + H_SAT
N_MOT = np.sqrt(MU / A**3)
V_SAT = np.sqrt(MU / A)


def rx_ecef(lat, lon, alt=ALT0):
    r = R_E + alt
    return np.array([r * np.cos(lat) * np.cos(lon), r * np.cos(lat) * np.sin(lon), r * np.sin(lat)])


def sat_ecef(t, raan, u0):
    u = u0 + N_MOT * t
    x = A * (np.cos(raan) * np.cos(u) - np.sin(raan) * np.sin(u) * np.cos(INC))
    y = A * (np.sin(raan) * np.cos(u) + np.cos(raan) * np.sin(u) * np.cos(INC))
    z = A * np.sin(u) * np.sin(INC)
    th = OMEGA_E * t
    return np.stack([np.cos(th) * x + np.sin(th) * y, -np.sin(th) * x + np.cos(th) * y, z], axis=-1)


def elevation(t, raan, u0, rr):
    d = sat_ecef(t, raan, u0) - rr
    up = rr / np.linalg.norm(rr)
    return np.arcsin(d @ up / np.linalg.norm(d, axis=-1))


def doppler(t, raan, u0, rr, dt_eph=0.0, h=0.05):
    r1 = np.linalg.norm(sat_ecef(t + dt_eph + h, raan, u0) - rr, axis=-1)
    r0 = np.linalg.norm(sat_ecef(t + dt_eph - h, raan, u0) - rr, axis=-1)
    return -(F0 / C) * (r1 - r0) / (2 * h)


def find_pass(rng):
    rr = rx_ecef(LAT0, LON0)
    while True:
        raan, u0 = rng.uniform(0, 2 * np.pi, 2)
        tc = np.arange(0, 86400, 10.0)
        el = elevation(tc, raan, u0, rr)
        idx = np.where(el > MASK)[0]
        if idx.size < 3:
            continue
        # ilk ardışık geçiş bloğu
        brk = np.where(np.diff(idx) > 1)[0]
        blk = idx[: brk[0] + 1] if brk.size else idx
        t = np.arange(tc[blk[0]] - 10, tc[blk[-1]] + 10, 1.0)
        e = elevation(t, raan, u0, rr)
        t = t[e > MASK]
        if t.size < 60:
            continue
        return raan, u0, t, np.degrees(elevation(t, raan, u0, rr).max())


def hdist(lat1, lon1, lat2, lon2):
    return R_E * np.arccos(np.clip(np.sin(lat1) * np.sin(lat2) + np.cos(lat1) * np.cos(lat2) * np.cos(lon1 - lon2), -1, 1))


def fit_position(passes, rng, est_drift=True):
    """passes: [(raan, u0, t, meas, dt_eph_model)]; kestirim: lat, lon + her geçiş için b (ve d)."""
    k = len(passes)
    m = 2 if est_drift else 1
    ang = rng.uniform(0, 2 * np.pi)
    x0 = [LAT0 + 20e3 / R_E * np.cos(ang), LON0 + 20e3 / (R_E * np.cos(LAT0)) * np.sin(ang)] + [0.0] * (m * k)

    def res(p):
        rr = rx_ecef(p[0], p[1])
        out = []
        for j, (raan, u0, t, meas, dte) in enumerate(passes):
            b = p[2 + m * j]
            d = p[3 + m * j] if est_drift else 0.0
            tt = t - t[0]
            out.append(doppler(t, raan, u0, rr, dte) + b + d * tt - meas)
        return np.concatenate(out)

    scale = [1e-5, 1e-5] + ([10.0, 0.01] if est_drift else [10.0]) * k
    r = least_squares(res, x0, x_scale=scale, method="lm")
    return hdist(r.x[0], r.x[1], LAT0, LON0)


def simulate(rng, sigma_f, sigma_along_m, n_pass, est_drift=True):
    rr = rx_ecef(LAT0, LON0)
    passes, emax = [], []
    for _ in range(n_pass):
        raan, u0, t, em = find_pass(rng)
        b = rng.normal(0, 137.0)       # ~1 ppm alıcı ofseti
        d = rng.normal(0, 0.02) if est_drift else 0.0  # Hz/s kayma (kararlı osilatörde 0 ve biliniyor)
        meas = doppler(t, raan, u0, rr) + b + d * (t - t[0]) + rng.normal(0, sigma_f, t.size)
        dte = rng.normal(0, sigma_along_m / V_SAT) if sigma_along_m > 0 else 0.0
        passes.append((raan, u0, t, meas, dte))
        emax.append(em)
    return fit_position(passes, rng, est_drift), max(emax)


def main(n_trials=150, seed=11, est_drift=True, pass_counts=(1, 3)):
    rng = np.random.default_rng(seed)
    print(f"Kağıthane, uydu {H_SAT/1e3:.0f} km / eğim {np.degrees(INC):.0f}°, f0={F0/1e6:.1f} MHz, "
          f"yükselim maskesi {np.degrees(MASK):.0f}°, {n_trials} rastgele geometri")
    print(f"{'frekans gürültüsü':>18s} | {'yörünge hatası (1σ)':>20s} | {'geçiş':>5s} | "
          f"{'medyan hata (m)':>15s} | {'P90 (m)':>8s}")
    print("Osilatör kayması (d) " + ("BİLİNMİYOR, kestiriliyor" if est_drift else "BİLİNİYOR (kararlı osilatör)"))
    for n_pass in pass_counts:
        for sigma_f in (1.0, 10.0, 50.0):
            for sig_al in (0.0, 1000.0):
                errs = []
                for _ in range(n_trials):
                    try:
                        e, _ = simulate(rng, sigma_f, sig_al, n_pass, est_drift)
                        errs.append(e)
                    except Exception:
                        continue
                errs = np.array(errs)
                print(f"{sigma_f:15.0f} Hz | {sig_al:17.0f} m | {n_pass:5d} | "
                      f"{np.median(errs):15.0f} | {np.percentile(errs, 90):8.0f}")


if __name__ == "__main__":
    main()
    print()
    main(est_drift=False, pass_counts=(1,))
