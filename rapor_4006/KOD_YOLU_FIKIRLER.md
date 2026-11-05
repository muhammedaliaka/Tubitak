# Kod Yolu: Fikir Üretimi, 5 Ölçütle Eleme ve Sıralama (6 Kasım gece)

**Bu belge, ebru ve el işi fikirlerini eler ve `FIKIR_PORTFOLYOSU.md` puanlarının yerine geçer.** Yeni kural: kod merkezde olacak, dış kaynak serbest, tek sınır 5 TÜBİTAK ölçütü.

## 0. Önce iki gerçek (kod yolunu etkiler)
1. **Başvuru 13 Kasım'da kapanır, fuar Mart–Haziran 2027'dedir.** Başvuruda yalnızca proje fikrini ve 4 kısa metni (amaç, yöntem, beklenen sonuç) yazarsınız. Kodun kendisi **Aralık–Nisan** arasında yazılır. Ekipte kod bilen yok, ama öğrenmek için 4 ay var; bu, kod riskini azaltır.
2. **4006 kuralı: alt projeyi öğrenciler yapar.** Ben kodu sizin yerinize yazarsam kural bozulur ve başvuruda "Üretken Yapay Zekâ" beyanında bunu belirtmeniz gerekir. Benim rolüm: adım adım öğretmek, örnek vermek, sizin yazdığınız kodu kontrol etmek. Her projede kodun **öğrenciler tarafından yazılacak çekirdeği** aşağıda ayrıca işaretli.

## 1. Fikir üretimi: 6 yoldan 29 kod fikri
- **Gök hesabı:** Güneş/Ay konumu programı → hilal kriterleri, namaz vakti, tarih dönüşümü
- **Kültür × veri:** Osmanlı camileri, kitabeler, ebced → ölçülebilir veri kümeleri
- **Dil × kod:** Osmanlıca ve Arapça (sizin ekipteki özel beceri) → algoritma
- **Sensör × sinyal:** telefon/ESP32 → FFT, filtre, algoritma
- **Simülasyon:** tahliye, kuyruk, su hasadı → model + gerçek ölçümle doğrulama
- **Açık veri:** AFAD, İSKİ, Kandilli, OpenStreetMap → analiz

**Ortak çekirdek (bağlantı):** Güneş ve Ay konumunu hesaplayan **tek bir Python modülü** (pyephem/skyfield ile sınanır) şu fikirlerin hepsinin temelidir: hilal kriterleri, kıble Güneş anı, gölgeden yön bulma, namaz vakitleri, tarih dönüşümü. Bir fikir seçilse bile modül diğerlerine yedek/uzantı olur.

## 2. 5 ölçütle puanlama (29 fikir, 100 puan)
C1 amaç/önem · C2 veri odaklı yöntem · C3 beklenen sonuç/ürün · C4 bilimsel dil ve etik · C5 program amaçlarıyla uyum (her biri 20). Risk kesintisi: benzerlik, izin/ret, tamamlanma, kod yükü. Belirsizlik ±5, yani **5 puandan az fark eşit sayılır.**

