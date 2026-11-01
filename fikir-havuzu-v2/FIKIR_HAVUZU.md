# Fikir Havuzu v2 — "Gerekli hissedilmeyen ama olursa avantaj sağlayan" projeler

> **Hazırlanma tarihi:** 1 Kasım 2026 · **Amaç:** Sınav haftalarında (2–15 Kas) *tartışılacak* aday listesi. Plan değil, menü. Karar sonrası seçilen fikir için `PLAN.md` yazılır.
> **Dosya durumu:** Her olgu "doğrulandı / haber-özet / bulamadım / tahmin" olarak işaretlendi. **"Bulamadım", "yok" demek değildir;** aramam standart web aramasıyla sınırlıdır (Google Scholar/ULAKBİM taranmadı).

---

## 1. Yeni çerçeve (sizin mesajınızdan çıkardığım)

| Konu | Önceki | Şimdi |
|---|---|---|
| Harcama tavanı | 6.000 TL | **25.000 TL** (yeni alınacaklar; mevcut Arduino R3 ×4, ESP32, küçük ekran, lehim seti, laptop, okul sistemleri sayılmıyor) |
| Hedef kitle | ≥ 500 bin kişi, yılda ≥ 10 kez | **Aranmıyor.** Savunma sanayisine bile yarasa yeter; taslak bile olsa yeter |
| Çekicilik | Sıklık | Birbirinden farklı, ilginç; **gerekli hissedilmeyen ama olursa avantaj sağlayan** |
| Yazılım/donanım | ≤ %70 yazılım | Tamamen yazılım ya da yazılım + fiziksel bağlantı; yazılım ağırlıklı |
| Yapay zekâ | İsteğe bağlı | **Yalnızca gerekirse.** Gerekmiyorsa eğitilmez; "gerekli mi?" sorusu araştırmanın parçası |
| Evren | Opsiyonel | Görüntü/video formatlarını kabul ediyor (avi, mp4, mov, png, jpg, tif, webm vb.): görüntü etiketleme/eğitim için. Gerekirse |

