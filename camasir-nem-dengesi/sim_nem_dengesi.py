"""Çamaşır–Nem Dengesi: ILLÜSTRATİF fizik modeli.

AMAÇ: Bir yük asılı çamaşırın oda havasını nasıl nemlendirdiğini ve
havalandırma stratejilerinin kuruma süresi, iç nem, soğuk yüzey yoğuşması ve
ısı kaybı üzerindeki etkisini BÜYÜKLÜK mertebesi olarak göstermek.

BU BİR MODELDİR, ÖLÇÜM DEĞİLDİR. Aşağıdaki parametrelerin çoğu VARSAYIMDIR
(ALPHA, BETA, G_OTHER, F_RSI, dış hava nemi). Proje boyunca gerçek ölçümlerle
uydurulacaktır. Dış sıcaklıklar MGM 1991-2020 Ocak BÖLGE normalleridir; il
bazlı değildir; dış hava nemi varsayımdır.

Fizik:
  1) Kuruma: E = ALPHA * (T_hava - T_yaş_termometre)   [kg/h]
     (Lewis ilişkisi: h_c*A/h_fg ile ölçeklenir) ; azalan hız döneminde
     kalan suyla orantılı olarak düşer.
  2) Oda nem dengesi (iyi karışmış hava + yüzey tamponlama):
     (1+BETA) * rho * V * dw/dt = E + G_other + ACH*rho*V*(w_dış - w) - nem_alıcı
  3) Yüzey: T_si = T_dış + f_Rsi*(T_iç - T_dış);  RH_yüzey = p_v / p_sat(T_si)
     (ISO 13788 yaklaşımı: RH_yüzey >= %80 küf riski ölçütü, %100 yoğuşma)
"""
import math

P_ATM = 101325.0
RHO_A = 1.2  # kg/m3

# --- Varsayım parametreleri (ölçümle uydurulacak) -----------------------------
ALPHA = 0.055  # kg/(h*K): h_c ~6 W/m2K, A ~6 m2 kabulü ile h_c*A/h_fg
BETA = 4.0  # yüzey/eşya nem tamponu çarpanı (depolama kapasitesi (1+BETA)*hava)
G_OTHER = 0.05  # kg/h: yaşayanlar vb. taban nem üretimi
X_CRIT = 0.15  # kg su / kg kuru (azalan hız dönemi başlangıcı) -- varsayım
X_EQ = 0.07  # denge nemi (pamuk, ~%50 BN) -- varsayım
F_RSI = {"yalıtımsız köşe (f=0.65)": 0.65, "yalıtımlı duvar (f=0.80)": 0.80}


def psat(T):
    return 610.94 * math.exp(17.625 * T / (T + 243.04))


def w_from_pv(pv):
    return 0.622 * pv / (P_ATM - pv)


def pv_from_w(w):
    return P_ATM * w / (0.622 + w)


def rh_air(T, w):
    return pv_from_w(w) / psat(T)


def w_from_rh(T, rh):
    return w_from_pv(rh * psat(T))


def wet_bulb(T, rh_frac):
    rh = max(5.0, min(99.0, rh_frac * 100.0))
    return (
        T * math.atan(0.151977 * math.sqrt(rh + 8.313659))
        + math.atan(T + rh)
        - math.atan(rh - 1.676331)
        + 0.00391838 * rh ** 1.5 * math.atan(0.023101 * rh)
        - 4.686035
    )