| # | Fikir | Grup | C1 | C2 | C3 | C4 | C5 | Ara | Risk | **Net** |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Rüzgâr tüneli: kesit şekli + girdap sesi FFT (kod payı düşük) | Fizik | 16 | 17 | 17 | 15 | 17 | 82 | -8 | **74** |
| 2 | Hicrî ay başlangıcı: Diyanet takvimi hangi kriterle uyuşuyor? (tersine mühendislik) | Gök hesabı | 17 | 18 | 16 | 15 | 17 | 83 | -11 | **72** |
| 3 | Osmanlı camilerinin kıble yönelimi: açık harita + çift ölçümlü veri + istatistik | Kültür×veri | 14 | 18 | 17 | 15 | 16 | 80 | -8 | **72** |
| 4 | Pusula güvenilirlik algoritması (Mıknatıssız Kıble, kod sürümü) | Sensör | 16 | 16 | 17 | 15 | 17 | 81 | -9 | **72** |
| 5 | Kubbe profilleri: dijital yük hattı + fiziksel yük testi | Fizik | 14 | 17 | 16 | 15 | 16 | 78 | -7 | **71** |
| 6 | Okul tahliye simülasyonu + tatbikat süresiyle doğrulama | Simülasyon | 18 | 16 | 17 | 15 | 17 | 83 | -16 | **67** |
| 7 | Afet toplanma alanı erişilebilirliği, Kağıthane (açık veri + yürüme ağı) | Açık veri | 18 | 14 | 16 | 14 | 17 | 79 | -12 | **67** |
| 8 | Okul binası doğal frekansı (telefon ivmeölçeri + FFT) | Sensör | 16 | 17 | 16 | 15 | 16 | 80 | -13 | **67** |
| 9 | Duman/buhar/toz ayrımı (ESP32 + referans sensör) | Sensör | 17 | 17 | 17 | 15 | 16 | 82 | -17 | **65** |
| 10 | Osmanlıca ünlüsüz yazı belirsizliğini ölçme + okuma adayı sıralayıcı | Dil×kod | 14 | 16 | 15 | 15 | 14 | 74 | -9 | **65** |
| 11 | Yağmur suyu hasadı hesaplayıcısı + okul çatısı verisi | Simülasyon | 16 | 13 | 15 | 14 | 17 | 75 | -10 | **65** |
| 12 | Gölge fotoğrafından yön/konum bulan algoritma (Güneş pusulası) | Sensör | 14 | 16 | 15 | 14 | 15 | 74 | -10 | **64** |
| 13 | Hicrî/Rumî/Miladî tarih dönüşüm tablolarının farkı (belgedeki gün adıyla sınama) | Gök hesabı | 13 | 17 | 14 | 14 | 14 | 72 | -9 | **63** |
| 14 | Namaz vakti açı eşikleri ve Diyanet tablosuyla farkı | Gök hesabı | 14 | 15 | 14 | 13 | 14 | 70 | -7 | **63** |
| 15 | Camide kalabalıkta CO₂ ve havalandırma modeli | Sensör | 17 | 16 | 15 | 14 | 16 | 78 | -15 | **63** |
| 16 | Ebced tarih mısralarının tesadüf testi | Dil×kod | 12 | 17 | 13 | 15 | 13 | 70 | -7 | **63** |
| 17 | Arapça kök-vezin çözümleyici (Türkçedeki Arapça kökenli kelimeler) | Dil×kod | 14 | 14 | 15 | 14 | 14 | 71 | -9 | **62** |
| 18 | Isı kamerasıyla erken yangın uyarısı (MLX90640) | Sensör | 17 | 15 | 16 | 14 | 16 | 78 | -17 | **61** |
| 19 | Cami/sınıf akustiği: telefonla yankı süresi | Sensör | 14 | 15 | 14 | 14 | 13 | 70 | -11 | **59** |
| 20 | Baraj doluluk–tüketim modeli (İSKİ açık veri) | Açık veri | 15 | 12 | 13 | 13 | 14 | 67 | -9 | **58** |
| 21 | Kantin kuyruk simülasyonu | Simülasyon | 14 | 13 | 14 | 13 | 12 | 66 | -8 | **58** |
| 22 | Çatı güneş enerjisi potansiyeli, Kağıthane (açık veri) | Açık veri | 15 | 12 | 14 | 13 | 15 | 69 | -12 | **57** |
| 23 | Kitabe metin madenciliği (yalnız 4006-A İnceleme) | Dil×kod | 13 | 11 | 12 | 14 | 12 | 62 | -6 | **56** |
| 24 | Deprem b-değeri (Kandilli kataloğu) | Açık veri | 13 | 15 | 13 | 12 | 13 | 66 | -12 | **54** |
| 25 | Metro ağı dayanıklılığı (graf kuramı) | Açık veri | 14 | 13 | 13 | 13 | 13 | 66 | -12 | **54** |
| 26 | Ezan makam tanıma (perde histogramı) | Sensör | 13 | 15 | 14 | 14 | 13 | 69 | -16 | **53** |
| 27 | Hava kalitesi tahmini (makine öğrenmesi) | Açık veri | 15 | 13 | 14 | 13 | 14 | 69 | -16 | **53** |
| 28 | Osmanlıca el yazısı tanıma (derin öğrenme) | Dil×kod | 16 | 15 | 16 | 13 | 16 | 76 | -23 | **53** |
| 29 | Çift sarkaç kaosu (video + simülasyon) | Fizik | 8 | 16 | 12 | 14 | 10 | 60 | -8 | **52** |
| 30 | Ses kaynağı yönü bulma (iki telefon, TDOA) | Sensör | 10 | 14 | 12 | 13 | 11 | 60 | -8 | **52** |

