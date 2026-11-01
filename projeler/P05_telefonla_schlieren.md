# P05 — Telefonla Görünmez Havayı Ölçmek: Arka Plan Tabanlı Schlieren ile Sıcaklık Alanı

> **Tek cümle:** Rastgele noktalı bir arka planın önündeki sıcak havanın kırılma indisi değişimini telefon videosundaki piksel kaymalarından ölçüp, mum/ısıtıcı dumanının sıcaklık alanını nicel olarak çıkarmak ve termokuplla doğrulamak.
> **Aile:** Optik/akışkan · **Yazılım payı:** ~%80 · **Yeni harcama (tahmin):** ~5–20 USD · **Yapay zekâ:** gerekmez (karşılaştırma isteğe bağlı)

## Neden ilginç
Görünmeyen hava akışını ve ısıyı yalnızca telefonla görmek; pahalı schlieren aynaları yerine yazıcıdan çıkmış bir kâğıt.

## Araştırma soruları ve hipotezler
- **H1:** Telefon BOS ölçümü, eksenel simetrik bir mum/ısıtıcı dumanında Abel tersine çevirmeyle sıcaklık profilini termokupla göre belirli bir hata sınırında verir (eşik pilot sonrası).
- **H2:** Duyarlılık, nesne–arka plan uzaklığı ve odak uzaklığıyla kuramın öngördüğü gibi ölçeklenir.
- **H3:** Klasik optik akış (çapraz korelasyon/Farnebäck) öğrenilmiş optik akışa (ör. RAFT) göre yeterlidir.

## Fizik
Gladstone–Dale bağıntısı (n − 1 = K·ρ, hava için K ≈ 2,26×10⁻⁴ m³/kg), ideal gaz yasası, ışın sapması ε ≈ ∫ (1/n) ∂n/∂y dz, Abel dönüşümü, kırınım/odak derinliği sınırları.

## Deneyler
E1 duyarlılık–geometri ölçümü · E2 mum ve sıcak plaka dumanı: Abel ile sıcaklık profili vs termokupl (MAX6675 + K tipi) · E3 saç kurutma makinesi jeti (hız/sıcaklık) · E4 kamera ayarları (pozlama, sıkıştırma) hatası · E5 klasik vs öğrenilmiş optik akış karşılaştırması.

## Yazılım
Video çerçeve hizalama, optik akış/PIV, sapma → kırılma indisi gradyanı → Poisson/Abel çözümü → yoğunluk ve sıcaklık, belirsizlik yayılımı.

## Donanım
**Yeni:** Termokupl + MAX6675 modülü, yazdırılmış rastgele nokta deseni. **Mevcut:** telefon, laptop, Arduino.

## Yapay zekâ gerekli mi?
Hayır. ML optik akış yalnızca karşılaştırma (H3).

## Öncül → kama
**Öncül:** Pocket Schlieren (telefonda BOS platformu, arXiv 2404.16060), telefonla BOS (Experiments in Fluids 2019), tüketici donanımıyla jet egzozu BOS (Aeronautical Journal 2025), Hargather & Settles derlemesi; **bir lise projesi (Smuts) telefonla eksenel simetrik akışta yoğunluk ölçmüş.**
**Kama:** Termokupl ile tam belirsizlik bütçeli nicel doğrulama ve kamera ayarlarının hataya etkisi; klasik vs ML karşılaştırması. Öncül lise düzeyinde de olduğu için kama orta-zayıf.

## Etkileyici gösteri
Elden yükselen ısının, mum alevinin, nefesin canlı görüntüsü + renkli sıcaklık haritası.

## Savunma anlatısı
BOS havacılıkta şok dalgası ve egzoz izi görüntülemede kullanılıyor (tüketici donanımıyla jet egzozu çalışması mevcut).

## Riskler
Titreşim, kamera otomatik ayarları (pro modla kilitle), telefon video sıkıştırması; düşük kama.

## İlk pilot (sıfır maliyet)
Rastgele nokta deseni yazdır, önüne mum koy, telefonla çek, OpenCV ile piksel kaymasını çiz.

## Kaynaklar
[Pocket Schlieren](https://arxiv.org/pdf/2404.16060) · [Telefonla BOS (Exp Fluids)](https://link.springer.com/doi/10.1007/s00348-019-2817-z) · [Tüketici donanımıyla BOS](https://resolve-he.cambridge.org/core/services/aop-cambridge-core/content/view/EB19D7F4099333BE38A83CDFF26B54B0/S0001924024001192a.pdf/onboard-background-oriented-schlieren-imaging-using-consumer-grade-hardware.pdf) · [Hargather derlemesi](https://nmt.edu/academics/mecheng/faculty/mhargather/docs/Mier2016.pdf) · [Lise projesi (Smuts)](https://abstracts.societyforscience.org/Home/PrintPdf/15428)
