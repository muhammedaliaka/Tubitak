# P10 — Çatıdaki Uydu Çanağı Radyo Teleskop: Güneş ve Ay'ın Mikrodalga Sıcaklığını Ölçmek

> **Tek cümle:** Türkiye'de yaygın olan bir TV uydu çanağı ve LNB'yi, Arduino'ya bağlı bir güç dedektörüyle "toplam güç radyometresi"ne çevirip Güneş'in ve Ay'ın 11 GHz'deki parlaklık sıcaklığını ölçmek.
> **Aile:** Radyo astronomi · **Yazılım payı:** ~%65 · **Yeni harcama (tahmin):** ~20–60 USD (çanak varsa) · **Yapay zekâ:** gerekmez

## Neden ilginç
Neredeyse her apartmanda bulunan çanak anten aslında küçük bir radyo teleskoptur. "Ay'ı radyoyla görmek" etkileyicidir.

## Araştırma soruları ve hipotezler
- **H1:** Ev tipi çanakla Güneş sürüklenme taramasından ışın genişliği ve Güneş'in parlaklık sıcaklığı ölçülür.
- **H2:** Ay, ~0,9 m çanakla ölçülebilir bir anten sıcaklığı farkı yaratır.
- **H3 (zor, isteğe bağlı):** Ay'ın mikrodalga parlaklığı evreyle değişir ve optik evreye göre gecikmelidir (yüzey altı ısıl gecikme).

## Fizik
Kara cisim ışıması, Rayleigh–Jeans yaklaşımı, anten sıcaklığı, ışın seyrelmesi, radyometre denklemi, Dünya dönüşüyle sürüklenme (15°/saat).
**Kaba hesap (ışın ≈ 70λ/D, 11,7 GHz):** D = 0,8 m → ~2,2°, 0,9 m → ~2,0°, 1,2 m → ~1,5°. Ay (0,52°, ~200 K kabul) için anten sıcaklığı ~11 K (0,8 m), ~14 K (0,9 m), ~24 K (1,2 m). Ay sıcaklığı değeri doğrulanmadı; literatürden alınacak.

## Deneyler
E1 kalibrasyon (soğuk gökyüzü vs sıcak duvar/zemin, Y-faktörü) · E2 Güneş sürüklenme taramaları (ışın genişliği, Güneş sıcaklığı) · E3 Ay tespiti · E4 (isteğe bağlı) 2+ hafta Ay evresi izlemi · E5 LNB kazanç kaymasının sıcaklıkla ilişkisi.

## Yazılım
Arduino ADC kaydı, sürüklenme taraması uydurma (Gauss ışın), efemeris (astropy/Skyfield), kalibrasyon, kazanç kayması düzeltme.

## Donanım
**Mevcut (muhtemel):** evdeki uydu çanağı, Arduino, laptop. **Yeni:** universal LNB (yedek), güç enjektörü/bias-T (13–18 V), log güç dedektörü (ör. AD8318 modülü) veya uydu bulucu metre; alternatif: RTL-SDR (LNB ara frekansı 950–2150 MHz, RTL-SDR üst sınırı ~1,77 GHz, doğrulanmadı).

## Yapay zekâ gerekli mi?
Hayır.

## Öncül → kama
**Öncül:** Jodrell Bank "Yeni Ay zamanının radyo ile belirlenmesi" (3,7 m çanak, LNB 10,3–11,3 GHz), ESA–Dresden 1,2 m TV çanağı radyometresi (Güneş ve Ay), Kiel 10 GHz belgeleri, 1,2 m çanak + Airspy, RTL-SDR'li küçük motorlu 11,2 GHz teleskop, ARRL QST ev yapımı teleskop.
**Kama:** Türkiye'de yaygın ~80–90 cm ofset çanak + Arduino radyometreyle Ay tespiti ve kalibrasyon yöntemi; 6 haftada Ay evresi denemesi (zor).

## Etkileyici gösteri
Çanak Güneş'e dönünce yükselen sinyal; Ay'ın "radyo fotoğrafı" (tarama haritası).

## Savunma anlatısı
Pasif mikrodalga radyometrisi (uzaktan algılama, ısıl mikrodalga imza).

## Riskler
Ofset çanakta işaretleme geometrisi; LNB kazanç kayması; Ay sinyali küçük; geostatik uydu kuşağından (Türksat) kaçınma; çatı güvenliği (yetişkin gözetiminde).

## İlk pilot
Çanağı Güneş'e çevir, uydu bulucu metre/dedektörle sinyal yükselişini Arduino ile kaydet.

## Kaynaklar
[Jodrell Bank, arXiv 1312.5956](https://arxiv.org/pdf/1312.5956) · [ESA–Dresden](https://portia.astrophysik.uni-kiel.de/~koeppen/ue7e/docs/RA_5dresden.pdf) · [Kiel gürültü belgesi](https://portia.astrophysik.uni-kiel.de/%7Ekoeppen/10GHz/docs/Noise.pdf) · [1,2 m çanak + Airspy](https://www.rtl-sdr.com/building-an-11-2-ghz-radio-telescope-with-an-airspy-and-1-2m-tv-satellite-dish/) · [Küçük motorlu teleskop](https://www.rtl-sdr.com/a-small-11-2-ghz-motorized-radio-telescope-with-tv-dish-and-rtl-sdr/) · [ARRL QST](https://www.arrl.org/files/file/ETP/Radio%20Astronomy/Build%20a%20Homebrew%20Radio%20Telescope-QST-0609.pdf)
