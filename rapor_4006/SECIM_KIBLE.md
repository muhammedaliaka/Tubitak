# Seçilen Alt Proje: Mıknatıssız Kıble (6 Kasım akşam revizyonu)

> **Durum notu (6 Kasım gece):** Daha geniş araştırma sonrası bu proje artık **finalistlerden biri** (77/100), tek aday değil. Üç finalist (ebru-çöven, rüzgâr-kesit, kıble) puanda eşit; karar ön denemelerle verilecek. Bkz. `FIKIR_PORTFOLYOSU.md` §5.

**Çağrı:** 4006-B olasılığı yüksek (yürütücü doğrulamalı) · **Kurul:** 7 Kasım sabah · **Son başvuru:** 13 Kasım 17:30
**Bütçe:** Ekibin üst sınırı **7.000 TL**; TÜBİTAK desteği **henüz verilmedi ve tutarı kesin değil**. Aşağıdaki hiçbir rakam "alınmış para" varsayımına dayanmaz. Dış kaynak (ödünç alet, üniversite, tanıdık) kullanılabilir.

---

## 0. Bu revizyonda ne değişti? (dürüst liste)

Önceki sürümde üç zayıf nokta vardı. Onları denetleyip düzelttim:

| Önceki iddia | Denetim sonucu | Ne yaptım |
|---|---|---|
| "Bina içinde ortalama 45° pusula hatası" | Kaynak eski (2011) bir konumlama makalesi, ikincil alıntı, PDF'ine erişemedim. Yeni çalışmalar yöntem ve cihaza göre **2° ile 20°+** arası değerler bildiriyor; tek bir kesin sayı yok | Cümleyi kaldırdım. Problemin büyüklüğünü **kendi ölçümünüz** gösterecek; bunun için **ön deneme** ekledim (§5.0) |
| "Güneş kıblenüması yeni bir ürün" | **Değil.** Osmanlı'da kıble göstergeli yatay güneş saatleri var: British Museum'daki fildişi alet (yaklaşık 1582–83, gnomon açısı 41°K yani İstanbul), Topkapı'daki yaklaşık 1480 tarihli kadran, Ayasofya yatay güneş saati restorasyonu, *Risâle-i Vaz'-ı Rühâme* | Ürünü "yenilik" olarak değil, **tarihî bir aletin telefonla ölçülerek karşılaştırılan yeniden yapımı** olarak konumladım. Yenilik ürün değil, **ölçüm sorusu** |
| Araştırma kısmı yalnızca "hata ne kadar?" | Tek başına zayıf bir soru | Soruyu keskinleştirdim: **"Telefon, pusulasının ne zaman yanıldığını kendi ölçtüğü manyetik alandan anlayabilir mi?"** (§1) |

## 1. Ne yapıyoruz?

Telefon pusulası Dünya'nın manyetik alanını okur. İstanbul'da bu alanın **yatay** bileşeni yalnızca yaklaşık **24,8 µT** (toplam 48,2 µT, eğim 59,1°, sapma +6,1° doğu; WMM modeliyle kendi hesabım, 2027 baharı). Yatay bileşen küçük olduğu için, binadaki çelik veya kablodan gelen **birkaç µT'lik** bir bozucu alan bile yönü ciddi saptırır:

| Bozucu alan (yatay, kuzeye dik) | Beklenen yön hatası δ = arctan(b/24,8 µT) |
|---|---|
| 2 µT | 4,6° |
| 5 µT | 11,4° |
| 10 µT | 22,0° |
| 24,8 µT | **45,0°** |

Bu bir **fizik modeli**: telefonun ölçtüğü alanın beklenen değerden sapması, yön hatasını tahmin ettirebilir. Ama model kusurlu olabilir: bozucu alan kuzey doğrultusundaysa alan şiddeti değişir ama yön değişmez; iki bozucu birbirini götürebilir. İşte **araştırma sorusu** budur:

> **Telefon pusulası bina içinde kıbleyi ne kadar yanlış gösteriyor, ve bu hata telefonun kendi ölçtüğü manyetik alan sapmasından önceden tahmin edilebiliyor mu?**

Üç çıktı:
1. **Hata haritası:** 60+ noktada telefon kıble hatası (°).
2. **Model testi:** Ölçülen alan sapmasından hesaplanan hata ile gözlenen hata arasındaki ilişki (grafik, korelasyon). Uyuyorsa "güvenilmez bölge" uyarısı için eşik çıkar; uymuyorsa nedenleri yazılır (ikisi de bulgu).
3. **Ürün:** Manyetizmadan etkilenmeyen **Güneş Kıblenüması** (tarih ve saate göre ayarlanan, gölgeyle çalışan yatay kadran) + "telefon pusulasına ne zaman güvenilmez" tek sayfalık kullanıcı kartı.

