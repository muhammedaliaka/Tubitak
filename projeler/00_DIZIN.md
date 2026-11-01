# Proje Fikirleri Dizini (17 aday) — TÜBİTAK 2204-A, Fizik, Kağıthane

> **Seçilen (1 Kasım):** P01 + P09 birleşimi → **`../uydu-isik-radyo/PLAN.md`** (plan, benzetim, geçiş tahmini, Pilot-0 föyü). Diğer kartlar yedek olarak duruyor.

> **Tarih:** 1 Kasım 2026 · **Amaç:** Sınav haftalarında (2–15 Kas) okunup tartışılacak fikir kartları. Her kart aynı şablonda: tek cümle, neden ilginç, hipotezler, fizik, deneyler, yazılım, donanım (mevcut/yeni), yapay zekâ gerekli mi, öncül → kama, gösteri, savunma anlatısı, riskler, ilk pilot, kaynaklar.
> **İşaretler:** *(doğrulanmadı)* = kaynağını bulamadım/okumadım; *(tahmin)* = kendi kaba hesabım; *"bulamadım"* ≠ "yok" (arama standart web aramasıyla sınırlı; Google Scholar/ULAKBİM taraması yapılmadı). **Tüm USD fiyatları tahmindir, Türkiye fiyatı/kur/gümrük doğrulanmadı.**

## 1. Ortak çerçeve (ekibin verdiği bilgiler)

- Danışman fizik hocası → **Fizik alanı**; fizik derinliği birinci ölçüt.
- **Bilimsel ama etkileyici hissedilmeli**; savunma sanayi yalnızca "faydalı olabilir" anlatısı, zorunlu değil.
- Yazılım ağırlıklı ya da yazılım + fiziksel bağlantılı; **yapay zekâ yalnızca gerekirse** (her kartta "gerekli mi?" sorusu ayrı).
- Harcama tavanı **25.000 TL** (yeni alınanlar). Mevcut: 4 Arduino R3, ESP32, küçük ekran, lehim seti, orta-üst laptop, okul bilgisayarları. **3D yazıcı, CNC, osiloskop, sinyal üreteci muhtemelen yok.**
- Konum **Kağıthane, İstanbul**. Sınav **2–15 Kasım**; son başvuru **4 Ocak 2027, 17:30**.

## 2. Özet tablo ve puanlar (1–5; öznel, tartışmaya açık)

Puanlar: **Fizik** derinliği · **Etki** (etkileyicilik/gösteri) · **Kama** (öncüle göre yenilik) · **Bitirme** olasılığı (7 haftada) · **Maliyet** (5 = en ucuz).

