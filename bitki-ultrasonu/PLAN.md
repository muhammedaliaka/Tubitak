# Bitkilerin Ultrasonik "Susuzluk Sesi": Ucuz ve Açık Donanımla Tespit, Menzil Sınırları ve Erken Uyarı

> **Durum: ADAY FİKİR (#2).** Fikir seçimi sürüyor. Bu plan, seçilirse hemen başlamak için hazırlandı.
> **Hazırlanma tarihi:** 1 Kasım 2026 · **Hedef:** TÜBİTAK 2204-A (58. dönem), son başvuru **4 Ocak 2027, 17:30**.
> **Karar tarihi:** Fikir en geç **7 Kasım**'da kesinleşmeli. Ana bitki deneyi en geç **23 Kasım** haftasında başlamalı.

---

## 1. Tek cümlelik özet

Stresli bitkilerin havaya yaydığı ultrasonik tıkırtılar (Khait ve ark., Cell 2023) **3.000 TL altında, açık kaynak bir düzenekle** duyulabilir mi, kaç metreye kadar, ve bu tıkırtılar toprak nemi ve saksı ağırlığı gösterge vermeden **önce** başlıyor mu?

## 2. Araştırma soruları ve hipotezler

| Kod | Hipotez | Nasıl sınanır |
|---|---|---|
| H1 | Susuz bırakılan domateslerde, sulanan kontrollere göre saatte anlamlı derecede fazla ultrasonik olay vardır. | E3, grup karşılaştırması |
| H2 | Olay oranı, bitkinin su kaybıyla (saksı ağırlığı) birlikte artar ve görünür solmadan önce başlar. | E3, zaman serisi |
| H3 | Düşük maliyetli mikrofonun menzili, yayılma kaybı + atmosferik soğurma + gürültü tabanıyla öngörülebilir. | E1, E2 ve bağlantı bütçesi modeli |
| H4 | Açık veri setiyle eğitilen dedektör, mikrofon tepkisi ve gürültü simüle edilerek bizim donanımımıza aktarılabilir. | E4, alan kayması (domain shift) deneyi |

> **Olumsuz sonuç da geçerli sonuçtur.** H1 reddedilirse proje "ucuz donanımla tespit sınırları" raporuna dönüşür. Rehber öz eleştiri ve dürüstlüğü açıkça ister.

## 3. Günlük ihtiyaç bağlantısı

Saksı bitkisi olan biri yılda yaklaşık 50 kez "bitkim susadı mı?" sorusuyla karşılaşır (haftalık sulama). Toprak nemi sensörleri toprağı ölçer, bitkinin fizyolojik durumunu değil. Bitkinin kendi sinyalini dinlemek bu boşluğu hedefler. Kritik bir not: bu iddia hâlâ **araştırma sorusudur**, kanıtlanmış bir üstünlük değildir. Bazı yorumcular toprak nemi ve mevcut stres yöntemlerinin zaten yeterli olduğunu savunuyor. Projenin H2'si bu eleştiriye doğrudan cevap verir.

---

## 4. Doğrulama durumu (dürüst tablo)

| Bilgi | Durum |
|---|---|
| Stresli domates ve tütün 40–80 kHz'de tıkırtı yayar (Khait ve ark., Cell, 30 Mart 2023) | Yayın kaydı doğrulandı; metin okunamadı |
| ~65 dB SPL @ 10 cm | İkincil kaynak (ön baskı özeti), **teyitsiz** |
| Tıkırtı sayısı: domates kuraklık ~35/saat, kesilmiş ~25/saat; tütün kuraklık ~11/saat, kesilmiş ~15/saat | İkincil kaynak (sci.news ön baskı özeti), **teyitsiz** |
| Orijinal mikrofon: CM16 tipi ultrason kondansatör mikrofon, ~10 cm | İkincil kaynak, **teyitsiz** |
| "3–5 m'den duyulur" | Tek haber kaynağı, **zayıf** |
| Sınıflandırma doğruluğu | **Doğrulanamadı.** Önceki mesajlarda geçen "%70–84" rakamını kullanmayın. |
| Açık veri seti (Dryad, CC0, ~10 MB, 500 kHz, 2 ms klipler, kontrol gürültüsü dahil) | Metadata doğrulandı; **indirilemedi** (API kimlik istedi, web bağlantısı 403) |
| Mekanizma | Muhtemelen ksilem kavitasyonu, ancak **kesin değil** (Zweifel & Zeugin 2008). "Mekanizmayı kanıtladık" demeyin; "strese bağlı ultrasonik olay" deyin. |

**Yapılacak:** Dryad zip'ini tarayıcıdan indirip depoya koyun (`data/` altında; CC0). İlk iş olarak klip spektrumları, süreleri ve genlik dağılımı analiz edilmeli. Bu analiz mikrofon bandını ve kazancı somutlaştırır.

---

## 5. Fizik

### 5.1 Kaynak
Ksilemde su negatif basınç altındadır. Hava kabarcığı oluşunca (kavitasyon) gerilim aniden boşalır ve kısa bir akustik darbe doğar. Darbe gövdeden havaya geçer; empedans uyumsuzluğu nedeniyle havadaki seviye düşüktür.

### 5.2 Havada soğurma
ISO 9613-1 formülüyle hesaplandı (20 °C). **Not:** Standart resmen 10 kHz'e kadar doğrulanmıştır, 40–80 kHz için ekstrapolasyondur. 10 kHz (0,16 dB/m) ve 40 kHz (~1,3 dB/m) literatür değerleriyle tutarlıdır. E1 deneyi bu ekstrapolasyonu sınar.

| Frekans | %30 nem | %50 nem | %70 nem |
|---|---|---|---|
| 20 kHz | 0,60 | 0,52 | 0,42 |
| 40 kHz | 1,07 | 1,32 | 1,29 |
| 60 kHz | 1,47 | 1,98 | 2,17 |
| 80 kHz | 1,96 | 2,61 | 3,00 |

(dB/m)

### 5.3 Bağlantı bütçesi (MODEL, varsayımlı)
Girdiler: kaynak 55/65/70 dB SPL @ 10 cm; mikrofon+yükselteç gürültü tabanı **35/45/55 dB SPL (bilinmiyor, ölçülecek)**; gereken SNR 10 dB; %50 nem; 60 kHz. Yayılma: küresel (−20·log₁₀ r).

| Kaynak | Gürültü tabanı | Çıplak mikrofon | 20 dB yansıtıcı | 30 dB yansıtıcı |
|---|---|---|---|---|
| 65 dB | 35 dB | 0,84 m | 4,1 m | 6,8 m |
| 65 dB | 45 dB | 0,30 m | 2,0 m | 4,1 m |
| 65 dB | 55 dB | 0,10 m | 0,84 m | 2,0 m |
| 55 dB | 45 dB | 0,10 m | 0,84 m | 2,0 m |

**Çıkarım:** Menzili belirleyen asıl bilinmeyen gürültü tabanıdır. Yansıtıcı büyük bir kaldıraçtır. Tüm modeller `link_budget.py` içindedir. Bu bir **modeldir**, ölçüm değildir.

### 5.4 Parabolik yansıtıcı
G ≈ η (πD/λ)². 60 kHz'de (λ ≈ 5,7 mm), η = 0,5:

| Çap | Kazanç | Işın genişliği |
|---|---|---|
| 5 cm | ~26 dB | ~8° |
| 10 cm | ~32 dB | ~4° |
| 15 cm | ~35 dB | ~2,7° |
| 20 cm | ~38 dB | ~2° |

Işın dar olduğu için hedefe (gövde/yaprak) nişan almak gerekir. Kase pratik olarak ideal paraboloid değildir; E2 gerçek kazancı ölçer.

### 5.5 ADC ve yükselteç
RP2040 ADC: 12 bit, 500 kS/s, ENOB ≈ 8,7. Nicelemeye bağlı gürültü ≈ 2,3 mV rms. Yükselteç kazancı ≥ 1000 olursa ADC gürültüsü mikrofon girişine ~19–40 dB SPL olarak yansır (60 kHz'deki bağıl duyarlılığa bağlı). SPU0410LR5H'in 40–80 kHz'deki gerçek duyarlılığı kaynaklarda **tutarsız** (bir kaynak "80 kHz'e kadar düz" der, başka bir kaynak "yüksek frekansta duyarlılık düşer" der). **Datasheet eğrisi okunmalı ve ölçülmelidir.**

---

## 6. Özgünlük ve önceki çalışmalar

**Önceki çalışmalar (raporun literatür bölümüne girer):**
- Temas tabanlı akustik emisyon: Tyree & Sperry (1989). Asma çalışmalarında piezo sensörler 100 kHz–1 MHz bandında kullanılmış (Oletić ve ark.).
- Kaynak tartışması: Zweifel & Zeugin (2008), emisyonların tamamının kavitasyon olmayabileceğini söyler.
- Havadan algılama: Khait ve ark. (2023).
- Patent tarzı (hakemsiz, **doğrulanmamış**) bir belge MEMS mikrofon dizisi + ML ile sulamayı anar.

**Bizim dört farkımız (raporun ilk sayfalarında net yazılmalı):**
1. **Maliyet ve açıklık:** 3.000 TL altında, tamamen açık kaynak donanım ve yazılım.
2. **Fizik tabanlı duyarlılık analizi:** Havada soğurma ölçümü (E1) ve yansıtıcı kazancı ölçümü (E2) ile menzil modelinin deneysel doğrulaması.
3. **Alan kayması sorusu (H4):** Açık veri setindeki tıkırtıları mikrofon tepkisinden geçirip ölçülmüş gürültü ekleyerek eğitilen model, gerçek kayıtlarda çalışıyor mu?
4. **Erken uyarı sorusu (H2):** Tıkırtı oranı, saksı ağırlığı ve toprak nemi ile karşılaştırıldığında zaman olarak önde mi?

**Kopya riski:** Rehber, başka bir projenin bire bir kopyasını "önemli ihlal" sayar ve jüri intihal yazılımı kullanır. Bu nedenle literatür taraması ve farkların açık yazılması şarttır.

---

## 7. Donanım (~%30)

### Blok şema
```
bitki ── (hava) ── [yansıtıcı kase] ── MEMS mikrofon ── yükselteç (kazanç ~1000,
GBW ≥ ~5 MHz, ~100 kHz alçak geçiren) ── RP2040 ADC (DMA, 250–500 kS/s)
── USB ── bilgisayar        yan sensörler: BME280 (sıcaklık/nem), toprak nemi, terazi
```
Ses yalıtımlı kutu (köpük, kauçuk ayak), pil/powerbank ile besleme.

### Parça listesi (TAHMİNİ fiyat; güncel fiyat DOĞRULANMADI)
| Parça | Adet | Tahmini TL |
|---|---|---|
| Raspberry Pi Pico (veya RP2040) | 2–3 | 150–300 / adet |
| Ultrason MEMS mikrofon (SPU0410LR5H veya muadili) | 2–3 | 100–300 / adet (TR'de bulunabilirliği doğrulanmadı; ithalat gerekebilir) |
| Yükselteç (op-amp, pasifler, devre kartı) | 2–3 set | 150–300 |
| 40 kHz verici-alıcı çifti (E1, E2 için) | 2 çift | 30–80 |
| BME280 | 2 | 100–150 |
| Kapasitif toprak nemi sensörü | 4–6 | 150–250 toplam |
| Mutfak terazisi | 1 | 150–400 |
| Domates fidesi + saksı + toprak | 12+ | 300–500 |
| Akustik kutu malzemesi (köpük, MDF, kauçuk) | | 300–600 |
| Yansıtıcı için paslanmaz kaseler | 3–4 çap | 100–300 |
| Powerbank | 2 | 200–400 |
| **Toplam** | | **~2.000–4.000 TL** |

### Önemli teknik uyarılar
- **USB bant genişliği:** 500 kS/s × 2 bayt ≈ 1 MB/s; USB tam hız sınırında olabilir (doğrulanmadı). Olay tetiklemeli kayıt veya 250 kS/s tercih edilmeli.
- **Anti-aliasing:** 500 kS/s tek kanalda Nyquist 250 kHz; ~100 kHz analog alçak geçiren filtre şart.
- **Gürültü kaynakları (kayıtta kapalı olmalı):** ultrasonik nemlendirici, LED sürücüleri, anahtarlamalı adaptörler, şarj cihazları, fanlar.
- **Referans mutlak SPL kalibrasyonu yok:** Bu yüzden ana ölçütler **bağıl** (SNR, olay oranı) olmalı.

---

## 8. Deneyler

### E1. Havada ultrasonik soğurma (saf fizik deneyi)
40 kHz verici-alıcı ile 0,1–1,5 m arası, 3 nem düzeyinde (ör. normal / nemlendirilmiş / kurutulmuş oda). Sinyal düşüşü vs mesafe → 20·log₁₀ yayılma + soğurma. ISO 9613-1 ekstrapolasyonunu 40 kHz'de sınar.

### E2. Yansıtıcı kazancı
Farklı kase çapları; eksen üstü kazanç ve ışın deseni (±20° tarama). Teori G = η(πD/λ)² ile karşılaştırma.

### E3. Bitki deneyi (ana deney)
- **Bitki:** Domates (öncelik). Yedek: Khait'in de denediği kaktüs, buğday, mısır.
- **Gruplar:** (a) sulanan kontrol, (b) susuz bırakılan, (c) boş saksı + toprak, (d) plastik bitki. (Opsiyonel: (e) sap kesme, pilot için hızlı pozitif kontrol.)
- **Büyüklük (öneri, güç analizi yapılmadı):** Grup başına ≥ 5 bitki; en az 2 bağımsız tekrar döngüsü.
- **Her gün:** saksı tartılır, toprak nemi ve oda sıcaklık/nemi kaydedilir, solma skoru fotoğraflanır.
- **Kayıt:** her bitki ses yalıtımlı kutuda, saatlerce (tıkırtılar nadir; saat sayısı kritiktir). Kutular paralel (2–3) çalıştırılır.
- **Kontroller:** boş kutu, boş saksı, kuru/nemli toprak, plastik bitki, pil beslemesi, cihazlar kapalı.

### E4. Yazılım deneyi
- Dedektör: bant geçiren filtre (≈20–100 kHz), uyarlamalı eşik (CFAR), özellikler (tepe frekansı, süre, yükselme zamanı, spektral ağırlık merkezi).
- Alan kayması: açık veri setindeki tıkırtıları mikrofon tepkisinden geçir, ölçülmüş gürültü ekle, bizim kayıtlarda test et.
- Sınıflandırma: sulanan vs susuz (olay oranı + özellikler).

### İstatistik ve yöntem disiplini
- **Ön kayıtlı analiz planı** (deneyden önce yazılır; `sinek-noronlari` deposundaki ön kayıt alışkanlığı burada da kullanılır).
- Dedektör eşiği, grup etiketlerini bilmeyen biri tarafından ayarlanır.
- **Doğrulamada leave-one-plant-out:** Aynı bitkinin tıkırtıları birbirine benzer; bitki bazında bölünmezse sızıntı olur.
- Hangi eşik/ayar değişikliğinin hangi sonucu verdiği kayıt altına alınır.

---

## 9. Yazılım mimarisi (~%70)

1. **Firmware (RP2040):** DMA ile halka tampon, olay tetiklemeli veya sürekli akış, USB-CDC üzerinden ikili çerçeve; periyodik gürültü tabanı metrikleri.
2. **PC (Python):** kayıt/arşiv, bant geçiren filtre, dedektör, özellik çıkarımı, Parquet/CSV depolama.
3. **Analiz:** olay oranı vs gün; ağırlık/toprak nemi ile birlikte grafikler; istatistik testleri; leave-one-plant-out sınıflandırma.
4. **Alan kayması modülü:** mikrofon tepkisi simülasyonu + ölçülmüş gürültü ile veri artırma.
5. **Panel:** canlı olay sayacı, gürültü tabanı, sıcaklık/nem.

## 10. Evren platformunun rolü

**Bulgular (arama özetlerinden; resmî dokümantasyon bulunamadı):**
- e-Devlet kimlik doğrulaması ile giriş; GPU hesaplama (saatte 10–35 kredi), SAM-2/YOLO tabanlı veri etiketleme, nesne tespiti/segmentasyon/sınıflandırma eğitimi, açık ağırlıklı **11 LLM'e OpenAI uyumlu API**.
- **1 Kasım 2026'ya kadar** yapılan API çağrıları krediden düşmüyordu (bugün son gün); sonrası belirsiz.
- Tıbbi bir model bulunamadı; API anahtarı alma adımları ve lise öğrencisi erişimi **doğrulanmadı**.

**Bu projede:** Veri akustik olduğu için Evren **zorunlu değil**. İsteğe bağlı: spektrogram sınıflandırıcısı eğitimi için GPU, ya da bitki fotoğraflarında solma skorlaması için etiketleme. Yerel GPU yeterlidir. Evren kullanılırsa **raporda belirtilmelidir**.

---

## 11. Takvim (9 hafta)

Hedef: **28 Aralık'ta yükle**, tampon kalsın (son gün sistem yoğun olabilir).

| Hafta | Tarih | İş |
|---|---|---|
| 1 | 2–8 Kas | Parça siparişi, fide temini, Dryad verisini indir + analiz, dedektör taslağı, ön kayıt planı |
| 2 | 9–15 Kas | Devre, firmware, kutu; kapalı kutuda gürültü tabanı ölçümü → **Kapı A** |
| 3 | 16–22 Kas | E1 ve E2; pilot kayıt (sap kesme) |
| 4 | 23–29 Kas | Ana kuraklık deneyi başlar (döngü 1) |
| 5 | 30 Kas–6 Ara | Tekrar döngüsü (döngü 2) → **Kapı B** |
| 6 | 7–13 Ara | ML: leave-one-plant-out, alan kayması |
| 7 | 14–20 Ara | Eksik deneyler, rapor yazımı |
| 8 | 21–27 Ara | Rapor, grafikler, özet, ekler |
| 9 | 28 Ara–3 Oca | Tampon, gönderim |

**Kapı A (2. hafta sonu):** Kapalı kutuda gürültü tabanı ve 40 kHz verici ile ~30 cm'de SNR yeterli mi? Değilse yansıtıcı, kazanç veya mikrofon değiştirilir.
**Kapı B (5. hafta sonu):** Susuz bitkilerde kontrole göre anlamlı fazla olay var mı? Yoksa "tespit sınırları" raporuna dönülür; yedek olarak temas piezo yaklaşımı değerlendirilir.

---

## 12. Riskler

| Risk | Olasılık/Etki | Azaltma |
|---|---|---|
| Ucuz mikrofonun ultrasonik gürültüsü yüksek | Yüksek/Yüksek | Yansıtıcı, kazanç, kutu; Kapı A; olumsuz sonuç raporu |
| Kış mevsiminde bitki temini/yetişme | Orta/Orta | Hazır fide; kaktüs/buğday yedeği |
| Kuraklık döngüsü uzun (4–6 gün) | Yüksek/Orta | Paralel kutular, Hafta 4'te başla |
| "Khait kopyası" itirazı | Orta/Yüksek | Dört fark + literatür bölümü |
| Ortam kaynaklı yanlış tıkırtılar | Yüksek/Yüksek | Çok katmanlı kontroller (§8) |
| USB/ADC sınırları | Orta/Orta | 250 kS/s veya olay tetiklemeli |
| Teyitsiz rakamların rapora girmesi | Orta/Orta | §4 tablosu; kaynak makaleden doğrula |

## 13. Kurallar ve uyum (rehber ve çağrı metninden)

- **Ekip:** En fazla **3 öğrenci** + 1 danışman. Proje öğrenciler tarafından yapılmalı; kullanılan kaynaklar, destek ve **araçlar (yapay zeka kodlama asistanları dahil)** raporda belirtilmeli. Jüri sözlü sorar; öğrenciler kodu ve fiziği anlatabilmeli.
- **Başvuru:** TYBS üzerinden; **4 Ocak 2027, 17:30**.
- **Biçim:** Proje adı ≤ 15 kelime; özet 150–250 kelime; rapor tek PDF, 2–20 sayfa; ek belgeler (≤ 10 MB, dosya adı ≤ 25 karakter, kişisel bilgi yok) isteğe bağlı.
- **Fizik alanı beklentisi:** Hipotez, gerçek deney, tekrarlanabilir sonuç, kuramla tartışma. Yazılım/Teknolojik tasarım için özgünlük ve kullanılabilirlik testi.
- **Güvenlik:** Düşük gerilim, pil beslemeli; şebeke gerilimi yok. Hayvan/insan deneyi yok (yalnızca bitki).
- **İntihal:** Jüri intihal yazılımı kullanır. Açık veri setinden ve yayınlardan yapılan alıntılar atıflanmalı.

## 14. Rapor iskeleti (≤ 20 sayfa)

1. Özet (150–250 kelime) · 2. Giriş ve problem · 3. Literatür ve özgünlük (dört fark) · 4. Kuram (kaynak, yayılım, soğurma, yansıtıcı, bağlantı bütçesi) · 5. Yöntem (donanım, E1–E4, ön kayıt) · 6. Bulgular (E1, E2, E3, E4) · 7. Tartışma (sınırlar, olumsuz sonuçlar, alternatif açıklamalar) · 8. Sonuç ve uygulanabilirlik (sulama uyarısı kavramı) · 9. Kaynakça (yalnızca atıf yapılanlar) · Ekler (kod, ham veri bağlantıları, ön kayıt).

## 15. Açık sorular ve yapılacaklar

- [ ] Dryad zip'ini indir → `data/` (CC0); klip spektrum ve genlik analizi.
- [ ] Cell makalesinin tam metninden §4'teki teyitsiz rakamları doğrula.
- [ ] SPU0410LR5H (veya muadili) datasheet frekans-duyarlılık eğrisini oku.
- [ ] Türkiye'de güncel parça fiyatları ve bulunabilirlik.
- [ ] Domates fidesi/kaktüs/buğday temini ve kış koşullarında yetiştirme yeri.
- [ ] Ekibin 3 öğrencisini belirle; danışmanla hipotezleri gözden geçir.
- [ ] Ön kayıtlı analiz planını deneyden önce yaz.

## 16. Kaynaklar

- Khait ve ark., Cell (2023): <https://cris.iucc.ac.il/en/publications/sounds-emitted-by-plants-under-stress-are-airborne-and-informative/>
- Açık veri seti (Dryad, CC0): <https://datadryad.org/dataset/doi:10.5061/dryad.jwstqjqf7>
- Ön baskı özeti: <https://www.sci.news/biology/plants-ultrasonic-clicks-07895.html>
- bioRxiv ön baskı (okunamadı): <https://www.biorxiv.org/content/10.1101/507590v4.full.pdf+html>
- Asma akustik emisyon: <https://www.bib.irb.hr/1080046>
- Zweifel & Zeugin (2008): <https://bio.acousti.ca/sites/default/files/Zweifel_et_al-2008-New_Phytologist.pdf>
- MEMS mikrofonla sulama (patent tarzı, doğrulanmamış): <https://liveinthefuture.org/priorart/xylem-cavitation-irrigation.html>
- RP2040 ADC (Pico SDK): <https://www.raspberrypi.com/documentation/pico-sdk/hardware.html>
- RP2040 örnekleme örneği: <https://www.hackster.io/sandy-roberts2/quadrupling-the-sample-rate-of-an-rp2040-oscilloscope-5f9a74>
- Ultrasonik yarasa dedektörü (Pi): <https://www.raspberrypi.com/news/ultrasonically-detect-bats-with-raspberry-pi/>
- Evren (Webtekno): <https://www.webtekno.com/turkiye-yapay-zeka-platformu-evren-erisime-acildi-h225949.html>
- TÜBİTAK 2204-A sayfası: <https://tubitak.gov.tr/tr/yarismalar/2204-lise-ogrencileri-arastirma-projeleri-yarismasi>
- Atmosferik soğurma: ISO 9613-1 formülü, `link_budget.py` içinde uygulanmıştır.
