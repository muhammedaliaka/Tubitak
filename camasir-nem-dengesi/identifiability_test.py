"""Sentetik kimliklendirilebilirlik testi (Çamaşır–Nem Dengesi, H2'nin ön sınaması).

Soru: Nem kaynağı (çamaşırın buharlaşma hızı E(t)) BİLİNİYORSA, yalnızca T/BN
serisinden hava değişim oranı (ACH) daha iyi tahmin edilebilir mi?

Yöntem (tamamı SENTETİK; gerçek ölçüm değildir):
  1. sim_nem_dengesi.py modeliyle "gerçek" bir nem serisi üret (ACH, BETA, G_OTHER bilinen).
  2. Ölçüm gürültüsü ekle (BN: ±sigma_rh mutlak; yük hücresi: kütle gürültüsü).
  3. İki durumda ACH'yi en küçük kareler ile geri bul:
       A) E(t) bilinmiyor  -> fizik modeli (ALPHA bilinmeyen) ile E'yi de tahmin et
       B) E(t) yük hücresinden ölçülüyor -> ACH, BETA, G_OTHER'i tahmin et
  4. 40 gürültü gerçekleşmesinde ACH'nin bağıl hatasını karşılaştır.

SINIRLAR: Model, veriyi üreten modelle aynı (en iyi senaryo, "inverse crime").
Gerçek odada tam karışma, tek tampon çarpanı ve sabit ACH varsayımları bozulur.
Bu test yalnızca "ölçülen kaynak fikri teoride işe yarar mı?" sorusunu yanıtlar.
"""
import importlib.util
import math
import random

import numpy as np
from scipy.optimize import least_squares

spec = importlib.util.spec_from_file_location("s", "sim_nem_dengesi.py")
s = importlib.util.module_from_spec(spec)
spec.loader.exec_module(s)

T_IN, T_OUT, RH_OUT, V = 20.0, 5.2, 0.80, 30.0
DT_MIN = 2.0
HOURS = 12
N = int(HOURS * 60 / DT_MIN)
M_AIR = s.RHO_A * V
W_OUT = s.w_from_rh(T_OUT, RH_OUT)
DRY_MASS, RMC = 5.0, 0.52


def true_series(ach, beta, g_other, alpha, x_crit=None, drift=0.0):
    """Sentetik gerçek: w(t) ve E(t). x_crit/drift: kuruma yasasında MODEL HATASI."""
    dt_h = DT_MIN / 60.0
    w = min(W_OUT + g_other / (0.3 * M_AIR), s.w_from_rh(T_IN, 0.95))
    m = DRY_MASS * RMC
    m_eq = DRY_MASS * s.X_EQ
    m_c = DRY_MASS * (s.X_CRIT if x_crit is None else x_crit)
    ws, es = [], []
    for i in range(N):
        rh = s.rh_air(T_IN, w)
        if m > m_eq + 1e-9:
            e = max(0.0, alpha * (T_IN - s.wet_bulb(T_IN, rh)))
            if m < m_c:
                e *= (m - m_eq) / max(m_c - m_eq, 1e-9)
            e = min(e, (m - m_eq) / dt_h)
            e *= 1.0 + drift * math.sin(2 * math.pi * i * DT_MIN / 60.0 / 6.0)
        else:
            e = 0.0
        m -= e * dt_h
        w += dt_h * (e + g_other + ach * M_AIR * (W_OUT - w)) / ((1 + beta) * M_AIR)
        ws.append(w)
        es.append(e)
    return np.array(ws), np.array(es)


def forward_given_e(ach, beta, g_other, e_series):
    dt_h = DT_MIN / 60.0
    w = min(W_OUT + g_other / (0.3 * M_AIR), s.w_from_rh(T_IN, 0.95))
    out = np.empty(N)
    for i in range(N):
        w += dt_h * (e_series[i] + g_other + ach * M_AIR * (W_OUT - w)) / ((1 + beta) * M_AIR)
        out[i] = w
    return out


def forward_model_e(ach, beta, g_other, alpha):
    ws, _ = true_series(ach, beta, g_other, alpha)
    return ws


def rh_of_w(ws):
    return np.array([s.rh_air(T_IN, w) for w in ws])


def fit_B(rh_obs, e_meas):
    def res(p):
        ach, beta, g = p
        return rh_of_w(forward_given_e(ach, beta, g, e_meas)) - rh_obs
    r = least_squares(res, x0=[1.0, 3.0, 0.04], bounds=([0.05, 0.0, 0.0], [10.0, 20.0, 0.5]))
    return r.x


def fit_A(rh_obs):
    def res(p):
        ach, beta, g, alpha = p
        return rh_of_w(forward_model_e(ach, beta, g, alpha)) - rh_obs
    r = least_squares(res, x0=[1.0, 3.0, 0.04, 0.05],
                      bounds=([0.05, 0.0, 0.0, 0.01], [10.0, 20.0, 0.5, 0.2]))
    return r.x


def main(n_trials=40, sigma_rh=0.015, sigma_e=0.03, seed=7, misspec=False):
    rng = np.random.default_rng(seed)
    random.seed(seed)
    beta_t, g_t, alpha_t = 4.0, 0.05, 0.055
    print(f"Gürültü: BN ±{sigma_rh*100:.1f}% (mutlak), E ölçümü ±{sigma_e:.2f} kg/h; "
          f"{n_trials} deneme; gerçek BETA={beta_t}, G={g_t}, ALPHA={alpha_t}")
    print(f"{'gerçek ACH':>10s} | {'A: E bilinmiyor (medyan |hata|%)':>34s} | {'B: E ölçülü (medyan |hata|%)':>30s}")
    for ach_t in (0.3, 0.6, 1.0, 2.0):
        if misspec:
            ws, es = true_series(ach_t, beta_t, g_t, alpha_t, x_crit=0.25, drift=0.30)
        else:
            ws, es = true_series(ach_t, beta_t, g_t, alpha_t)
        rh_true = rh_of_w(ws)
        errA, errB = [], []
        for _ in range(n_trials):
            rh_obs = rh_true + rng.normal(0, sigma_rh, N)
            e_meas = np.clip(es + rng.normal(0, sigma_e, N), 0, None)
            try:
                a = fit_A(rh_obs)[0]
                b = fit_B(rh_obs, e_meas)[0]
            except Exception:
                continue
            errA.append(abs(a - ach_t) / ach_t * 100)
            errB.append(abs(b - ach_t) / ach_t * 100)
        print(f"{ach_t:10.1f} | {np.median(errA):13.1f} (P90 {np.percentile(errA,90):6.1f}) "
              f"| {np.median(errB):13.1f} (P90 {np.percentile(errB,90):6.1f})")


if __name__ == "__main__":
    print("--- Durum 1: model doğru (en iyimser) ---")
    main()
    print("\n--- Durum 2: kuruma yasası YANLIŞ belirlenmiş (x_crit=0.25, ±%30 yavaş modülasyon) ---")
    main(misspec=True)
