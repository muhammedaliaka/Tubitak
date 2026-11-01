# P02 — Kağıthane Manyetometresi: Metronun ve Güneş Fırtınalarının Manyetik İzini Ayırmak

> **Tek cümle:** Ucuz bir manyetometreyle Kağıthane'de M7 metro hattının (1.500 V DC, viyadük) ürettiği manyetik alanı Biot–Savart modeliyle ölçüp, aynı veriden Güneş kaynaklı jeomanyetik değişimleri Kandilli'nin İznik gözlemevi (IZN) referansıyla ayırmak.
> **Aile:** Manyetizma/uzay havası · **Yazılım payı:** ~%70 · **Yeni harcama (tahmin):** ~30–60 USD · **Yapay zekâ:** gerekmez (karşılaştırma isteğe bağlı)

## Neden ilginç
Şehirdeki her ölçümün altında "görünmez" bir manyetik gürültü var; DC raylı sistemlerin gözlemevlerini onlarca km'den bozduğu biliniyor. Kimse evindeki manyetik alanı düşünmez, ama GNSS'siz navigasyon (manyetik harita eşleme) ve uzay havası izleme için bu gürültüyü ayırmak avantajdır.

## Araştırma soruları ve hipotezler
- **H1:** M7'de tren geçişleri, hatta uzaklıkla Biot–Savart'a uyan (tek tel 1/r, katener–ray çifti ~1/r²) bir manyetik iz bırakır.
- **H2:** Metro çalışmadığı saatler ve IZN referansı kullanılarak kentsel gürültü çıkarılınca, jeomanyetik günlük değişim (ve varsa fırtına) ucuz sensörle görülebilir.
- **H3:** Basit fizik modeli + Kalman filtresi, kentsel gürültüyü ML'e gerek kalmadan bastırır.

## Fizik
Biot–Savart, akım döngüsü/dipol alanı, kaçak (stray) akımlar, Dünya manyetik alanı ve bileşenleri, manyetosfer ve halka akımı (jeomanyetik fırtına), indüksiyon.
**Kaba hesap (illüstratif, varsayımlı):** Tren akımı 1–3 kA, katener–ray aralığı 5 m kabulüyle 100 m'de ~100–300 nT, 300 m'de ~11–33 nT, 500 m'de ~4–12 nT; dengesiz (kaçak) akımda tek tel modeli çok daha büyük değerler verir (100 m'de 2.000–6.000 nT). Gerçek değer ölçümle bulunacak. Orta enlemde güçlü bir jeomanyetik fırtına yüzlerce nT mertebesindedir (genel bilgi, doğrulanmadı).

## Deneyler
E1 sensör gürültüsü ve sıcaklık kayması (köpük kutu) · E2 M7 Kağıthane viyadüğünden 50–500 m uzaklıklarda tren geçişi ölçümü → B(r) eğrisi · E3 gece (metro kapalı, saatler doğrulanmalı) / gündüz karşılaştırması · E4 IZN (İznik, Kağıthane'ye ~96 km) ile korelasyon, fark sinyali · E5 Kalman/regresyon ile gürültü bastırma; ML ile karşılaştırma.
**Uzantı (isteğe bağlı):** Çift frekanslı GNSS'li bir telefonla iyonosfer toplam elektron içeriği (TEC) ölçümü; büyük ölçekte telefonlarla iyonosfer haritalama yapılmış bir Google çalışması var (Nature 2024, kendi bilgim, bu oturumda doğrulamadım).

## Yazılım
ESP32 firmware (yüksek örnekleme, zaman damgası), tren olayı tespiti, Biot–Savart model uydurma, Kalman filtresi, IZN verisiyle eşleme, panel (canlı grafik, mevcut küçük ekranda da gösterilebilir).

## Donanım
**Yeni:** RM3100 (veya MMC5983MA) manyetometre modülü (QMC5883L gibi çok ucuz sensörler yüzlerce nT gürültülü olabilir; doğrulanmadı). **Mevcut:** ESP32/Arduino, ekran, laptop; telefon (phyphox ile ön ölçüm).

## Yapay zekâ gerekli mi?
Hayır; fizik modeli + Kalman. ML yalnızca karşılaştırma için.

## Öncül → kama
**Öncül:** DC demiryolu alanlarının gözlemevlerini onlarca km'den etkilediği (2007 modelleme), Pekin gözlemevinde uyarlanır Kalman ile bastırma (2021), Roma yakınında akıllı telefonla DC demiryolu alanı ölçümü (fizik eğitimi, 2020), Utrecht/Delft hafif raylı sistem azaltma çalışması.
**Kama (bulamadım):** İstanbul M7'nin (1.500 V DC, viyadük) uzaklığa bağlı manyetik izinin ucuz sensörle haritalanması ve IZN referansıyla jeomanyetik sinyalden ayrılması.

## Etkileyici gösteri
Canlı grafik: her tren geçişinde sıçrama + Biot–Savart eğrisi üst üste; gece sessizliği; IZN ile aynı günlük dalga.

## Savunma / kritik altyapı anlatısı
Uzay havası GNSS, HF haberleşme ve elektrik şebekesini etkiler; kentsel manyetik gürültü haritası manyetik navigasyon için gereklidir.

## Riskler
Fırtına 6 haftada garanti değil (ama metro izi her gün var → sonuç garantili). IZN dakikalık veriye erişim doğrulanmadı (Kandilli bültenleri resmî başvuru diyor; INTERMAGNET portalı kontrol edilecek). Bina demiri, sıcaklık kayması. **Güvenlik:** yalnızca kamuya açık alanlarda, raylara yaklaşmadan ölçüm.

## İlk pilot (sıfır maliyet)
Telefonda phyphox manyetometresiyle M7 Kağıthane viyadüğüne 50–100 m mesafeden 10 dk kayıt: tren geçişlerinde sıçrama görünüyor mu?

## Kaynaklar
[M7 (Wikipedia)](https://en.wikipedia.org/wiki/M7_(Istanbul_Metro)) · [Kağıthane istasyonu](https://en.wikipedia.org/wiki/Ka%C4%9F%C4%B1thane_(Istanbul_Metro)) · [Demiryolu manyetik alanları (arXiv 2020)](https://arxiv.org/pdf/2006.06481) · [Pekin gözlemevi (EPS 2021)](https://earth-planets-space.springeropen.com/articles/10.1186/s40623-021-01428-x) · [TU Delft hafif raylı](https://tudelft.nl/2020/tnw/pieter-kruit-et-al-published-paper-on-reducing-the-magnetic-fields-around-dc-light-rail-systems) · [Kandilli IZN](https://jeomanyetizma.bogazici.edu.tr/sites/jeomanyetizma.boun.edu.tr/files/u145/jeoman_deprem_bilgi_eng.pdf)