| Kod | Proje | Fizik | Etki | Kama | Bitirme | Maliyet | Toplam | Yeni harcama (tahmin) | Yapay zekâ |
|---|---|---|---|---|---|---|---|---|---|
| [P01](P01_uydu_doppler_konum.md) | Sputnik'ten TRANSIT'e: uydu Doppler'iyle GNSS'siz konum | 5 | 5 | 4 | 4 | 5 | **23** | ~60–100 USD | Gerekmez |
| [P02](P02_manyetometre_metro_gunes.md) | Kağıthane manyetometresi: metro ve Güneş fırtınası izi | 5 | 4 | 4 | 4 | 5 | **22** | ~30–60 USD | Gerekmez |
| [P04](P04_lazer_benek_parmak_izi.md) | Kâğıdın parmak izi: lazer benek | 5 | 4 | 3 | 4 | 5 | **21** | ~20–80 USD | Gerekmez |
| [P05](P05_telefonla_schlieren.md) | Telefonla görünmez hava: BOS schlieren | 4 | 5 | 2 | 5 | 5 | **21** | ~5–20 USD | Gerekmez |
| [P09](P09_telefon_fotograflarindan_yorunge.md) | Üç telefon fotoğrafından uydu yörüngesi (Gauss) | 5 | 5 | 3 | 3 | 5 | **21** | ~10–30 USD | Gerekmez |
| [P03](P03_hidrojen_cizgisi_samanyolu.md) | 21 cm hidrojen çizgisiyle Samanyolu'nun dönüşü | 5 | 5 | 2 | 4 | 4 | **20** | ~100–150 USD | Gerekmez |
| [P06](P06_akustik_tomografi.md) | Sesle sıcaklık haritası: akustik tomografi | 4 | 4 | 4 | 3 | 5 | **20** | ~20–50 USD | Gerekmez |
| [P07](P07_bogaz_sisi_gorus_mesafesi.md) | Sisi kameradan ölçmek: Koschmieder mi, yapay zekâ mı? | 4 | 4 | 4 | 3 | 5 | **20** | ~0–20 USD | **Araştırma sorusu** |
| [P15](P15_karadeniz_mikrosismik.md) | Karadeniz fırtınasının sismik izi (açık veri) | 4 | 3 | 4 | 4 | 5 | **20** | 0 | Fizik vs ML |
| [P08](P08_odanin_seklini_sesle_duymak.md) | Odanın şeklini sesle duymak | 4 | 5 | 3 | 2 | 5 | **19** | ~20–60 USD | Gerekmez |
| [P10](P10_canak_anten_radyo_teleskop.md) | Uydu çanağı radyo teleskop: Güneş ve Ay | 5 | 4 | 3 | 3 | 4 | **19** | ~20–60 USD | Gerekmez |
| [P11](P11_isil_imza_yayinirlik.md) | Isıl imza ve yayınırlık: ucuz termal kamera | 4 | 4 | 3 | 4 | 4 | **19** | ~50–80 USD | Gerekmez |
| [P12](P12_enf_sebeke_parmak_izi.md) | Ampulün titremesi kaydın saatini söyler (ENF) | 3 | 4 | 3 | 3 | 5 | **18** | ~0–30 USD | Gerekmez |
| [P14](P14_termoakustik_aktif_kontrol.md) | Isının şarkısını susturmak: Rijke tüpü | 5 | 5 | 2 | 2 | 4 | **18** | ~40–100 USD | Gerekmez |
| [P13](P13_dijital_gunes_tasi.md) | Dijital güneş taşı: polarizasyonla yön | 4 | 4 | 2 | 2 | 5 | **17** | ~10–50 USD | Gerekmez |
| [P16](P16_muon_bina_metro.md) | Müonlarla binanın ve metronun içini görmek | 5 | 5 | 2 | 1 | 3 | **16** | ~200–400 USD | Gerekmez |
| [P17](P17_geminid_radyo_meteor.md) | Geminidleri radyoyla yakalamak (GRAVES) | 4 | 4 | 1 | 1 | 5 | **15** | ~0–40 USD | Gerekmez |

**Genel gözlem:** 17 fikrin 16'sında yapay zekâ gerekmiyor; fizik modeli yeterli. P07 ve P15'te "yapay zekâ gerekli mi?" sorusu araştırmanın kendisi olabilir; Evren burada (görüntü eğitimi) doğal olarak kullanılabilir.

## 3. Benim ilk beşim (kısa gerekçe)

1. **P01 – Uydu Doppler'iyle konum:** Fizik + etki + net soru + benzetim kanıtı (`fikir-havuzu-v2/doppler_konum_sim.py`) bir arada. Asıl risk: 2026'da hangi uyduların yayın yaptığı (pilotla çözülür).
2. **P02 – Metro + Güneş manyetometresi:** Kağıthane'ye özgü (M7 viyadüğü, 1.500 V DC), sonucu garantili (metro izi her gün var), sıfır maliyetli pilot (phyphox).
3. **P04 – Lazer benek parmak izi:** Dalga optiği, düşük risk, ucuz; Nature 2005 öncülü bilinçli olarak anılmalı.
4. **P09 – Telefon fotoğraflarından yörünge:** Gauss/Ceres hikâyesi, P01 ile güçlü birleşim; bulut riski.
5. **P07 – Sisi kameradan ölçmek:** "Yapay zekâ gerekli mi?" sorusunu doğrudan araştıran tek proje; sis garanti değil ama görüş aralığı her gün değişir.

## 4. Birleştirme önerileri (iki kart → tek güçlü proje)

| Birleşim | Fikir |
|---|---|
| **P01 + P09 (+P17)** | "Kağıthane'den Uzayı Ölçmek": aynı uydunun yörüngesini hem radyo Doppler'iyle hem fotoğraf astrometrisiyle belirleyip karşılaştırmak |
| **P05 + P06** | "Görünmez Havayı Işıkla ve Sesle Ölçmek": aynı sıcak hava dumanını BOS (optik) ve akustik tomografi (ses) ile ölçüp çapraz doğrulamak |
| **P02 + P15** | "Kağıthane'nin Görünmez Titreşimleri": manyetik ve sismik kentsel gürültüyü doğal sinyallerden (Güneş, deniz) ayırmak |
| **P07 + P13** | "Balkondan Atmosfer Optiği": görüş mesafesi (saçılma) + gök polarizasyonu, aynı kamerayla |
| **P01 + P03 + P10** | "Tek SDR ile üç radyo deneyi" (geniş ama dağınık; jüri için tek soru seçilmeli) |

