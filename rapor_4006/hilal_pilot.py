import ephem, math
# Yeni ay (kavusum) ve her gun batimda Ay yuksekligi/elongasyonu
def conj(d0):
    d = ephem.previous_new_moon(d0)
    return d
def at_sunset(date_utc_day, lat, lon):
    o = ephem.Observer(); o.lat=str(lat); o.lon=str(lon); o.elevation=0; o.pressure=0
    o.date = date_utc_day
    s = ephem.Sun(); m = ephem.Moon()
    t = o.next_setting(s)
    o.date = t
    s.compute(o); m.compute(o)
    alt = math.degrees(m.alt); elong = math.degrees(ephem.separation(s,m))
    return t, alt, elong
# Ramazan 1447: yeni ay 17 Subat 2026 ~12:01 UTC (kontrol)
nm = ephem.next_new_moon('2026/02/10')
print("Yeni ay (UTC):", nm)
for lbl,lat,lon in [("Istanbul",41.08,28.97),("Wellington",-41.29,174.78),("Hawaii-Honolulu",21.3,-157.86),("Mekke",21.42,39.83)]:
    for day in ['2026/02/17','2026/02/18']:
        t,alt,el = at_sunset(day,lat,lon)
        print(f"{lbl:16s} gunbatimi {t}  Ay alt={alt:5.1f}  elong={el:5.1f}")
