# Uyduyu Işıkla ve Radyoyla Ölçmek: Telefon Fotoğrafı ve Doppler'le GNSS'siz Konum ve Yörünge

> *Çalışma başlığı, 13 kelime (kural: ≤15).* P01 (uydu Doppler'iyle konum) ve P09 (telefon fotoğraflarından yörünge) kartlarının birleşimi.

> **Durum: SEÇİLEN FİKİR (P01 + P09).** Ekip 2–15 Kasım'da sınavda. **Kapı 0: 19 Kasım** (Pilot-0 sonrası, `PILOT0_PROTOKOL.md`).
> **Hazırlanma:** 1 Kasım 2026 · **Hedef:** TÜBİTAK 2204-A, son başvuru **4 Ocak 2027, 17:30**.
> **Alan:** Fizik (Doppler olayı, kütle çekimi ve Kepler yasaları, astrometri, ölçüm kuramı) · **Yazılım payı:** ~%75 · **Yapay zekâ:** gerekmez.
> **Yeni harcama (tahmin, doğrulanmadı):** temel kurulum ~8.000–15.000 TL; tavan 25.000 TL.
> **Bu klasördeki dosyalar:** `birlesik_sim.py` (benzetim), `gecis_tahmini.py` (geçiş saatleri), `yapay_uydu.html` (kamera saati kalibrasyonu), `PILOT0_PROTOKOL.md` (ilk 3 gün). Önceki Doppler benzetimi: `../fikir-havuzu-v2/doppler_konum_sim.py`.

---

## 1. Tek cümlelik özet

Kağıthane'den geçen Uluslararası Uzay İstasyonu'nu (ISS) aynı anda **telefonla yıldızların önünde fotoğraflayıp** (açı ölçümü) ve **ucuz bir SDR alıcıyla radyo sinyalini dinleyip** (Doppler kayması), iki ters problemi çözmek: konumumuzu bilerek uydunun yörüngesini bulmak (Gauss 1801, Sputnik 1957) ve yörüngeyi bilerek kendi konumumuzu bulmak (TRANSIT 1958). Proje, ışık ile radyonun birbirinin zayıf yanını ne kadar kapattığını ölçer.

## 2. Hikâye ve neden önemli

- **1801:** Gauss, Ceres'in yalnızca birkaç açı ölçümünden yörüngesini hesapladı. Bugün "yalnız açılı yörünge belirleme" bu yöntemle başlar.
- **Ekim 1957:** Johns Hopkins APL'den Guier ve Weiffenbach, Sputnik'in radyo sinyalindeki Doppler kaymasından yörüngesini çıkardı. **Mart 1958:** McClure tersini önerdi: yörünge biliniyorsa Doppler eğrisinden alıcının konumu bulunur. Bu fikirden ilk uydu navigasyon sistemi TRANSIT doğdu.
- **1966–1974:** Dünya uydu üçgenlemesi (PAGEOS balonu): istasyonlar uyduyu yıldızların önünde fotoğraflayarak kıtalar arası konum farkını ölçtü (Schmid, NOAA PP-7). Deklanşörler radyo zaman sinyaline ~300 µs içinde eşlendi; **zamanlama o zaman da işin kalbiydi.**
- **Bugün:** GNSS (GPS vb.) sinyali bastırılabiliyor ya da aldatılabiliyor. EASA'nın güvenlik bülteni (SIB 2022-02R3, 5 Temmuz 2024) Karadeniz bölgesinde **FIR İstanbul (LTBB)** ve **FIR Ankara (LTAA)**'yı etkilenen alanlar arasında sayıyor; Temmuz 2026'da dördüncü revizyon yayımlandı (ikincil kaynak, bülten metni okunmadı).

**"Gerekli hissedilmeyen ama avantaj sağlayan":** GPS çalışırken kimse uydunun fotoğrafından konum bulmaya ihtiyaç duymaz. Ama GNSS'ten bağımsız, **iki ayrı fiziksel ilkeye** (ışık ve radyo) dayanan bir yedek, sinyal kesildiğinde avantajdır. Ayrıca aynı düzenek "uzay durumsal farkındalığı" (uydu takibi) yapar.

**Dürüstlük notu (raporda yazılmalı):** Sistem kendi GNSS alıcımızı kullanmaz, ama **saat** (internet NTP) ve **ilk yörünge bilgisi** (TLE) için dışarıya bağlıdır. Proje bu bağımlılığı ölçer ve azaltır (kendi yörüngemizi belirleriz, §6), tamamen ortadan kaldırmaz.

---

## 3. Araştırma soruları ve hipotezler

| Kod | Hipotez | Deney |
|---|---|---|
| H1 | Telefonla (teleskopsuz) Kağıthane'den ISS izinin uç noktaları, yıldızlara göre plaka çözümüyle **ölçülebilir açısal doğrulukla** belirlenir; kamera saati NTP'ye göre kalibre edilebilir. | E0, E1 |
| H2 | RTL-SDR + basit antenle ISS (437,8 MHz) ve Meteor-M2-4 (137,9 MHz) Doppler eğrileri ölçülebilir; frekans gürültüsü pilotta belirlenir. | E2 |
| H3 | **Yörünge (Gauss/Sputnik yönü):** Tek geçişte açılara Doppler eklemek, bir tur sonraki geçiş zamanı öngörüsünün hatasını yalnız açıya göre **belirgin biçimde** azaltır. Benzetim tahmini: Doppler gürültüsü 10 Hz ise ~8–25 kat, 50 Hz ise ~2–9 kat. | E3 |
| H4 | **Konum (TRANSIT yönü):** Yörünge TLE'den bilindiğinde telefon açıları konumu yüzlerce metre mertebesinde verir. Kamera saati bilinmiyorsa radyo Doppler'i bu saati kalibre ederek konumu iyileştirir. | E4 |
| H5 | **Diferansiyel:** Konumu bilinen bir istasyon (okul) aynı geçişte TLE'nin zaman hatasını ölçüp ikinci istasyona verirse, ikinci istasyonun konum hatası düşer. | E5 |
| H6 | **İki geçiş:** Aynı akşamki iki ISS geçişi birleştirilince öngörü hatası bir mertebeden fazla düşer. Yalnız açıyla bazen yanlış çözüme gidilir, Doppler bunu önler. | E6 |

> **Başarı eşikleri ön kayıtta yazılacak:** Pilot verisi geldikten sonra (Kapı A, 29 Kas) ve E3 öngörülerinden önce. Öngörüler git'e tarihli olarak işlenir, sonra gözlemle karşılaştırılır. Ölçümden önce eşik uydurmuyoruz.

---

## 4. Fizik (lise fiziğiyle bağ)

**Doppler olayı:** Δf = −(f₀/c)·dρ/dt (ρ: uyduya uzaklık). ISS ~7,66 km/s hızla gider. 437,8 MHz'de kayma en fazla **~±10 kHz**, Meteor-M2-4 için (137,9 MHz, ~820 km) **~±3 kHz**. Eğrinin sıfırdan geçtiği an uydunun en yakın olduğu andır (TCA). Eğimi, en yakın uzaklığı verir.

**Kütle çekimi ve dairesel hareket:** v = √(GM/r), T = 2π√(r³/GM). ISS için ~92,8 dakika. Periyottaki küçük bir hata her turda birikir: yarı büyük eksende 1 km hata, tur başına ~1,2 s zamanlama hatası demektir.

**Gauss yöntemi:** Üç açı ölçümü ve zamanından iki cisim yörüngesi bulunur. Yöntem 8. dereceden bir polinoma ve f, g serilerine dayanır (Curtis, Alg. 5.5). Sonra çok ölçümle en küçük kareler (EKK) ile iyileştirilir.

**Astrometri:**
- Plaka çözümünde fotoğraftaki yıldızlar katalogla eşleştirilir ve her pikselin gökteki yönü (sağ açıklık ve dik açıklık) bulunur. Lens bozulması polinomla düzeltilir (astrometry.net).
- Telefon ana kamerası ~65–75° görüş alanı ve ~4.000 piksel genişlikle piksel başına ~1 yay dakikası verir (tahmin; telefona göre değişir).

**Paralaks:**
- 600 km uzaktaki uydu, gözlemci 1 km kayınca yıldızlara göre **~0,1°** kayar. Konumu fotoğraftan bulmanın fiziği budur.
- Zamanlama hatası da açıya dönüşür: 0,05 s hata ≈ 380 m yörünge boyu ≈ ISS tepedeyken ~0,05°.

**Osilatör:** RTL-SDR'nin kristali (TCXO, ~1 ppm) 437,8 MHz'de ~±440 Hz ofset demektir. Ofset ve uydunun verici ofseti çözümde bilinmeyen olarak kestirilir.

**Ölçüm kuramı:** Doğrusal olmayan EKK, hata yayılımı, kovaryans ve "gözlenebilirlik" (hangi ölçüm hangi bilinmeyeni belirler).

**Projenin fizik özü (benzetimde görüldü, §6):** Açı ölçümü uydunun **yönünü** iyi, **uzaklığını** kötü belirler. Doppler ise **uzaklaşma hızını** (menzil değişimini) doğrudan ölçer. İkisi birbirinin zayıf yanını kapatır.

---

## 5. Yöntem

### 5.1 Optik hat (telefon)
1. **Hedefler:**
   - ISS: çok parlak, 437,8 MHz'de yayın yapıyor.
   - Çin uzay istasyonu (CSS/Tiangong): yalnız optik. Radyo yayını doğrulanmadı.
   - Gerekirse parlak roket gövdeleri.
2. **Çekim:** Telefon tripodda, manuel ("Pro") mod, odak sonsuz, pozlama 2–4 s, ISO 800–3200 (pilotta ayarlanır), aralıklı çekim (interval) ve Bluetooth deklanşör.
   - Her fotoğraf bir iz verir. İzin iki ucu, pozlamanın açılış ve kapanış anlarıdır.
   - 10 fotoğraf × 2 uç = 20 ölçüm.
   - iPhone'da manuel uzun pozlama için ayrı uygulama gerekebilir (**doğrulanacak**).
3. **Plaka çözümü:** astrometry.net. Yerel kurulum (Linux/WSL) geniş açı için 4100 serisi indeksleri kullanır. Çevrimiçi sürüm (nova.astrometry.net) de olur; yüklenen fotoğrafların gizlilik ayarı kontrol edilmeli.
   - Kağıthane ışık kirliliğinde yeterli yıldız çıkmazsa çözüm başarısız olur. Bu, Pilot-0'ın ilk sorusu.
   - B planı: 2×/3× telefoto lensle dar alan, okul bahçesi gibi daha karanlık nokta, ya da aynı yöne çekilmiş kısa pozlamaların yığılması.
4. **Zaman (en kritik adım, §6'daki benzetim bunu gösteriyor):**
   - Dizüstü saati NTP ile eşlenir (kayma time.is gibi bir sitede kontrol edilir).
   - Kamera saati **"yapay uydu" yöntemiyle** kalibre edilir: dizüstü ekranında, bilinen bir zaman yasasıyla hareket eden bir nokta çizilir. Telefon aynı modda (2–4 s pozlama) bu ekranı çeker. İzin başı ve sonu, pozlamanın gerçek açılış ve kapanış anını verir.
   - Ekran 60 Hz'de tazelenir (~17 ms adım). Böylece EXIF zaman damgasının ofseti ve dağılımı ölçülür.
   - Satır satır okuma (rolling shutter) etkisi de görülür.
   - Sayfa hazır: `yapay_uydu.html` (tarayıcıda açılır; dizüstü dışında donanım gerekmez).
5. **İz uçları:** Eşikleme ve çizgi uydurma, ardından uçta parlaklık profili. Uçaklar yanıp sönen ışıklarından ve öngörülen yoldan ayrılır.

### 5.2 Radyo hattı (SDR)
1. **Alıcı:** RTL-SDR Blog V4 ya da V4L. V4'ün üretimi tuner çipi bittiği için sona erdi; V4L aynı 1 ppm TCXO'yu taşıyor ve 500 kHz–1.766 MHz aralığını kapsıyor (satıcı sayfası).
2. **Anten:**
   - 437 MHz: tel ile yer düzlemli (ground-plane) ya da dipol, kol başı ≈17 cm. Elde tutulan Yagi isteğe bağlı.
   - 137 MHz: V-dipol, kol başı ≈53 cm.
   - **FM bant durdurucu filtre:** İstanbul'daki güçlü FM ve TV vericileri alıcıyı doyurabilir.
3. **Kayıt:** IQ kaydı (ör. rtl_sdr komutu ya da SDR++), başlangıç zamanı dizüstü saatinden, sonrası örnek sayacından.
4. **Frekans kestirimi:**
   - FM ses ve paket (ISS): her parçada FM ayırıcı çıkışının ortalaması ya da spektrum ağırlık merkezi alınır.
   - QPSK (Meteor LRPT): sinyalin 4. kuvveti alınır, 4·Δf'de bir çizgi çıkar.
   - Hepsi FFT ile.
5. **Hedefler:**
   - **ISS 437,800 MHz** (ses aktarıcısı; yalnızca biri konuşunca yayın yapar) ve **437,825 MHz** (APRS paketi). ARISS, 27 Ekim 2026 durumu. Mod sık değişir; her gözlemden önce ARISS sayfası kontrol edilir.
   - **Meteor-M2-4 137,9 MHz** (sürekli LRPT; SatNOGS'ta "operational"). Optik olarak görülmez, yalnız TRANSIT yönü (E4) için. Kağıthane'den her gün öğleden sonra 14:00–16:30 arası geçişleri var (§7).
   - **NOAA-15/18/19 kapatıldı** (Haziran–Ağustos 2025, NOAA). Kullanılamaz.
   - Orbcomm ve amatör küp uydular yedek; 2026 durumları doğrulanmadı.

### 5.3 Hesaplama (Python, açık kaynak)
- **Öngörü:** Skyfield + SGP4 + CelesTrak TLE (`gecis_tahmini.py`).
- **Yörünge:** Gauss → EKK (yalnız açı) → EKK (açı + Doppler, her geçişe ayrı frekans ofseti) → isteğe bağlı kamera saati ofseti de bilinmeyen.
- **Konum:** TLE yörüngesiyle enlem ve boylam (+ frekans ofseti + saat ofseti). Diferansiyel çözümde A istasyonu TLE'nin zaman hatasını kestirir, B istasyonu bu düzeltmeyle çözer.
- **Doğrulama:**
  - Yörünge: taze TLE (ISS'inki günde birkaç kez güncellenir) ve **bir sonraki geçişin gözlenen zamanı.**
  - Konum: haritadan bilinen koordinat. Telefonun GNSS'i yalnızca referans olarak ayrı kaydedilir, çözüme girmez.

---

## 6. Benzetim sonuçları (`birlesik_sim.py`; SENTETİK, ölçüm değil)

**Model:**
- Yörünge: ISS benzeri dairesel, 420 km / 51,6°. Küresel Dünya, dönme dahil, iki cisim.
- Ölçüm koşulları: 15° yükselim maskesi (kentsel ufuk). Her geçişte 10 fotoğraf × 4 s (20 iz ucu) ve 30 aralıklı Doppler ölçümü (437,8 MHz).
- Frekans ofseti ~500 Hz, bilinmiyor.
- Her durum 150 rastgele geçiş geometrisiyle denendi. Tablolarda **medyan / P90** var.
- Telefon için varsayılan açı ve zaman hataları (0,02–0,1°, 0,02–0,1 s), amatör gözlemcilerin özel kameralarla bildirdiği değerlerden (5–30″, 1–10 ms; Langbroek, Bassa ve Molczan, 2023) ~10 kat kötüdür. Bilerek kötümser tutuldu; **gerçek değerleri E0–E1 ölçecek.**

### 6.1 Yörünge belirleme (konum biliniyor): bir tur sonraki geçiş zamanı hatası, s

| Optik gürültü (açı / zaman) | Gauss, ham (3 nokta) | 3 nokta, EKK ile iyileştirilmiş | Açı EKK (20 nokta) | **Açı + Doppler (10 Hz)** | Açı + Doppler (50 Hz) |
|---|---|---|---|---|---|
| 0,02° / 0,02 s | 138 / 371 | 88 / 248 | 25 / 78 | **3 / 10** | 15 / 45 |
| 0,05° / 0,05 s | 256 / 608 | 204 / 611 | 84 / 241 | **5 / 14** | 19 / 46 |
| 0,10° / 0,10 s | 451 / 829 | 423 / 919 | 171 / 497 | **7 / 20** | 20 / 49 |

Epokta (geçiş ortasında) konum hatası, medyan: Gauss 6–17 km, 3 nokta 3–16 km, açı EKK 0,9–5,4 km, **açı + Doppler 0,2–1,1 km**.

**Okuma:**
1. Ham Gauss yöntemi tek başına kabadır; gürültüsüz veride bile ~6 km hata verir (f, g serisinin kesilmesi). Yalnızca başlangıç tahmini olarak kullanılır.
2. Ölçüm sayısını 3'ten 20'ye çıkarmak hatayı ~2–3,5 kat azaltıyor.
3. **Doppler eklemek, bir tur sonraki öngörü hatasını yalnız açıya göre ~8–25 kat (10 Hz) ya da ~2–9 kat (50 Hz) azaltıyor** (H3). Nedeni: tek kısa geçişte açılar uzaklığı ve dolayısıyla periyodu zayıf belirliyor; Doppler menzil değişimini doğrudan ölçüyor.

### 6.2 Kamera saati bilinmiyorsa (ofset σ = 0,3 s; açı 0,05°/0,05 s; Doppler 10 Hz)

| Yöntem | Epok hatası (km) | Bir tur sonra (s) |
|---|---|---|
| Açı EKK | 3,4 / 12,1 | 74 / 240 |
| Açı + Doppler | 1,3 / 3,1 | 4 / 13 |
| Açı + Doppler + saat ofseti kestirimi | **0,7 / 2,1** | 4 / 14 |

Radyo, kameranın saat ofsetini **~80 ms (medyan) / 280 ms (P90)** doğrulukla kestiriyor. Bu, doğrudan kalibrasyondan (E0, hedef ≤50 ms) kötüdür; **E0 yapılmalı**, radyo ise bağımsız bir sağlamadır.

### 6.3 Aynı akşam iki geçiş (~93 dk arayla): ikinci geçişten bir tur sonraki zamanlama hatası, s

| Optik gürültü | Tek geçiş, açı | İki geçiş, açı | **İki geçiş, açı + Doppler** |
|---|---|---|---|
| 0,05° / 0,05 s | 167 / 487 | 0,06 / 870 (**%16'sı yanlış çözüm**, >60 s) | **0,04 / 0,11** (%0 yanlış) |
| 0,10° / 0,10 s | 325 / 756 | 0,13 / 888 (**%22'si yanlış çözüm**) | **0,07 / 0,19** (%0 yanlış) |

**Okuma (H6):** İki geçiş, periyodu ölçüm aralığının kendisiyle belirler; hata saniyenin onda birine iner. Yalnız açıyla çözüm her 4–6 denemeden birinde yanlış bir yörüngeye kilitleniyor. **Doppler bu belirsizliği bütünüyle kaldırıyor.**

Gerçek fırsatlar (§7): 16 Kasım 18:16 ve 19:53 (ikincisi kısa), 28 Kasım 18:24 ve 20:01.

### 6.4 Konum belirleme (yörünge TLE'den; kamera saati kalibre): yatay hata, m

| TLE yörünge boyu hatası | Optik (açı / zaman) | Yalnız Doppler (10 Hz) | Yalnız açı | Birleşik |
|---|---|---|---|---|
| 0 | 0,02° / 0,02 s | 789 / 2.078 | 99 / 205 | **98 / 196** |
| 0 | 0,10° / 0,10 s | 830 / 2.417 | 531 / 1.039 | **369 / 766** |
| 1 km | 0,02° / 0,02 s | 1.001 / 2.092 | 637 / 1.613 | 648 / 1.609 |
| 1 km | 0,10° / 0,10 s | 1.179 / 2.671 | 840 / 1.859 | 747 / 1.645 |

Doppler gürültüsü 50 Hz olursa yalnız Doppler hatası ~3,2–3,9 km'ye çıkar; açılar değişmez.

**Kamera saati bilinmiyorsa** (σ 0,3 s, TLE hatası 1 km, açı 0,05°/0,05 s):

| Yöntem | Yatay hata (m) |
|---|---|
| Yalnız Doppler | 1.145 / 2.417 |
| Yalnız açı | 1.822 / 3.873 |
| Birleşik, saat ofseti kestirilmeden | 1.495 / 3.097 |
| Birleşik, saat ofseti de kestirilerek | **820 / 1.897** |

**Okuma:**
1. **Sürpriz sonuç:** ISS yakın (420 km) olduğu için paralaks büyük. Saat iyi kalibre edilirse **telefon fotoğrafı, aralıklı ISS Doppler'inden daha iyi konum veriyor** (~100 m'ye karşı ~800 m).
2. Doppler'in konumdaki asıl katkısı, kameranın saatini düzeltmek: 1.822 m'den 820 m'ye.
3. TLE hatası ~1 km olunca bütün yöntemler ~0,6–1,2 km'de takılıyor. Bu, H5'in (diferansiyel) gerekçesi.
4. Sürekli sinyalli Meteor-M2-4 ile yalnız Doppler konumu, önceki benzetimde (137,5 MHz, 1 Hz gürültü, tek geçiş) ~190 m / 3,4 km çıkmıştı (`../fikir-havuzu-v2/DERIN_INCELEME.md` §1.6). Yani ISS'in aralıklı sinyali yerine sürekli bir uydu, Doppler hattının hakkını verir.

### 6.5 Diferansiyel (A: konumu bilinen okul, B: 3–10 km uzakta, aynı geçiş; TLE hatası 1 km, Doppler 10 Hz)

| Kamera saati | A–B uzaklığı, optik gürültü | B, ham TLE ile (m) | **B, A'nın düzeltmesiyle (m)** | A'nın TLE zaman hatası kestirimi |
|---|---|---|---|---|
| Kalibre | 3 km, 0,05° / 0,05 s | 739 / 1.912 | **294 / 551** | 19 / 51 ms |
| Kalibre | 3 km, 0,10° / 0,10 s | 824 / 1.997 | **437 / 932** | 21 / 68 ms |
| Kalibre | 10 km, 0,05° / 0,05 s | 723 / 1.560 | **261 / 563** | 18 / 43 ms |
| Bilinmiyor (σ 0,3 s) | 3 km, 0,05° / 0,05 s | 763 / 1.776 | 468 / 1.515 | 45 / 147 ms |
| Bilinmiyor (σ 0,3 s) | 10 km, 0,05° / 0,05 s | 736 / 1.851 | 437 / 1.313 | 37 / 120 ms |

**Okuma (H5):** Kamera saatleri kalibre edilirse diferansiyel düzeltme B'nin hatasını medyanda **~2–3 kat**, P90'da ~2–3,5 kat azaltıyor (ör. 3 km, 0,05°: P90 1,9 km'den 0,55 km'ye). Saat kalibre değilse kazanç küçük. DGPS'in mantığı aynıdır. Dört öğrenci iki istasyon olarak çalışabilir.

### 6.6 Sınırlar (raporda açıkça yazılacak)
- **"Inverse crime":** Veriyi üreten ve çözen model aynı.
- Modellenmeyenler:
  - Hava sürtünmesi, J2 (basık Dünya), ışık zamanı (~2 ms), atmosferik kırılma, iyonosfer.
  - Uydunun gölgeye girmesi: geçişin tamamı görünür sayıldı, gerçekte çoğu geçişin bir kısmı görünür.
  - TLE'nin radyal ve yörüngeye dik hataları; yalnız yörünge boyu hata eklendi.
  - Doppler'de "ayna" belirsizliği: ilk tahmin doğru tarafta başlatıldı. Fotoğraf bu belirsizliği zaten çözer.
  - Çok yollu yayılma.
- Bu sonuçlar "ilke olarak işe yarar mı ve hangi hata baskın?" sorusunu yanıtlar. **Gerçek doğrulama E1–E6'dır.**
- Çalıştırma: `numpy`, `scipy`; ~2 dakika.

---

## 7. Gözlem pencereleri (Kağıthane, `gecis_tahmini.py`, TLE epoğu 1 Kasım 2026)

**Uyarı:** TLE 2–8 hafta ileriye yayıldı. ISS yörünge düzeltmeleri yaptığı için **saatler dakikalarca kayabilir**. Tarih pencereleri yörünge düzleminin dönüşüne bağlıdır ve daha güvenilirdir. **Her gözlemden 1–2 gün önce tahmini taze TLE ile yenileyin.**

**ISS, akşam görünür geçişleri (yükselim > 15°, uydu güneşte, Güneş < −6°):**

| Tarih | Tepe (TSİ) | Tepe yükselim | Görünür süre |
|---|---|---|---|
| 16 Kas Pzt | 18:16 | 61° | 4,0 dk |
| 16 Kas Pzt | 19:53 | 17° | 0,5 dk (aynı akşam 2. geçiş, kısa) |
| 17 Kas Sal | 19:05 | 21° | 3,2 dk |
| 18 Kas Çar | 18:17 | 28° | 4,3 dk |
| 20 Kas Cum | 18:18 | 17° | 2,3 dk |
| 25 Kas Çar | 19:11 | 23° | 1,5 dk |
| 26 Kas Per | 18:23 | 18° | 2,6 dk |
| 27 Kas Cum | 19:12 | 44° | 2,5 dk |
| **28 Kas Cmt** | **18:24 ve 20:01** | 30° ve 38° | 4,4 ve 1,2 dk (**E6: iki geçiş**) |
| 29 Kas Paz | 19:13 | 69° | 4,1 dk |
| 30 Kas Pzt | 18:25 | 69° | 5,3 dk |
| 1 Ara Sal | 19:14 | 23° | 3,7 dk |
| 2 Ara Çar | 18:26 | 39° | 4,9 dk |

**Sonra:**
- **ISS sabah penceresi:** 12–18 Aralık ve 24–31 Aralık, 06:20–07:15. Hafta sonları: 12 Ara Cmt 07:09 (35°), 13 Ara Paz 06:21 (20°), 26 Ara Cmt 07:13 (24°), 27 Ara Paz 06:25 (19°).
- **Çin uzay istasyonu (yalnız optik):**
  - Sabah 19 Kas–1 Ara.
  - Akşam **13–26 Aralık**, 18:15–20:10 arası; geçişlerin yaklaşık yarısında tepe yükselimi 60°'nin üstünde, örneğin 20 Ara Paz 18:31 (84°), 23 Ara Çar 18:42 (78°).

**Radyo (bulutta da çalışır):**
- ISS'in Kağıthane'den günde ~4–5 geçişi var (maske 15°), örneğin 17 Kas 17:28 (79°), 18 Kas 16:40 (44°).
- Meteor-M2-4 her gün öğleden sonra 14:00–16:30 arası 1–2 geçiş yapar, örneğin 16 Kas 14:34 (33°) ve 16:14 (31°), 17 Kas 15:52 (50°), 18 Kas 15:30 (79°).

---

## 8. Deneyler

**E0 – Kurulum ve kalibrasyon (Pilot-0'ın parçası):**
- **Kamera saati:** "yapay uydu" yöntemi (§5.1). Her telefon için ofset ve dağılım (ms) ölçülür, uzun pozlamada EXIF zamanının neyi gösterdiği (açılış mı, kapanış mı) bulunur.
- **Görüş alanı ve bozulma:** Bir yıldız fotoğrafının plaka çözümü.
- **SDR:** Frekans ofseti (ppm) ve ısınma kayması. Uzun kayıtta sabit bir yayın taşıyıcısına göre bağıl kayma ölçülür; **mutlak ofset çözümde kestirilir.**

**E1 – Optik ölçüm doğruluğu:**
- Taze TLE ile ISS geçişinde iz uçlarının öngörülen yönle farkı alınır. Bu farklar açı hatası (σ_θ) ile zaman hatasını (σ_t) ayırmak için yörünge boyunca ve dik olarak ikiye bölünür.
- Yıldız sayısı ve görüş alanı (ana kamera / telefoto) karşılaştırılır.
- Çıktı: H1 ve benzetimin gerçek girdileri.

**E2 – Radyo Doppler eğrisi:**
- ISS (437,8 MHz) ve Meteor-M2-4 (137,9 MHz) geçişleri kaydedilir, ölçülen ve TLE'den öngörülen Doppler eğrileri karşılaştırılır.
- Frekans gürültüsü (σ_f), geçiş başına kaç saniye sinyal olduğu (ISS'in ses ve paket yoğunluğu) ve FM filtresinin etkisi ölçülür.
- Çıktı: H2.

**E3 – Yörünge belirleme ve "öngör–doğrula" testi (çekirdek):**
- Her uygun ISS akşam geçişinde fotoğraf ve radyo birlikte alınır.
- Üç yöntemle yörünge hesaplanır: Gauss, açı EKK, açı + Doppler.
- **Her yöntem için bir sonraki görünür geçişin zamanı ve yönü git'e işlenir (ön kayıt)**, sonra gözlenir.
- Ölçüt: öngörülen ve gözlenen geçiş zamanının farkı (s), taze TLE ile fark (km).
- Çıktı: H3.

**E4 – Konum (çekirdek):**
- Konumu "bilinmiyor" sayılan noktalarda (öğrencilerin evleri) konum çözülür:
  - **(a)** yalnız Meteor-M2-4 Doppler'i (tek ve çok geçiş)
  - **(b)** yalnız ISS açıları
  - **(c)** ISS açı + Doppler
- Referans: haritadan koordinat. Telefon GNSS'i yalnızca karşılaştırma için ayrı kaydedilir.
- Çıktı: H4 ve hata elipsleri.

**E5 – Diferansiyel (iki istasyon):**
- A istasyonu okulda (konumu biliniyor), B istasyonu bir öğrencinin evinde (3–10 km). Aynı ISS geçişinde iki ekip eş zamanlı ölçer.
- A, TLE'nin zaman hatasını kestirir; B ham TLE ile ve düzeltilmiş TLE ile çözülür.
- B'de ikinci SDR yoksa B yalnız optik çalışır (saat kalibre olmalı).
- Çıktı: H5.

**E6 – Aynı akşam iki geçiş:**
- 28 Kasım Cumartesi (18:24 ve 20:01) en iyi aday; yedekler 16 Kas ve 17 Ara (CSS, yalnız optik).
- İki geçişin ölçümleri birleştirilir ve tek geçişle karşılaştırılır.
- Çıktı: H6.

**E7 – (opsiyonel) Çin uzay istasyonu:** 13–26 Aralık akşam penceresinde yalnız optik yörünge belirleme. Farklı yörünge eğimi (41,5°) ve yükseklikte yöntemin tekrarlanabilirliği sınanır.

**Yöntem disiplini:**
- Öngörüler gözlemden önce git'e işlenir.
- Ham veri (fotoğraflar, IQ kayıtları, zaman günlüğü) saklanır.
- Başarısız geceler de raporlanır (bulut, sinyal yok).
- Benzetim, ölçülen σ değerleriyle yeniden çalıştırılır ve tahmin ile gözlem karşılaştırılır.

---

## 9. Donanım ve bütçe

### 9.1 Mevcut (maliyete girmez)
Telefonlar (manuel pozlama modu olan en az 2 tane, **pilotta doğrulanacak**), dizüstü bilgisayarlar, Arduino/ESP32 (isteğe bağlı: SDR sıcaklık kaydı).

### 9.2 Yeni harcama (TAHMİN; Türkiye fiyatları ve kur DOĞRULANMADI)
Referans fiyat: WiMo, RTL-SDR V4 + anten seti 99 € (Temmuz 2026). Kur kabulü 1 € ≈ 50–55 TL; kargo ve gümrük belirsiz.

| Kalem | Adet | Tahmini TL |
|---|---|---|
| RTL-SDR V4 / V4L + dipol anten seti | 1 | 5.000–8.000 |
| FM bant durdurucu filtre | 1 | 1.000–2.000 |
| Koaksiyel uzatma (~5 m) + SMA adaptörler | 1 | 500–1.000 |
| 437 MHz anten malzemesi (tel, SMA konnektör, PVC boru) | 1 | 200–500 |
| Tripod + telefon tutucu | 2 | 1.000–3.000 |
| Bluetooth deklanşör kumandası | 2 | 300–800 |
| **Temel toplam (1 radyo + 2 optik istasyon)** | | **~8.000–15.300 TL** |
| *Opsiyonel:* ikinci SDR seti + filtre + kablo + anten (E5'te B istasyonu için) | 1 | +6.700–11.500 |

**Not:** Opsiyonel kalemle üst sınır 25.000 TL'yi aşabilir. İkinci SDR **yalnızca doğrulanmış fiyatlarla toplam tavanın altında kalıyorsa** alınır. Yoksa E5'te B istasyonu yalnız optik çalışır.

---

## 10. Yazılım (~%75)

1. **Öngörü ve planlama:** `gecis_tahmini.py` (hazır). Gözlem gecesi için gökyüzü haritası: izin nereden geçeceği, hangi parlak yıldızların yanında olacağı.
2. **Optik boru hattı:**
   - EXIF okuma, iz bulma ve uç noktalar.
   - astrometry.net çağrısı ve WCS ile piksel → sağ açıklık/dik açıklık dönüşümü.
   - Kamera saati düzeltmesi.
   - "Yapay uydu" kalibrasyon sayfası (hazır: `yapay_uydu.html`).
3. **Radyo boru hattı:**
   - IQ kaydı ve zaman damgası.
   - Spektrogram, sinyalli parçaların bulunması, parça başına frekans kestirimi.
4. **Kestirim:** Gauss, EKK (açı / Doppler / birleşik, saat ofsetli), konum çözücü, diferansiyel düzeltme, belirsizlik (kovaryans → hata elipsi). Çekirdeği `birlesik_sim.py`'de var; gerçek veriye uyarlanacak.
5. **Gösteri:**
   - Uydu geçerken hoparlörde yükselip alçalan Doppler "ıslığı".
   - Ekranda fotoğraf izi ile öngörülen iz üst üste.
   - Harita üzerinde her ölçümle daralan konum elipsi.
   - 3B'de yörünge.
6. **Yapay zekâ:** Gerekmez. Fizik modeli ve EKK yeterli. İz bulma klasik yöntemle (eşik ve çizgi uydurma) başarısız olursa, bir öğrenme yöntemi **ancak fizik tabanlı yöntemle karşılaştırılarak** denenir. Evren kullanılırsa raporda belirtilir.
7. **Açık kaynak:** Kod ve (kişisel veri içermeyen) ham veri depoda paylaşılır.

---

## 11. Takvim (7 çalışma haftası)

**Varsayım:** Ekip 2–15 Kasım'da sınavda; proje işi **16 Kasım'da** başlar. Hedef **28 Aralık'ta yükleme**; son gün 4 Ocak 17:30.

**Sınav haftalarında (2–15 Kas) ekipten iş beklenmez.** Bu depoda hazırlık yapılabilir:
- Optik ve radyo boru hattı iskeleti.
- Ön kayıt taslağı.
- Literatür taraması.

**Opsiyonel (ekip kararı):** SDR setini sınav haftasında sipariş etmek, radyo pilotunu 16–18 Kasım'a yetiştirir. Optik pilot ek parça istemez (tripod yoksa telefon sabit bir yere dayanır).

| Hafta | Tarih | İş |
|---|---|---|
| 0 | 2–15 Kas | Sınav. Yalnızca hazırlık |
| 1 | 16–22 Kas | **Pilot-0** (`PILOT0_PROTOKOL.md`): ISS 16 Kas 18:16 (61°), 17 Kas 19:05, 18 Kas 18:17. Meteor-M2-4 ve ISS radyo kaydı (SDR geldiyse). E0 kalibrasyonları. **Kapı 0 (19 Kas)** |
| 2 | 23–29 Kas | ISS akşam kampanyası (fotoğraf + radyo): 25, 26, 27, **28 (iki geçiş, E6)**, 29 Kas. E1, E2. **Kapı A (29 Kas):** σ değerleri ölçüldü → ön kayıt ve eşikler yazılır, ilk öngörüler git'e işlenir |
| 3 | 30 Kas–6 Ara | Son akşam ISS geçişleri: 30 Kas (69°), 1 ve 2 Ara. **E3 öngör–doğrula, E5 diferansiyel** (okul + ev). **Kapı B (6 Ara)** |
| 4 | 7–13 Ara | E4: Meteor-M2-4 ile her gün öğleden sonra Doppler konumu (evlerde). Analiz. ISS sabah penceresi 12–13 Ara (hafta sonu) |
| 5 | 14–20 Ara | E4 ve E5 tekrarları (sabah ISS), **E7** (CSS akşam, 15–20 Ara). Benzetimi ölçülen σ'larla yeniden çalıştır |
| 6 | 21–27 Ara | Rapor, grafikler, özet, gösteri videosu |
| 7 | 28 Ara–3 Oca | Tampon, gönderim |

**Kapı 0 (19 Kas):**
- Optik: Bir ISS fotoğrafı plaka çözüldü mü? İz uçları seçilebiliyor mu?
- Radyo: Bir Doppler eğrisi (Meteor ya da ISS) spektrogramda görülüyor mu?
- Kararlar:
  - **İkisi de evet →** birleşik plan sürer.
  - **Yalnız optik →** P09 ağırlıklı devam, radyo sonra.
  - **Yalnız radyo →** P01 ağırlıklı devam (Meteor ile konum), optik B planı (telefoto, karanlık nokta).
  - **İkisi de hayır →** 22 Kasım'a kadar sorun giderilir ya da yedek fikre (`../projeler/00_DIZIN.md`) geçilir.
- **Birleşik planın güçlü yanı:** Bir hat başarısız olsa bile diğeri tek başına bir projedir.

**Kapı A (29 Kas):** En az 3 ISS geçişinde fotoğraf ve en az 3 geçişte Doppler var mı? σ_θ, σ_t ve σ_f ölçüldü mü? Hayırsa E5 ve E6 kesilir, E3 tek yöntemle (açı) sürer.

**Kapı B (6 Ara):** E3 öngörüleri doğrulandı mı? Aralık'ta yalnızca sabah ISS geçişleri ve CSS (yalnız optik) kalıyor, buna göre E4–E7 seçilir.

**Süre sıkışırsa kapsam kesme sırası:**
1. E7 (CSS)
2. E5'te ikinci SDR (B istasyonu yalnız optik çalışır)
3. E6 (iki geçiş)
4. E4'te tek ev

**E1, E2, E3 ve E4'ün en az bir noktası projenin çekirdeğidir, kesilmez.**

---

## 12. Riskler

| Risk | Olasılık / Etki | Azaltma |
|---|---|---|
| **Bulut** (İstanbul, Kasım–Aralık) akşam geçişlerini kapatır | Yüksek / Yüksek | 16 Kas–2 Ara arası 15 akşam geçişi (bazıları 1 dakikadan kısa) + sabah ve CSS pencereleri. Radyo bulutta çalışır: E2 ve E4a havadan bağımsız |
| Işık kirliliğinde yeterli yıldız yok, plaka çözümü başarısız | Orta / Yüksek | Pilot-0'ın ilk sorusu. Telefoto, karanlık nokta (okul bahçesi), kısa pozlamaların yığılması, bilinen parlak yıldızlarla elle eşleme |
| **Kamera zamanlaması** (EXIF semantiği, deklanşör gecikmesi, satır satır okuma) | Yüksek / Yüksek | E0 "yapay uydu" kalibrasyonu; radyo ile çapraz sağlama (§6.2) |
| ISS radyo modu değişir ya da kapalıdır (ARISS: Zvezda telsizi onarımda) | Orta / Orta | Her gece ARISS durumuna bak. E4'te Meteor-M2-4 yedek; ISS sesi yoksa birleşik deney o gece yalnız optik |
| Meteor-M2-4 yayını keser (kaynaklar "aktifken" diyor) | Orta / Orta | Meteor-M2-3, Orbcomm, amatör küp uydular. SatNOGS'ta canlı gözlemlere bak |
| FM ve TV vericilerinin girişimi (Çamlıca) | Orta / Orta | FM bant durdurucu filtre, anten yeri, kazanç ayarı |
| Telefonda manuel uzun pozlama yok | Düşük / Orta | Ekipte en az bir uygun telefon; gerekirse üçüncü taraf uygulama |
| Uçak izleri (İstanbul hava trafiği) | Orta / Düşük | Yanıp sönme deseni ve öngörülen yol |
| ISS'in yörünge düzeltme manevrası öngörüyü bozar | Düşük / Orta | Taze TLE; manevra haberleri; öngör–doğrula testinde not edilir |
| **Güvenlik:** gece dışarıda, çatı | Orta / Yüksek | Çatı kenarına çıkılmaz; bahçe, balkon ya da teras; akşam gözlemleri bir yetişkinle; veli bilgisi |
| "Amatörler bunu zaten yapıyor" itirazı | Orta / Yüksek | §13'teki fark tablosu: telefon + ucuz SDR, aynı geçişte birleşik çözüm, iki ters problem, diferansiyel, ön kayıtlı öngörü |

---

## 13. Özgünlük ve önceki çalışmalar

**Öncüller (literatür bölümüne girer):**
- **Tarih:**
  - Guier ve Weiffenbach (Sputnik Doppler'i), McClure ve TRANSIT (APL Technical Digest).
  - Gauss (Ceres).
  - Schmid'in dünya uydu üçgenlemesi (PAGEOS, BC-4 kameraları, NOAA PP-7).
- **Amatör uydu gözlemcileri (Seesat-L):**
  - Langbroek, Bassa ve Molczan (2023), "Tracking the Dark Side on a Shoestring Budget": dürbün ve kronometreden DSLR'ye, CCTV kameralarına; GPS ya da NTP zamanlaması; ~200 gizli nesnenin yörüngesi.
  - Astrometrik doğruluk 5–30″ (500 km'de ~15–75 m), zamanlama 1–10 ms.
  - Kışın bazı nesneler **radyo Doppler eğrisiyle** izleniyor.
  - Bassa'nın açık kaynak yazılımları: STVID (video) ve Doppler eğrisi araçları.
- **Profesyonel birleşik ilk yörünge belirleme:**
  - Açı + Doppler (radar), "IODAD", Montaruli ve ark., SDC9.
  - Açı + menzil + menzil değişimi, "Stare and Chase", SDC7.
  - Diferansiyel cebirle kısa yay, Losacco ve ark.
- **Optik ve radyo navigasyon:**
  - Alçak yörünge uydularını yıldızların önünde gözleyerek konum bulma patentleri.
  - Globalstar uydularıyla yer deneylerinde ~250 m RMS konum (Sensors 2025 derlemesinden arama özeti; makale açılamadı, yöntem ayrıntısı doğrulanmadı).
  - Orbcomm Doppler konumlama: 1.687 m → 782 m (NSF yayını).
- **Teleskoplu akademik örnek:** Cal Poly tezi (8 inç teleskop + DSLR).

**Bizim katkımız (raporun ilk sayfalarında net yazılmalı):**
1. **Yalnızca telefon + ~100 € SDR:** Teleskop, GPS zaman ekleyici ya da özel kamera yok. Hata bütçesi **ölçülerek** çıkarılır: astrometri, zaman, frekans, TLE.
2. **Aynı geçişte açı + Doppler'in iki yönde birlikte kullanımı:** Hem yörünge (Gauss/Sputnik) hem konum (TRANSIT). Birinin diğerinin zayıf yanını kapattığının nicel gösterimi: tek geçişte öngörüde ~2–25 kat kazanç (frekans gürültüsüne bağlı), iki geçişte yanlış çözümün ortadan kalkması.
3. **Radyonun kamera saatini kalibre etmesi** ve **ucuz diferansiyel uydu konumu** (iki öğrenci istasyonu).
4. **Ön kayıtlı "öngör–doğrula" testi:** Kendi ölçtüğümüz yörüngeyle bir sonraki ISS geçişini öngörüp gözlemek.
5. İstanbul'dan açık veri ve kod.

**Bu kombinasyonu bulamadım,** ama aramam sınırlı (standart web araması). Google Scholar ve ULAKBİM taraması §16'da. **Bassa'nın araçları hem optik hem Doppler takibi yapıyor;** ikisinin aynı geçişte tek çözümde birleştirilip birleştirilmediğini göremedim. Rapor bu farkı abartmadan yazmalı.

**Kopya riski:** Rehber, başka projenin kopyasını "önemli ihlal" sayar. Literatür taraması ve fark tablosu zorunlu.

---

## 14. Kurallar ve uyum

- **Ekip:** En fazla **3 öğrenci** + 1 danışman. Dördüncü öğrenci resmî ekipte yer alamaz. Nasıl katkı vereceği (ör. gözlem gönüllüsü, raporda teşekkür) **danışmanla ve yarışma kurallarıyla netleştirilmeli.**
- **Sözlü sunum:** Proje öğrencilerce yapılmalı. Kaynaklar, destek ve **araçlar (yapay zekâ kodlama asistanları dahil) raporda belirtilmeli.** Jüri sözlü sorar; öğrenciler Gauss yöntemini, Doppler'i ve kodu anlatabilmeli.
- **Başvuru:** TYBS, **4 Ocak 2027, 17:30.** Proje adı ≤15 kelime; özet 150–250 kelime; rapor tek PDF, 2–20 sayfa; ek belgeler ≤10 MB.
- **Yalnızca alıcı:** Hiçbir verici kullanılmaz. Ticari ya da kişisel içerik çözülüp yayımlanmaz; yalnızca **taşıyıcı frekansı** ölçülür. ISS APRS paketlerindeki çağrı işaretleri raporda yer almaz. Türkiye'de alıcı kullanımının yasal çerçevesi danışmanla teyit edilmeli (**doğrulamadım**).
- **Güvenlik:**
  - Gece gözlemleri bir yetişkinle.
  - Çatı kenarı yok.
  - Kablolar takılma riski yaratmayacak biçimde.
  - Şebeke gerilimiyle iş yok (SDR USB'den beslenir).
- **Kişisel veri:** Ev konumları raporda yuvarlatılır (ör. ~1 km) ya da yalnızca hata olarak verilir. Tam koordinatlar paylaşılmaz.
- **Sağlık iddiası yok** (konu gereği).
- **İntihal:** Atıflar tam; açık kaynak parçalar lisansıyla belirtilir.

## 15. Rapor iskeleti (≤20 sayfa)

1. Özet
2. Giriş: Sputnik → TRANSIT → GNSS kırılganlığı
3. Literatür ve özgünlük (fark tablosu)
4. Kuram: Doppler, iki cisim, Gauss, astrometri, paralaks, EKK ve gözlenebilirlik
5. Benzetim (§6) ve ön kayıt
6. Yöntem: donanım, kalibrasyon, E0–E7
7. Bulgular
8. Tartışma: hata bütçesi, sınırlar, olumsuz sonuçlar, benzetim ile gerçek karşılaştırması
9. Sonuç ve uygulanabilirlik (GNSS'siz yedek, uydu takibi)
10. Kaynakça

Ekler: kod, ham veri örnekleri, ön kayıt, gözlem günlüğü.

## 16. Yapılacaklar

**Sınav haftaları (2–15 Kas): ekibin yapacağı iş yok.**

- [x] "Yapay uydu" kalibrasyon sayfası (`yapay_uydu.html`) ve geçiş tahmini (`gecis_tahmini.py`).
- [ ] *(Hazırlık, bu depoda)* Optik ve radyo boru hattı iskeleti; ön kayıt taslağı.
- [ ] *(Opsiyonel, ekip kararı)* RTL-SDR V4/V4L seti ve FM filtresi siparişi (Türkiye fiyatı ve teslim süresi doğrulanmalı).
- [ ] Ekipteki telefonlar: manuel modda 2–4 s pozlama ve ISO ayarı var mı? EXIF'te milisaniye (SubSec) alanı yazılıyor mu?
- [ ] **Pilot-0 (16–18 Kas)** → **Kapı 0 (19 Kas)**.
- [ ] Gözlem noktaları: okul bahçesi ya da terası (A istasyonu, koordinatı haritadan) ve 1–2 ev (B). Ufuk, özellikle geçişlerin tepe noktası yönünde açık mı?
- [ ] ARISS durum sayfası ve SatNOGS Meteor-M2-4 sayfasını gözlem haftalarında takip et.
- [ ] Literatür: Google Scholar ve ULAKBİM'de "angles-only orbit determination smartphone", "angles and Doppler initial orbit determination", "satellite Doppler positioning RTL-SDR", "uydu Doppler konum belirleme".
- [ ] Danışmanla: hipotezler, güvenlik (gece gözlemi), alıcı kullanımının yasal çerçevesi, 4. öğrencinin durumu.
- [ ] TYBS için 3 resmî öğrenci (Aralık başı).

## 17. Kaynaklar

- Sputnik ve TRANSIT: [APL Technical Digest – Guier](https://secwww.jhuapl.edu/techdigest/Content/techdigest/pdf/V02-N01/02-01-Guier.pdf)
- Dünya uydu üçgenlemesi: [Schmid, NOAA PP-7](https://geodesy.noaa.gov/library/pdfs/NOAA_PP_0007.pdf), [NOAA BC-4 kamera ve zamanlama](https://celebrating200years.noaa.gov/foundations/satellite_geodesy/BC4_400.html)
- GNSS girişimi: [EASA SIB 2022-02R3 özeti (FIR İstanbul ve Ankara)](https://rntfnd.org/2024/07/10/europe-renews-its-info-about-gnss-interference-easa/), [Temmuz 2026 revizyonu haberi](https://runwaygirlnetwork.com/2026/07/easa-updates-aircraft-gnss-jamming-and-spoofing-guidance/)
- Amatör uydu gözlemi: [Langbroek, Bassa ve Molczan 2023 – Tracking the Dark Side on a Shoestring Budget](https://conference.sdo.esoc.esa.int/proceedings/neosst2/paper/59/NEOSST2-paper59.pdf), [Bassa, OSCW 2019 sunumu](https://events.libre.space/event/3/contributions/63/attachments/56/80/bassa_oscw2019.pdf), [DSLR ile zamanlama sorunu (LSF forumu)](https://community.libre.space/t/satellite-optical-observations-with-dslr-and-timer/12638)
- Birleşik ilk yörünge belirleme: [IODAD – SDC9](https://conference.sdo.esoc.esa.int/proceedings/sdc9/paper/55/SDC9-paper55.pdf), [Stare and Chase – SDC7](https://conference.sdo.esoc.esa.int/proceedings/sdc7/paper/336/SDC7-paper336.pdf), [Losacco ve ark. (arXiv 2204.13966)](https://ar5iv.labs.arxiv.org/html/2204.13966)
- Uydularla optik konum: [Sensors 2025 derlemesi](https://www.mdpi.com/1424-8220/25/19/6149/htm), [ABD patenti 9217643](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9217643)
- Doppler konumlama: [NSF yayını (Orbcomm)](https://par.nsf.gov/servlets/purl/10413009)
- Teleskoplu akademik örnek: [Cal Poly tezi](https://digitalcommons.calpoly.edu/theses/2951)
- Uydu durumu:
  - [NOAA POES'un kapatılması](https://www.nesdis.noaa.gov/news/legacy-orbit-noaa-decommissions-the-poes-satellite-constellation), [OSPO durum sayfası](https://www.ospo.noaa.gov/Operations/POES/status.html)
  - [SatNOGS Meteor-M2-4](https://db.satnogs.org/satellite/59051), [SatNOGS Meteor-M2-3](https://db.satnogs.org/satellite/57166/), [137 MHz'de 2026'da ne çalışıyor (sdrstore)](https://www.sdrstore.eu/rtl-sdr-weather-satellite-reception-2026-what-still-works/)
  - [ARISS ISS istasyon durumu](https://www.ariss.org/current-status-of-iss-stations.html), [AMSAT ISS frekansları](https://www.amsat.org/?p=63833)
  - [rtl-sdr.com Orbcomm](https://www.rtl-sdr.com/tag/orbcomm/)
- Donanım: [RTL-SDR V4L duyurusu](https://rtl-sdr.com/rtl-sdr-blog-v4l-lite-now-available-for-purchase), [V4 üretiminin sonu (Passion Radio)](https://passion-radio.com/rtl-sdr-stick/r828d-v4-2402.html), [WiMo V4 seti fiyatı](https://www.wimo.com/en/rtl-sdr-v4-kit)
- Yazılım: [astrometry.net belgeleri](https://astrometrynet.readthedocs.io/en/latest/readme.html), [CelesTrak GP/TLE](https://celestrak.org/NORAD/elements/gp.php?CATNR=25544&FORMAT=TLE), [Skyfield](https://rhodesmill.org/skyfield/)
- Kitap: H. D. Curtis, *Orbital Mechanics for Engineering Students* (Alg. 3.3–3.4 evrensel değişken, Alg. 5.5 Gauss yöntemi)
- TÜBİTAK 2204-A: [yarışma sayfası](https://tubitak.gov.tr/tr/yarismalar/2204-lise-ogrencileri-arastirma-projeleri-yarismasi)