## 5. Ortak takvim iskeleti (her kart için uyarlanır)

| Dönem | İş |
|---|---|
| 2–15 Kas (sınav) | Ekip işi yok. Hazırlık: seçilen kartın kodu/benzetimi, sipariş listesi (gerekirse sipariş) |
| 16–22 Kas | Pilot + kurulum → **Kapı 0 (19 Kas):** pilot olumlu mu? Değilse yedek karta geç |
| 23 Kas–13 Ara | Ana deneyler → **Kapı B (6 Ara):** ana hipotez sınanabiliyor mu? Değilse kapsam daralt |
| 14–20 Ara | Analiz, "yapay zekâ gerekli mi?" karşılaştırması |
| 21–27 Ara | Rapor (≤ 20 sayfa), özet (150–250 kelime), başlık (≤ 15 kelime) |
| 28 Ara–3 Oca | Tampon; **hedef yükleme 28 Aralık** |

## 6. Ortak alışveriş listesi (tahmin; Türkiye fiyatı/bulunabilirliği doğrulanmadı)

| Parça | Kullanan kartlar |
|---|---|
| RTL-SDR V4 + dipol seti | P01, P03, P17 (P10 alternatif) |
| FM bant durdurucu süzgeç | P01 (P17) |
| H-çizgisi LNA + süzgeç | P03 |
| RM3100 / MMC5983MA manyetometre | P02 |
| INMP441 MEMS mikrofon ×4–8, küçük hoparlör + amfi | P06, P08 |
| MLX90640 termal kamera | P11 |
| Class 2 lazer modülü + lensi sökülebilir webkamera | P04 |
| K tipi termokupl + MAX6675 | P05 |
| LNB + güç enjektörü + AD8318 güç dedektörü | P10 |
| Polarizör film + kalsit kristali | P13 |
| Tripod + telefon tutucu | P09 (P07) |
| Boru, nikrom ısıtıcı, güç kaynağı, hoparlör | P14 |
| Sintilatör + SiPM + PCB | P16 |

## 7. Ortak kurallar (her kart için geçerli)

- **2204-A:** En çok 3 öğrenci + 1 danışman; proje öğrencilerin işi olmalı; kullanılan araçlar (yapay zekâ kodlama asistanı dahil) raporda belirtilir; başlık ≤ 15 kelime; özet 150–250 kelime; rapor ≤ 20 sayfa PDF; intihal denetimi.
- **Sağlık iddiası yok.**
- **Yalnızca alma (receive-only):** Hiçbir kartta radyo yayını yapılmaz; karıştırma/aldatma yok.
- **Güvenlik:** Lazer yalnızca Class 2; sıcak yüzeyler ≤ 60 °C (P11) ya da danışman gözetiminde (P14); şebekeye doğrudan bağlantı yok (P12); çatı/balkon çalışmaları yetişkin gözetiminde (P01, P03, P10); metro çevresinde yalnızca kamuya açık alan ve izinle (P02, P16).
- **Mahremiyet:** Kamera kartlarında (P07, P09) kişi görüntüsü toplanmaz.
- **Öncül dürüstlüğü:** Her kartta öncül çalışmalar raporun literatür bölümünde açıkça atıf alır; kama ancak tarama sonrası iddia edilir.

## 8. Diğer dosyalardaki önceki adaylar

- `camasir-nem-dengesi/` — Çamaşır–Nem Dengesi (tam plan + Pilot-0 protokolü; bitirme garantisi en yüksek, etki/savunma zayıf).
- `bitki-ultrasonu/` — Bitki ultrasonu (tam plan; ölçüm riski yüksek).
- `fikir-havuzu-v2/FIKIR_HAVUZU.md` — A (GNSS'siz zaman; P01 içine katıldı), C (pasif radar; elendi), F (EMC tarayıcı; alet eksikliği nedeniyle ikinci planda).
- `fikir-havuzu-v2/DERIN_INCELEME.md` — P01, P04, P12, P13'ün ayrıntılı incelemesi ve benzetim.
