# Derin İnceleme — Finalist Fikirler (fizik hocasıyla, bilimsel + etkileyici, laboratuvar aleti yok, Kağıthane)

> **GÜNCELLEME:** 17 adaylı tam liste ve karşılaştırma için bkz. `projeler/00_DIZIN.md`. Bu dosyadaki H → P01, G → P04, B → P12, D → P13.

> **Tarih:** 1 Kasım 2026 · Önceki menü: `FIKIR_HAVUZU.md`. Bu dosya, ekibin son yanıtlarına göre adayları süzer ve en güçlülerini derinleştirir.
> **İşaretler:** *doğrulandı* = kaynağı okudum; *haber/özet* = ikincil; *bulamadım* = aramamda çıkmadı ("yok" demek değil); *benzetim* = kendi sentetik hesabım, ölçüm değil.

## 0. Yeni kısıtlar ve adaylara etkisi

| Kısıt (ekipten) | Etki |
|---|---|
| Danışman fizik hocası → proje **Fizik** alanında | Fizik derinliği ilk ölçüt oldu |
| 3D yazıcı, CNC, osiloskop, sinyal üreteci **muhtemelen yok** | Mekanik tarayıcı/jig isteyenler zorlaşır; ölçümü SDR, kamera veya Arduino'ya yaptıran fikirler öne çıkar |
| Konum **Kağıthane** (Avrupa yakası, vadi) | Anten/gökyüzü görüşü balkon/çatıya bağlı; Çamlıca'ya görüş hattı belirsiz |
| **Bilimsel + etkileyici**; savunma bağı yalnızca anlatı | Net bir araştırma sorusu + canlı gösteri olan fikirler öne çıkar |

| Önceki aday | Karar | Neden |
|---|---|---|
| F – EMC tarayıcı | İkinci plana | XY mekaniği için 3D yazıcı/CNC yok; elle ızgara yavaş, gösteri zayıflar |
| C – Pasif radar | Elendi | En riskli; Kağıthane vadisinden Çamlıca'ya görüş hattı belirsiz |
| A – GNSS'siz zaman | **H'nin içine katıldı** | Osilatör kayması H'de baskın hata kaynağı çıktı (§1.6); A tek başına soyut, H içinde ölçülebilir bir deney oluyor |
| B – ENF, G – Lazer benek, D – Polarizasyon pusulası | Kaldı | Laboratuvar aleti gerektirmiyor, fiziği güçlü |
| **H – Uydu Doppler'iyle konum** | **Yeni, birinci sıra** | Aşağıda |

---

## 1. H — "Sputnik'ten TRANSIT'e": Kağıthane'den uydu Doppler'iyle GNSS'siz konum

### 1.1 Fikir ve hikâye
Ekim 1957'de Johns Hopkins APL'den fizikçiler **Guier ve Weiffenbach**, Sputnik'in radyo sinyalindeki Doppler kaymasından, **tek istasyonda tek geçişin Doppler eğrisiyle uydunun yörüngesini** çıkardı. Mart 1958'de **McClure** bunun tersini önerdi: yörünge biliniyorsa Doppler eğrisinden **alıcının konumu** bulunur. Bu fikir ilk uydu navigasyon sistemi **TRANSIT**'i doğurdu (Transit 1B, Nisan 1960) *(APL Technical Digest, doğrulandı)*.
**Proje:** Bu iki deneyi bugün, Kağıthane'den bir ucuz SDR ve tel antenle tekrar etmek; hata bütçesini (frekans ölçümü, osilatör kayması, yörünge/TLE hatası) ölçmek ve hangi ucuz iyileştirmenin konumu ne kadar düzelttiğini göstermek.

### 1.2 Neden "gerekli hissedilmeyen ama avantajlı" ve etkileyici
- GNSS parazitlenince ya da aldatılınca konum biter; uydu Doppler'i **bağımsız ikinci bir konum kaynağıdır** (savunma anlatısı: TRANSIT bir donanma sistemiydi).
- **Canlı gösteri:** Uydu geçerken hoparlörde yükselip alçalan "ıslık" (Doppler), ekranda konum elipsinin her saniye daralması, sonunda Kağıthane'nin haritada belirmesi.

