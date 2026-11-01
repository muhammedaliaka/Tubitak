# Çamaşır–Nem Dengesi: Asılı Çamaşırı Ölçülen Nem Kaynağı Yaparak İstanbul Konutlarında Yoğuşma Riskini Tahmin Etme

> *Çalışma başlığı, 14 kelime (kural: ≤15). İlk sürümdeki başlık 17 kelimeydi ve kuralı aşıyordu; düzeltildi.*

> **1 Kasım güncellemesi: Ekip P01 + P09 birleşimini seçti → `../uydu-isik-radyo/PLAN.md`. Bu plan artık yedektir.**
> **Eski durum: ÇALIŞMA FİKRİ (#1), konum: İstanbul.** Alternatif: `bitki-ultrasonu/PLAN.md` (#2). Ekip 2–15 Kasım'da sınavda; ağır iş yok. **Kesin karar Kapı 0'dan (Pilot-0, 16–19 Kas) sonra, en geç 22 Kasım'da** (§11).
> **Hazırlanma tarihi:** 1 Kasım 2026 (İstanbul güncellemesi: 1 Kasım) · **Hedef:** TÜBİTAK 2204-A (58. dönem), son başvuru **4 Ocak 2027, 17:30**.
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
- **İstanbul iklimi (ekibin bulunduğu il):** MGM İstanbul il sayfası: Ocak ortalama sıcaklık **6,8 °C**, Şubat 6,9 °C (ortalama en düşük 4,2 °C); **ölçüm dönemi 1950–2025, yani 1991–2020 normali değil**, istasyon sayfada belirtilmemiş. **İstanbul'un aylık oransal nemi bulamadım**; modelde dış BN %78 varsayım (duyarlılık §6).
- **TS 825 derece-gün bölgeleri:** Antalya 1., İstanbul 2., Elazığ 3., Kayseri 4. bölge (METU çalışması). Diğer illerin bölgesi doğrulanmadı.
- **Yoğuşma standardı:** ISO 13788:2012 yüzey sıcaklığı/küf ölçütü için basitleştirilmiş yöntemler verir. **Türkiye'deki karşılığının (TS EN ISO 13788) numarası ve TS 825 ile ilişkisi doğrulanmadı.**
- **Enerji fiyatları (haber aktarımı):** BOTAŞ konut kademeli tarifesi, 4 Nisan 2026'dan beri: 1. kademe 10,625 TL/m³, 2. kademe 18 TL/m³ **(BOTAŞ toptan fiyatı; vergi ve dağıtım bedeli yok)**. Aboneye yansıyan fiyat (ÖTV, KDV, sistem kullanım bedeli dahil) haberlerde 1. kademe için **16,23–17,88 TL/m³** (Ankara için 16,84), 2. kademe için ~25,7–26,1 TL/m³ olarak geçiyor; kaynaklar birbirini tutmuyor, bölge ve ay farkı olabilir. Elektrik (Nisan 2026): 100 kWh için 323,8 TL (≈ 3,2 TL/kWh).
  - **DÜZELTME:** İlk sürümde ısı maliyeti için 1,11 TL/kWh kullanmıştım; bu *toptan* fiyattı ve abone maliyetini ~%35–40 düşük gösteriyordu. Güncel hesap: 16,23–17,88 TL/m³ ÷ (10,6 kWh/m³ × 0,9) ≈ **1,70–1,87 TL/kWh**. Isıl değer (10,6) ve kazan verimi (0,9) **kabuldür**, doğrulanacak.
  - **İstanbul kasım 2026 limiti:** BOTAŞ konut limiti Kasım için 136,01 m³, Aralık için 259,35 m³ (30 Ekim 2026 haberleri); limiti aşan abonenin o aydaki *tüm* tüketimi 2. kademeden hesaplanır. Çamaşır başına ek ısı kaybı ~0,3–0,6 m³ olduğundan limiti tek başına etkilemez, ama limite yakın evlerde 2. kademe fiyatıyla maliyet ~%50 artar.
  - **Güncel fiyatı abone faturasından (ya da İGDAŞ/BOTAŞ tablosundan) alın;** Kasım 2026 için yeni birim fiyat açıklaması bulamadım.
- **Konut tipleri:** Apartman, cam balkon, kombi/kalorifer, soba; 2000 öncesi yalıtımsız binalar. Deney evlerinde bu bilgiler envanterlenecek (§8, E0).

### 3.4 İstanbul odağı (ekibin konumu)

| Veri | Durum |
|---|---|
| Ocak ortalama sıcaklığı 6,8 °C (1950–2025, MGM il sayfası) | Doğrulandı (sayfa okundu); 1991–2020 normali değil |
| Ocak oransal nemi | **Bulunamadı;** %78 varsayım. Pilot-0'da kendi termo-higrometrenizle dış (balkon) nemi de ölçün |
| TS 825 bölgesi | 2. bölge (METU çalışması) |
| Hane büyüklüğü | İstanbul 3,09 kişi (TÜİK, haber aktarımı); **İstanbul toplam hane sayısını bulamadım** |
| Bina stoku | 2000 ve öncesi yapılan **818 binden fazla** bina; bunların 264 bini 1980 öncesi (İBB–Kandilli 2020 deprem projesi, 15.02.2023 haberi). Toplam bina sayısı o kaynakta yok; yaygın aktarılan "~%70" oranı bir özetten geliyor, **doğrulanmadı.** "2000 öncesi = yalıtımsız" varsayımı yapılmamalı; **yalıtım durumuna dair kaynak bulamadım,** her evde ölçülecek (f_Rsi). |
| Doğalgaz | Kasım limiti 136,01 m³, Aralık 259,35 m³ (BOTAŞ, 30.10.2026 haberi) |

**İstanbul'a özgü hipotez (model çıktısına göre, ölçümle sınanmalı):** Kapalı oda bütün senaryolarda uzun süre yoğuşma üretir; sürekli aralık pencere bunu her senaryoda önler ama pahalıdır (~9–10 TL/yük). "Her saat 10 dk aç" gibi ucuz bir kural merkez parametrelerde yoğuşmayı sıfırlar, ancak hızlı kuruma/düşük tampon kabullerinde 2–5 saat yoğuşma kalır (§6.1). Yani **İstanbul'da ucuz kuralın yeterli olup olmadığı, her evin α, β ve f_Rsi değerlerine bağlıdır**; "tek kural herkese uymaz" önermesi ölçümle sınanacaktır.

**Kapsam notu:** Ekip tüm veriyi İstanbul'da toplayacak. Rapor, sonuçları "İstanbul konutları" için iddia eder; Türkiye geneli için yalnızca modelin iklim girdisini değiştirerek yapılan *senaryo* analizi (§6 alt tablo) verilir, ölçülmüş genelleme iddia edilmez.

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

`sim_nem_dengesi.py` (oda 30 m³, 5 kg kuru yük, %52 kalan nem, 20 °C iç sıcaklık, 2,6 L su). **Dış nem, α, β, G_diğer ve f_Rsi varsayımdır;** dış sıcaklık İstanbul için MGM il sayfasından (6,8 °C, 1950–2025), diğer bölgeler için MGM 1991–2020 bölge normalinden. Isı kaybı TL'si 1,70–1,87 TL/kWh aralığıyla (vergili abone fiyatı, §3.3; **doğrulanmadı**) hesaplandı. Taban BN'si %65 (İstanbul, G_diğer=0,05 kg/h kabulü ile).

### 6.1 İstanbul (ana senaryo)

| Strateji | Kuruma (h) | Tepe BN | BN>%60 (h) | Yoğuşma (h) f=.65 / .80 | Ek ısı kaybı |
|---|---|---|---|---|---|
| Pencere kapalı (ACH 0,3) | >24 | %93 | 24,0 | 22,6 / 20,2 | 0 |
| Pencere aralık, sürekli (ACH 2) | 9,1 | %65 | 8,3 | 0 / 0 | 5,5 kWh ≈ 9,3–10,3 TL |
| Her saat 10 dk tam aç | 11,1 | %73 | 12,1 | 0 / 0 | 3,1 kWh ≈ 5,2–5,8 TL |
| Kapalı + nem alıcı (0,3 kg/h) | 8,5 | %65 | 3,5 | 0 / 0 | elektrik ayrı |

**İstanbul duyarlılık (ACH, α, β, G_diğer, dış nem değiştirildi):**
- **Sağlam sonuç 1:** Kapalı odada tepe BN **%86–95**, yoğuşma (f=.65) **18–24 saat**; dış nem %70–85 ve G_diğer 0,02–0,05 aralığında da tepe %88–94.
- **Sağlam sonuç 2:** Sürekli aralık pencerede yoğuşma tüm BETA (1–10) ve ALPHA (0,03–0,09) kombinasyonlarında **0 saat**, tepe BN %64–70; ama kuruma 6,5–14,5 saat ve maliyet en yüksek.
- **Sağlam olmayan sonuç:** "Her saat 10 dk" için yoğuşma süresi parametreye bağlı: merkez değerde 0 saat, ama α=0,09 (hızlı kuruma) ve β=1'de **1,9–5,3 saat** (tepe BN %78–86). Yani bu stratejinin yeterli olup olmadığı, yalnızca modele güvenilerek söylenemez; **bu tam olarak α ve β'nın ölçülmesinin gerekçesidir.**

### 6.2 Diğer bölgeler (yalnızca senaryo; İstanbul dışında ölçüm yok)

| Bölge-benzeri | Strateji | Kuruma (h) | Tepe BN | Yoğuşma (h) f=.65 / .80 | Ek ısı kaybı |
|---|---|---|---|---|---|
| Marmara (+5,2 °C) | Kapalı | >24 | %93 | 22,7 / 20,3 | 0 |
| | Aralık, sürekli | 8,7 | %62 | 0 / 0 | 6,2 kWh ≈ 10,5–11,5 TL |
| | Her saat 10 dk | 10,5 | %72 | 0,1 / 0 | 3,4 kWh ≈ 5,9–6,5 TL |
| İç Anadolu (−0,6 °C) | Kapalı | 22,7 | %90 | 22,9 / 20,7 | 0 |
| | Aralık, sürekli | 7,3 | %54 | 0 / 0 | 8,6 kWh ≈ 14,6–16,1 TL |
| | Her saat 10 dk | 8,7 | %67 | 2,4 / 0 | 4,8 kWh ≈ 8,2–9,0 TL |
| Doğu Anadolu (−4,3 °C) | Kapalı | 19,9 | %89 | 23,1 / 21,0 | 0 |
| | Aralık, sürekli | 6,8 | %52 | 0 / 0 | 10,1 kWh ≈ 17,2–19,0 TL |
| | Her saat 10 dk | 8,1 | %65 | 4,6 / 0 | 5,7 kWh ≈ 9,6–10,6 TL |

**Okuma (nitel):**
1. Kapalı odada bir yük çamaşır, modelde odayı neredeyse doyuruyor ve yalıtımsız köşede 18+ saat yoğuşma üretiyor; İstanbul dahil bütün senaryolarda ve duyarlılık aralığında.
2. Sürekli aralık pencere her senaryoda yoğuşmayı önlüyor ama ısı kaybı en yüksek: İstanbul'da bir yük için ~9–10 TL, soğuk bölgelerde ~15–19 TL.
3. "Her saat 10 dk" maliyeti yaklaşık yarıya indiriyor; ancak yoğuşmayı önleyip önlemediği parametrelere ve bölgeye bağlı (İstanbul'da sınırda, Doğu Anadolu'da yoğuşma kalıyor).
4. **En iyi strateji iklime, odaya ve duvar yalıtımına (f_Rsi) bağlı; bu yüzden ölçüm gerekiyor.** Bu, projenin gerekçesidir. Bu bir model çıktısıdır; tersi gerçek veride çıkabilir ve bu da bulgu olur.

**Dikkat:** Bir yük başına ~5–10 TL (İstanbul) ısı kaybı ile kurutma makinesi elektriği (yük başına kWh değeri bu çalışmada doğrulanmadı) aynı mertebede olabilir. Bu bir *hipotez*; E5 ve maliyet analizi ile test edilecek.

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

**E0 – Ev envanteri ve sensör karakterizasyonu.** 3–5 evde (hepsi İstanbul): oda hacmi, pencere türü, ısıtma sistemi, çamaşır makinesi kapasitesi/devri, kurutma alışkanlığı, duvar yalıtımı (var/yok). Sensör kalibrasyonları. *(Pilot-0 = Kapı 0: donanım gelmeden mutfak terazisi ve ucuz termo-higrometre ile 3 gün elle kayıt; sınavlardan sonra 16–19 Kasım; fikrin kesin kararına veri. Protokol §11.)*

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

## 11. Takvim (sınav haftaları dikkate alınmış; 7 çalışma haftası)

**Varsayım:** Ekip 2–15 Kasım'da sınavda; proje işi **16 Kasım'da** başlar (sınav bitişi değişirse tablo kayar). Hedef: **28 Aralık'ta yükle**, son gün 4 Ocak 17:30.

**Sınav haftalarında (2–15 Kas) ekipten iş beklenmez.** Bu depoda yapay zekâ destekli hazırlık yapılabilir: Pilot-0 protokol föyü, firmware iskeleti, ön kayıt taslağı, literatür taraması, parça listesi ve fiyat doğrulaması. *Opsiyonel (ekibin kararı):* ortak ucuz parçaların (ESP32, HX711, baskül hücreleri, kablo; tahmini ~700–1.000 TL, fiyat doğrulanmadı) sınav haftasında sipariş edilmesi kargo beklemesini ortadan kaldırır; Pilot-0 olumsuz çıkarsa kayıp küçüktür.

| Hafta | Tarih | İş |
|---|---|---|
| 0 | 2–15 Kas | Sınav. Yalnızca hazırlık (yukarıda), ekip işi yok |
| 1 | 16–22 Kas | **Pilot-0** (16–18 Kas: bir yük çamaşır, mutfak terazisi + termo-higrometre, elle kayıt) → **Kapı 0 (19 Kas)**; kit montajı ve kalibrasyon (E0); 3 evin envanteri → **Kapı A (22 Kas)** |
| 2 | 23–29 Kas | E1 kuruma kinetiği (kontrollü oda), E3 bilinen kaynak |
| 3 | 30 Kas–6 Ara | E2 (ACH_RH vs ACH_CO₂) 2–3 evde, E4 yüzey → **Kapı B (6 Ara)** |
| 4 | 7–13 Ara | Tekrar ölçümler, model uydurma, leave-one-home-out |
| 5 | 14–20 Ara | Öneri motoru, E5 A/B (2 evde); E6 yalnızca etik formu hazırsa |
| 6 | 21–27 Ara | Rapor, grafikler, özet, ekler |
| 7 | 28 Ara–3 Oca | Tampon, gönderim |

**Kapı 0 (19 Kas, Pilot-0 sonrası):** Elle tartılan çamaşırın kütle–zaman eğrisi düzgün bir kuruma eğrisi veriyor mu (çıplak terazide ≥ ~1 L kayıp ölçülebiliyor mu) ve termo-higrometrede çamaşır asıldıktan sonra nem artışı görülüyor mu? **Evet → fikir #1 kesinleşir. Hayır/belirsiz → 22 Kas'a kadar #2'ye geçilir;** kalan süre ~6 hafta olduğundan #2 de donanım siparişi gerektirir ve çok sıkışıktır. Bu yüzden Kapı 0 bilerek kısa ve ucuz tutuldu.
**Kapı A (22 Kas):** Yük hücresi kararlılığı ve nem sensörü çapraz uyumu ön kayıttaki eşikte mi? Değilse donanım değişir.
**Kapı B (6 Ara):** ACH_RH, ACH_CO₂ ile ≥2–3 evde uyumlu mu? Değilse proje "kuruma tahmini + oda nem tepkisi + yoğuşma marjı" olarak daralır (H2 olumsuz sonuç olarak raporlanır; sentetik sonuç yine de bir bulgudur).

**Süre sıkışırsa kapsam kesme sırası:** (1) E6 kullanılabilirlik testi (etik formu gerektirir) → (2) ev sayısı 3'e iner (hepsi İstanbul'da) → (3) E5 tek evde → (4) E3 yalnızca tek ev. Kuruma kinetiği (E1) ve ACH karşılaştırması (E2) projenin çekirdeği olduğundan kesilmez.