### Elenenler ve nedeni
- **Osmanlıca el yazısı tanıma (53):** Yapay Zekâ + Kültürel Miras temaları en kalabalık, GPU ve veri ister.
- **Hava kalitesi tahmini (53), Deprem b-değeri (54):** çok yaygın veya yanlış yorum riski ("deprem tahmini" algısı).
- **Ezan makam tanıma (53):** literatür büyük; ses kaydı için izin sorunu.
- **Çift sarkaç (52):** fiziksel güzel ama "günlük hayat" (C1) yok.

## 3. En iyi tercihler (sıralı)

### 🥇 1. Hicrî ay başlangıcı: Diyanet takvimi hangi kriterle uyuşuyor? (72)
- **Soru:** Son 10 yılda Türkiye'nin yayımladığı Ramazan/Şevval/Zilhicce başlangıçlarını hangi hilal kriteri (yerel görünürlük, 5°/8° eşikleri, küresel kriter, saf hesap) en iyi yeniden üretiyor? Hangi aylar hiçbir kriterle uyuşmuyor?
- **Neden güçlü:** Her yıl herkesin gördüğü bir tartışma (2026 Ramazan: Türkiye 19 Şubat, bazı ülkeler 18 Şubat). Yanıt **veriyle çürütülebilir** (C2 yüksek). İmam Hatip kimliğine doğal uyar. 2204-A bölge listelerinde Astronomi neredeyse yok (300 projede 1), yani rakip az.
- **Kodun çekirdeği (öğrenciler yazar):** Güneş/Ay konumu → günbatımında yükseklik ve elongasyon → kriter fonksiyonları → 120 aylık karşılaştırma tablosu. Doğrulama: yazdığınız hesabı hazır kütüphane (pyephem) ile karşılaştırıp hata payı verirsiniz.
- **Ön deneme (bugün yaptım, doğrulandı):** `hilal_pilot.py` 17 Şubat 2026 yeni ayını hesapladı: kavuşum 12:01 UTC; İstanbul'da 17 Şubat akşamı Ay'ın yüksekliği **0,2°** (görünmez), 18 Şubat'ta **12,1° yükseklik / 13,3° elongasyon**. Bu, Türkiye'nin 19 Şubat'ı Ramazan başı alması ile tutarlı. Büyük resmi sınama (120 ay) yapılmadı.
- **Eleştiri (acımasız):**
  - **Diyanet'in tam kriter metnini doğrulayamadım** (2016 İstanbul Kongresi'nin 5°/8° kuralının nerede ve ne zaman uygulandığı net değil; 1978 İstanbul konferansı kararlarına da atıf var). Bu yüzden proje "kuralı biliyoruz" değil, **"kuralı veriden çıkarmaya çalışıyoruz"** diye kurgulandı. Kriter metinleri kaynakla yazılmalı.
  - **Hassasiyet:** Konu dinî. Poster ve sunumda "dinî hüküm değil, hesap karşılaştırması" cümlesi şart; hilalin görülüp görülmediği değil, **yayımlanmış tarihle hesabın uyumu** ölçülür.
  - Yayımlanmış tarihleri toplamak (Diyanet dinî günler listeleri) emek ister; resmî kaynakla doğrulayın.
  - Benzerlik: "hilal hesabı" yazılımları var; yeniliğiniz **kriter karşılaştırması + Diyanet uyumu ölçümü**, yazılımın kendisi değil.