### 1.3 Fizik (lise fiziğiyle bağ)
- **Doppler olayı** (elektromanyetik dalgalar): Δf = −(f₀/c)·dρ/dt.
- **Kütle çekimi ve düzgün çembersel hareket / Kepler**: v = √(GM/r), yörünge periyodu, Dünya'nın dönmesi.
- **Osilatör ve rezonans**: kristalin sıcaklıkla frekans kayması, ppm, Allan sapması.
- **Ölçüm kuramı**: en küçük kareler, geometri (DOP), hata yayılımı.

### 1.4 Araştırma soruları ve hipotezler
| Kod | Hipotez | Deney |
|---|---|---|
| H1 | Kağıthane'den RTL-SDR + V-dipol ile alçak yörünge uydusunun Doppler eğrisi, konum için yeterli frekans doğruluğuyla ölçülebilir (eşik pilot sonrası yazılacak) | E1 |
| H2 | **Sputnik yönü:** Bilinen konumdan ölçülen Doppler eğrisi, TLE'den hesaplanan yörüngenin zamanlama (yörünge boyu) hatasını düzeltir | E2 |
| H3 | **TRANSIT yönü:** Bilinmeyen konum tek geçişte km, çok geçişte yüzlerce m mertebesinde bulunur; baskın hata kaynakları osilatör kayması ve TLE'dir (benzetim tahmini) | E3 |
| H4 | Osilatör kayması bağımsız biçimde düzeltilirse (sıcaklık kararlılığı / yer vericisiyle kalibrasyon) tek geçişteki büyük hatalar belirgin azalır | E4 |
| H5 | Uydu/sinyal türü (dar bantlı taşıyıcı, APT, CW işaretçi) konum doğruluğunu değiştirir | E5 |

### 1.5 Deneyler (laboratuvar aleti gerekmez)
- **E1 – Alıcı ve ilk geçiş:** V-dipol (iki tel, 137 MHz için kol başı ~53 cm), balkon/çatı. Geçiş tahmini (SGP4 + CelesTrak TLE). Kayıt → spektrogram → taşıyıcı frekansı (FFT tepe + ara değerleme).
- **E2 – Yörünge düzeltme (Sputnik):** Konum telefon GNSS'iyle biliniyor; ölçülen eğriye TLE modelini otur, zamanlama hatası ve alıcı ofseti kestirilir.
- **E3 – Konum (TRANSIT):** Konum bilinmiyormuş gibi kestirilir; telefon GNSS'i doğruluk referansı. Tek geçiş vs 3+ geçiş.
- **E4 – Osilatör:** RTL-SDR'nin ofsetini bir yer sinyaliyle (ör. bilinen frekanslı yayın/baz istasyonu; A fikrinin yöntemi) veya sıcaklık kararlı tutarak ölç; kaymayı bilinen kabul edince konum hatası değişimi.
- **E5 – Sinyal türleri:** Ulaşılabilen uydular arasında karşılaştırma (aşağıdaki "uydu durumu" riskine bakın).

### 1.6 Benzetim sonucu (`doppler_konum_sim.py`; BENZETİM, ölçüm değil)
Model: küresel Dünya, dairesel yörünge 750 km/45° (Orbcomm benzeri, örnek), 137,5 MHz, yükselim maskesi 15° (kentsel ufuk), alıcı ofseti ~1 ppm, rastgele 150 geçiş geometrisi. Medyan / P90 yatay hata (m):

