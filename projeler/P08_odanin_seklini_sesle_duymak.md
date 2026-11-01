# P08 — Odanın Şeklini Sesle Duymak: Yankılardan Duvarları Bulan Ucuz Mikrofon Dizisi

> **Tek cümle:** Bir hoparlörden çıkan kısa bir ses taramasının (chirp) duvarlardan dönen yankılarını 4 ucuz mikrofonla yakalayıp, Öklid uzaklık matrisleriyle odanın geometrisini (duvar konumlarını) çıkarmak.
> **Aile:** Akustik/sonar · **Yazılım payı:** ~%80 · **Yeni harcama (tahmin):** ~20–60 USD · **Yapay zekâ:** gerekmez

## Neden ilginç
Gözler kapalıyken bilgisayarın odayı çizmesi; karanlıkta/dumanlı ortamda haritalama.

## Araştırma soruları ve hipotezler
- **H1:** Boş/sade bir odada ucuz mikrofonlarla duvar uzaklıkları şerit metreye göre cm mertebesinde bulunur.
- **H2:** Eşyalı odalarda doğruluk, yankı karışıklığıyla nicel olarak düşer; hangi koşulda çalışmadığı ölçülür.
- **H3:** Mikrofon dizisinin geometrisi kabaca biliniyorsa da çözüm kararlıdır.

## Fizik
Yansıma, görüntü kaynak yöntemi, ses hızı, darbe sıkıştırma (radardaki gibi chirp + eşleşmiş süzgeç), geometri (Öklid uzaklık matrisleri).

## Deneyler
E1 koridor/boş sınıf: tek mikrofonla yankı gecikmeleri · E2 4 mikrofonla 3B duvar kestirimi · E3 okul spor salonu / merdiven boşluğu · E4 eşyalı ev odaları · E5 SNR ve mikrofon sayısı etkisi.

## Yazılım
Chirp üretimi, eşleşmiş süzgeç, tepe bulma, yankı–duvar eşleme (EDM tabanlı), 3B çizim.

## Donanım
**Yeni:** 4 INMP441 mikrofon (ESP32'nin iki I2S kanalı), hoparlör + amfi, küçük ahşap/karton çerçeve. **Mevcut:** ESP32, laptop.

## Yapay zekâ gerekli mi?
Hayır; EDM tabanlı eşleme klasik. ML yalnızca yankı sıralamada karşılaştırma.

## Öncül → kama
**Öncül:** Dokmanić ve ark., PNAS 2013 "Acoustic echoes reveal room shape": 4 mikrofon, basit dışbükey odada mm mertebesi, Lozan Katedrali; ICASSP 2016 dizi geometrisi bilinmiyorken. Telefon uygulaması bulunamadı.
**Kama:** Çok ucuz ESP32 dizisi ve eşyalı Türk apartman odalarında sistematik başarısızlık analizi.

## Etkileyici gösteri
Ekranda gerçek zamanlı çizilen oda; şerit metreyle karşılaştırma.

## Savunma anlatısı
Karanlık/dumanlı ortamda akustik haritalama (arama-kurtarma, robotik), sonar ilkeleri.

## Riskler
Eşya karmaşası, yankılanma, ESP32'de çok kanallı eşzamanlı örnekleme, hoparlör doğrusal olmayanlığı. **Bitirme riski orta-yüksek.**

## İlk pilot
Boş koridorda bir hoparlör + bir mikrofon: chirp yankısında duvar uzaklığına karşılık gelen gecikmeler görünüyor mu?

## Kaynaklar
[Dokmanić ve ark. (Illinois)](https://experts.illinois.edu/en/publications/acoustic-echoes-reveal-room-shape/) · [EPFL kaydı](https://infoscience.epfl.ch/record/186657?ln=en) · [IEEE Spectrum](https://spectrum.ieee.org/echolocation-by-smartphone-possible)