def simulate(T_in, T_out, RH_out, ach_fn, V=30.0, dry_mass=5.0, RMC=0.52,
             dehum_kg_h=0.0, hours=24, dt_min=1.0):
    dt_h = dt_min / 60.0
    m_dry_air = RHO_A * V
    m0 = dry_mass * RMC
    m_eq = dry_mass * X_EQ
    m_c = dry_mass * X_CRIT
    w_out = w_from_rh(T_out, RH_out)

    # Taban (çamaşırsız) başlangıç: ACH 0.3'te kararlı hal
    ach0 = 0.3
    w = w_out + G_OTHER / (ach0 * m_dry_air)
    w = min(w, w_from_rh(T_in, 0.95))
    m = m0
    t = 0.0
    n = int(hours * 60 / dt_min)
    out = {
        "dry_h": None, "peak_rh": 0.0, "h_rh60": 0.0,
        "h_si80": {k: 0.0 for k in F_RSI}, "h_si100": {k: 0.0 for k in F_RSI},
        "extra_vent_kwh": 0.0, "rh0": rh_air(T_in, w),
    }
    for i in range(n):
        ach = ach_fn(t)
        rh = rh_air(T_in, w)
        # kuruma
        if m > m_eq + 1e-9:
            tw = wet_bulb(T_in, rh)
            e = max(0.0, ALPHA * (T_in - tw))
            if m < m_c:
                e *= (m - m_eq) / max(m_c - m_eq, 1e-9)
            e = min(e, (m - m_eq) / dt_h)
        else:
            e = 0.0
        m -= e * dt_h
        # nem alıcı (RH>%50 iken, sabit çekim)
        d = dehum_kg_h if rh > 0.50 else 0.0
        # oda nem dengesi
        dwdt = (e + G_OTHER - d + ach * m_dry_air * (w_out - w)) / (
            (1 + BETA) * m_dry_air
        )
        w += dwdt * dt_h
        w = max(w, 1e-5)
        rh = rh_air(T_in, w)
        out["peak_rh"] = max(out["peak_rh"], rh)
        if rh > 0.60:
            out["h_rh60"] += dt_h
        for k, f in F_RSI.items():
            T_si = T_out + f * (T_in - T_out)
            rh_si = pv_from_w(w) / psat(T_si)
            if rh_si >= 0.80:
                out["h_si80"][k] += dt_h
            if rh_si >= 1.0:
                out["h_si100"][k] += dt_h
        out["extra_vent_kwh"] += 0.34 * V * max(ach - ach0, 0.0) * (T_in - T_out) * dt_h / 1000.0
        if out["dry_h"] is None and (m - m_eq) <= 0.05 * (m0 - m_eq):
            out["dry_h"] = t / 60.0 + dt_h
        t += dt_min
    return out


# --- Havalandırma stratejileri --------------------------------------------------
def kapali(t):
    return 0.3


def aralik_surekli(t):  # pencere aralık (sürekli) ~2 ACH (varsayım)
    return 2.0


def tam_ac_10dk_saat(t):  # her saat 10 dk tam açık (~6 ACH), kalan 0.3
    return 6.0 if (t % 60.0) < 10.0 else 0.3


STRATEJILER = [
    ("pencere kapalı (ACH 0,3)", kapali, 0.0),
    ("pencere aralık sürekli (ACH 2)", aralik_surekli, 0.0),
    ("her saat 10 dk tam aç", tam_ac_10dk_saat, 0.0),
    ("kapalı + nem alıcı (0,3 kg/h)", kapali, 0.3),
]

# MGM 1991-2020 Ocak BÖLGE normalleri (ısı). Dış nem: VARSAYIM.
BOLGELER = [
    ("Marmara-benzeri", 5.2, 0.80),
    ("Ege-benzeri", 6.3, 0.72),
    ("İç Anadolu-benzeri", -0.6, 0.78),
    ("Doğu Anadolu-benzeri", -4.3, 0.80),
]

GAZ_TL_KWH = 1.11  # 10,625 TL/m3 / (10,6 kWh/m3 * 0,9) -- Nisan 2026 tarifesi, DOĞRULA


def main():
    T_in = 20.0
    print("Varsayımlar: oda 30 m3, kuru yük 5 kg, kalan nem (RMC) %52, iç sıcaklık 20 C")
    print(f"Yüklü su: {5.0*0.52:.1f} L; ALPHA={ALPHA}, BETA={BETA}, G_OTHER={G_OTHER} kg/h\n")
    for ad, T_out, rh_out in BOLGELER:
        print(f"=== {ad}: dış {T_out:+.1f} C, dış BN {rh_out*100:.0f}% (nem varsayım) ===")
        print(f"{'strateji':34s} {'kuruma(h)':>9s} {'tepe BN':>8s} {'BN>60 (h)':>9s} "
              f"{'yoğuşma(h) f.65/.80':>20s} {'ek ısı kaybı kWh':>16s} {'TL':>5s}")
        for ad_s, fn, dh in STRATEJILER:
            r = simulate(T_in, T_out, rh_out, fn, dehum_kg_h=dh)
            dry = f"{r['dry_h']:.1f}" if r["dry_h"] else ">24"
            k65, k80 = list(F_RSI.keys())
            cond = f"{r['h_si100'][k65]:.1f}/{r['h_si100'][k80]:.1f}"
            print(f"{ad_s:34s} {dry:>9s} {r['peak_rh']*100:7.0f}% {r['h_rh60']:9.1f} "
                  f"{cond:>20s} {r['extra_vent_kwh']:16.1f} {r['extra_vent_kwh']*GAZ_TL_KWH:5.1f}")
        print()


if __name__ == "__main__":
    main()