| Frekans gürültüsü | TLE yörünge boyu hatası (1σ) | 1 geçiş, kayma bilinmiyor | 1 geçiş, **kayma biliniyor** | 3 geçiş, kayma bilinmiyor |
|---|---|---|---|---|
| 1 Hz | 0 | 190 / 3.397 | **107 / 455** | 70 / 230 |
| 1 Hz | 1 km | 723 / 2.153 | 579 / 1.517 | 682 / 1.376 |
| 10 Hz | 0 | 1.792 / 20.666 | 1.036 / 4.740 | 727 / 1.833 |
| 10 Hz | 1 km | 2.299 / 18.247 | 1.390 / 5.225 | 1.168 / 2.457 |
| 50 Hz | 0 | 9.370 / 59.720 | 5.303 / 22.946 | 4.142 / 10.919 |

**Okuma:**
1. Frekans ölçümü ~1–10 Hz'de tutulabilirse konum **yüzlerce m – birkaç km** mertebesinde. Bu, yayımlanmış Orbcomm sonuçlarıyla aynı mertebe (SGP4 ile 1.687 m, iyileştirilmiş efemerisle 782 m; *haber/özet*).
2. **Osilatör kayması tek geçişte konumla karışıyor:** kayma bilinince tek geçişin P90'ı 3,4 km'den 0,46 km'ye iniyor (1 Hz, TLE hatasız). → H4 ve E4'ün gerekçesi; A fikri burada ölçülebilir bir deney oluyor.
3. TLE hatası (~1 km) eklendiğinde gürültü düşükken bile hata ~0,6–0,7 km'de kalıyor → H2 (yörünge düzeltme) gerçek bir katkı.
4. **Sınırlar:** İyonosfer, basık Dünya, verici frekans kayması, çok yollu yayılma ve "ayna" belirsizliği modellenmedi; ilk tahmin doğru tarafta başlatıldı. Gerçek doğrulama E1–E3'tür.