- **Tür / ana alan / tema:** Araştırma (veya Tasarım) · Astronomi ve Astrofizik (veya Matematik) · STEAM ya da Somut Olmayan Kültürel Miras.
- **Maliyet:** ≈ 0 TL (yazılım ücretsiz). Poster/baskı hariç.

### 🥈 2. Osmanlı camilerinin kıble yönelimi (72)
- **Soru:** İstanbul'daki camilerin kıble duvarı doğrultusu, gerçek kıble doğrultusundan yüzyıllara göre ne kadar sapıyor? Dönemler arası fark var mı?
- **Neden güçlü:** Sizin ekiple birebir: Osmanlıca (yapım yılı/kitabe) + Arapça (kıble) + kod (harita verisi). Büyük örneklem (yüzlerce cami) elde edilebilir. Veri açık (OpenStreetMap). **İstanbul için sistemli uydu ölçümü arayıp bulamadım** (İzmir'de 21 camiyle GNSS tezi var; Erzurum için hakemsiz basın iddiası var). Bu "yok" iddiası kendi taramam, kapsamlı değil.
- **Kodun çekirdeği (öğrenciler yazar):** OSM'den cami sınırlarını alma → ölçüm aracı (haritada kıble duvarına tıklayıp açı hesaplayan basit web sayfası) → büyük daire kıble azimutu hesabı → yüzyıl bazlı istatistik ve grafik.
- **Metod sağlamlığı:** İki öğrenci **bağımsız** ölçer (aradaki fark = ölçüm hatası); beş camide **yerinde gölge yöntemiyle** kontrol.
- **Eleştiri (acımasız):**
  - **Hassasiyet çok yüksek:** Basında "camilerde kıble yanlış" haberleri çıkıyor. Poster **"yanlış/doğru" demez**, yalnızca "sapma (derece)" der; fıkhî tolerans ve ihtiyat konusunda hüküm vermez. Öğretmen/müftülük danışmanlığı alın.
  - **OSM cami sınırları İstanbul'da eksik/hatalı olabilir; test edemedim** (sandbox'tan Overpass erişimi kapalı). Hafta sonu ilk iş bu.
  - Kıble duvarı çoğu camide görüntüde net seçilmez (mihrap çıkıntısı arar). Bu yüzden ölçümler belirsiz çıkarsa örneklem küçülür.
  - Uydu görüntüsü lisansı: Google görüntüsünü kopyalayıp yayımlamak sorun olabilir; OSM/açık altlık kullanın.
- **Tür / ana alan / tema:** Araştırma · Matematik veya Coğrafya (bilgisayar bilimi) · Somut Olmayan Kültürel Miras / STEAM.
- **Maliyet:** ≈ 0–300 TL (gölge kontrolü için çubuk, açıölçer).

### 🥉 3. Pusula güvenilirlik algoritması: Mıknatıssız Kıble, kod sürümü (72)
- Mevcut `SECIM_KIBLE.md` projesi, çekirdeği **kod** olacak şekilde yeniden kurulur: telefonun ham manyetik alan verisini (Phyphox) alan, "|B| beklenen 48,2 µT'dan ne kadar saptı?" ve "eğim açısı 59°'ye uyuyor mu?" kontrollerinden **"bu pusula şu an güvenilir değil" uyarısı** üreten bir algoritma. Algoritmanın doğru/yanlış uyarı oranı Güneş yönüyle ölçülür.
- **Neden üçüncü:** Çekirdek fikir güçlü ama problemin büyüklüğü hâlâ doğrulanmadı (ön denemeye bağlı); Osmanlı kıblenümaları var (ürün yeni değil, algoritma yeni olabilir).

