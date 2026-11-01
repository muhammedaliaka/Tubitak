# P04 — Kâğıdın Parmak İzi: Lazer Benek Deseniyle Ucuz ve Kopyalanamaz Belge Doğrulama

> **Tek cümle:** Kâğıt/plastik yüzeyin mikroskobik pürüzünün lazerle oluşturduğu benek desenini lensi sökülmüş bir webkamerayla okuyup, aynı nesneyi tanımak ve kopyasını reddetmek.
> **Aile:** Dalga optiği · **Yazılım payı:** ~%75 · **Yeni harcama (tahmin):** ~20–80 USD · **Yapay zekâ:** gerekmez (karşılaştırma isteğe bağlı)

## Neden ilginç
QR/barkod kopyalanabilir; malzemenin kendi pürüzü kopyalanamaz. Sahte belge/etiket/parça sorununa ek etiket gerektirmeyen bir fiziksel kimlik.

## Araştırma soruları ve hipotezler
- **H1:** Ucuz okuyucuyla aynı kâğıdın tekrar okumaları (iç mesafe) ile farklı kâğıtlar (dış mesafe) istatistiksel olarak net ayrışır.
- **H2:** Fotokopi/fotoğraf baskısı kopyalar dış mesafe dağılımına düşer (reddedilir).
- **H3:** Kimlik, buruşturma/ıslanma/zamana karşı belirli bir sınıra kadar dayanır; açı toleransı ölçülebilir.

## Fizik
Koherans, girişim, benek istatistiği (tam gelişmiş benekte yoğunluk dağılımı üstel, kontrast 1), benek boyutu.
**Hesap:** Lenssiz (nesnel) benek s ≈ λz/D: 650 nm, z = 3 cm, 1 mm leke → ~20 µm (0,5 mm leke → ~39 µm); webkamera pikseli birkaç µm → rahat çözülür. Telefon lensiyle (öznel) benek ~3 µm, piksel boyutuna yakın: sınırda.

## Deneyler
E1 benek boyutu/kontrastının kuramla karşılaştırması · E2 30 tekrar × 50 farklı kâğıt (iç/dış Hamming dağılımı, yanlış kabul/ret) · E3 kopya testi · E4 buruşturma, nem, sıcaklık, 2–4 hafta yaşlanma · E5 açı/konum toleransı.

## Yazılım
Görüntü yakalama, hizalama, öznitelik (Gabor/faz), bulanık çıkarıcı (fuzzy extractor) ile anahtar, istatistik raporu, NIST rastgelelik testleri, basit doğrulama arayüzü.

## Donanım
**Yeni:** Class 2 lazer modülü (650 nm, <1 mW), lensi sökülebilir ucuz webkamera, ahşap/alüminyum profil vidalı düzenek (3D yazıcı gerekmez). **Mevcut:** laptop.

## Yapay zekâ gerekli mi?
Hayır. CNN ile karşılaştırma isteğe bağlı (Evren görüntü eğitimine uygun).

## Öncül → kama
**Öncül:** Buchanan ve ark., Nature 436, 475 (2005): lazerle taranan kâğıt yüzeyi, dört açıdan dedektör, 200–500 bayt parmak izi; takipler IEEE S&P 2009, CCS 2011 (haber/özet).
**Kama (bulamadım):** Webkamera düzeyinde okuyucuyla Hamming dağılımı + yaşlanma + açı sağlamlığını birlikte ölçen açık kodlu çalışma.

## Etkileyici gösteri
Aynı paketten iki A4'ü ayırt edip fotokopisini reddeden canlı okuyucu.

## Savunma anlatısı
Sahte belge, kimlik kartı, etiket ve parça doğrulama.

## Riskler
Okuma tekrarlanabilirliği (dar açı toleransı) → sağlam düzenek + hizalama yazılımı. **Lazer güvenliği:** yalnızca Class 2, göze doğrultma yok, danışmanla kural.

## İlk pilot (sıfır/çok düşük maliyet)
Lazer işaretçi + telefon: aynı kâğıdı 20 kez, 20 farklı kâğıdı birer kez çek; korelasyon dağılımları ayrışıyor mu?

## Kaynaklar
[Royal Holloway – Nature 2005 kaydı](https://pure.royalholloway.ac.uk/en/publications/forgery-fingerprinting-documents-and-packaging/) · [ScienceDaily 2005](https://www.sciencedaily.com/releases/2005/07/050731233046.htm) · [Kâğıt parmak izi arXiv 2017](https://eprints.whiterose.ac.uk/116192/1/1705.02510.pdf) · [Optik PUF arXiv](https://arxiv.org/pdf/2109.03505)
