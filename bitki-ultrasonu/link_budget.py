"""Bitki ultrasonik tıkırtısı için bağlantı bütçesi (link budget) modeli.

Amaç: ucuz bir MEMS mikrofonla tıkırtı hangi mesafeye kadar tespit edilebilir?
Bu bir MODELDİR; girdilerin çoğu varsayımdır (aşağıda işaretli). Gerçek değerler
1. hafta deneyleriyle ölçülmelidir.
"""
import math

# --- ISO 9613-1 atmosferik soğurma (dB/m) --------------------------------
# Not: standart resmen 10 kHz'e kadar doğrulanmıştır; 40-80 kHz için
# ekstrapolasyon olarak kullanılır (yarasa akustiği literatüründe yaygın).
def alpha_db_per_m(f, T_c=20.0, rh=50.0, p_kpa=101.325):
    T = T_c + 273.15
    T0 = 293.15
    T01 = 273.16
    pr = 101.325
    C = -6.8346 * (T01 / T) ** 1.261 + 4.6151
    psat_over_pr = 10 ** C
    h = rh * psat_over_pr / (p_kpa / pr)  # molar su buharı derişimi (%)
    frO = (p_kpa / pr) * (24 + 4.04e4 * h * (0.02 + h) / (0.391 + h))
    frN = (p_kpa / pr) * (T / T0) ** -0.5 * (
        9 + 280 * h * math.exp(-4.170 * ((T / T0) ** (-1 / 3) - 1))
    )
    a = 8.686 * f * f * (
        1.84e-11 * (p_kpa / pr) ** -1 * (T / T0) ** 0.5
        + (T / T0) ** -2.5
        * (
            0.01275 * math.exp(-2239.1 / T) / (frO + f * f / frO)
            + 0.1068 * math.exp(-3352.0 / T) / (frN + f * f / frN)
        )
    )
    return a


print("=== Atmosferik soğurma (dB/m), 20 C ===")
print("f(kHz)  RH30   RH50   RH70")
for f in (1e3, 10e3, 20e3, 40e3, 60e3, 80e3):
    print(
        f"{f/1e3:6.0f} "
        + " ".join(f"{alpha_db_per_m(f, 20, rh):6.2f}" for rh in (30, 50, 70))
    )

# --- Bağlantı bütçesi -------------------------------------------------------
# Kaynak: bioRxiv ön baskısı ~65 dB SPL @ 10 cm (arama özeti; metin teyitli değil).
# Gürültü tabanı: VARSAYIM. SPU0410LR5H için datasheet SNR ~63 dB(A) -> ~31 dBA
# öz-gürültü (1 kHz). Ultrasonik banttaki (40-80 kHz) gürültü yoğunluğu bilinmiyor.
# Bu yüzden 35 / 45 / 55 dB SPL'lik ÜÇ senaryo (iyi/orta/kötü) hesaplanır.
F_MID = 60e3  # tıkırtı bandının ortası
R0 = 0.10  # m, referans mesafe


def snr_db(r, src_db=65.0, noise_db=45.0, rh=50.0, reflector_gain_db=0.0):
    spreading = 20 * math.log10(r / R0)
    absorb = alpha_db_per_m(F_MID, 20, rh) * max(r - R0, 0)
    return src_db - spreading - absorb + reflector_gain_db - noise_db


def max_range(snr_min=10.0, **kw):
    lo, hi = R0, 50.0
    if snr_db(lo, **kw) < snr_min:
        return 0.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if snr_db(mid, **kw) >= snr_min:
            lo = mid
        else:
            hi = mid
    return lo


print("\n=== Maksimum tespit mesafesi (m), gereken SNR = 10 dB, RH 50% ===")
print("kaynak seviyesi dBSPL@10cm | gürültü tabanı dBSPL | yansıtıcı kazancı -> menzil")
for src in (55, 65, 70):
    for noise in (35, 45, 55):
        row = []
        for g in (0, 20, 30):
            row.append(f"{max_range(10, src_db=src, noise_db=noise, reflector_gain_db=g):5.2f}")
        print(f"  src={src}  noise={noise}  gain 0/20/30 dB -> " + " / ".join(row))

# --- Parabolik yansıtıcı kazancı (basit fiziksel optik/akustik kestirim) ------
print("\n=== Parabolik yansıtıcı: kazanç ve ışın genişliği (60 kHz, verim 0.5) ===")
lam = 343.0 / 60e3
for D_cm in (5, 10, 15, 20):
    D = D_cm / 100
    G = 0.5 * (math.pi * D / lam) ** 2
    bw = math.degrees(70 * lam / D / 57.2958)  # yaklaşık yarı-güç genişliği (derece)
    print(f"  D={D_cm:2d} cm  kazanç≈{10*math.log10(G):5.1f} dB  ışın≈{70*lam/D:5.1f}°")

# --- ADC ve yükselteç gürültü bütçesi (RP2040 ADC, ENOB 8.7) ----------------
vref = 3.3
enob = 8.7
lsb = vref / 2 ** enob
adc_noise_rms = lsb / math.sqrt(12)
print(f"\n=== ADC (RP2040, ENOB {enob}) ===")
print(f"  etkin LSB ≈ {lsb*1e3:.2f} mV, nicelemeye bağlı gürültü ≈ {adc_noise_rms*1e3:.2f} mV rms")
sens_1k_dbv_pa = -38.0  # SPU0410LR5H @1kHz (datasheet, ±3 dB)
for rel_db in (0, -10, -20):  # 60 kHz'de bağıl duyarlılık (BİLİNMİYOR -> aralık)
    sens_v_pa = 10 ** ((sens_1k_dbv_pa + rel_db) / 20)
    for gain in (300, 1000, 3000):
        v_in_ref = adc_noise_rms / gain  # mikrofon çıkışına indirgenmiş ADC gürültüsü
        pa = v_in_ref / sens_v_pa
        spl = 20 * math.log10(pa / 20e-6)
        sig_v = (20e-6 * 10 ** (65 / 20)) * sens_v_pa * gain  # 65 dB SPL tıkırtı, rms
        print(
            f"  60kHz bağıl duyarlılık {rel_db:4d} dB, kazanç {gain:5d}: "
            f"ADC gürültüsü mikrofon girişinde ≈ {spl:5.1f} dB SPL, "
            f"65 dB tıkırtı ADC'de ≈ {sig_v*1e3:6.1f} mV rms"
        )