### Yedekler
- **Okul tahliye simülasyonu (67):** İlk yangın merakınızı karşılar. Risk: tatbikat ölçümü için okul onayı; "tahliye simülasyonu" lise projelerinde yaygın. NetLogo ile kod yükü düşük.
- **Afet toplanma alanı erişilebilirliği (67):** C1 çok güçlü; AFAD'ın zaten sorgu servisi var, yeniliğiniz kapasite/nüfus analizi olabilir.
- **Osmanlıca ünlüsüz yazı belirsizliği (65):** Sizin Osmanlıca bilginizin en saf kullanımı, ama gerçek Osmanlıca test verisi hazırlamak zor.

## 4. Eşitlik bozma: hafta sonu ön denemeleri (0 TL)
| Fikir | Ön deneme | Devam kuralı |
|---|---|---|
| Hicrî kriterler | `python hilal_pilot.py` çalışsın; 2016–2026 için Diyanet'in yayımladığı 12×10 ay başlangıcını listeye alın | Listeyi **en az 100 ay** doldurabiliyorsanız ve hesap, hazır kütüphane ile 1 dakikadan az farklıysa devam |
| Cami yönelimi | Kağıthane/Eyüp'te **20 cami** seçin; iki kişi ayrı ayrı kıble duvarı açısı ölçsün | İki ölçüm arası medyan fark **≤ 3°** ise devam; > 5° ise yöntem güvenilmez, eleyin |
| Pusula algoritması | `SECIM_KIBLE.md` §5.0 | ≥ 3 noktada hata > 15° ise devam |

**Karar:** Pazar akşamı (8 Kasım). Üçü geçerse ekibin en çok merak ettiği. Hiçbiri geçmezse yedek tahliye simülasyonu.

## 5. Başvuru metinleri (öğrenciler kendi sözleriyle yeniden yazmalı; kelime sayıları sınır içinde)
### 5.1 Hicrî ay başlangıcı (başlık 10, B Amaç ve Önem 69, A Amaç 31, Yöntem 68, Sonuç 54)
**Ad:** Ramazan Hangi Gün Başlar? Hicrî Ay Başlangıç Kriterlerinin Bilgisayarla Karşılaştırılması
**Amaç ve Önem (B):** Her yıl Ramazan ve bayram başlangıçlarında ülkeler ve kurumlar arasında bir günlük farklar ortaya çıkmaktadır. Bu farkların bir kısmı, Ay'ın konumuna uygulanan kriterlerin farklı olmasından kaynaklanmaktadır. Bu projede Ay ve Güneş'in konumunu hesaplayan bir yazılım geliştirilecek, farklı hilal kriterleri aynı yeni aylara uygulanacak ve sonuçlar son on yılda yayımlanmış Türkiye takvim tarihleriyle karşılaştırılacaktır. Böylece hangi kriterin yayımlanan tarihlerle uyuştuğu sayısal olarak gösterilecek ve tarih farklarının nedeni anlaşılır biçimde açıklanacaktır.
**Amaç (A):** Ay ve Güneş'in konumunu hesaplayan bir yazılım geliştirerek farklı hilal kriterlerini son on yılın yeni aylarına uygulamak ve sonuçları yayımlanmış takvim tarihleriyle karşılaştırarak hangi kriterin hangi tarihlerle uyuştuğunu sayısal olarak göstermektir.
**Yöntem:** Ay ve Güneş'in konumunu hesaplayan bir Python programı yazılacak ve hazır gökbilim kitaplığının çıktılarıyla karşılaştırılarak doğrulanacaktır. Son on yılın her yeni ayı için kavuşum anı ile günbatımında Ay'ın yüksekliği ve Güneş'ten açısal uzaklığı İstanbul, Mekke ve dünyanın diğer noktaları için hesaplanacaktır. Yerel görünürlük ve küresel eşik gibi kriterler her aya uygulanıp bulunan ay başlangıç tarihleri yayımlanmış resmî takvim tarihleriyle karşılaştırılacak, her kriterin uyum yüzdesi ve uyuşmayan aylar belirlenecektir.
**Beklenen sonuç:** Programın hesaplarının referans kitaplıkla farkı hata payı olarak verilecektir. Her kriter için uyum oranı ve farklı çıkan aylar tablolaştırılacak, farkların hangi astronomik koşullardan doğduğu açıklanacaktır. Hiçbir kriter tüm tarihleri açıklamazsa bunun nedenleri ortaya konulacaktır. Ürün olarak herkesin tarih seçip kriterleri deneyebileceği bir hesaplama aracı hazırlanacaktır. Çalışma yalnızca hesap ve karşılaştırma yapmakta, dinî hüküm vermemektedir.

