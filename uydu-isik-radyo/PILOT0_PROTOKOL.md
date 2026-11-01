# Pilot-0 Protokolü (Kapı 0): 16–18 Kasım, 3 gün

> **Amaç:** Ana plana (`PLAN.md`) zaman ve para harcamadan önce iki soruyu yanıtlamak:
> 1. **Optik:** Kağıthane'den telefonla çekilen bir ISS fotoğrafında yeterli yıldız çıkıyor mu, plaka çözümü yapılabiliyor mu, iz uçları seçilebiliyor mu? Telefonun saati NTP'ye göre kaç ms kayık?
> 2. **Radyo:** RTL-SDR ile bir uydunun Doppler eğrisi spektrogramda görülüyor mu, frekans gürültüsü ne kadar?
>
> SDR henüz gelmediyse yalnızca optik kısım yapılır. Radyo kararı **22 Kasım**'a kadar bekleyebilir; Meteor-M2-4 ve ISS her gün geçiyor.
> Aşağıdaki saatler 1 Kasım TLE'siyle hesaplandı, **dakikalarca kayabilir.** 15 Kasım akşamı TLE'yi yenileyip `gecis_tahmini.py` ile tekrar hesaplayın.

## Kişiler ve güvenlik
- Optik: 2 öğrenci (iki telefon, aynı noktada ya da biri okulda biri evde). Radyo: 1 öğrenci.
- Akşam gözlemlerinde **bir yetişkin** bulunur. Çatı kenarına çıkılmaz; bahçe, balkon ya da teras yeterli.
- Soğuk havaya göre giyinin; telefonun pili soğukta hızlı biter, powerbank alın.

## Malzeme
- **Optik:**
  - Manuel ("Pro") modu olan telefon.
  - Tripod ya da telefonu sabit tutacak bir dayanak.
  - Bluetooth deklanşör (yoksa 2 s zamanlayıcı).
  - Dizüstü bilgisayar (kalibrasyon için, `yapay_uydu.html`).
- **Radyo:**
  - RTL-SDR seti (dipol anten), FM bant durdurucu filtre, koaksiyel uzatma.
  - Dizüstüne kurulu SDR yazılımı (ör. SDR++). IQ kaydı yapabilmeli.
  - 437 MHz için kol başı ≈17 cm dipol; 137 MHz için kol başı ≈53 cm V-dipol.
- **Kayıt defteri** (aşağıdaki tablo).

## Önce yap (15 Kasım Pazar)
1. TLE'leri indir (ISS 25544, Meteor-M2 4 59051; bkz. `gecis_tahmini.py` başı) ve 16–18 Kasım geçişlerini yeniden hesapla:
   ```
   python gecis_tahmini.py iss.tle --bas 2026-11-16 --gun 3
   python gecis_tahmini.py iss.tle --bas 2026-11-16 --gun 3 --radyo
   python gecis_tahmini.py meteor.tle --bas 2026-11-16 --gun 3 --radyo
   ```
