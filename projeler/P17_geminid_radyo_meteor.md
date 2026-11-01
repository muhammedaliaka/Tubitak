# P17 — Geminid Akan Yıldızlarını Radyoyla Yakalamak: Kağıthane'den İleri Saçılma Gözlemi

> **Tek cümle:** Fransa'daki GRAVES uzay gözetim radarının (143,050 MHz) yayınının meteor iyonlaşma izlerinden saçılmasını RTL-SDR ile dinleyip, Geminid yağmuru (Aralık ortası) sırasında meteor sayım hızını ve günlük değişimini ölçmek.
> **Aile:** Radyo/atmosfer · **Yazılım payı:** ~%75 · **Yeni harcama (tahmin):** ~0–40 USD (RTL-SDR P01 ile ortak) · **Yapay zekâ:** isteğe bağlı karşılaştırma

## Neden ilginç
Görünmeyen meteorları gündüz bile radyoyla saymak; Geminidler proje süresinin içinde.

## Araştırma soruları ve hipotezler
- **H1:** Kağıthane'den GRAVES meteor yankıları alınabilir (**belirsiz:** uzaklık ~1.986 km, ileri saçılmanın yaklaşık 500–2.000 km sınırında).
- **H2:** Sayım hızı Geminid zirvesinde artar ve günün saatine göre (Dünya'nın yörünge yönü) değişir.
- **H3:** Kısa (az yoğun) ve uzun (çok yoğun) izler süre dağılımında ayrışır.

## Fizik
Meteoroidin atmosfere girişi, iyonlaşma izi, ileri saçılma geometrisi, az/çok yoğun izler, Doppler, meteor yağmuru radyantı.

## Deneyler
E1 dinleme ve ilk yankılar · E2 otomatik algılama algoritması · E3 Geminid öncesi/zirve/sonrası sayım · E4 süre dağılımı · E5 (isteğe bağlı) uçak yansımalarını ayırma.

## Donanım
**Yeni:** 143 MHz Yagi veya dipol (tel), bant geçiren süzgeç. **Mevcut/ortak:** RTL-SDR (P01), laptop.

## Yapay zekâ gerekli mi?
Hayır; spektrogramda eşikleme yeter. ML ile karşılaştırma isteğe bağlı.

## Öncül → kama
**Öncül:** GRAVES ile meteor/uçak/uzay aracı yansımaları amatörlerde yaygın; İngiltere ve Slovakya'da kurulumlar; Belçika BRAMS ağı; IMO bildirileri.
**Kama (zayıf):** Güneydoğu Avrupa'dan GRAVES alımının sınanması.

## Etkileyici gösteri
Canlı spektrogramda "ping" sesleriyle meteorlar.

## Savunma anlatısı
Meteor izi haberleşmesi (meteor burst) ve uzay gözetim radarı kavramı.

## Riskler
**En yüksek fizibilite riski:** İstanbul GRAVES menzilinin sınırında ve radar ışını güneye bakıyor (genel bilgi); tek bir meteor yağmuru penceresi; kentsel gürültü. Pilot olumsuzsa proje düşer.

## İlk pilot
Bir gece 143,050 MHz'i dinle; sabaha karşı yankı var mı?

## Kaynaklar
[GRAVES ile dinleme (rtl-sdr.com)](https://www.rtl-sdr.com/using-the-graves-radar-to-listen-to-reflections-from-meteors-planes-and-spacecraft/) · [BAA meteor radar SDR](https://britastro.org/sites/default/files/MeteorRadarSDRReceiver.pdf) · [IMO 2014](https://www.imo.net/imcs/imc2014/2014-04-dolinsky-final-e.pdf) · [IMC 2012](https://imo.net/imcs/imc2012/sites/default/files/IMC2012_pinter.pdf) · [FRIPON](https://www.fripon.org/?p=293)
