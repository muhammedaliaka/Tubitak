# Çamaşır–Nem Dengesi: Asılı Çamaşırı Ölçülen Nem Kaynağı Olarak Kullanarak Türk Konutlarında Havalandırma ve Yoğuşma Riskini Tahmin Etme

> **Durum: ANA ADAY (#1).** Alternatif: `bitki-ultrasonu/PLAN.md` (#2). Fikir en geç **7 Kasım**'da kesinleşmeli.
> **Hazırlanma tarihi:** 1 Kasım 2026 · **Hedef:** TÜBİTAK 2204-A (58. dönem), son başvuru **4 Ocak 2027, 17:30**.
> **Tema:** Fizik (buharlaşma kinetiği, nem kütle dengesi, psikrometri, yüzey yoğuşması) · **Yazılım ağırlığı:** ~%70.
> **Çerçeve:** Yoğuşma, yapı nemi ve enerji. **Sağlık iddiası yoktur** (bkz. §13).

---

## 1. Tek cümlelik özet

Asılı çamaşırın kütle kaybı bir yük hücresiyle ölçülürse, çamaşır **bilinen bir nem kaynağına** dönüşür; bu sayede odanın hava değişim oranı (ACH) ve soğuk duvar yüzeylerindeki yoğuşma riski, ucuz sensörlerle ve tek bir kurutma olayından tahmin edilip kişiye "pencereyi şu kadar aç / çamaşırı şuraya as" önerisine çevrilebilir mi?

## 2. Araştırma soruları ve hipotezler

| Kod | Hipotez | Nasıl sınanır |
|---|---|---|
| H1 | Asılı çamaşırın kütle–zaman eğrisi, oda sıcaklığı/nemi/hava hızıyla iki dönemli modelle (sabit hız + azalan hız) öngörülebilir; kalan kuruma süresi tahmin hatası düşüktür. | E1 |
| H2 | Çamaşırın ölçülen buharlaşma hızı nem kaynağı olarak girildiğinde, ACH yalnızca T/BN serisinden CO₂ azalma yöntemine yakın tahmin edilir. Kaynak bilinmediğinde tahmin belirgin kötüleşir. | E2, E3 |
| H3 | Odadaki soğuk yüzeyin sıcaklık faktörü (f_Rsi) ölçülürse, yoğuşma başlangıç BN'si ve riskli saat sayısı öngörülebilir. | E4 |
| H4 | Modelin önerdiği havalandırma/yerleşim stratejisi, kullanıcının alışkanlık stratejisine göre aynı kuruma süresinde daha düşük tepe nem veya daha düşük ısı kaybı sağlar. | E5 |
| H5 | Gerçek kullanıcılar öneriyi anlar ve uygular. | E6 |

> **Başarı eşikleri (hata sınırları) ön kayıtta, pilot veri geldikten sonra ve ana deneylerden önce yazılacak.** Burada sayı vermek, ölçümden önce uydurma sayı üretmek olurdu.

---

## 3. Türkiye bağlamı

### 3.1 Grup büyüklüğü ve sıklık (kaynak durumu işaretli)

| Veri | Değer | Kaynak durumu |
|---|---|---|
| Toplam hane sayısı (2025) | 26,98 milyon | TÜİK "İstatistiklerle Aile 2025", **haber aktarımı** |
| Kurutma makinesi olan hane | 100 haneden 26 | Ticaret Bakanlığı İsraf Raporu'na dayanan yazı, **ikincil**; rapor tarihi/yöntemi doğrulanmadı |
| Kurutma makinesi olmayan hane (hesap) | ~%74 ≈ **~20 milyon hane** | Türetilmiş |
| Makinede yıkayanların haftada 3–4 yıkama oranı | %64 (Ipsos, 4.500 hane) | Basın aktarımı; kurutma yöntemini ölçmez |
| Sızdırma, nemlenme, çürüme yaşayan konut | %34,7 (≈ 9,4 milyon hane) | TÜİK 2020, **haber aktarımı**; yıllar karışık, kaba tahmin |
| Yalıtım kaynaklı ısınma sorunu | %36,7 | Aynı kaynak |

**Hedef kitle gerekçesi (ekibin görüşü):** Kurutma makinesi olmayan evler çoğunlukla düşük ve orta gelirli kesimde yoğunlaşıyor; bu kesim >1 milyon kişi eder. Bu *hipotezdir*: gelir–kurutma makinesi ilişkisini gösteren bir kaynak bulamadım. Ancak kurutma makinesi olmayan ~20 milyon haneden yalnızca %5'i bile 1 milyon hane eder; eşik rahat aşılır. Yılda ≥10 kez ihtiyaç: haftada 3–4 yıkama (Ipsos) → yılda 150–200 yıkama olayı.

### 3.2 Türkiye'de ölçülmüş saha verisi eksik
Yaptığım aramada (standart web araması) Türk konutlarında asılı çamaşırın iç nem ve yoğuşma üzerindeki etkisini ölçen bir **saha çalışması bulamadım**. Bulunanlar haber ve satıcı yazıları (Milliyet, CNN Türk, nem alıcı blogları) ve kurutma *makinesi* enerjisi üzerine İTÜ tezleri. Bu, projeye Türkiye'ye özgü ilk açık veri seti üretme fırsatı verir. **Bu iddia aramamın sınırıyla sınırlıdır**; Google Scholar ve ULAKBİM taraması yapılmalı (§15).

### 3.3 Türkiye'ye özgü parametreler
- **Çamaşır makinesi:** Perakende "çok satan" listelerinde 9–10 kg, 1000–1200 devir yaygın (resmî pazar verisi değil). AB etiketi örnekleri: kalan nem (RMC = su kütlesi / kuru pamuk kütlesi) %50–54, 1.150–1.400 devirde (Electrolux, Beko, Miele). **5 kg kuru yük × %52 ≈ 2,6 L su**. Glasgow Sanat Okulu da yük başına yaklaşık 2 L bildirir.
- **İklim:** MGM 1991–2020 Ocak bölge normalleri: Marmara 5,2 °C, Ege 6,3 °C, Akdeniz 7,5 °C, İç Anadolu −0,6 °C, Doğu Anadolu −4,3 °C, Türkiye ortalaması 2,9 °C. **İl bazlı sıcaklık ve nem ile Karadeniz değeri doğrulanmadı;** MGM il istatistiklerinden alınacak.
- **TS 825 derece-gün bölgeleri:** Antalya 1., İstanbul 2., Elazığ 3., Kayseri 4. bölge (METU çalışması). Diğer illerin bölgesi doğrulanmadı.
- **Yoğuşma standardı:** ISO 13788:2012 yüzey sıcaklığı/küf ölçütü için basitleştirilmiş yöntemler verir. **Türkiye'deki karşılığının (TS EN ISO 13788) numarası ve TS 825 ile ilişkisi doğrulanmadı.**
- **Enerji fiyatları (Nisan 2026, haber aktarımı; Kasım 2026'da değişmiş olabilir):** doğalgaz konut kademeli tarife 1. kademe 10,625 TL/m³, 2. kademe 18 TL/m³; elektrik 100 kWh için 323,8 TL (≈ 3,2 TL/kWh). **EPDK ve BOTAŞ'tan güncel tarife alınmalı.** Modelde ısı maliyeti için 1,11 TL/kWh kullanıldı (10,625 TL/m³ ÷ (10,6 kWh/m³ × 0,9 verim)).
- **Konut tipleri:** Apartman, cam balkon, kombi/kalorifer, soba; 2000 öncesi yalıtımsız binalar. Deney evlerinde bu bilgiler envanterlenecek (§8, E0).

---

## 4. Özgünlük ve önceki çalışmalar

**Önceki çalışmalar (literatür bölümüne girer):**
- **Kurutma makinesi patentleri:** Nem/buharlaşma hızından kalan süre tahmini (ör. giriş/çıkış havası mutlak nem oranı). Makine içindir, oda ve askı için değildir.
- **Birzeit öğrenci projesi:** Sensörlü kurutma rafı; yalnızca proje tanımı, doğrulanmış sonuç yok.
- **Bir YÖK Açık Bilim kaydı (özet düzeyinde, doğrulanmadı):** Giysi asan bir kabin prototipi için enerji ölçümü bildirilmiş.
- **Nem kütle dengesi modelleri:** TenWolde (1987, FPLRH1) ve sonrası; iç nem = üretim − havalandırma − depolama. Üretim ve havalandırma tek bir BN serisinden ayrışmakta zorlanır (Glass & TenWolde 2009 derlemesi bu belirsizliği anar).
- **Evde çamaşır kurutma ve nem:** Glasgow Sanat Okulu basın bülteni (Birleşik Krallık): yük başına ~2 L. Strathclyde tezinde ESP-r nem modeliyle evde çamaşır kurutma etkisi bir bölüm olarak geçiyor (sonuçlarını doğrulamadım). "%60 BN üstü riskli" ifadesi bir Malta rehberinden; bilimsel olarak doğrulanmadı, pratik kural olarak kullanılmayacak.
- **Tüketici nem cihazları:** Çiy noktası/yüzey sıcaklığı ile uyarı verir; bağımsız doğrulama bulunamadı.

**Bizim katkımız (raporun ilk sayfalarında net yazılmalı):**
1. **Çamaşırı ölçülen nem kaynağı yapmak:** Bildiğim literatürde bu kullanım bulunamadı. Kimliklendirme sorununu doğrudan hedefler (aşağıda sentetik kanıt).
2. **Türkiye'ye özgü saha verisi:** Türk konutlarında (farklı bölge/yalıtım) açık veri seti.
3. **Karar önerisi:** Yoğuşma marjı + ısı kaybı maliyeti (TL) + kuruma süresini birlikte optimize eden öneri motoru.
4. **Açık donanım:** Yaklaşık 3.000–5.000 TL, açık kaynak.

**Kopya riski:** Rehber, başka bir projenin bire bir kopyasını "önemli ihlal" sayar ve jüri intihal yazılımı kullanır. Literatür taraması ve fark tablosu zorunlu.

---

## 5. Fizik ve model

### 5.1 Kuruma (asılı çamaşır)
Sabit hız döneminde buharlaşma hızı, hava ile yaş termometre sıcaklığı farkıyla orantılıdır (Lewis ilişkisi):

E = α · (T_hava − T_yaş_termometre), α = h_c·A / h_fg

Azalan hız döneminde (m < m_c) E, kalan suyla orantılı düşer. Varsayılan α = 0,055 kg/(h·K) (h_c ≈ 6 W/m²K, A ≈ 6 m² kabulü). Deney E1 bu parametreleri ve alternatif yasaları (Lewis, Page) uyduracak.

### 5.2 Oda nem dengesi (iyi karışmış tek bölge + yüzey tamponu)
(1+β)·ρ·V·dw/dt = E + G_diğer + ACH·ρ·V·(w_dış − w) − nem_alıcı

- w: nem oranı (kg/kg), V: oda hacmi, β: yüzey/eşya tampon çarpanı.
- Bilinmeyenler: ACH, β, G_diğer. **E biliniyorsa (yük hücresi) bu üçü ayrışır** (H2).

### 5.3 Yüzey yoğuşması
T_si = T_dış + f_Rsi·(T_iç − T_dış); RH_yüzey = p_v / p_sat(T_si). RH_yüzey ≥ %100 → yoğuşma; ≥ %80 → küf büyümesi için yaygın kullanılan ölçüt (**ISO 13788 metninden doğrulanmalı**). f_Rsi cihazla ölçülür (iç/dış/yüzey sıcaklığı).

### 5.4 Isı kaybı maliyeti
Havalandırmanın ek ısı kaybı: Q = 0,34·V·ΔACH·(T_iç − T_dış) [W] (0,34 Wh/m³K). TL maliyeti güncel gaz tarifesiyle hesaplanır.

---

## 6. Ön model sonuçları (İLLÜSTRATİF; ölçüm değildir)

`sim_nem_dengesi.py` (oda 30 m³, 5 kg kuru yük, %52 kalan nem, 20 °C iç sıcaklık, 2,6 L su). Dış sıcaklık = MGM bölge normali; **dış nem ve diğer parametreler varsayım.** Taban BN'si %62 (G_diğer=0,05 kg/h kabulü ile).

| Bölge-benzeri | Strateji | Kuruma (h) | Tepe BN | Yoğuşma (h) f=.65 / .80 | Ek ısı kaybı |
|---|---|---|---|---|---|
| Marmara (+5,2 °C) | Pencere kapalı | >24 | %93 | 22,7 / 20,3 | 0 |
| | Aralık, sürekli (ACH 2) | 8,7 | %62 | 0 / 0 | 6,2 kWh ≈ 6,8 TL |
| | Her saat 10 dk tam aç | 10,5 | %72 | 0,1 / 0 | 3,4 kWh ≈ 3,8 TL |
| | Kapalı + nem alıcı (0,3 kg/h) | 8,3 | %62 | 0 / 0 | elektrik ayrı |
| İç Anadolu (−0,6 °C) | Pencere kapalı | 22,7 | %90 | 22,9 / 20,7 | 0 |
| | Aralık, sürekli | 7,3 | %54 | 0 / 0 | 8,6 kWh ≈ 9,5 TL |
| | Her saat 10 dk tam aç | 8,7 | %67 | 2,4 / 0 | 4,8 kWh ≈ 5,3 TL |
| Doğu Anadolu (−4,3 °C) | Pencere kapalı | 19,9 | %89 | 23,1 / 21,0 | 0 |
| | Aralık, sürekli | 6,8 | %52 | 0 / 0 | 10,1 kWh ≈ 11,2 TL |
| | Her saat 10 dk tam aç | 8,1 | %65 | 4,6 / 0 | 5,7 kWh ≈ 6,3 TL |

**Okuma (nitel, duyarlılık testinde sağlam):**
1. Kapalı odada bir yük çamaşır, modelde odayı neredeyse doyuruyor ve yalıtımsız köşede 20+ saat yoğuşma üretiyor.
2. Sürekli aralık pencere en hızlı ve en güvenli, ama ısı kaybı en yüksek (bir yük için ~7–11 TL, Nisan 2026 gaz tarifesiyle).
3. "Her saat 10 dk" yarı maliyetle çalışıyor, ancak soğuk bölgelerde yalıtımsız köşede yoğuşma saatleri kalıyor.
4. **En iyi strateji bölgeye, odaya ve duvar yalıtımına (f_Rsi) bağlı; bu yüzden ölçüm gerekiyor.** Bu, projenin gerekçesidir.

**Duyarlılık (Marmara-benzeri):** G_diğer=0,02 → taban BN %43, kapalı oda tepe %88; BETA 1–10 ve ALPHA 0,03–0,09 aralığında nitel sonuç değişmedi (kapalı: tepe %88–95; aralık pencere: %59–68). Sayısal değerler parametreye bağlıdır.

**Dikkat:** Bir yük başına ~7–11 TL ısı kaybı ile kurutma makinesi elektriği (yük başına kWh değeri bu çalışmada doğrulanmadı) aynı mertebede olabilir. Bu bir *hipotez*; E5 ve maliyet analizi ile test edilecek.

## 7. Sentetik kimliklendirilebilirlik kanıtı (H2'nin ön sınaması)

`identifiability_test.py`: Modelle sentetik nem serisi üretildi (BN ±%1,5 gürültü; E ölçümü ±0,03 kg/h), ACH iki durumda geri bulundu. **Medyan mutlak bağıl hata (%), 40 deneme:**

| Gerçek ACH | Model doğru: E bilinmiyor | Model doğru: E ölçülü | Kuruma yasası yanlış: E bilinmiyor | Kuruma yasası yanlış: E ölçülü |
|---|---|---|---|---|
| 0,3 | 27,0 | **1,3** | 41,7 | **1,4** |
| 0,6 | 7,3 | **1,0** | 24,2 | **0,9** |
| 1,0 | 0,5 | 0,5 | 9,8 | **0,5** |
| 2,0 | 0,6 | 0,7 | 33,2 | **0,9** |

**Okuma:** E ölçüldüğünde ACH hatası ~%1 ve kuruma yasasının yanlış belirlenmesinden etkilenmiyor; E bilinmediğinde, özellikle düşük havalandırmada (kapalı oda) ve model hatası varsa %10–40 hata var.

**Sınırlar (raporda açıkça yazılmalı):** Tamamı sentetik; aynı karışım modeli hem veriyi üretiyor hem tahmin ediyor ("inverse crime"); gerçek odada tam karışma, sabit ACH, dış nem ve sensör sapması varsayımları bozulur. Bu test yalnızca "fikir teoride işe yarar mı?" sorusunu yanıtlar. **Gerçek doğrulama E2/E3'tür.** Betikleri çalıştırmak için `numpy` ve `scipy` gerekir.

---

## 8. Donanım ve kurulum

### 8.1 Ölçüm düzeneği
- **Kütle (ana sensör):** Katlanır çamaşır askısının 4 ayağı, 4 adet baskül (bar tipi) yük hücresinin üzerine oturtulur; hücreler tek HX711 ile okunur. (Banyo tartısı iç parçaları yeterli olabilir; kapasite ~50 kg × 4.) Hedef: 8–12 kg toplam, ±5–10 g çözünürlük (**doğrulanacak**).
- **Oda:** 2 adet sıcaklık/nem sensörü (oda ortası + soğuk duvar köşesi), **yüzey sıcaklığı** (temaslı sensör veya IR), **CO₂ sensörü** (ACH doğrulaması için), **ESP32**.
- **Güç:** Isıtıcı/nem alıcı enerjisi için sertifikalı akıllı priz (enerji ölçerli) kullanılır; **şebeke devrelerine müdahale yok.**
- **Opsiyonel:** Hava hızı (yaklaşık, fan karşılaştırması için).

### 8.2 Tahmini bütçe (Türkiye fiyatları DOĞRULANMADI)
| Kalem | Tahmini TL |
|---|---|
| ESP32 ×2 | 400–600 |
| HX711 ×2, baskül hücresi setleri ×2 | 450–700 |
| Sıcaklık/nem sensörü ×4 | 500–800 |
| CO₂ sensörü ×1–2 | 1.000–2.000 |
| Yüzey/IR sıcaklık ×2 | 400–600 |
| Akıllı priz (enerji ölçerli) ×2 | 500–700 |
| Kablo, kasa, askı, bağlantı | 300–500 |
| **Toplam** | **~3.500–5.900 TL** (üst sınır 6.000 TL'ye yakın; ilk 2 kit tam, diğer 3 ev "hafif" kit) |

**Strateji:** 2 tam kit + 3 hafif kit (yalnızca sıcaklık/nem + yüzey) veya kitleri evler arasında dönüşümlü kullanmak.

### 8.3 Kalibrasyon (fizik deneyleri)
- **Yük hücresi:** Bilinen kütle (1 L su = ~1 kg), doğrusallık, sıcaklık sürüklenmesi, sallanma filtresi.
- **Nem sensörü:** Doygun tuz çözeltileri (NaCl ~%75, MgCl₂ ~%33 BN) ile çapraz kalibrasyon.
- **CO₂ sensörü:** Dış hava referansı.

---

## 9. Deneyler

**E0 – Ev envanteri ve sensör karakterizasyonu.** 5 evde: oda hacmi, pencere türü, ısıtma sistemi, çamaşır makinesi kapasitesi/devri, kurutma alışkanlığı, duvar yalıtımı (var/yok). Sensör kalibrasyonları. *(Pilot-0: donanım gelmeden mutfak terazisi ve ucuz termo-higrometre ile 3 gün elle kayıt; 7 Kasım kararına veri.)*

**E1 – Kuruma kinetiği.** Standart yük (aynı pamuk havlu seti, aynı makine/devir). T, BN, hava hızı (fan açık/kapalı), asma yoğunluğu değişir. α, X_c ve alternatif yasaları (Lewis, Page) uydur. Çıktı: H1, kalan süre hatası.

**E2 – Oda nem tepkisi ve ACH.** Aynı yük, farklı pencere durumları. ACH_RH (nem + ölçülen E ile) ve ACH_CO₂ (CO₂ azalma yöntemi; ASTM E741 mantığı). Bland–Altman karşılaştırması.

**E3 – Bilinen kaynak doğrulaması.** Çamaşırdan bağımsız: terazide tartılan açık su kabı veya ultrasonik nemlendirici (tartılan) bilinen nem kaynağıdır. H2'yi çamaşır belirsizliğinden bağımsız doğrular. *(CO₂ izleyici enjeksiyonu gerekiyorsa güvenli yöntem danışmanla belirlenmeli.)*

**E4 – Yüzey yoğuşma marjı.** İki sensörle f_Rsi ölçümü; kritik BN ve riskli saat sayısı tahmini. Gerçek yoğuşma gözlemi (kamera/ elle not) ile karşılaştır.

**E5 – Öneri motoru A/B testi.** Aynı yük ve evde iki strateji (kullanıcı alışkanlığı vs önerilen), sıra rastgele; ölçütler: kuruma süresi, tepe BN, riskli saat, ısı kaybı (kWh/TL).

**E6 – Kullanılabilirlik.** 10–15 yetişkin kullanıcı, görev tabanlı test, SUS ölçeği. **İnsan katılımı: bilimsel etik formu ve bilgilendirilmiş onam;** reşit olmayan öğrenciler için veli onayı.

**Yöntem disiplini:** Ön kayıtlı analiz planı (deneyden önce); leave-one-home-out çapraz doğrulama; ham veriyi saklayıp paylaş; başarısız denemeleri de rapora yaz.

---

## 10. Yazılım (~%70)

1. **Firmware (ESP32):** HX711 örnekleme (10/80 Hz), medyan + alçak geçiren filtre, sıcaklık/nem/CO₂/yüzey okuma, Wi-Fi ile veri gönderme.
2. **Backend (Python):** SQLite/Parquet kayıt, zaman damgası senkronu, veri kalitesi denetimi.
3. **Durum kestirimi:** α, X_c, ACH, β, G_diğer için en küçük kareler/özyinelemeli tahmin veya EKF; belirsizlik aralıkları.
4. **Simülasyon ve öneri motoru:** Psikrometri, nem dengesi, f_Rsi yoğuşma marjı; seçenekleri (pencere süresi, yerleşim, nem alıcı) karşılaştırır; kullanıcı kısıtı (maksimum açık pencere süresi, ısı maliyeti) altında en iyisini önerir.
5. **Arayüz:** Türkçe, telefonda web uygulaması (PWA); bildirim ("Çamaşırlar %92 kurudu, ~40 dk"); yoğuşma marjı göstergesi.
6. **Hava durumu girdisi:** Ücretsiz bir hava API'si (ör. Open-Meteo; ücretsiz kullanım koşulları **doğrulanmalı**) veya MGM. Çevrimdışı mod.
7. **Yerel işleme:** Kişisel veri toplanmaz.
8. **Evren:** Zorunlu değil. Kullanılırsa (ör. Türkçe doğal dil açıklaması için LLM API) **raporda belirtilir**; bilimsel çekirdek LLM'den bağımsız kalır. Ücretsiz API penceresi 1 Kasım 2026'da bitti; sonrası kredi sistemi.

---

## 11. Takvim (9 hafta)

Hedef: **28 Aralık'ta yükle**; tampon kalsın.

| Hafta | Tarih | İş |
|---|---|---|
| 1 | 2–8 Kas | Pilot-0 (elle kayıt), E0 envanteri, sipariş, literatür (Türkçe + yabancı), ön kayıt taslağı, firmware iskeleti; **7 Kas: fikir kararı** |
| 2 | 9–15 Kas | Kit montajı, yük hücresi/T-RH/CO₂ kalibrasyonu (E0) → **Kapı A** |
| 3 | 16–22 Kas | E1 kuruma kinetiği (kontrollü oda), E3 bilinen kaynak |
| 4 | 23–29 Kas | E2 (ACH_RH vs ACH_CO₂) 2 evde; veri hattı |
| 5 | 30 Kas–6 Ara | 5 evde tekrar (E1/E2), E4 yüzey → **Kapı B** |
| 6 | 7–13 Ara | Model uydurma, leave-one-home-out, öneri motoru |
| 7 | 14–20 Ara | E5 A/B testi, E6 kullanılabilirlik, maliyet analizi |
| 8 | 21–27 Ara | Rapor, grafikler, özet, ekler (etik formu) |
| 9 | 28 Ara–3 Oca | Tampon, gönderim |

**Kapı A (2. hafta sonu):** Yük hücresi kararlılığı ve nem sensörü çapraz uyumu ön kayıttaki eşikte mi? Değilse donanım değişir.
**Kapı B (5. hafta sonu):** ACH_RH, ACH_CO₂ ile ≥3 evde uyumlu mu? Değilse proje "kuruma tahmini + oda nem tepkisi + yoğuşma marjı" olarak daralır (H2 olumsuz sonuç olarak raporlanır; sentetik sonuç yine de bir bulgudur).

## 12. Riskler

| Risk | Olasılık/Etki | Azaltma |
|---|---|---|
| Yük hücresi sallanma, sıcaklık sürüklenmesi | Yüksek/Orta | Dört ayaklı platform, filtre, referans kütle, sıcaklık telafisi |
| Nem sensörü gecikmesi ve ofseti | Orta/Orta | Tuz kalibrasyonu, ikili sensör, hızlı yanıt sensörü |
| Gerçek odada tam karışma/sabit ACH varsayımı bozulur | Yüksek/Yüksek | Pencere-kapı olaylarını kaydet; parçalı ACH; model hatası analizi |
| 5 evde aynı anda deney lojistiği | Orta/Orta | Dönüşümlü kit; standart protokol; hafif kit |
| Ailelerin katılımı ve çamaşır yükü değişkenliği | Orta/Orta | Standart yük (aynı havlu seti); alışkanlık yükleri ayrı etiketlenir |
| Hava sıcaklığı/ısıtma ayarları farklı | Orta/Orta | Her koşulu kaydet; modelde kontrol değişkeni |
| "İyi bilinen modelin tekrarı" itirazı | Orta/Yüksek | Çamaşırın ölçülen kaynak olması + Türkiye verisi + karar motoru (§4) |
| Teyitsiz rakamların rapora girmesi | Orta/Orta | §3.1 tablosu; kaynak doğrulama listesi |

## 13. Kurallar ve uyum (rehber ve çağrı metninden)

- **Ekip:** En fazla **3 öğrenci** + 1 danışman. Proje öğrenciler tarafından yapılmalı; kullanılan kaynaklar, destek ve **araçlar (yapay zekâ kodlama asistanları dahil) raporda belirtilmeli.** Jüri sözlü sorar; öğrenciler kodu ve fiziği anlatabilmeli.
- **Başvuru:** TYBS; **4 Ocak 2027, 17:30.** Proje adı ≤15 kelime; özet 150–250 kelime; rapor tek PDF, 2–20 sayfa; ek belgeler ≤10 MB.
- **Sağlık iddiası yok.** Küf/alerji/akar gibi sağlık ifadelerini ve bu tür haberleri gerekçe olarak kullanma. Çerçeve: yoğuşma, yapı nemi (boya/sıva hasarı), enerji ve konfor. "Küf" yalnızca yüzey RH ölçütü olarak anılırsa yapı hasarı bağlamında.
- **İnsan katılımı:** E6 kullanılabilirlik testi ve ev bireyleri için bilgilendirilmiş onam; bilimsel etik formu.
- **Güvenlik:** Düşük gerilim; şebeke gerilimi ölçümü sertifikalı hazır enerji ölçerli priz ile; askı ağırlığı ve kablo güvenliği.
- **İntihal:** Atıflar tam; açık kaynak parçalar lisansıyla belirtilir.

## 14. Rapor iskeleti (≤20 sayfa)

1. Özet · 2. Giriş ve problem (Türkiye bağlamı) · 3. Literatür ve özgünlük · 4. Kuram (kuruma, nem dengesi, yoğuşma, kimliklendirme) · 5. Yöntem (donanım, kalibrasyon, E0–E6, ön kayıt) · 6. Bulgular · 7. Tartışma (sınırlar, model hatası, olumsuz sonuçlar) · 8. Sonuç ve uygulanabilirlik (TL cinsinden karar) · 9. Kaynakça · Ekler (kod, ham veri, etik formu, ön kayıt).

## 15. Yapılacaklar

- [ ] **Pilot-0 (1–6 Kas):** Mutfak terazisi + termo-higrometre ile 3 gün elle kayıt; 7 Kas kararı.
- [ ] Beş evin envanteri (oda hacmi, pencere, ısıtma, makine devri, yalıtım).
- [ ] Türkçe + yabancı literatür taraması (Google Scholar/ULAKBİM): "laundry as moisture source", "ventilation rate from moisture balance", "asılı çamaşır kuruma kinetiği", "TS EN ISO 13788".
- [ ] MGM il bazlı Kasım–Şubat sıcaklık ve nem normalleri; hangi illerde olunduğunu belirle.
- [ ] EPDK/BOTAŞ güncel tarifeleri; kurutma makinesi yük başı enerji (üretici etiketi).
- [ ] TS 825 bölge listesi ve TS EN ISO 13788 numarası.
- [ ] Parça fiyatları ve bulunabilirlik; sipariş.
- [ ] Ön kayıt planı (hata eşikleri pilot sonrası).
- [ ] 3 resmî öğrenciyi belirle; danışmanla hipotezleri gözden geçir.
- [ ] Bilimsel etik formu ve onam metni.

## 16. Kaynaklar

- TÜİK konut sorunları (haber): <https://www.steelradar.com/haber/turkiyedeki-konutlarin-yuzde-35inde-sizdirma-nemlenme-ve-curume-sorunu-yasaniyor/>
- Hane sayısı (haber): <https://www.dunya.com/ekonomik-veriler/tuik-hanehalki-kuculuyor-tek-kisilik-yasam-artiyor-haberi-824831>
- Kurutma makinesi oranı (ikincil): <https://www.posta.com.tr/yazarlar/bilal-emin-turan/kurutmanin-hangisi-hesapli-2130802>
- Yıkama sıklığı (Ipsos, Milliyet): <https://www.milliyet.com.tr/pembenar/turkiyede-en-fazla-on-yikama-yapiliyor-6400973>
- Evde çamaşır kurutma ve nem (Glasgow): <https://gsamediacentre.co.uk/research-highlights-health-and-economic/>
- Kurutucu patenti: <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11905644>
- Birzeit kurutma rafı: <https://purop.birzeit.edu/projects/148/show>
- YÖK Açık Bilim kaydı (askı kabini, doğrulanmadı): <https://acikbilim.yok.gov.tr/handle/20.500.12812/99084?show=full>
- Nem kütle dengesi modeli (USDA): <https://research.fs.usda.gov/treesearch/33708>
- AB etiketi, kalan nem örnekleri: <https://eprel.ec.europa.eu/informationsheet/Fiche_299284_EN.pdf>
- AB enerji etiketi (RMC sınıfları): <https://en.wikipedia.org/wiki/European_Union_energy_label>
- ISO 13788:2012: <https://www.iso.org/standard/51615.html>
- MGM Ocak 2026 değerlendirmesi: <https://www.mgm.gov.tr/FILES/iklim/yillikiklim/2026/Ocak_Sicaklik_Yagis_Degerlendirmesi.pdf>
- TS 825 derece-gün bölgeleri (METU): <https://open.metu.edu.tr/handle/11511/50741>
- Enerji zammı Nisan 2026: <https://tr.euronews.com/2026/04/03/elektrik-ve-dogal-gaza-yuzde-25-zam>
- Elektrik tarifesi Nisan 2026: <https://uzmanpara.milliyet.com.tr/uzmanpara/elektrik-zammi-2026-nisanda-ne-kadar-oldu-elektrige-ne-kadar-zam-geldi-iste-yeni-tarife-7565631>
- Evren (Webtekno): <https://www.webtekno.com/turkiye-yapay-zeka-platformu-evren-erisime-acildi-h225949.html>
- TÜBİTAK 2204-A sayfası: <https://tubitak.gov.tr/tr/yarismalar/2204-lise-ogrencileri-arastirma-projeleri-yarismasi>