## 2. Neden bu proje? (ve neden hâlâ kesin değil)

**Lehine:**
- Problem günlük hayata dokunuyor (kıbleyi telefonla bulmak çok yaygın) ve **ölçülebilir**; ölçülecek modelin fiziği net (yukarıdaki tablo).
- Türkiye'de bu konuda öğrenci projesi bulamadım (kapsamlı tarama değil). TÜBİTAK 2204 bölge listelerindeki 300 projede Astronomi teması yalnızca 1 projede.
- Ekibe uyuyor: fizik öğretmeni (manyetizma ve ışık), Osmanlıca bilen öğrenci (Rühâme risalesi, kıblenüma metinleri), Arapça bilen öğrenci (klasik kıble hesap kaynakları). **Kod gerekmiyor.**
- Düşük risk: insan denekler yok, anket yok, tehlikeli madde yok.
- Telefon manyetometresi ücretsiz: **Phyphox** uygulaması alanı µT cinsinden gösterir.

**Aleyhine (ruhsuzca):**
- **"Önem" zayıf çıkabilir.** Diyanet'e atfedilen fıkhî tolerans 45° (ikincil kaynak). Telefon hatası çoğu noktada bunun çok altındaysa "problem küçük" denir. Ön deneme bunu baştan gösterecek.
- **Ürün yenilik değil** (yukarıda). Jüri "bu zaten var" diyebilir; cevap: biz ölçüyoruz ve telefonla karşılaştırıyoruz.
- **Dinî hassasiyet:** Konu *telefon sensörü*, cami kıblesi değil. Caminin kıblesini ölçmek veya hüküm vermek yok.
- **İç mekânda "gerçek yön" zordur:** Gölge için içeri güneş girmesi gerekir. İç mekân gerçeği çoğunlukla **duvar açısından** gelir (uydu haritasından ±1–2° doğrulukla; dışarıda bilinen bir hizayla doğrulanmalı).

**Rakipler:** Duman/yanlış alarm Tasarım projesi (referans PM sensörüyle güçlenir; ama kod ve benzerlik riski var) ve kitabe RTI düzeneği (Osmanlıca bilen var; ama mezarlık izni ve Kültürel Miras temasının kalabalığı var). Aralarındaki farklar ±5 puan içinde; seçimi **ön deneme** netleştirecek (§5.0).

## 3. Başvuru kartı

| Alan | Değer |
|---|---|
| **Proje adı** | Mıknatıssız Kıble: Telefon Pusulası Bina İçinde Ne Zaman Yanılır? |
| **Tür** | Tasarım (ürün + test). Soru ağırlıklı kalsın isterseniz Araştırma da olur; ikisi de B'de geçerli |
| **Ana alan** | Fizik |
| **Tematik konu** | STEAM varsayımı (okul onaylarsa). Olmazsa: Astronomi ve Astrofizik |
| **Öğrenci / danışman** | 4 öğrenci (2–4 sınırı) / fizik öğretmeni |

> Bunlar taslaktır. Öğrenciler kendi cümleleriyle yeniden yazmalı: sistem benzerlik taraması yapıyor; formda "Üretken Yapay Zekâ Kullanım" beyanı var ve bu taslak yapay zekâ ile hazırlandı (dürüstçe beyan edin); metinde okul/kişi adı olmamalı (kılavuz §5).

**4006-B Amaç ve Önem (50–150 kelime; 73):**
Telefon pusulası, Dünya'nın manyetik alanını ölçerek yön bulur. Bu alanın yatay bileşeni İstanbul'da yaklaşık 25 mikrotesla gibi küçük bir değerdir; binadaki çelik ve elektrik tesisatı onu kolayca bozabilir. Kıble yönünü telefon pusulasıyla bulan çok sayıda kişi, pusulanın ne zaman yanıldığını bilemez. Bu projede telefon pusulasının bina içi kıble hatası ölçülecek, hatanın telefonun ölçtüğü manyetik alan sapmasından önceden tahmin edilip edilemeyeceği araştırılacak ve Güneş gölgesiyle çalışan, manyetizmadan etkilenmeyen bir kıble bulucu tasarlanıp test edilecektir.

