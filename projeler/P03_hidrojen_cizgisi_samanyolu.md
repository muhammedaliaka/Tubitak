# P03 — Kağıthane'den Samanyolu'nun Dönüşünü Ölçmek: Karton Antenle 21 cm Hidrojen Çizgisi

> **Tek cümle:** Karton + alüminyum folyo boynuz anten ve RTL-SDR ile galaksideki nötr hidrojenin 1420 MHz yayınını alıp, Doppler kaymasından Samanyolu'nun dönme eğrisini çıkarmak ve görünür kütleyle karşılaştırmak.
> **Aile:** Radyo astronomi/SDR · **Yazılım payı:** ~%70 · **Yeni harcama (tahmin):** ~100–150 USD (RTL-SDR P01 ile ortak) · **Yapay zekâ:** gerekmez

## Neden ilginç
"Evin balkonundan galaksinin dönüşünü ölçmek" çok etkileyici; fiziği lise müfredatıyla (Doppler, kütle çekimi) doğrudan bağlı.

## Araştırma soruları ve hipotezler
- **H1:** Kağıthane'nin kentsel radyo gürültüsünde 21 cm çizgisi karton boynuzla ölçülebilir.
- **H2:** Teğet nokta yöntemiyle elde edilen dönme eğrisi, yayımlanmış eğrilerle (ör. Clemens 1985) belirsizlik içinde uyumludur.
- **H3:** Ölçülen eğri yalnızca görünür kütleyle açıklanamaz ("eksik kütle" göstergesi; **dikkat:** az noktalı iç galaksi eğrisi karanlık madde için zayıf kanıttır, sınırlı kapsamda sunulmalı).

## Fizik
Hidrojen ince yapı geçişi (1420,405 MHz), Doppler, galaktik dönme ve teğet nokta yöntemi, v² = GM(r)/r, boynuz anten kazancı ve ışın genişliği (18,6 dBi boynuz ≈ 24° ışın, kaba hesap), radyometre denklemi.

## Deneyler
E1 boynuz yapımı ve Güneş geçişiyle ışın ölçümü · E2 galaktik boylam l = 10°–90° (Kağıthane'den görülen ilk çeyrek) taraması · E3 dönme eğrisi ve belirsizlik · E4 kütle profili ve görünür kütle modeliyle karşılaştırma · E5 kentsel RFI (radyo girişimi) ölçümü.

## Yazılım
Frekans anahtarlamalı/yük referanslı spektrum ortalama, taban çizgisi düzeltme, yerel durgunluk standardına (LSR) çevirme, teğet hız çıkarımı, eğri uydurma, astronomik koordinat dönüşümü (astropy).

## Donanım
**Yeni:** RTL-SDR V4 (P01 ile ortak), H-çizgisi LNA + filtre modülü, karton/folyo boynuz, boya kutusu dalga kılavuzu besleme, koaksiyel. **Mevcut:** laptop.

## Yapay zekâ gerekli mi?
Hayır.

## Öncül → kama
**Öncül (yaygın!):** Harvard lisans projesi (karton-folyo boynuz, 6 hafta, Clemens 1985 ile uyumlu eğri), Pandian ve ark. (RTL-SDR ile dönme eğrisi, arXiv 2202.11039), 2025 piramidal boynuz (arXiv 2512.19262), tahıl kutusundan teleskop.
**Kama (zayıf):** İstanbul kentsel RFI'sinin nicel etkisi, belirsizlik bütçesi; yalnızca "tekrar" olmaması için kentsel ölçüm ve hata analizi öne çıkarılmalı.

## Etkileyici gösteri
Canlı spektrumda hidrojen tümseği; boylam değiştikçe kayan tepe; balkondan çizilmiş galaksi dönme eğrisi.

## Savunma anlatısı
Zayıf sinyal algılama, radyometre ve spektrum izleme teknikleri (ör. pasif algılama). Zayıf bir anlatı; bu projenin gücü bilimsel.

## Riskler
**Öncül çok yaygın** → özgünlük eleştirisi; kentsel RFI; işaretleme doğruluğu (telefon eğim/pusula ile). Aralık akşamlarında galaktik merkez bölgesi Güneş'e yakın (l ≈ 0°'ın yakınından kaçınılmalı).

## İlk pilot
Boynuzu Kuğu (Cygnus) bölgesine (l ≈ 60–80°) çevirip 5–10 dk ortalama: 1420,4 MHz civarında tümsek var mı?

## Kaynaklar
[Harvard boynuz posteri](https://lweb.cfa.harvard.edu/%7Enpatel/hornAntennaAASposterPDF2.pdf) · [Pandian ve ark.](https://ar5iv.labs.arxiv.org/html/2202.11039) · [arXiv 2512.19262](https://arxiv.org/pdf/2512.19262) · [Tahıl kutusu teleskop](https://www.rtl-sdr.com/a-hydrogen-line-telescope-made-from-cereal-boxes-and-an-rtl-sdr/) · [Açık kaynak H-çizgisi teleskop](https://www.rtl-sdr.com/building-an-open-source-sdr-based-hydrogen-line-radio-telescope/)