### 5.2 Osmanlı camilerinin kıble yönelimi (başlık 11, B 63, A 25, Yöntem 64, Sonuç 59)
**Ad:** Osmanlı Camileri Kıbleye Ne Kadar Yöneldi? İstanbul'da Dönemlere Göre Yönelim Analizi
**Amaç ve Önem (B):** Camilerin kıble yönü, tarih boyunca astronomik gözlem, geleneksel yöntemler ve yerel koşullarla belirlenmiştir. İstanbul'daki farklı dönemlere ait camilerin yönelimlerinin gerçek kıble doğrultusundan ne kadar saptığına dair sistemli ve geniş örneklemli ölçümler sınırlıdır. Bu projede açık harita verisi ve uydu görüntüsünden camilerin kıble duvarı doğrultuları ölçülecek ve yapım dönemlerine göre karşılaştırılacaktır. Sonuçlar, geçmişte kıble tayininin hassasiyetini ve zaman içindeki değişimini sayısal olarak ortaya koyacaktır.
**Amaç (A):** İstanbul'daki farklı dönemlere ait camilerin kıble duvarı doğrultularını açık harita verisi ve uydu görüntüsünden ölçerek gerçek kıble doğrultusundan sapmalarını yapım dönemlerine göre sayısal olarak karşılaştırmaktır.
**Yöntem:** Açık harita verisinden İstanbul'daki cami yapı sınırları alınacak ve her camide kıble duvarının yönü uydu görüntüsü üzerinde iki öğrenci tarafından bağımsız ölçülecektir. İki ölçüm arasındaki fark ölçüm hatası olarak belirlenecek, her camiye ait doğru kıble azimutu koordinattan hesaplanacaktır. Yapım yılı kitabe ve kaynaklardan bulunacak, camiler yüzyıllara göre gruplanıp sapma dağılımları ortalama, standart sapma ve grafiklerle karşılaştırılacaktır. Beş camide yerinde gölge yöntemiyle kontrol ölçümü yapılacaktır.
**Beklenen sonuç:** Yüzyıllara göre kıble sapma dağılımlarını gösteren tablolar ve grafikler elde edilecektir. Yerinde kontrol edilen camilerle uydu ölçümlerinin uyumu verilerek yöntemin hata payı belirtilecektir. Dönemler arasında anlamlı fark çıkarsa olası nedenleri tartışılacak, çıkmazsa bu da sonuç olarak bildirilecektir. Ürün olarak camilerin yönelimini harita üzerinde gösteren etkileşimli bir web sayfası hazırlanacaktır. Çalışma dinî hüküm vermemekte, yalnızca tarihsel ve geometrik ölçüm yapmaktadır.

Pusula algoritması metinleri: `SECIM_KIBLE.md` §3 (kod vurgusu için "yazılım/uyarı algoritması" cümlesi eklenmeli).

## 6. Doğrulanmayanlar (açıkça)
1. Diyanet'in 2026 kriterinin tam metni ve 5°/8° kuralının uygulama koşulu **doğrulanmadı.**
2. Yayımlanmış ay başlangıcı tarihlerinin tam listesi **toplanmadı**; yalnızca 2026 Ramazan (19 Şubat) ve bazı ülkelerde 18 Şubat olduğu haber kaynaklarından görüldü.
3. OSM'de İstanbul cami poligonlarının tamlığı **test edilemedi** (Overpass sandbox'tan kapalı).
4. "İstanbul için sistemli kıble ölçümü yok" ifadesi kapsamlı literatür taraması değildir.
5. 4006-A/B ve tematik konu kuralları hâlâ açık: A'da ≥5, B'de ≤5 tema.