**Değişmeyen:** TÜBİTAK 2204-A kuralları (en çok 3 öğrenci + 1 danışman, kamu güvenliği riski olmamalı, yapay zekâ/araç kullanımı raporda belirtilmeli, başlık ≤ 15 kelime, özet 150–250 kelime, rapor ≤ 20 sayfa), **sağlık konusu yok**, fizik temalı olma isteği (aşağıdaki soru 1'e bakın).

## 2. Dürüst not: "Tamamen yeni" fikir neredeyse yoktur; yenilik "kama"dan gelir

Taradığım her sensör + fizik fikrinin bir öncülü çıktı (aşağıdaki kartlarda). Bu kötü haber değil: jüri "dünyada ilk" aramaz, **net bir boşluğu ve iyi kurulmuş bir deneyi** arar. Her kartta bu yüzden üç şeyi ayırdım: *öncül* (yapılmış olan), *kama* (bizim ekleyeceğimiz, bulamadığım şey), *risk*. Kama iddiası yalnızca "aramamda bulamadım" düzeyindedir; yazmadan önce literatür taraması şarttır.

## 3. Ortak tasarım ilkesi: "Yapay zekâ gerekli mi?" sorusunun cevabı projenin içinde olsun

Her fikirde şu üç basamak raporun yöntem bölümüne girer:
1. **Fizik tabanlı temel çözüm** (kural/model/filtre; eğitim yok).
2. **Ölçülmüş yetersizlik:** Temel çözüm hangi koşulda hedef hatayı sağlamıyor? (sayısal)
3. **Ancak o zaman** makine öğrenmesi (Evren veya laptop). Kazanç ölçülür: ML temel çözümü anlamlı biçimde geçmiyorsa **kullanılmaz ve bu da bulgu olarak yazılır.**

Bu, "yapay zekâ var mı?" sorusuna jüri karşısında savunulabilir bir cevap verir. Laptop (orta-üst segment) tüm DSP işleri için yeterli; GPU yalnızca ML aşamasında gerekir.

## 4. Karşılaştırma tablosu

| Kod | Fikir (kısa) | Yazılım | Yeni donanım maliyeti* | AI gerekli mi? | Savunma/kritik altyapı bağı | Öncül yoğunluğu | Kama gücü | Risk | Gösteri |
|---|---|---|---|---|---|---|---|---|---|
| **A** | GNSS'siz zaman/frekans: yayın, baz istasyonu ve şebeke sinyalleriyle ucuz osilatörü ayakta tutma | ~%75 | ~150–350 USD | Hayır (kestirici + filtre) | Yüksek (PNT dayanıklılığı) | Orta | **Orta-yüksek** (aramamda bu kombinasyon çıkmadı) | Orta | Orta |
| **B** | Şebeke frekansı (ENF) ile ses/video kaydının zaman damgası ve bütünlüğü | ~%85 | ~0–50 USD | Hayır | Orta (delil/dezenformasyon) | **Yüksek** (UMD, Uludağ) | Orta (Türkiye referansı + mesajlaşma uygulamaları) | Düşük | Orta |
| **F** | Ucuz yakın alan EMC tarayıcı (elektronik kartın yayın haritası) | ~%65 | ~250–600 USD | Hayır | Yüksek (EMC her savunma ürününde) | Orta | Orta | Düşük-orta | **Yüksek** (ısı haritası) |
| **D** | Gök polarizasyon pusulası (GNSS ve manyetiksiz yön) | ~%60 | ~50–150 USD | Hayır (fizik modeli) | Yüksek | Orta-yüksek | Düşük-orta | Orta (bulutlu İstanbul) | **Yüksek** |
| **G** | Lazer benek (speckle) ile sahteciliğe karşı malzeme parmak izi | ~%75 | ~20–80 USD | Hayır (karşılaştırma yapılır) | Orta-yüksek (sahte parça) | Orta | Orta | Orta (okuma tekrarlanabilirliği) | Orta |
| **C** | Pasif radar: İstanbul'da yayın sinyalleriyle uçak, ADS-B ile doğrulama | ~%75 | ~200–500+ USD | Hayır | **Çok yüksek** | Orta-yüksek | Düşük-orta | **Yüksek** | **Yüksek** |

\* Tüm USD değerleri tahmindir; Türkiye fiyatı/kur/gümrük doğrulanmadı. Doğrulanan tek veri noktaları: KrakenSDR 499 USD (üretici listesi); tinySA Ultra yaklaşık 79–185 EUR/USD aralığında satıcıya göre. **Kur ve gümrükle KrakenSDR bütçenin büyük kısmını yer.** Türk mağazası fiyatı bulunamadı.

**Benim sıralamam (özgünlük > savunma bağı > gösteri > bitirme garantisi):** **A**, **F**, **B** ilk üç; sonra **D**, **G**, **C**. A ve B aynı konuda birleşebilir (§5-A sonu). Bu sıralama öznel, tartışmaya açık.

---

## 5. Fikir kartları

### A. "Havadaki saat": GNSS kesilince zaman ve frekansı ayakta tutmak

**Fikir.** GNSS parazitlenirse ya da aldatılırsa, ucuz bir kristal osilatörü İstanbul'da zaten havada olan sinyallerle (DVB-T/T2 taşıyıcısı, LTE/GSM baz istasyonu, FM pilot tonu, şebeke frekansının uzun dönem ortalaması) sürekli düzeltmek ve **hangi sinyalin ne kadar kararlı olduğunu İstanbul'da ölçmek**.
**Neden "gerekli hissedilmeyen, avantajlı".** Kimse saatinin sapmasını düşünmez; GNSS gidince zaman damgası, ağ eşzamanı, radyo ve yüksek hassasiyetli ölçüm bozulur. GNSS parazit/aldatma izleme, uluslararası literatürde etkin bir konu (ör. arXiv 2509.13600, ucuz alıcılarla izleme).
**Fizik.** Kristal osilatör sıcaklık–frekans eğrisi ve yaşlanma, **Allan sapması**, PLL/Kalman döngüsü, OFDM pilot taşıyıcıları, taşıyıcı ofseti kestirimi.
**Yazılım (~%75).** SDR örneklerinden frekans ofseti kestirimi (pilot/senkron sinyali korelasyonu), Allan sapma hesabı, sıcaklık düzeltme modeli, Kalman tabanlı disiplin döngüsü, "GNSS kesintisi" emülasyonu (referansı bilerek keserek holdover ölçmek), İstanbul sinyal kararlılığı "atlası".
**Donanım.** Yeni: RTL-SDR V4 (1–2), PPS çıkışlı GPS modülü (sadece *referans*), TCXO/OCXO modülü, anten. Mevcut: Arduino/ESP32 (sayaç/DAC), laptop.
**AI gerekli mi?** Hayır; ML yalnızca sıcaklık–sapma modeli tek başına yetmezse karşılaştırılır.
**Öncül (bulduklarım).** IMDEA LTESS-track (RTL-SDR ile LTE'den osilatör ofseti), Tröger ve ark. DVB-T ile frekans senkronizasyonu (düşük maliyetli SDR, Allan sapma), NTNU/SINTEF 2023 LTE/5G holdover analizi.
**Kama.** Bulamadığım: *düşük maliyetli bir RTL-SDR'nin DVB-T/LTE/FM/şebekeyle GNSS kesintisi sırasındaki holdover performansını, birden çok sinyal tipini yan yana karşılaştırarak ölçen bir çalışma* ve İstanbul'da bir kararlılık haritası.
**Risk.** (1) Ppb düzeyi ölçüm ciddi metroloji gerektirir. (2) Baz istasyonu ve DVB-T vericisinin gerçekten disiplinli olup olmadığı belirsiz; bu, deneyin kendisidir (3GPP şartnamesi geniş alan baz istasyonları için ~0,05 ppm der; doğrulanmadı). (3) RTL-SDR V4'ün üst frekans sınırı ~1,77 GHz'dir (doğrulanmadı), yani LTE 2600 MHz bandı kapsanmaz. (4) 6–7 hafta.
**İlk iki gün (sınavdan sonra).** RTL-SDR'yi bir saat DVB-T ve LTE taşıyıcısına kilitleyip ofset–zaman grafiğini çıkar; sıcaklıkla ilişkisine bak. Ofset düzgün çıkıyorsa A'nın temeli var.
**A+B birleşimi (hipotez).** Şebeke frekansı kısa vadede oynar ama uzun dönem ortalaması çok kararlıdır (sistem işletmecileri zaman hatasını düzeltir; Türkiye ENTSO-E'ye bağlı olduğu için bu geçerli olmalı, doğrulanmadı). "Kısa vadede kristal, orta vadede yayın, uzun vadede şebeke" tek bir katmanlı referans olabilir.

### B. Şebeke parmak izi (ENF) ile "bu kayıt ne zaman çekildi, kesilmiş mi?"

**Fikir.** Mains ışığı ve mikrofonu 50 Hz çevresinde şebeke frekansının mikro dalgalanmasını kaydeder. Bir ses/video kaydındaki bu iz, bir **referans kayıtla** karşılaştırılırsa kaydın *zamanı* ve *kesilip yapıştırılıp yapıştırılmadığı* test edilebilir.
**Neden "avantajlı".** Yapay ses/görüntünün yaygınlaştığı dönemde bağımsız bir fiziksel doğrulama katmanı; kimse "kaydımın ENF'si var" diye düşünmez.
**Fizik.** Şebeke frekansı dinamiği (üretim–tüketim dengesi), aliasing, ışık titreşimi, kamera **yuvarlanan perde (rolling shutter)** örneklemesi, harmonikler.
**Yazılım (~%85).** Referans kaydedici firmware'i, ENF çıkarımı (STFT, harmonik birleştirme), eşleştirme/korelasyon, kesinti/ekleme tespiti, ölçüm raporu.
**Donanım.** Mevcut: ESP32/Arduino, laptop, telefon. Yeni: küçük **izole** transformatör/adaptör ile ENF algılayıcı (**şebekeye doğrudan bağlanılmaz**). Maliyet ~0–50 USD.
**AI gerekli mi?** Hayır; klasik DSP yeter. ML'nin (ör. kesinti dedektörü) eklenip eklenmeyeceği §3'teki 3 basamakla karar verilir.
**Öncül (bulduklarım).** UMD Min Wu laboratuvarı (video ENF patenti, "Seeing ENF"), Uludağ Üniversitesi'nden Vatansever (rolling shutter ENF, 2019), harmonik tabanlı güçlü yöntemler; 2025 Sensors: ses iletişiminde yüksek geçiren filtre temel bileşeni siliyor, harmonikler kullanılıyor.
**Kama.** Bulamadığım: *WhatsApp/Telegram ses mesajı (Opus) içinde ENF'nin sağ kalıp kalmadığını ölçen test*; *Türkiye için açık bir referans arşivi* (ENTSO-E'ye bağlı tek bir şebeke olduğu için İstanbul referansı Türkiye geneli için de geçerli olabilir; doğrulanmadı).
**Risk.** Düşük. Olumsuz sonuç ("WhatsApp'ta ENF kalmıyor") da bilimsel bulgudur.
**İlk gün.** Telefonla 5 dk sessiz ortamda kayıt al, aynı anda ESP32 referansı topla; STFT'de 50/100/150 Hz çizgileri ve korelasyon.

### F. Ucuz yakın alan EMC tarayıcı: kartın "elektromanyetik haritası"

**Fikir.** Küçük bir XY tarayıcıya takılı **yakın alan H-alan probu** ve ucuz spektrum analizörüyle bir elektronik kartın yaydığı gürültüyü ısı haritası olarak çıkarmak; hangi bileşenin/izin sorumlu olduğunu bulmak ve (yaklaşık) uzak alan değerine çevirmek.
**Neden "avantajlı".** EMC testi pahalı ve kuyruklu; ürün geliştirenlerin çoğu ön ölçüm yapmaz. Savunma ve tüm elektronik ürünlerde zorunlu bir süreç.
**Fizik.** Maxwell, Biot–Savart, döngü probu duyarlılığı (kaldırma/geri çevirme), yakın alan → uzak alan dönüşümü, anahtarlamalı kaynak harmonikleri.
**Yazılım (~%65).** Tarayıcı kontrolü (GRBL), spektrum okuma, 2B harita, hotspot kümeleme, probu dikkate alan alan-yeniden-yapılandırma (ters problem), rapor üretici.
**Donanım.** Yeni: tinySA Ultra (veya benzeri), DIY koaksiyel döngü probları (veya hazır set), düşük gürültülü ön yükselteç, XY mekaniği (3D yazıcı/CNC parçaları). Mevcut: Arduino (GRBL), laptop.
**AI gerekli mi?** Hayır; hotspot–bileşen eşleştirmesinde ML denenebilir, ama önce fizik tabanlı.
**Öncül (bulduklarım).** Beehive/Tekbox hazır prob setleri (yaklaşık 350 USD), YIC EMS4000 (4.195 €), Brno'da XYZ tarayıcı makalesi, DIY prob rehberleri.
**Kama.** Bulamadığım: *açık kaynak bir tarayıcı + ısı haritası yazılımı ve düşük maliyetli kurulumun hazır tarayıcıyla ölçülmüş kıyası*. Bu kıyas için bir referans cihaz/okul laboratuvarı lazım; yoksa kama zayıflar.
**Risk.** Mekanik hassasiyet, prob kalibrasyonu (DIY prob kalibre değil, **göreli** haritalama yapılır), tinySA gürültü tabanı.
**İlk üç gün.** Elle hareket ettirilen prob + tinySA ile bir anahtarlamalı güç kaynağının harmonikleri; hotspot belirgin mi?

### D. Gök polarizasyon pusulası: GNSS ve manyetiği olmadan yön

**Fikir.** Rayleigh saçılmasıyla oluşan gökyüzü polarizasyon deseninden güneşin azimutunu ve dolayısıyla **yönü** bulan ucuz bir sensör (böcek/karınca gibi).
**Neden "avantajlı".** Manyetik pusula şehirde bozulur, GNSS parazitlenebilir; gökyüzü her yerde bedava bir referans.
**Fizik.** Rayleigh saçılması, Stokes parametreleri, polarizasyon derecesi, güneş efemerisi (SPA), hava/aerosol etkisi.
**Yazılım (~%60).** Görüntüden/fotodiyotlardan Stokes çıkarımı, azimut kestirimi, güneş konumu modeli, bulutluluk altında doğruluk değerlendirmesi, filtre.
**Donanım.** Yeni: polarizör film + döner mekanizma (servo) + Pi/ESP32-CAM ya da fotodiyot halkası. Mevcut: Arduino/ESP32, ekran, laptop.
**AI gerekli mi?** Önce fizik modeli. Bulutlu gökte hata fizik modeliyle kabul edilemeyecek kadar büyükse görüntü tabanlı ML (Evren) denenir.
**Öncül (bulduklarım).** Aix-Marseille: renk kamerayla (~30 €) yön sensörü, polarimetrik kamera ~2.500 € karşılaştırması; Heriot-Watt: 8 fotodiyot çiftli halka, bulutlu/engelli gökte; Photonics 2024: aerosol düzeltmeli yöntem, farklı hava koşullarında ±2° içinde hata.
**Kama.** Zayıf-orta: akademik çalışmalar var. Ekleyebileceğimiz: İstanbul koşullarında (kış bulutu, binalar) bulutluluk–hata ilişkisinin ölçümü ve fizik-modeli vs ML karşılaştırması.
**Risk.** Ekim–Ocak İstanbul'da bulutlu gün çoktur: veri yetersizliği. Bu bir araştırma sorusuna çevrilebilir (hangi bulutlulukta çalışır).
**İlk gün.** Açık günde 3 açıda polarizör ile fotoğraf; yoğunluğun cos² değişimi görünüyor mu?

### G. Lazer benek (speckle) ile malzeme parmak izi: sahte parça ve etiket doğrulaması

**Fikir.** Kâğıt/plastik gibi bir yüzeyin mikroskobik pürüzünün lazer ışığında oluşturduğu **benek deseni** kopyalanamaz bir kimlik gibidir; ucuz bir okuyucuyla (Class 2 lazer işaretçi + telefon/kamera) yüzeyin parmak izini çıkarıp doğrulamak.
**Neden "avantajlı".** Sahte parça/etiketler tedarik zinciri sorunudur; şu an çoğu doğrulama barkod/QR gibi kopyalanabilir.
**Fizik.** Koherans, benek istatistiği (Goodman), Rayleigh yoğunluk dağılımı, benek kontrastı, korelasyon uzunluğu, ölçüm geometrisi hassasiyeti.
**Yazılım (~%75).** Görüntü hizalama, öznitelik çıkarımı, bulanık çıkarıcı (fuzzy extractor) ile anahtar/hash üretimi, **iç/dış Hamming mesafesi dağılımı**, yanlış kabul/ret oranı, entropi, NIST testleri, yaşlanma/sıcaklık sağlamlığı.
**Donanım.** Yeni: lazer işaretçi (Class 2), 3D yazıcı ile jig, makro lens. Mevcut: telefon, laptop.
**AI gerekli mi?** Hayır; klasik öznitelik yeter. CNN ile karşılaştırma mümkün (Evren görüntü eğitimine uygun).
**Öncül (bulduklarım).** Optik PUF literatürü: ucuz lazer ve telefon kamerasıyla okunabilen benek PUF'lar anılıyor; lotus yaprağı PUF'ı (50 kart, tekrar okuma). Bir tezde faza dayalı etiketlerde bakış açısı toleransı 0,2°.
**Kama.** Bulamadığım: *kâğıt/plastik gibi basit alt tabakalarda telefonla okunan benek parmak izinin Hamming dağılımı + yaşlanma/açı sağlamlığını birlikte ölçen ve açık kod veren çalışma*.
**Risk.** Okuma tekrarlanabilirliği (açı toleransı çok dar olabilir) → jig şart. **Lazer güvenliği:** yalnızca Class 2, göze doğrultmama, danışmanla kural yazılmalı.
**İlk gün.** Aynı kâğıdı 20 kez okuyup iç mesafeyi ölç; 20 farklı kâğıtta dış mesafeyi ölç.

### C. Pasif radar: İstanbul'un yayın kulelerini radar yapmak

**Fikir.** Çamlıca gibi kulelerden zaten yayılan FM/DVB-T sinyali havadaki uçaktan yansıyınca küçük bir Doppler/gecikme farkı oluşturur. **Hiç sinyal yaymadan** (yalnızca dinleyerek) uçak tespiti; doğrulamayı **ADS-B'yi etiket olarak kullanarak** yapmak.
**Neden "avantajlı".** Vericisi kapalı (transponder'sız) hedefler görülebilir; vericisiz sistem tespit edilemez. TÜBİTAK BİLGEM'in pasif radar ve PYAS projeleri bu alanın ulusal önceliğini gösterir.
**Fizik.** İkili (bistatik) geometri, Doppler, gecikme–Doppler **çapraz belirsizlik fonksiyonu**, doğrudan sinyal bastırma, CFAR, takip.
**Yazılım (~%75).** Referans/gözetim kanalı eşzamanlama, adaptif girişim bastırma, ambiguity fonksiyonu, CFAR, Kalman takip, ADS-B ile eşleştirme ve doğruluk istatistiği.
**Donanım.** Yeni: 2× RTL-SDR (ortak saat) **ya da** KrakenSDR (499 USD, 5 koherent kanal), Yagi/log-periyodik antenler, LNA. Mevcut: laptop.
**AI gerekli mi?** Hayır; klasik DSP. ML yalnızca zor çevrede (kentsel girişim) CFAR'a alternatif olarak karşılaştırılır.
**Öncül (bulduklarım).** KerberosSDR tabanlı bir lisans bitirme (iki RTL-SDR, ortak saat), Fransız bir çalışma: RTL-SDR ile DVB-T 482 MHz'de uçak (≈5 km) tespit etmiş (GNU Radio bildirisi), Queensland tezi (gerçek zamanlı Python), OnAir (yalnızca simülatörle test edilmiş).
**Kama.** Zayıf-orta: *ADS-B ile etiketli, istatistiksel tespit menzili (yakalama olasılığı–mesafe) ölçümü; İstanbul'un yoğun kentsel/hava trafiği ortamında*; düşük maliyetli saat eşleme.
**Risk.** En yüksek: donanım eşzamanı, doğrudan sinyal bastırma, 6–7 hafta. Küçük drone tespiti gerçekçi değil (düşük RCS), hedefi uçakla sınırlayın.
**İlk gün.** İki RTL-SDR'yi aynı sinyali dinletip çapraz korelasyonla gecikme/doğrusal faz uyumunu gör.

---

## 6. Elediklerim ve nedenleri (kısa)

| Fikir | Neden elendi / ikinci planda |
|---|---|
| **AIS etiketli hidrofon ("Boğaz'ın sesi")** | Boğaz'da düşük maliyetli hidrofonla ölçüm yapan YÖK tezi, İTÜ 2009 gürültü haritası tezi ve Gazioğlu & Okutan 2016 makalesi var; AIS etiketli açık veri setleri başka denizlerde var (VTUAD vb.). Lojistik (kıyı erişimi, su geçirmezlik, güvenlik) ağır |
| **GNSS parazit izleme (receive-only)** | Ucuz COTS alıcılarla izleme akademik literatürde var (arXiv 2509.13600, JRC ölçüm istasyonu); ADS-B'den parazit haritası çıkaran açık servisler de biliniyor (ör. gpsjam.org; bu oturumda doğrulamadım). Kama zayıf. A'nın *girdi/veri kaynağı* olarak kullanılabilir |
| **Mikro-Doppler (24 GHz) ile drone–kuş ayrımı** | St Andrews (Rahman & Robertson) literatürü güçlü; ucuz DemoRad ile yapılan bir lisans çalışmasında ayırt edici özellik bulunamamış; SNR riski |
| **Enkaz altı jeofon TDOA** | İTÜ'de "Jeofon Dizinleri Vasıtasıyla Kazazede Tespit Sistemi" çalışması, USGS prototipi ve Politecnico di Milano çalışması var. Kama zayıf |
| **Yer radarı (GPR) ucuz** | HackRF ile 6 cm kuru kum bloğu / 20 cm ıslak blok; Hackaday FMCW denemesi "ikna edici değil". Anten ve yer eşleşmesi zor |
| **Gölgeden saat/konum doğrulama** | Bellingcat ve IMAGEGUARD (arXiv 1811.08951) mevcut; ±birkaç yüz dakikalık belirsizlik; yenilik zayıf |
| **Muon tomografi (CosmicWatch)** | Fiziği çok güçlü ve gösterişli, ama yazılım oranı düşük, parça temini/kargo riski, veri toplama süresi uzun; 7 haftaya zor sığar |
| **Sıcaklığa göre kızılötesi NDT, video titreşim ölçümü** | Akademik yaygın; kama bulamadım |

## 7. Önceki iki fikrin yeni ölçütlere göre durumu

- **Çamaşır–Nem Dengesi** (`camasir-nem-dengesi/`): **Bitirme garantisi en yüksek** (donanımın çoğu mevcut, deney basit), ama "savunma bağı" ve "gösteri" yeni ölçütlerde zayıf. Yedek olarak güvenli.
- **Bitki ultrasonu** (`bitki-ultrasonu/`): Fikir çekici ama literatür (Khait 2023) ve ölçüm riski (ultrasonik mikrofon, menzil) yüksek. Yeni ölçütlere belirgin bir avantajı yok.

## 8. Takvim gerçeği (karar ve sipariş zamanı)

- Sınav 2–15 Kas; proje çalışması **16 Kas–3 Oca** (≈ 7 hafta). Yurtdışından gelen parçalar (SDR, tinySA, KrakenSDR) için kargo/gümrük 1–3 hafta sürebilir (tahmin).
- Bu yüzden **kararı ~12 Kasım civarı** vermek ve sipariş için **sınav haftasında** (parça listesi hazırsa) karar vermek, deneylere başlamayı 2 hafta öne alır. Parça bulunabilirliğini (Türkiye mağazaları) ben kontrol edebilirim.
- Karar sonrası seçilen fikir için `PLAN.md` + ilk-iki-gün deney föyü yazılır (çamaşır için yaptığım gibi).

## 9. Sorular (cevaplar fikir sırasını değiştirir)

1. **Fizik teması hâlâ şart mı?** "Tamamen yazılımsal" da olur dediniz; ama ana alan listesi (TÜBİTAK çağrı metni) bu projenin hangi alana gireceğini belirler. Bir ikincil kaynak 12 ana alandan yalnızca 9'unu listeledi (Biyoloji, Coğrafya, Değerler Eğitimi, Fizik, Kimya, Matematik, Psikoloji, Sosyoloji, Tarih); **Mühendislik/Bilgisayar alanı var mı, resmî çağrı metninden teyit edilmeli.** Yoksa projenin fizik ana alanında olması gerekir ve yukarıdaki fikirlerin hepsinde fizik ağırlığı (Allan sapması, Rayleigh saçılması, speckle istatistiği, yakın alan) vurgulanır.
2. **3D yazıcı, CNC/lazer kesici, osiloskop, sinyal üreteci** okul ya da evde var mı? (F ve G için belirleyici.)
3. **Balkon/çatı erişimi** ve İstanbul'da hangi semt? (A, C, D için anten ve görüş hattı.)
4. **Gösteri mi, araştırma sorusunun derinliği mi** daha önemli? (F/D/C gösterişli; A/B/G daha "bilimsel".)
5. **Savunma bağı** sadece "fayda anlatısı" mı, yoksa SSB'ye ya da bir firmaya sunum hedefi var mı? (Hedef varsa A, C, F öne çıkar.)
6. **Sınav haftasında parça siparişi** yapılabilir mi? (Karar 12 Kasım civarı.)

## 10. Kaynaklar

- Pasif radar: [rtl-sdr.com pasif radar etiketi](https://www.rtl-sdr.com/tag/passive-radar/page/2/), [GNU Radio bildirisi (RTL-SDR DVB-T)](https://pubs.gnuradio.org/index.php/grcon/article/download/101/59), [OnAir pasif radar](https://github.com/adswill/OnAir/wiki/Guide-Passive-radar), [BİLGEM pasif radar projesi](https://en.bilgem.tubitak.gov.tr/en/?p=109440), [TÜBİTAK pasif radar çağrısı](https://tubitak.gov.tr/tr/destekler/cagri-pasif-radar-gelistirilmesi-projesi)
- Polarizasyon pusulası: [Aix-Marseille renk kamera yön sensörü](https://ism.univ-amu.fr/doc/hal-04521170/_1), [Heriot-Watt fotodiyot halkası](https://researchportal.hw.ac.uk/en/publications/celestial-compass-sensor-mimics-the-insect-eye-for-navigation-und/), [Photonics 2024](https://doaj.org/article/0ab7060b95fa45a985212577dfd2ba26)
- ENF: [UMD Min Wu laboratuvarı](https://www.mast.umd.edu/research.php?t=enf), [Vatansever, Uludağ (rolling shutter ENF)](https://acikerisim.uludag.edu.tr/items/13b7142f-9d7b-4b16-9668-1003ca016515), [2025 Sensors (ses iletişiminde ENF)](https://www.mdpi.com/1424-8220/25/12/3697)
- Sinyal fırsatları ve zaman: [LTE/5G holdover (NTNU/SINTEF)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10781334/), [IMDEA LTESS-track](https://dspace.networks.imdea.org/bitstream/20.500.12761/433/1/paper.pdf), [DVB-T syntonization (Tröger ve ark.)](https://cris.fau.de/publications/123364384/)
- GNSS izleme: [arXiv 2509.13600](https://arxiv.org/pdf/2509.13600)
- Hidrofon: [Boğaz'da düşük maliyetli hidrofon tezi](https://acikbilim.yok.gov.tr/handle/20.500.12812/135006?show=full), [Boğaz sualtı gürültüsü (İstanbul Üniv.)](https://avesis.istanbul.edu.tr/publication/details/a2301579-f09c-4c55-93b2-9ba1eb653dac/underwater-noise-pollution-at-the-strait-of-istanbul-bosphorus), [İTÜ Boğaz ortam gürültüsü tezi](https://polen.itu.edu.tr/entities/publication/ef602b57-999a-47cd-bb7b-95d3b734d822)
- Mikro-Doppler: [Rahman & Robertson 2018](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6255807/), [Newhaven lisans raporu](https://oit-portal-test2.newhaven.edu/wp-content/uploads/2024/06/Brunell_Ashton_SURFReport_2019.pdf)
- GPR: [HackRF ile düşük maliyetli GPR](https://www.rtl-sdr.com/creating-a-low-cost-ground-penetrating-radar-with-two-hackrfs/), [Hackaday FMCW GPR](https://hackaday.io/project/203825-diy-8001600-mhz-fmcw-gpr-in-progress)
- Jeofon: [İTÜ jeofon kazazede tespiti](https://research.itu.edu.tr/en/publications/jeofon-dizinleri-vasitasiyla-kazazede-tespit-sistemi/), [USGS](https://pubs.usgs.gov/publication/ofr20091095)
- Gölge analizi: [Bellingcat](https://www.bellingcat.com/resources/2021/05/18/unsure-when-a-video-or-photo-was-taken-how-to-tell-by-measuring-the-length-of-shadows/), [IMAGEGUARD](https://arxiv.org/pdf/1811.08951)
- EMC tarayıcı: [DIY yakın alan probları](https://interferencetechnology.com/diy-near-field-probes-preamplifiers/), [Brno XYZ tarayıcı](https://www.fch.vut.cz/en/rad/results/detail/186881)
- Speckle PUF: [Optik PUF arXiv örneği](https://arxiv.org/pdf/2109.03505), [Fotonik PUF + telefon doğrulama](https://arxiv.org/pdf/2001.11794)
- Fiyat noktaları: [KrakenSDR (üretici)](https://www.krakenrf.com/product-page/krakensdr), [tinySA Ultra (rtl-sdr.com)](https://www.rtl-sdr.com/page/84/?pg=422)
- Evren: [Dünya haberi (11 model)](https://www.dunya.com/sektorler/bilim-ve-teknoloji/yapay-zekada-yerli-altyapi-buyudu-11-model-evrene-baglandi-haberi-841742), [Daily Sabah](https://www.dailysabah.com/business/defense/turkiye-launches-defense-focused-ai-platform-evren/amp)
- TÜBİTAK 2204-A alanları (ikincil): [bilimsenligi.com](https://www.bilimsenligi.com/tubitak-2204-a-lise-ogrencileri-arastirma-projeleri-yarismasi-2026-2027-cagrisi-yayinlandi.html/)