**Yöntem (50–150; 79):**
Okul ve konutlarda, metal yapı elemanlarına farklı uzaklıklarda en az 60 ölçüm noktası belirlenecektir. Her noktada telefon uygulamaları kıble yönünü gösterirken telefonun manyetik alan bileşenleri de kaydedilecektir. Gerçek kıble yönü, Güneş'in kıble doğrultusunda bulunduğu anda bir çubuğun gölgesiyle ve haritadan ölçülen duvar açısıyla belirlenecektir. Gözlenen hata açısı, ölçülen alanın beklenen değerden sapmasından hesaplanan hata ile karşılaştırılacaktır. Ardından tarih ve saate göre ayarlanan, Güneş gölgesiyle çalışan mekanik bir kıble bulucu tasarlanıp aynı noktalarda test edilecek ve hatası telefon pusulasıyla karşılaştırılacaktır.

**Beklenen Sonuç (50–150; 57):**
Telefon pusulasının bina içindeki kıble hatasının ortalaması ve dağılımı sayısal olarak ortaya konulacaktır. Hatanın, ölçülen manyetik alan sapmasıyla ne kadar tahmin edilebildiği grafik ve ilişki katsayısıyla gösterilecektir. Tasarlanan Güneş kıble bulucunun hatasının telefon pusulasından düşük olması beklenmektedir. Beklentiler doğrulanmazsa nedenleri sınırlılıklarla birlikte raporlanacaktır. Sonuçlar, kullanıcıların telefon pusulasına hangi koşullarda güvenebileceğine dair veriye dayalı bir uyarı ölçütü sunacaktır.

*(4006-A olursa Amaç, 20–50 kelime; 33):* Telefon pusulasının bina içinde kıble yönünü ne kadar yanlış gösterdiğini ve bu hatanın ölçülen manyetik alan sapmasından tahmin edilip edilemeyeceğini araştırmak; Güneş gölgesiyle çalışan, manyetizmadan etkilenmeyen bir kıble bulucu tasarlayıp doğruluğunu telefonla karşılaştırmaktır.

## 4. Bilimsel temel

