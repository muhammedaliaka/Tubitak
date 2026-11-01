"""Kağıthane'den uydu geçiş tahmini (Skyfield + SGP4).

İki tür liste verir:
  - "görünür" geçişler: uydu Güneş ışığında, gözlemci karanlıkta (Güneş < -6°), yükselim > maske
    (telefonla fotoğraf için)
  - "radyo" geçişleri: yükselim > maske (gece/gündüz fark etmez; bulutta da çalışır)

Kullanım:
  1) TLE indir (tarayıcıyla da olur), örneğin ISS:
       https://celestrak.org/NORAD/elements/gp.php?CATNR=25544&FORMAT=TLE  -> iss.tle
     Diğerleri: CSS 48274, Meteor-M2 4 59051, Meteor-M2 3 57166
  2) python gecis_tahmini.py iss.tle --bas 2026-11-16 --gun 7            (görünür geçişler)
     python gecis_tahmini.py meteor.tle --bas 2026-11-16 --gun 3 --radyo  (bütün geçişler)
İlk çalıştırmada Skyfield, Güneş konumu için de421.bsp dosyasını (~17 MB) indirir.

UYARI: TLE birkaç günden eskiyse ISS saatleri dakikalarca kayabilir (ISS yörünge düzeltmesi
yapar). Gözlemden 1–2 gün önce TLE'yi yenileyip tekrar çalıştırın.
Gereken paket: skyfield (numpy ve sgp4'ü de kurar).
"""
import argparse
import datetime as dt

import numpy as np
from skyfield.api import Loader, EarthSatellite, wgs84

TSI = dt.timezone(dt.timedelta(hours=3))   # Türkiye saati (UTC+3, yaz saati yok)
GUNLER = ("Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz")


def main():
    ap = argparse.ArgumentParser(description="Kağıthane'den uydu geçiş tahmini")
    ap.add_argument("tle", help="3 satırlı TLE dosyası (ad + 2 satır)")
    ap.add_argument("--bas", default=dt.date.today().isoformat(), help="başlangıç tarihi YYYY-AA-GG")
    ap.add_argument("--gun", type=int, default=7, help="kaç gün")
    ap.add_argument("--lat", type=float, default=41.08)
    ap.add_argument("--lon", type=float, default=28.97)
    ap.add_argument("--yukseklik", type=float, default=80.0, help="metre")
    ap.add_argument("--maske", type=float, default=15.0, help="en düşük yükselim (derece)")
    ap.add_argument("--radyo", action="store_true", help="görünürlüğe bakmadan bütün geçişler")
    ap.add_argument("--efemeris-dizini", default=".", help="de421.bsp nereye indirilsin")
    a = ap.parse_args()

    ld = Loader(a.efemeris_dizini)
    ts = ld.timescale()
    eph = ld("de421.bsp")
    sun, earth = eph["sun"], eph["earth"]
    obs = wgs84.latlon(a.lat, a.lon, elevation_m=a.yukseklik)
    lines = [s for s in open(a.tle, encoding="utf-8").read().splitlines() if s.strip()]
    sat = EarthSatellite(lines[1], lines[2], lines[0].strip(), ts)
    y, m, d = map(int, a.bas.split("-"))
    t0 = ts.from_datetime(dt.datetime(y, m, d, tzinfo=TSI))
    t1 = ts.from_datetime(dt.datetime(y, m, d, tzinfo=TSI) + dt.timedelta(days=a.gun))
    print(f"{sat.name}  (TLE epoğu {sat.epoch.utc_strftime('%Y-%m-%d %H:%M')} UTC)  maske {a.maske:.0f}°  "
          f"{'radyo: bütün geçişler' if a.radyo else 'görünür geçişler'}")
    print("tarih        doğuş   tepe(TSİ)  batış   tepe yük.  görünür süre")

    t, ev = sat.find_events(obs, t0, t1, altitude_degrees=a.maske)
    i = 0
    while i <= len(ev) - 3:
        if not (ev[i] == 0 and ev[i + 1] == 1 and ev[i + 2] == 2):
            i += 1
            continue
        tr, tc, tset = t[i], t[i + 1], t[i + 2]
        i += 3
        tt = ts.linspace(tr, tset, 60)
        alt = (sat - obs).at(tt).altaz()[0].degrees
        if a.radyo:
            frac = 1.0
        else:
            lit = sat.at(tt).is_sunlit(eph)
            sun_alt = (earth + obs).at(tt).observe(sun).apparent().altaz()[0].degrees
            frac = float(np.mean(lit & (sun_alt < -6)))
            if frac < 0.1:
                continue
        dur = (tset - tr) * 86400
        f = lambda x: x.astimezone(TSI)
        lc = f(tc.utc_datetime())
        print(f"{lc:%d.%m.%Y} {GUNLER[lc.weekday()]}  {f(tr.utc_datetime()):%H:%M}   {lc:%H:%M:%S}  "
              f"{f(tset.utc_datetime()):%H:%M}   {alt.max():5.0f}°     {frac * dur / 60:4.1f} / {dur / 60:4.1f} dk")


if __name__ == "__main__":
    main()
