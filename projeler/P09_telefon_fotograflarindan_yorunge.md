# P09 — Üç Telefon Fotoğrafından Uydu Yörüngesi: Gauss Yöntemiyle Kağıthane'den Uzay Gözetimi

> **Tek cümle:** Gece gökyüzünde geçen parlak bir uydunun (ISS, Starlink, roket gövdesi) telefonla çekilmiş birkaç fotoğrafından yıldızlara göre konumunu ölçüp, Gauss'un 1801'de Ceres için kullandığı yöntemle yörüngesini hesaplamak ve TLE ile karşılaştırmak.
> **Güncel:** P01 ile birleştirildi ve seçildi → `uydu-isik-radyo/PLAN.md`.
> **Aile:** Optik astrometri/gök mekaniği · **Yazılım payı:** ~%80 · **Yeni harcama (tahmin):** ~10–30 USD (tripod) · **Yapay zekâ:** gerekmez

## Neden ilginç
Telefon + tripodla "uzay gözetimi"; P01 (radyo Doppler) ile birleşirse aynı uyduyu hem ışıkla hem radyoyla ölçmek.

## Araştırma soruları ve hipotezler
- **H1:** Telefon fotoğrafları plaka çözümüyle (astrometry.net) uydu izinin uç noktalarını belirli bir açısal doğrulukla verir.
- **H2:** Pozlama başlangıç zamanının belirsizliği (deklanşör gecikmesi) baskın hata kaynağıdır ve kalibre edilebilir.
- **H3:** Yalnızca açılı gözlemlerle Gauss yöntemi, yörünge elemanlarını TLE'ye göre belirli bir hata sınırında verir; gözlemler arası süre 2–5 dk olduğunda hata en küçük olur (yayımlanmış benzetimle uyumlu).

## Fizik
Kepler yasaları, iki cisim problemi, yalnız açılı yörünge belirleme (Gauss/Laplace), astrometri, zaman ölçümü.

## Deneyler
E1 plaka çözüm doğruluğu · E2 deklanşör zamanlama kalibrasyonu (GNSS saatli ekranı fotoğraflama vb.) · E3 ISS/Starlink geçişlerinde yörünge belirleme · E4 gözlem aralığı ve sayısının etkisi · E5 (P01 ile) aynı uydunun radyo Doppler'iyle karşılaştırma.

## Yazılım
İz uç noktası bulma, plaka çözümü, Gauss/Gooding çözücü, SGP4 ile TLE karşılaştırması, belirsizlik analizi.

## Donanım
**Mevcut:** telefon (manuel/uzun pozlama modu), laptop. **Yeni:** tripod, telefon tutucu.

## Yapay zekâ gerekli mi?
Hayır.

## Öncül → kama
**Öncül:** Cal Poly tezi (8 inç teleskop + DSLR, ~4.000 USD; Gauss Extended varyantları en iyi durumda TLE'ye %0,02 yakın), KASI 0,6 m teleskop, Bridgewater lisans projesi (Python, benzetim verisi); klasik yöntemlerin küçük yörüngelerde zayıf kaldığı notu (UB).
**Kama (bulamadım):** Yalnızca telefonla (teleskopsuz), deklanşör zamanlama kalibrasyonlu, İstanbul ışık kirliliğinde yörünge belirleme ve hata bütçesi.

## Etkileyici gösteri
Üç fotoğraftan çizilen yörünge çemberi Dünya üzerinde döner; TLE yörüngesiyle üst üste.

## Savunma anlatısı
Uzay durumsal farkındalığı (uydu takibi).

## Riskler
Bulut; alçak yörünge uyduları yalnızca alacakaranlık saatlerinde (uydu güneşte, gözlemci karanlıkta) görülür; deklanşör zamanlaması; ışık kirliliği (parlak uydular yeterli).

## İlk pilot
Bir ISS veya parlak Starlink geçişinde 3–5 uzun pozlama; bir fotoğrafı plaka çöz.

## Kaynaklar
[Cal Poly tezi](https://digitalcommons.calpoly.edu/theses/2951) · [Gözlem aralığı (IAC-09)](https://iafastro.directory/iac/archive/browse/IAC-09/A6/1/4563/) · [Gauss hata duyarlılığı](https://koreascience.kr/article/JAKO200411722661755.pub) · [Bridgewater projesi](https://vc.bridgew.edu/honors_proj/724) · [Klasik yöntemler (UB)](https://diposit.ub.edu/items/72096297-492f-443d-8297-051b7d505487/full)
