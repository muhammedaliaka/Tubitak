# P11 — Isıl İmza Nasıl Gizlenir? Ucuz Termal Kamerayla Yayınırlık ve Tespit Menzili Ölçümü

> **Tek cümle:** 32×24 pikselli ucuz bir termal kamerayla (MLX90640) farklı malzemelerin yayınırlığını, açıya bağlılığını ve folyo battaniye gibi örtülerin ısıl imzayı nasıl değiştirdiğini ölçüp, sıcak bir hedefin tespit menzilini piksel doluluğu modeliyle tahmin etmek.
> **Aile:** Isıl ışınım · **Yazılım payı:** ~%65 · **Yeni harcama (tahmin):** ~50–80 USD · **Yapay zekâ:** gerekmez

## Neden ilginç
Termal kameralar her şeyi "görür" sanılır; oysa parlak metal yüzeyler çevreyi yansıtır. Deprem sonrası termal dronla arama yapılırken folyo battaniyenin kişiyi gizleyip gizlemediği de aynı fiziktir.

## Araştırma soruları ve hipotezler
- **H1:** Referans bant yöntemiyle 10 malzemenin yayınırlığı ucuz kamerayla belirli bir hata sınırında ölçülür.
- **H2:** Metallerde ve yalıtkanlarda yayınırlığın açıya bağlılığı kuramın öngördüğü farklı davranışı gösterir.
- **H3:** Sıcak bir hedefin görünür kontrastı uzaklıkla piksel doluluk modeline uygun düşer; folyo örtü tespit menzilini nicel olarak azaltır.

## Fizik
Stefan–Boltzmann, Planck/Wien (8–14 µm), Kirchhoff (opak cisimde ε = 1 − ρ), yansıyan arka plan terimiyle görünür sıcaklık denklemi, açıya bağlı yayınırlık, anlık görüş alanı (IFOV).
**Hesap:** 55° FOV / 32 piksel → piksel başına ~1,7°; 0,5 m genişliğinde hedef tek bir pikseli ~17 m'de doldurur (110° modelde ~8 m). Ötesinde kontrast piksel doluluğuyla azalır.

## Deneyler
E1 kamera gürültüsü ve doğruluğu · E2 sıcak su kabında (≤ 60 °C) referans bantla 10 malzemenin yayınırlığı · E3 açı taraması (0–80°) · E4 folyo battaniye: katman, hava boşluğu, zamanla ısınma · E5 hedef–uzaklık deneyi vs piksel doluluk modeli.

## Yazılım
ESP32/laptop ile görüntü alma, kalibrasyon, yayınırlık çözümü, görselleştirme (**mevcut küçük ekranda canlı termal görüntü**), model uydurma.

## Donanım
**Yeni:** MLX90640 modülü, DS18B20/termokupl, elektrik bandı (referans), malzemeler (folyo, folyo battaniye, karton, kumaş, boya). **Mevcut:** ESP32, ekran, laptop.

## Yapay zekâ gerekli mi?
Hayır.

## Öncül → kama
**Öncül:** Yayınırlık ölçümü ve ısıl kamuflaj genel olarak iyi bilinir; MLX90640 özellikleri (32×24, ~±1 °C, 55°/110° FOV) üretici belgelerinde.
**Kama (bulamadım):** Ucuz termal kamerayla yayınırlık + açı + folyo örtü + piksel doluluğuna dayalı tespit menzili modelinin birlikte doğrulandığı bir çalışma.

## Etkileyici gösteri
Canlı termal görüntüde folyo battaniyenin altındaki sıcak kabın "kaybolması"; parlak metalin oda sıcaklığını yansıtması.

## Savunma / arama-kurtarma anlatısı
Isıl imza yönetimi; termal dronla arama-kurtarmada örtülerin etkisi.

## Riskler
Düşük çözünürlük ve ±1 °C doğruluk; yansıma (fiziğin kendisi). **Güvenlik:** sıcak yüzeyler ≤ 60 °C; çocuk/insan üzerinde deney yapılmaz (hedef sıcak su kabı).

## İlk pilot
Sıcak bir kupaya yarım elektrik bandı yarım folyo yapıştır; termal kamerada iki yarının farkı.

## Kaynaklar
[MLX90640 veri sayfası](https://media.melexis.com/-/media/files/documents/datasheets/MLX90640-datasheet-melexis.pdf) · [Waveshare MLX90640](https://www.waveshare.com/wiki/MLX90640-D110_Thermal_Camera) · [Adafruit MLX90640](https://learn.adafruit.com/mlx90640-thermal-image-recording/overview)
