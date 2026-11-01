# P06 — Sesle Sıcaklık Haritası: Ucuz Mikrofonlarla Odanın Akustik Tomografisi

> **Tek cümle:** Ucuz hoparlör ve MEMS mikrofonlar arasındaki ses uçuş sürelerinden, ses hızının sıcaklığa bağlılığını kullanarak bir oda kesitinin sıcaklık (ve karşılıklı yollarla hava akışı) haritasını çıkarmak.
> **Aile:** Akustik · **Yazılım payı:** ~%75 · **Yeni harcama (tahmin):** ~20–50 USD · **Yapay zekâ:** gerekmez

## Neden ilginç
Odaya tek bir termometre sokmadan sıcaklık dağılımını "duymak"; sensörsüz alan ölçümü.

## Araştırma soruları ve hipotezler
- **H1:** ESP32 + INMP441 tabanlı ucuz sistem, bir kutu/oda kesitinde sıcaklığı DS18B20 ızgarasına göre belirli bir hata sınırında verir.
- **H2:** Karşılıklı yolların toplamı sıcaklığı, farkı hava akışını ayırır (pencere açıkken).
- **H3:** Doğruluk, yol sayısı ve zamanlama hassasiyetiyle kuramın öngördüğü gibi değişir.

## Fizik
c ≈ 331,3·√(1 + T/273,15) m/s; yol integrali; tomografi (SIRT/en küçük kareler); Fresnel bölgesi ve çözünürlük; ses yansıması.
**Zamanlama gereksinimi (hesap):** 1 °C fark, 1 m yolda ~5 µs, 3,4 m yolda ~17 µs, 5 m yolda ~25 µs uçuş süresi farkı yaratır; 48 kHz örnekleme 20,8 µs → çapraz korelasyon + ara değerlemeyle alt-örnek çözünürlük şart.

## Deneyler
E1 kutuda ses hızı–sıcaklık kalibrasyonu · E2 karton kutu/oda kesitinde ısıtıcıyla 2B sıcaklık haritası vs DS18B20 ızgarası · E3 yol sayısı ve geometri etkisi · E4 pencere açık: akış ayrıştırması · E5 tek hoparlör + tek mikrofonla erken yansımalar (Dresden yöntemi) denemesi.

## Yazılım
Chirp üretimi ve eşleşmiş süzgeç, alt-örnek gecikme kestirimi, aynı saatli örnekleme (zaman eşlemesi sorunu yok), SIRT, görselleştirme.

## Donanım
**Yeni:** 4–8 INMP441 MEMS mikrofon, 4 küçük hoparlör + amfi, 8 DS18B20 (referans). **Mevcut:** ESP32 (I2S), Arduino, laptop.

## Yapay zekâ gerekli mi?
Hayır (SIRT). Çok az yolda ML kestirimiyle karşılaştırma isteğe bağlı.

## Öncül → kama
**Öncül:** TU Dresden akustik seyahat süresi tomografisi (1,33 × 1,0 × 1,27 m kutuda 0,1–0,37 °C sapma; laboratuvar sınıfı hoparlör), 2023 derlemesi (~90 makale), Leipzig 2015, EPFL 2008 tezi.
**Kama (bulamadım):** Tüketici sınıfı MEMS mikrofon/hoparlör ile sistemin doğruluğunun ölçülmesi ve karşılıklı yollarla akış ayrıştırmasının ucuz kurulumda gösterilmesi.

## Etkileyici gösteri
Odada ısıtıcı açılınca ekranda "sesle çizilen" sıcaklık haritasının değişmesi.

## Savunma / kritik altyapı anlatısı
Temassız sıcaklık/akış izleme (depo, sunucu odası, kazan içi akustik pirometri).

## Riskler
Zamanlama hassasiyeti, yankı, hoparlör gecikmesi → aynı saatli tasarım, chirp, kalibrasyon. Konum hatası (Dresden çalışması duyarlılığı vurguluyor).

## İlk pilot
ESP32 + bir hoparlör + iki mikrofon (1 m aralık): saç kurutma makinesiyle ısıtınca uçuş süresi farkı ölçülüyor mu?

## Kaynaklar
[TU Dresden ATOM](https://tu-dresden.de/ing/elektrotechnik/ias/aha/forschung/akustik/acoustic-tomography-applications-for-buildings-temperature-measurement) · [Derleme](https://fis.tu-dresden.de/portal/en/publications/acoustic-tomographic-reconstruction-of-temperature-and-flow-fields-with-focus-on-atmosphere-and-enclosed-spaces-a-review(62eb6305-65fa-49d7-8f86-4ddffce21ae4).html) · [DAGA 2024](https://pub.dega-akustik.de/DAGA_2024/files/upload/paper/371.pdf) · [Leipzig](https://ul.qucosa.de/id/qucosa:16698)
