import math, datetime as dt
K=(21.422487,39.826206); P=(41.0815,28.9700)  # Kabe, Kağıthane (yaklaşık)
f1,l1=map(math.radians,P); f2,l2=map(math.radians,K)
dl=l2-l1
q=math.degrees(math.atan2(math.sin(dl), math.cos(f1)*math.tan(f2)-math.sin(f1)*math.cos(dl)))%360
d=6371*math.acos(math.sin(f1)*math.sin(f2)+math.cos(f1)*math.cos(f2)*math.cos(dl))
print(f"Kağıthane kıble azimutu (coğrafi kuzeyden): {q:.2f}°, Kabe'ye uzaklık {d:.0f} km")
print(f"1° sapma ≈ {d*math.radians(1):.0f} km yanal kayma; 45° sınırı")
try:
    from pygeomag import GeoMag
    gm=GeoMag(coefficients_file="wmm/WMMHR_2025.COF", high_resolution=True) if False else GeoMag()
    r=gm.calculate(glat=P[0],glon=P[1],alt=0,time=2027.3)
    print(f"Manyetik sapma (WMM, 2027.3): {r.d:.2f}° (+ doğu)")
except Exception as e: print("pygeomag yok:",e)
# Güneş azimutunun kıble azimutuna eşit olduğu saat (NOAA basit algoritma)
def sun(t, lat, lon):
    jd=t.timestamp()/86400+2440587.5; n=jd-2451545.0
    L=(280.46+0.9856474*n)%360; g=math.radians((357.528+0.9856003*n)%360)
    lam=math.radians(L+1.915*math.sin(g)+0.020*math.sin(2*g)); eps=math.radians(23.439-0.0000004*n)
    ra=math.atan2(math.cos(eps)*math.sin(lam),math.cos(lam)); dec=math.asin(math.sin(eps)*math.sin(lam))
    gmst=(280.46061837+360.98564736629*n)%360; H=math.radians((gmst+lon)%360)-ra
    la=math.radians(lat)
    alt=math.asin(math.sin(la)*math.sin(dec)+math.cos(la)*math.cos(dec)*math.cos(H))
    az=math.degrees(math.atan2(-math.sin(H), math.tan(dec)*math.cos(la)-math.sin(la)*math.cos(H)))%360
    return az, math.degrees(alt)
tz=dt.timezone(dt.timedelta(hours=3))
for day in ["2027-03-01","2027-04-01","2027-05-01","2027-05-28","2027-06-01"]:
    t0=dt.datetime.fromisoformat(day+"T06:00").replace(tzinfo=tz)
    best=None
    for m in range(0,8*60):
        t=t0+dt.timedelta(minutes=m); az,al=sun(t,*P)
        if best is None or abs(az-q)<best[0]: best=(abs(az-q),t,az,al)
    print(day, "güneş kıble yönünde:", best[1].strftime("%H:%M"), f"az={best[2]:.1f}° yükseklik={best[3]:.0f}°")