2. ISS'in gökte nereden geçeceğini bir gökyüzü uygulamasıyla (ör. Stellarium) ya da Heavens-Above'da gör. Kadrajı izin **tepe noktasının çevresine** ve birkaç parlak yıldızı içine alacak biçimde planla.
3. [ARISS durum sayfasına](https://www.ariss.org/current-status-of-iss-stations.html) bak: ISS 437,800 / 437,825 MHz'de yayında mı?
4. Dizüstü saatini NTP ile eşle. **time.is**'te kalan farkı not et.
5. Telefonda manuel mod denemesi:
   - Pozlama 3 s, ISO 1600, odak sonsuz.
   - **Gece modu, HDR ve "yapay zekâ" iyileştirmeleri kapalı.** Bunlar birden çok kareyi birleştirip zamanlamayı bozar.
   - Mümkünse beyaz dengesi sabit. RAW (DNG) isteğe bağlı.

## Üç gün

| Gün | Saat (TSİ, yenile!) | Ne | Not |
|---|---|---|---|
| **16 Kas Pzt** | 14:34 ve 16:14 | *Radyo:* Meteor-M2-4 (137,9 MHz), tepe 33° ve 31° | SDR geldiyse; V-dipol, IQ kaydı |
| | ~17:30 | **Kamera saati kalibrasyonu** (her telefon) | Aşağıdaki "yapay uydu" adımı |
| | **18:16** | **ISS görünür, tepe 61°, ~4 dk** (en iyi pilot geçişi) | Fotoğraf dizisi; SDR varsa aynı anda 437,8 MHz kaydı |
| | 19:53 | ISS görünür, tepe 17°, ~0,5 dk | İsteğe bağlı |
| **17 Kas Sal** | 17:28 | *Radyo:* ISS, tepe 79° (gündüz, görünmez) | 437,8 MHz Doppler |
| | 19:05 | ISS görünür, tepe 21°, ~3 dk | Fotoğraf dizisi |
| **18 Kas Çar** | 15:30 | *Radyo:* Meteor-M2-4, tepe 79° | En iyi Meteor geçişi |
| | 16:40 | *Radyo:* ISS, tepe 44° | |
| | **18:17** | **ISS görünür, tepe 28°, ~4 dk** | Fotoğraf dizisi + radyo |

### Kamera saati kalibrasyonu ("yapay uydu", ~15 dk, her telefon)
1. Dizüstünde `yapay_uydu.html`'i tam ekran aç. Ekran parlaklığını düşür. Nokta her 5 s'de soldan sağa bir tur atar.
2. Telefonu ekrana bakacak biçimde sabitle. **Uydu çekimindeki ayarlarla** (3 s pozlama) 10 fotoğraf çek. Her fotoğrafta noktanın izi görünür.
   - İzin sol ucu = pozlamanın açıldığı an; sağ ucu = kapandığı an.
   - Hangi turda olunduğu büyük sayıdan ve EXIF saatinden anlaşılır.
3. Ayrıca kısa pozlamayla (1/100 s) 10 fotoğraf çek. Ekrandaki yazılı UTC saatini EXIF saatiyle karşılaştır.
4. **Ölçülecek:**
   - EXIF zamanı pozlamanın başlangıcını mı, sonunu mu, yoksa başka bir anı mı gösteriyor?
   - Ortalama ofset (ms) ve dağılım (ms).
   - EXIF'te milisaniye alanı (SubSecTimeOriginal) var mı?
   - Ekran 60 Hz'de tazelendiği için çözünürlük ~17 ms.

### Fotoğraf dizisi (her ISS geçişi)
1. Telefonu tripodda öngörülen yöne çevir. **Geçiş boyunca telefonu oynatma.**
2. Uydu kadraja girince 3 s pozlamayla art arda çek (aralıklı çekim varsa her 4–5 s'de bir; yoksa kumandayla elle). Hedef: ≥10 fotoğraf.
3. Geçişten hemen sonra aynı yöne 3–5 fotoğraf daha çek. Bunlar yalnız yıldızlı kareler; plaka çözümü yedeği olur.
4. Deftere yaz: telefon modeli, pozlama, ISO, yer (okul / ev, **tam koordinat değil**), bulut durumu, time.is farkı.

### Radyo kaydı (her radyo geçişi)
1. Geçişten 2 dk önce kayda başla. Merkez frekans:
   - Meteor için 137,9 MHz.
   - ISS için 437,8 MHz. Doppler ±10 kHz olduğundan örnekleme hızı en az ~250 kHz.
2. Kayıt başlangıç saatini (dizüstü saati) ve dosya adını yaz. Kazancı sinyal doymayacak biçimde ayarla.
3. Geçiş bitince 1 dk daha kaydet.

## Kayıt tablosu (her çekim veya kayıt için bir satır)
`tarih | saat (TSİ) | uydu | optik/radyo | cihaz | ayarlar (pozlama, ISO / frekans, kazanç) | dosya adları | yer (okul/ev) | bulut | time.is farkı | not`

## Çözümleme (19 Kasım, 2–3 saat)
1. **Plaka çözümü:**
   - Bir ISS fotoğrafını astrometry.net ile çöz (nova.astrometry.net'e yüklerken görünürlüğü "özel" seç; ya da yerel kurulum).
   - Kaç yıldız eşleşti? Çözüm başarılı mı?
   - Başarısızsa yalnız yıldızlı kareyi ya da telefoto lensi dene.
2. **İz uçları:** Uçların piksel konumlarını elle işaretle (ör. GIMP ya da kısa bir Python betiği), WCS ile gökteki yönlerine çevir.
3. **Kaba açı hatası:**
   - Taze TLE ile Skyfield'dan, düzeltilmiş EXIF zamanındaki öngörülen yönü hesapla ve uçlarla farkını al.
   - Farkı iz boyunca ve ize dik iki bileşene ayır. İze dik bileşen açı hatasını, iz boyunca bileşen çoğunlukla zaman hatasını gösterir.
4. **Doppler:**
   - Spektrogramda (SDR++ şelale ekranı ya da Python) S biçimli eğri var mı?
   - Ölçülen frekansı TLE'den öngörülen Doppler + sabit ofset ile karşılaştır, kalıntının RMS'ini (Hz) hesapla.

## Beklenenler (model tahmini, eşik DEĞİL)

| Büyüklük | Beklenen mertebe | Kaynak |
|---|---|---|
| ISS Doppler, 16 Kas (tepe 61°) | ±9,5 kHz (15° maskede); en yakın anda eğim ~160 Hz/s | Skyfield, 1 Kas TLE; en yakın uzaklık ~470 km |
| Meteor-M2-4 Doppler, 18 Kas (tepe 79°) | ±3,0 kHz; en büyük eğim ~28 Hz/s | Skyfield, 1 Kas TLE; en yakın uzaklık ~830 km |
| ISS'in açısal hızı | Tepede ~0,8–1°/s; 3 s'lik iz ~2,5–3° | 420 km yükseklik |
| Benzetimde varsayılan telefon hataları | 0,02–0,1° açı, 0,02–0,1 s zaman | `PLAN.md` §6 |

## Kapı 0 (19 Kasım) kararı
- **Optik "evet":**
  - En az bir ISS fotoğrafı plaka çözüldü (ya da aynı yöndeki yalnız yıldızlı kare çözüldü).
  - İz uçları seçilebiliyor.
  - Yapay uydu kalibrasyonu EXIF zamanının anlamını ve ofsetini verdi.
- **Radyo "evet":**
  - En az bir geçişte (Meteor ya da ISS) Doppler eğrisi görüldü.
  - Kalıntı RMS'i kabaca **≤50 Hz.** Benzetimde 50 Hz'de bile Doppler, tek geçiş yörüngesinde 2–9 kat kazanç veriyor; daha kötüsü yöntemi zorlar.
- **Karar:**
  - İkisi evet → birleşik plan.
  - Yalnız biri evet → o hat ağırlıklı devam (`PLAN.md` §11).
  - İkisi de hayır → 22 Kasım'a kadar sorun giderilir ya da yedek fikre geçilir.
- Her durumda **sonuçları olduğu gibi** yaz. Başarısız gece de rapora girer.

## Kurallar
- Yalnızca alıcı kullanılır; verici yok.
- ISS APRS paketlerinin içeriği (çağrı işaretleri) yayımlanmaz, yalnızca frekans ölçülür.
- Fotoğraflarda kişi, ev ya da plaka görünmesin; gökyüzüne çekin.
- Ev konumları depoya tam koordinatla yazılmaz.