## 12. Riskler

| Risk | Olasılık/Etki | Azaltma |
|---|---|---|
| Yük hücresi sallanma, sıcaklık sürüklenmesi | Yüksek/Orta | Dört ayaklı platform, filtre, referans kütle, sıcaklık telafisi |
| Nem sensörü gecikmesi ve ofseti | Orta/Orta | Tuz kalibrasyonu, ikili sensör, hızlı yanıt sensörü |
| Gerçek odada tam karışma/sabit ACH varsayımı bozulur | Yüksek/Yüksek | Pencere-kapı olaylarını kaydet; parçalı ACH; model hatası analizi |
| 3–5 evde deney lojistiği (hepsi İstanbul, trafik/yol süresi) | Orta/Orta | Dönüşümlü kit; standart protokol; hafif kit; en az 3 ev |
| Ailelerin katılımı ve çamaşır yükü değişkenliği | Orta/Orta | Standart yük (aynı havlu seti); alışkanlık yükleri ayrı etiketlenir |
| Hava sıcaklığı/ısıtma ayarları farklı | Orta/Orta | Her koşulu kaydet; modelde kontrol değişkeni |
| "İyi bilinen modelin tekrarı" itirazı | Orta/Yüksek | Çamaşırın ölçülen kaynak olması + Türkiye verisi + karar motoru (§4) |
| Teyitsiz rakamların rapora girmesi | Orta/Orta | §3.1 tablosu; kaynak doğrulama listesi |
| Sınav nedeniyle kısa çalışma süresi (7 hafta), Pilot-0 olumsuzsa geri dönüş zamanı yok | Yüksek/Yüksek | Kısa ve ucuz Kapı 0; kapsam kesme sırası (§11); sınav haftalarında hazırlık (kod, protokol, ön kayıt) |
| Gaz fiyatı ve iklim girdileri güncel/yerel değil (1950–2025 dönem, haber fiyatı) | Orta/Orta | Abone faturası ve MGM 1991–2020 normali; modeli parametreleştirilmiş tut, sonuçları aralık olarak ver |

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

