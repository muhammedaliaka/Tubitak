# P07 — Sisi Kameradan Ölçmek: Kağıthane'den Gökdelenlerle Koschmieder Yasası mı, Yapay Zekâ mı?

> **Tek cümle:** Kağıthane'den bilinen uzaklıktaki gökdelenlere (Levent ~3,3 km, Maslak ~5,2 km, Çamlıca Kulesi ~10,2 km; yaklaşık) bakan sabit bir telefon kamerasıyla görüş mesafesini Koschmieder yasasıyla ölçmek, havalimanı METAR değerleriyle doğrulamak ve derin öğrenmeyle kıyaslamak.
> **Aile:** Atmosfer optiği · **Yazılım payı:** ~%85 · **Yeni harcama (tahmin):** ~0–20 USD · **Yapay zekâ:** araştırma sorusunun kendisi ("gerekli mi?")

## Neden ilginç
İstanbul Boğazı kısıtlı görüş (sis) nedeniyle Kıyı Emniyeti tarafından gemi trafiğine zaman zaman kapatılıyor (2023–2026 haberleri). Her balkondaki eski telefonun bir görüş mesafesi sensörü olabilmesi.

## Araştırma soruları ve hipotezler
- **H1:** Çok uzaklıklı yer işaretlerinin kontrastı Koschmieder modeline (C = C₀·e^(−σd)) uyar; tek σ tüm işaretlerde tutarlıdır.
- **H2:** Fizik tabanlı kestirim, METAR görüşüyle belirli bir hata sınırında uyuşur.
- **H3:** Bu veri boyutunda derin öğrenme fizik modelini anlamlı biçimde geçmez (ya da geçer: hangisi çıkarsa bulgu).

## Fizik
Beer–Lambert sönümü, Koschmieder bağıntısı (V ≈ 3,912/σ, %2 kontrast eşiği), hava ışığı (airlight), Mie saçılması, nem ve aerosol.

## Deneyler / analizler
E1 kamera pozlama kilidi ve doğrusallık (gamma) kalibrasyonu · E2 her dakika zaman atlamalı çekim (Kasım–Aralık) · E3 çok işaretli σ kestirimi · E4 METAR (IST/SAW) ve MGM ile karşılaştırma · E5 Evren'de CNN eğitimi ve fizik modeliyle karşılaştırma.

## Yazılım
Görüntü kayıt hizalama, işaret bölgeleri, kontrast ölçümü, doğrusal olmayan uydurma, METAR çekme/eşleme, ML hattı (gerekirse).

## Donanım
**Mevcut:** eski telefon (veya ESP32-CAM), şarj, sabit montaj, laptop. **Yeni:** gerekmeyebilir.

## Yapay zekâ gerekli mi?
Projenin merkez sorusu. Önce fizik; ML yalnızca karşılaştırma için (Evren görüntü eğitimine uygun).

## Öncül → kama
**Öncül:** KNMI 2015 fizibilite raporu (iki uzaklıkta Koschmieder kontrastı), Sládek 2023 (statik webkameralarla kNN), DMRVisNet (Koschmieder'i ağın içine koyan CNN, sentetik veri), visIvis (operasyonel).
**Kama (bulamadım):** Gerçek kamera verisinde çok uzaklıklı Koschmieder ile derin öğrenmenin doğrudan karşılaştırması; İstanbul kentsel ufku.

## Etkileyici gösteri
Zaman atlamalı video: gökdelenler kaybolurken ekrandaki görüş mesafesi göstergesi düşüyor; METAR eğrisi üst üste.

## Savunma / kritik altyapı anlatısı
Deniz ve hava ulaşımı güvenliği; elektro-optik sensörlerin görüş koşulları.

## Riskler
Görüş hattı balkona göre değişir (uzaklıklar harita üzerinden yaklaşık hesaplandı). Kasım–Aralık'ta yoğun sis garanti değil → pus, yağmur ve nem de görüşü değiştirir; sürekli bir aralık elde edilir. Kamera otomatik ayarları, cam yansıması. Mahremiyet: yalnızca manzara, kişi görüntüsü yok.

## İlk pilot (sıfır maliyet)
Bir gün dakikada bir manzara fotoğrafı; 3–5 işaretin kontrastından σ hesapla; işaretler arası tutarlılığa bak.

## Kaynaklar
[KNMI 2015](https://cdn.knmi.nl/knmi/pdf/bibliotheek/knmipubIR/IR2015-05.pdf) · [DMRVisNet](https://arxiv.org/pdf/2112.04278) · [visIvis (EMS 2021)](https://meetingorganizer.copernicus.org/EMS2021/EMS2021-69.html) · [Sládek 2023](https://www.citedrive.com/en/discovery/application-of-k-nearest-neighbor-classification-for-static-webcams-visibility-observation) · [Boğaz sis kapatması (NTV)](https://www.ntv.com.tr/galeri/turkiye/istanbulda-yogun-sis-bogazda-gemi-trafigi-durduruldu,SfaN5LWaNUaKMF3aMR7rVQ)