### 1.7 Donanım ve maliyet (tahmin, Türkiye fiyatı doğrulanmadı)
- **Yeni:** RTL-SDR V4 + dipol anten seti (~40–70 USD), **FM bant durdurucu filtre** (~20 USD; İstanbul'daki güçlü FM yayınları 137 MHz alıcısını doyurabilir), koaksiyel uzatma. İsteğe bağlı: LNA.
- **Mevcut:** Laptop; Arduino/ESP32 (sıcaklık kaydı, E4).
- **Yazılım:** Python (numpy/scipy), SGP4/Skyfield, kendi Doppler kestirici ve konum çözücümüz; açık kaynak SDR araçları (kayıt).
- Toplam yeni harcama 25.000 TL tavanının çok altında kalmalı.

### 1.8 Yapay zekâ gerekli mi?
**Hayır.** Doppler kestirimi (FFT/ara değerleme) ve konum (doğrusal olmayan en küçük kareler) klasik. ML yalnızca zayıf sinyalde taşıyıcı izleme fizik yöntemiyle başarısız olursa karşılaştırılır (§3 ilkesi, `FIKIR_HAVUZU.md`).

### 1.9 Öncül ve kama
- **Öncül (bulduklarım):** RTL-SDR ve VHF dipolle Orbcomm Doppler konumlama içeren bir ABD patent başvurusu; Orbcomm ile 2B hata 1.687 m (SGP4) → 782 m (iyileştirilmiş efemeris) bildiren bir NSF yayını; çok takımyıldızlı alıcıyla ~132 m (Sensors 2020); iki uydulu Doppler doğruluk analizi (arXiv 2026); Barselona URSI 2025; Orbcomm'u RTL-SDR ile almak/çözmek amatör çevrede yaygın.
- **Kama (bu kombinasyonu bulamadım, sınırlı arama):** (1) **Sputnik + TRANSIT iki yönünü** tek ucuz kurulumda yapıp, (2) **hata bütçesini deneyle ayrıştırmak** (osilatör, TLE, frekans gürültüsü; benzetimle karşılaştırmalı), (3) farklı ucuz uydu sinyallerini konum kalitesi için kıyaslamak, (4) İstanbul'dan açık veri ve kod.

### 1.10 Riskler
| Risk | Etki | Azaltma |
|---|---|---|
| **Uyduların 2026 durumu doğrulanmadı** *(1 Kas güncellemesi: NOAA-15/18/19 2025'te kapatıldı, bkz. `uydu-isik-radyo/PLAN.md` §5.2)*: NOAA-19 için kaynaklar çelişkili (WMO "ömür sonu Eylül 2025 bekleniyor", başka bir ikincil kaynak "Haziran 2026'da çalışıyor"); Meteor-M2-3 bir 2025 raporunda "zayıf"; Orbcomm OG2'nin güncel durumu bulunamadı | Yüksek | **Pilotun ilk işi:** SatNOGS gözlemleri ve kendi alıcımızla hangi uyduların gerçekten duyulduğunu görmek. Amatör küp uyduların CW işaretçileri (435 MHz) yedek |
| FM yayın girişimi (İstanbul) | Orta | FM bant durdurucu filtre |
| Kağıthane vadisinde alçak ufuk | Orta | Çatı/okul bahçesi; maske 15–20° ile planla (benzetim 15°) |
| Frekans kestirimi (modülasyonlu sinyalde taşıyıcı) | Orta | Dar bantlı/CW işaretçili uydular; uzun FFT; ara değerleme |
| "Ayna" belirsizliği | Düşük | İkinci geçiş veya kaba ön bilgi ("İstanbul'dayız") |

### 1.11 İlk iki gün (sınavdan sonra)
1. RTL-SDR + dipolle bir öğle ve bir akşam geçişini kaydet (geçiş saatleri SGP4/çevrimiçi tahminle).
2. Spektrogramda Doppler eğrisini çiz; tepe frekansın gürültüsünü (Hz) ölç. **1–10 Hz civarındaysa H uygulanabilir** (§1.6 tablosu).

---

## 2. G — Lazer benek (speckle) ile "kâğıdın parmak izi"

**Fikir.** Kâğıt/plastik yüzeyin mikroskobik pürüzü, lazer ışığında kopyalanamayan bir **benek deseni** üretir. Ucuz bir okuyucuyla bu deseni kimlik olarak kullanıp aynı kâğıdı tanımak, kopyayı ayırt etmek.
**Öncül:** Buchanan ve ark., *Nature* 436, 475 (2005), Imperial College: odaklanmış lazerle kâğıt yüzeyi taranıp dört açıdan fotodedektörle kayıt alınmış; parmak izi 200–500 bayt; spin-off Ingenia *(haber/özet)*. Takip çalışmaları (IEEE S&P 2009, CCS 2011) kâğıt yüzeyi parmak izine odaklanmış *(haber/özet)*.
**Kama (bulamadım):** Telefon/webkamerası düzeyinde bir okuyucuyla **iç/dış Hamming mesafesi dağılımı, yaşlanma, açı ve sıcaklık sağlamlığını birlikte** ölçen, açık kodlu bir lise çalışması.
**Fizik.** Koherans, girişim, **benek istatistiği** (yoğunluk dağılımı üstel; kontrast = 1), benek boyutu.
- *Lenssiz (nesnel) benek:* s ≈ λz/D. 650 nm, z = 30 mm, ışık lekesi D = 1 mm → **s ≈ 20 µm** (webkamera pikseli ~3 µm → benek başına ~6 piksel: rahat çözülür).
- *Telefon lensiyle (öznel) benek:* s ≈ 2,44·λ·(1+M)·F# ≈ 3 µm (F/1,8): piksel boyutuna yakın, sınırda. **Öneri:** Lensi çıkarılmış ucuz webkamera.
**Deneyler:** E1 benek boyutu ve kontrast ölçümü vs kuram; E2 aynı kâğıt 30 kez (iç mesafe), 50 farklı kâğıt (dış mesafe); E3 fotokopi/fotoğraf baskısı kopya testi; E4 buruşturma, ıslatma, sıcaklık, zaman; E5 okuyucu açısı/konumu toleransı.
**Donanım (yeni ~20–80 USD):** Class 2 lazer modülü (650 nm, <1 mW), lensi sökülebilir webkamera, ahşap veya alüminyum profil üzerine vidalı sabit düzenek (**3D yazıcı gerekmez**). Mevcut: laptop.
**Yapay zekâ gerekli mi?** Hayır; klasik öznitelik + korelasyon/hash. CNN ile karşılaştırma isteğe bağlı (Evren görüntü eğitimi).
**Etkileyici gösteri:** "Aynı paketten iki A4'ü ayırt eden ve fotokopisini reddeden" canlı okuyucu.
**Risk:** Okuma tekrarlanabilirliği (bir tezde başka bir etiket türü için 0,2° açı toleransı bildirilmiş) → sağlam düzenek ve hizalama yazılımı şart. **Lazer güvenliği:** yalnızca Class 2, göze doğrultma yok; danışmanla güvenlik kuralı yazılır.
**Savunma anlatısı:** Sahte belge/etiket/parça doğrulama.

---

## 3. B — Şebeke frekansı (ENF): "Ampulün titremesi kaydın saatini söyler"

**Fikir ve fizik:** Önceki karttaki gibi (`FIKIR_HAVUZU.md` §5-B). Ek bulgular:
- **Türkiye Kıta Avrupası şebekesiyle eşzamanlı:** 2010'da deneme bağlantısı yapılmış *(haber/özet)*; KIT'in açık şebeke frekansı veri tabanında Kıta Avrupası alanındaki ölçüm noktaları arasında Portekiz, Almanya ve **Türkiye** var (1 s çözünürlük, OSF'de) *(doğrulandı: arXiv özeti)*. Güncel eşzamanlılık durumunu resmî kaynaktan doğrulayamadım. Doğruysa anlatı güçlü: **"Kağıthane'deki ampul Lizbon'dakiyle aynı ritimde titrer."**
- **Ana risk: LED ışıklar.** Kaynaklara göre ışık türleri voltaj dalgalanmasına farklı tepki veriyor; 25/30 fps video titreşimi örnekleyemiyor (aliasing); rolling shutter yöntemi yardımcı oluyor ama telefon videosu zor *(haber/özet)*. **LED titreşimini doğrudan test eden bir çalışma bulamadım.**
**Deneyler (fizik ağırlıklı):** E1 evdeki 5–10 ampulün 100 Hz titreşim oranını **fotodiyot + Arduino** ile ölç (kendi başına bir fizik deneyi); E2 temassız referans: **endüktif bobin** (telefon toplama bobini) ile prize dokunmadan şebeke izini kaydet (Faraday indüksiyonu; şebekeye bağlantı yok); E3 video/ses ENF çıkarımı; E4 WhatsApp/Telegram ses mesajında ENF'nin sağ kalıp kalmadığı; E5 KIT verisiyle Avrupa ile eşzamanlılık karşılaştırması (yıllar farklıysa yöntem doğrulaması olarak).
**Yapay zekâ gerekli mi?** Hayır.
**Etkileyici gösteri:** Jüri önünde çekilen videonun dakikasını ampul titremesinden bulmak.
**Karar ölçütü:** E1'de evdeki LED'lerin çoğu ölçülebilir 100 Hz titreşim veriyorsa B güçlü; vermiyorsa B "ses + endüktif referans" ile daralır veya elenir.

---

## 4. D — "Dijital güneş taşı": güneş bulutun arkasındayken yön bulmak

**Fikir ve fizik:** Önceki karttaki gibi (`FIKIR_HAVUZU.md` §5-D) + **Viking güneş taşı** (kalsit/kordiyerit kristali) anlatısı.
**Öncül (bulduklarım):** Horváth grubu (ELTE): açık gökte kalsit, kordiyerit veya turmalinle net yön hatası ≤ 3°; kapalı gökte kristale göre ~6° (kalsit), ~10° (kordiyerit), ~17° (turmalin) (2016 psikofizik deney, 61° enlem); 1.080 gökyüzü durumu modeli (2017); yolculuk benzetimleri. Aix-Marseille'de ~30 € renk kamerasıyla yön sensörü *(haber/özet)*.
**Kama:** "Telefon + polarizör vs Viking kristali vs insan gözü" karşılaştırmasını **İstanbul'un kış bulutluluğunda** yapmak; fizik modeli (Rayleigh) ile ML karşılaştırması (yapay zekâ gerekli mi?).
**Donanım (yeni ~10–50 USD):** Polarizör film, kalsit (İzlanda spatı) kristali, telefon; isteğe bağlı servo. Hiç alet gerektirmez. **Polarize güneş gözlüğüyle sıfır maliyetli pilot.**
**Risk:** Kasım–Aralık İstanbul'da bulutlu gün çok; veri toplama günleri az olabilir. Bulutluluk araştırma değişkenine çevrilir ama kapalı/yağmurlu günlerde ölçüm olmaz.
**Etkileyici gösteri:** Güneş görünmezken yön bulmak; Viking hikâyesi.

---

## 5. Karşılaştırma (yeni ölçütlerle)

| | H Uydu Doppler'i | G Lazer benek | B ENF | D Güneş taşı |
|---|---|---|---|---|
| Fizik derinliği | **Yüksek** (Doppler, kütle çekimi, osilatör) | **Yüksek** (girişim, benek istatistiği) | Orta | Yüksek (saçılma, polarizasyon) |
| Etkileyicilik | **Çok yüksek** (canlı uydu, harita, Sputnik hikâyesi) | Yüksek | Yüksek | Yüksek (Viking hikâyesi) |
| Bilimsel sorunun netliği | **Yüksek** (hata bütçesi, H1–H5) | Yüksek | Orta (LED'e bağlı) | Orta |
| Alet ihtiyacı | SDR + tel anten | Lazer + webkamera + ahşap düzenek | Fotodiyot, bobin | Polarizör |
| Kağıthane uygunluğu | Balkon/çatı gerekir | Ev içi | Ev içi | Açık gök gerekir |
| Yeni maliyet (tahmin) | ~60–100 USD | ~20–80 USD | ~0–50 USD | ~10–50 USD |
| En büyük risk | Uydu durumu, frekans kestirimi | Okuma tekrarlanabilirliği | LED titreşimi zayıf olabilir | Bulut |
| Öncül yoğunluğu / kama | Akademik var / kombinasyon + hata bütçesi | Nature 2005 var / ucuz okuyucu + açık istatistik | Yüksek / Türkiye + mesajlaşma | Yüksek / İstanbul bulutu + karşılaştırma |
| Yapay zekâ | Gerekmez | Gerekmez (karşılaştırma isteğe bağlı) | Gerekmez | Gerekmez (karşılaştırma isteğe bağlı) |

**Önerim:** **H birinci** (fizik + etkileyicilik + net soru + benzetim kanıtı birlikte). **G ikinci**: H'nin pilotu başarısız olursa en düşük riskli fizik deneyi. B ve D, kendi bir günlük pilotları olumlu çıkarsa yükselir.

## 6. Sınavdan sonra karar için bir günlük mini pilotlar

| Fikir | Pilot | Gereken | Karar ölçütü |
|---|---|---|---|
| H | 2 geçiş kaydı, Doppler eğrisi | RTL-SDR + dipol (**satın alınması gereken tek şey**, sınav haftasında sipariş edilirse 16 Kas'ta hazır olur) | Taşıyıcı frekansı ~1–10 Hz gürültüyle izlenebiliyor mu? |
| G | 20 okuma aynı kâğıt + 20 farklı kâğıt | Lazer işaretçi (Class 2), telefon/webkamera | İç ve dış mesafe dağılımları ayrışıyor mu? |
| B | 5 ampulde titreşim ölçümü | Fotodiyot/LDR + Arduino veya telefonun ağır çekim videosu | 100 Hz titreşim ölçülebilir mi? |
| D | Polarize güneş gözlüğüyle gökyüzü fotoğrafları | Telefon + polarize gözlük | Açıyla parlaklık değişimi (cos²) görünüyor mu? |

## 7. Sorular

1. Ekipte **RTL-SDR** veya benzeri bir SDR var mı? Yoksa sınav haftasında bir RTL-SDR V4 + dipol seti sipariş edilebilir mi? (H'nin pilotu için tek ön koşul.)
2. **Açık gökyüzü gören bir balkon/çatı** (tercihen güneye bakan) var mı, ya da okul bahçesi kullanılabilir mi?
3. Evde **lazer işaretçi** ve **polarize güneş gözlüğü** var mı? (G ve D pilotları sıfır maliyet olur.)

## 8. Kaynaklar

- Sputnik/TRANSIT tarihi: [APL Technical Digest – Guier](https://secwww.jhuapl.edu/techdigest/Content/techdigest/pdf/V02-N01/02-01-Guier.pdf), [APL Technical Digest – Black](https://secwww.jhuapl.edu/techdigest/Content/techdigest/pdf/V02-N01/02-01-Black.pdf), [Transit (Wikipedia)](https://en.wikipedia.org/wiki/Transit_(satellite_navigation_system))
- Orbcomm Doppler konumlama: [ABD patent başvurusu (RTL-SDR + dipol)](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11960018), [NSF yayını](https://par.nsf.gov/servlets/purl/10413009), [Sensors 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7589965), [arXiv 2026 iki uydulu Doppler](https://arxiv.org/pdf/2607.10241), [URSI 2025](https://spcomnav.uab.es/docs/conferences/Fernandez_URSI_2025.pdf), [Electronics – Doppler chirp](https://www.mdpi.com/2079-9292/13/24/4882/html)
- Orbcomm alımı: [rtl-sdr.com Orbcomm](https://www.rtl-sdr.com/tag/orbcomm/), [SatNOGS Orbcomm FM 36](https://db.satnogs.org/satellite/25984)
- Uydu durumu: [WMO OSCAR NOAA-19](https://space.oscar.wmo.int/satellites/view/noaa_19), [Orbital Radar NOAA-19](https://orbitalradar.com/blog/noaa-19-poes-weather-satellite), [Dartcom durum metni](https://ftp.dartcom.co.uk/pub/preddata/winsupp.txt)
- Lazer benek: [Royal Holloway – Nature 2005 kaydı](https://pure.royalholloway.ac.uk/en/publications/forgery-fingerprinting-documents-and-packaging/), [ScienceDaily 2005](https://www.sciencedaily.com/releases/2005/07/050731233046.htm), [Kâğıt parmak izi arXiv 2017](https://eprints.whiterose.ac.uk/116192/1/1705.02510.pdf)
- ENF: [KIT şebeke frekansı veri tabanı](https://arxiv.org/abs/2006.01771), [Nature Communications analizi](https://arxiv.org/abs/2006.02481v1), [Türkiye–Avrupa senkron bağlantı 2010](https://www.renewableenergyworld.com/power-grid/turkish-power-system-connected-with-european-grid/), [Olaylardan ENF (CVPR 2023)](https://arxiv.org/pdf/2305.02597), [Işık türlerinin etkisi (USC)](https://research.usc.edu.au/esploro/outputs/conferencePaper/Analysis-of-the-Impact-of-Light/991087293902621)
- Güneş taşı: [Royal Society Open Science 2016](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4736922/), [ELTE Viking sentezi](https://arago.elte.hu/sites/default/files/VikingSynthesis_ProcA.pdf), [Smithsonian](https://www.smithsonianmag.com/smart-news/simulation-suggest-legendary-viking-sunstones-could-have-worked-180968710/)
- Jeomanyetizma (ileride yedek fikir için): [Kandilli IZN gözlemevi](https://jeomanyetizma.bogazici.edu.tr/sites/jeomanyetizma.boun.edu.tr/files/u145/jeoman_deprem_bilgi_eng.pdf)