| Kavram | Değer | Kaynak |
|---|---|---|
| Kağıthane'den kıble yönü | **151,7°** (coğrafi kuzeyden), Kâbe'ye 2.413 km; 1° ≈ 42 km | Kendi büyük daire hesabım (`kible_hesap.py`) |
| Manyetik alan (2027 baharı) | F = 48,2 µT, H = 24,8 µT, Z = 41,3 µT, eğim 59,1°, **sapma +6,1°** | WMM (pygeomag) |
| Pusula "kuzey"i | Coğrafi kuzeyden 6,1° doğuya sapık; düzeltmeyen uygulama dışarıda bile 6° şaşar | WMM |
| Güneş kıble yönündeyken (Türkiye saati) | 7–13 Kasım ≈ **11:03–11:04** (yükseklik ≈ 27°); 1 Mart 11:47; 1 Nisan 11:57; 1 Mayıs 12:07; **28 Mayıs 12:18** (Kâbe'nin tam üstü, Diyanet'in "Dünya Kıble Günü" saatiyle aynı) | Kendi güneş hesabım |
| Fıkhî tolerans | 45° (Diyanet'e atfedilen; ikincil kaynak) | [islamveihsan](https://www.islamveihsan.com/kible-yonunde-ne-kadarlik-sapma-namaza-mani-olur.html) |
| Telefon kıble uygulaması doğruluğu | Endonezya tezleri: dışarıda, theodolite karşısında 1–6° | [Hisabuna 2021](https://journal.uin-alauddin.ac.id/index.php/hisabuna/article/view/17177) |
| Bina içi yön hatası alan yazını | 2° ile 20°+ arası (yöntem ve cihaza göre); tek kesin sayı yok | [Ettlinger vd. 2024](https://repositum.tuwien.at/handle/20.500.12708/194971), [UNSW IPIN 2013](https://cgi.cse.unsw.edu.au/~mahbub/PDF_Publications/IPIN2013_heading.pdf) |
| Tarihî öncüller | Kıble göstergeli yatay güneş saatleri | [British Museum](https://www.britishmuseum.org/collection/object/W_1921-0625-1), [Rühâme makalesi](https://nazariyat.org/en/issues/2/m0007), [Ayasofya yatay güneş saati](https://www.ta-dip.de/fileadmin/user_upload/bilder6/AYASOFYA_YATAY_GUNES_SAATI_B.pdf) |
| Müfredat | FİZ.11.2 manyetik alan ve mıknatıs etkileşimi; ışığın doğrusal yayılması (gölge) | MEB 2026 Fizik Programı |

## 5. Plan

### 5.0 ÖN DENEME (bu hafta sonu, 1–2 saat, ücretsiz) — projeye karar verdiren test
Amaç: Telefon pusulası gerçekten şaşıyor mu? Başvuruyu 13 Kasım'a kadar sabitlemeniz gerektiği için bunu **önce** görün.
- **Alet:** Ekipten en az 3 farklı telefon, **Phyphox** (ücretsiz, magnetometer deneyi), bir kıble uygulaması, çekül/ip, şerit metre.
- **Noktalar (≥10):** 2 açık alan (kontrol), 8+ iç mekân (sınıf ortası, çelik dolap/kapı yanı, masa/bilgisayar yanı, hoparlör/TV yanı, merdiven boşluğu, mutfak, balkon). Evde de olur.
- **Her noktada kaydet:** (a) uygulamanın gösterdiği kıble yönü ile gerçeğin farkı, (b) Phyphox'ta toplam alan |B| (µT), (c) mümkünse yatay bileşen.
- **Gerçek yön:** Dışarıda **cumartesi veya pazar 11:03–11:04**'te (güneşliyse) bir çubuğun gölgesinin tersi kıble yönüdür; iç mekânda harita-duvar yöntemi. Bulutluysa sadece harita-duvar.
- **Karar kuralı:**
  - ≥3 noktada yön hatası **>15°** veya |B| beklenenden (48,2 µT) **%20'den fazla** sapıyorsa → problem gerçek, **projeye devam**.
  - Tüm noktalarda hata **<8°** ise → problem küçük (C1 zayıf); **yedek fikre geçin** (duman/yanlış alarm Tasarım projesi) veya soruyu "ne zaman güvenebiliriz" olarak yeniden yazın.
- Sonuçları bana yazarsanız karar kuralını birlikte yorumlarız.

### 5.1 Ana ölçüm (Mart–Nisan)
60+ nokta × ≥3 telefon × ≥2 uygulama; her noktada kalibrasyonsuz ve "8 hareketi" kalibrasyonlu okuma; metale uzaklık (cm). Gerçek yön: gölge + harita-duvar (iki yöntem birbiriyle dışarıda tutarlılık için kontrol edilir). **Dış kaynak:** Bir teodolit/total station ödünç alınabilirse (Yıldız Teknik'teki tanıdık üzerinden veya harita bölümünden) gerçek yön ±0,5° doğrulukla ölçülür; C2 (yöntem) güçlenir.

### 5.2 Güneş Kıblenüması (Nisan–Mayıs)
- İlke: Kağıthane enlemi (41,08°K) için hesaplanmış yatay kadran; gnomon gölgesi tarih/saat eğrisine denk gelene kadar kadran döndürülür; sabit ok kıbleyi gösterir.
- Tasarım döngüsü: v1 → test → v2. Hedef doğruluk ±2–3° (gölge kenarı bulanıklığı sınırı; sınırlılık olarak raporlanır).
- Kadran eğrilerini **öğrenciler** çizelgede kurar; ben yalnızca kontrol betiği veririm (`kible_hesap.py`).
- Yapım: akrilik/kontrplak, lazer kesim hizmeti, metalsiz gnomon, su terazisi.

### 5.3 Fuar günü
Telefonun çelik dolap yanında kıble okunun kaymasını canlı gösteren düzenek; yanında Kıblenüma; poster: hata haritası + model grafiği + tarihî aletlerle karşılaştırma. **28 Mayıs 12:18**'de Kâbe'nin üstündeki Güneş ile ek doğrulama (fuar tarihini bu güne denk getirmek gösteriyi güçlendirir).

## 6. Maliyet (tahmin; alışveriş sırasında güncel fiyat bakılmalı)

Seçim kriteri maliyet değil; bu liste "en az maliyetle aynı bilimsel gücü" arar. Ödünç alınabilen her şey alınmaz.

| Kalem | Tahmin (TL) | Dış kaynakla |
|---|---|---|
| Telefonlar (≥3 farklı model), Phyphox | 0 | Ekip + tanıdıklar |
| Kadran: lazer kesim akrilik/kontrplak hizmeti | 400–800 | — |
| Gnomon (metalsiz), su terazisi, açıölçer, şakul, şerit metre | 150–300 | — |
| Analog (sıvılı) pusula, karşılaştırma için | 100–200 | Okul laboratuvarı |
| Baskı/laminasyon, poster 100×80 cm | 200–400 | — |
| Teodolit / total station | 0 | **Ödünç** (üniversite/harita bölümü); satın alma gerekmez |
| **Çekirdek toplam** | **≈ 850–1.700** | |
| İsteğe bağlı: ikinci bağımsız manyetometre modülü (telefonla çapraz doğrulama; kod ister) | 300–800 | Kodlama için dış yardım gerekir |
| İsteğe bağlı: hassas imalat (CNC/metal kadran) | 800–2.500 | Atölye |
| **Üst sınır (hepsi)** | **≈ 5.000'in altında** | 7.000 TL sınırınızın altında |

Not: TÜBİTAK harcamayı karşılayacaksa faturalar **sözleşme tarihleri arasında** olmalı (SSS md. 29); dışarıdan karşılanan harcamalar için bu kural geçerli değildir. Kamera, bilgisayar, yazıcı gibi genel cihazlar TÜBİTAK harcaması olarak kabul edilmez.

## 7. Görev dağılımı (4 öğrenci + fizik öğretmeni)

| Rol | Görev |
|---|---|
| Ö1 (ölçüm) | Nokta listesi, Phyphox kayıtları, kayıt çizelgesi |
| Ö2 (hesap) | Kıble saatleri, duvar açıları, kadran eğrileri, hata modeli (çizelgede kendisi kurar) |
| Ö3 (imalat) | Kıblenüma v1/v2 |
| Ö4 (analiz, poster, tarih) | Grafikler, poster; **Osmanlıca bilen öğrenci** Rühâme/kıblenüma metinleri, **Arapça bilen öğrenci** klasik hesap kaynakları |
| Dış yardımcı (öğrencilerden birinin kuzeni, Yıldız Teknik mezunu, mekanik) | Tasarım/ölçüm danışmanlığı. Kılavuz: "belirli ölçüde yardım" serbest, **"destek alınan kişi belirtilmeli"** (§5); posterde adı geçer |

**Yapay zekâ:** Alt projeyi öğrencilerin yapması şart. Hesapları sizin yerinize yazmayacağım; adım adım anlatırım, siz kurarsınız.

## 8. Takvim

| Tarih | İş |
|---|---|
| 7 Kas (Cmt) | Kurul sunumu; **ön deneme** (güneşliyse 11:03–11:04) |
| 8 Kas (Paz) | Ön deneme tekrarı; sonuçları değerlendirme |
| 9–11 Kas | Karar (devam / yedek); metinleri öğrenci diliyle yeniden yazım; yürütücü sisteme girer |
| 13 Kas 17:30 | Son başvuru (11 Kas'a kadar gönderin) |
| Kas–Oca | Alan yazını, Rühâme/kıblenüma kaynakları, kadran hesabı (çizelge) |
| Şubat | Sonuç; sözleşme |
| Mart–Nisan | 60+ nokta ölçümü; kadran v1 |
| Nisan–Mayıs | Kadran testi, v2, analiz, poster |
| 28 Mayıs 12:18 | Kâbe'nin üstündeki Güneş ile ek doğrulama |
| 1 Mart–5 Haz | Fuar |

## 9. Riskler

| Risk | Olasılık | B planı |
|---|---|---|
| Ön deneme: hata küçük çıkar (<8°) | Orta | Yedek: duman/yanlış alarm Tasarım projesi veya soruyu "güven eşiği" olarak daralt |
| Ürün "zaten var" itirazı | Yüksek | Poster'da tarihî öncüller açıkça anılır; katkı ölçümdür |
| Dinî hassasiyet | Düşük–orta | Cami kıblesi ölçülmez, hüküm verilmez; mescit ölçümü yalnızca izinle |
| Bulutlu hava | Orta | Harita-duvar yöntemi; esnek takvim |
| Kadran ±2–3°'yi tutturamaz | Orta | Ölçülen hata ve nedeni raporlanır |
| İç mekân gerçek yönü yanlış | Orta | İki yöntemin dışarıda uyumu; teodolit ödüncü |

## 10. Jürinin soracakları

1. Telefon pusulası nasıl çalışır, neden bina içinde şaşar?
2. Manyetik sapma nedir, İstanbul'da kaç derece, neden önemli?
3. Hata modelini (δ = arctan(b/H)) nasıl kurdunuz, neden tam uymayabilir?
4. Güneş neden o saatte kıble yönünde olur?
5. İç mekânda gerçek yönü nasıl bildiniz?
6. Kıblenüma Osmanlı'dakinden ne farklı? (Yeni değil; biz ölçtük ve telefonla karşılaştırdık.)