**Sınav haftaları (2–15 Kas): ekibin yapacağı iş yok.**

- [ ] *(Hazırlık, bu depoda)* Pilot-0 protokol föyü, firmware iskeleti, ön kayıt taslağı, parça listesi/fiyat doğrulaması.
- [ ] *(Opsiyonel, ekip kararı)* Ortak ucuz parçaların siparişi (§11).
- [ ] **Pilot-0 (16–18 Kas):** Mutfak terazisi + termo-higrometre ile bir yük çamaşırın elle kaydı → **Kapı 0 (19 Kas)**.
- [ ] **Pilot-0 ile birlikte dış (balkon) nemini de ölç;** İstanbul'un Ocak/Şubat nemi için güvenilir bir kaynak bulamadım (§3.4).
- [ ] Üç evin envanteri (oda hacmi, pencere, ısıtma, makine devri, yalıtım). *"Kaç evde kışın çamaşır içeride asılıyor?" bilgisini ekip bilmiyor; envanterle öğrenilir.*
- [ ] *(İsteğe bağlı)* Sınıfta 5 soruluk anonim form (kışın çamaşır içeride mi asılıyor, kurutma makinesi var mı, ısıtma tipi, bina yaşı). Hedef kitle iddiasını İstanbul verisiyle destekler. **Kişisel veri toplanmayacak; okul/danışman onayı ve etik formu gerekip gerekmediği danışmanla netleştirilmeli.**
- [ ] Türkçe + yabancı literatür taraması (Google Scholar/ULAKBİM): "laundry as moisture source", "ventilation rate from moisture balance", "asılı çamaşır kuruma kinetiği", "TS EN ISO 13788".
- [ ] MGM İstanbul **1991–2020** normali ve aylık nem ("İllere ait mevsim normalleri" sayfası veya MEVBİS talebi); şu an elimizdeki 6,8 °C 1950–2025 dönemidir.
- [ ] **Abone faturasından güncel gaz TL/m³** (vergiler dahil) ve kurutma makinesi yük başı kWh (üretici etiketi).
- [ ] TS 825 bölge listesi ve TS EN ISO 13788 numarası.
- [ ] Parça fiyatları ve bulunabilirlik.
- [ ] Ön kayıt planı (hata eşikleri pilot sonrası).
- [ ] TYBS başvurusu için 3 resmî öğrenciyi belirle (Aralık başı); danışmanla hipotezleri gözden geçir.
- [ ] Bilimsel etik formu ve onam metni (E6 yapılacaksa).

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
- MGM İstanbul il istatistikleri (1950–2025): <https://www.mgm.gov.tr/Veridegerlendirme/il-ve-ilceler-istatistik.aspx?m=ISTANBUL>
- BOTAŞ kasım/aralık 2026 konut limitleri (İstanbul 136,01 / 259,35 m³): <https://www.tgrthaber.com/ekonomi/botas-dogal-gaz-tarifesini-guncelledi-kasim-ve-aralik-aylari-icin-il-bazli-tuketim-3368542>
- Vergili kademe fiyatları (Ankara 16,84 / 25,69 TL; haber): <https://www.karar.com/guncel-haberler/ankaralilara-dogalgazda-vergili-kademe-soku-1-metrekup-gazin-fiyati-25-2040128>
- Vergili kademe-1 fiyatı 17,88 TL (haber, doğrulanmadı): <https://www.hisse.net/haber/kombiyi-acanlar-dikkat-o-tarife-ilk-kez-uygulaniyor-fatura-2-katina-cikabilir-99572>
- İstanbul bina stoku (818 bin+ bina 2000 öncesi; İBB–Kandilli 2020, haber): <https://www.timeturk.com/genel/istanbul-da-eski-binalar-en-cok-hangi-ilcede-2000-oncesi-binalar-en-fazla-hangi-ilcede/haber-1760742>
- Enerji zammı Nisan 2026: <https://tr.euronews.com/2026/04/03/elektrik-ve-dogal-gaza-yuzde-25-zam>
- Elektrik tarifesi Nisan 2026: <https://uzmanpara.milliyet.com.tr/uzmanpara/elektrik-zammi-2026-nisanda-ne-kadar-oldu-elektrige-ne-kadar-zam-geldi-iste-yeni-tarife-7565631>
- Evren (Webtekno): <https://www.webtekno.com/turkiye-yapay-zeka-platformu-evren-erisime-acildi-h225949.html>
- TÜBİTAK 2204-A sayfası: <https://tubitak.gov.tr/tr/yarismalar/2204-lise-ogrencileri-arastirma-projeleri-yarismasi>
