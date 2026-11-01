# P14 — Isının Şarkısını Susturmak: Rijke Tüpünde Termoakustik Kararsızlığın Aktif Kontrolü

> **Tek cümle:** İçinde ısıtıcı ızgara olan bir borunun kendiliğinden ürettiği yüksek sesi (termoakustik kararsızlık) mikrofon–hoparlör geri beslemesiyle susturmak ve kararlılık haritasını çıkarmak.
> **Aile:** Akustik/ısı/kontrol · **Yazılım payı:** ~%55 · **Yeni harcama (tahmin):** ~40–100 USD · **Yapay zekâ:** gerekmez

## Neden ilginç
"Isı ses üretiyor, ses de ısıyı durduruyor": çok etkileyici bir canlı gösteri. Roket motorları ve gaz türbinlerinde yanma kararsızlığı gerçek bir mühendislik sorunu (genel bilgi).

## Araştırma soruları ve hipotezler
- **H1:** Kararsızlığın başlangıcı ısıtıcı gücü ve konumuyla Rayleigh ölçütünün öngördüğü bölgede oluşur.
- **H2:** Faz kaydırmalı geri besleme, ses düzeyini belirli bir kazanç/faz aralığında arka plana indirir.
- **H3:** Uyarlanır (LMS) denetleyici, boru ısındıkça değişen frekansı sabit denetleyiciden daha iyi izler.

## Fizik
Açık–açık boruda duran dalga (f ≈ c/2L), Rayleigh ölçütü (ısı salınımı basınçla aynı fazdaysa enerji beslenir), sönüm, geri besleme ve faz payı.

## Deneyler
E1 başlangıç haritası (güç, konum, L) · E2 faz–kazanç taraması ile bastırma haritası · E3 LMS uyarlanır kontrol · E4 pasif sönüm (Helmholtz rezonatörü) ile karşılaştırma.

## Yazılım
Laptop ses giriş/çıkışıyla düşük gecikmeli denetleyici (veya ESP32), sistem tanılama, kararlılık haritası, kayıt.

## Donanım
**Yeni:** ~1 m çelik/alüminyum boru (hırdavat), nikrom tel/ızgara ısıtıcı, düşük gerilim yüksek akım güç kaynağı (güç gereksinimi deneyle belirlenecek; doğrulanmadı), hoparlör + amfi, mikrofon. **Mevcut:** laptop, Arduino.

## Yapay zekâ gerekli mi?
Hayır (klasik kontrol). Pekiştirmeli öğrenme denemesi gereksiz.

## Öncül → kama
**Öncül:** Heckl (Cambridge) mikrofon–süzgeç–faz kaydırıcı–hoparlör ile aktif kontrol; PolyU 1999 tezi; Lund 2004 yüksek lisans tezi; UCLouvain ve Georgia Tech elektrikli Rijke düzenekleri; MethodsX'te mikro jetlerle ~100 dB'den 44 dB'ye ~10 s'de bastırma.
**Kama (zayıf):** Laptop tabanlı ucuz uyarlanır denetleyici ve açık eğitim düzeneği; tam kararlılık haritası.

## Etkileyici gösteri
Borunun yüksek sesle "şarkı söylemesi" ve bir düğmeyle susması.

## Savunma anlatısı
Roket/jet motoru yanma kararsızlığı ve aktif bastırma.

## Riskler
**Güvenlik en yüksek proje:** sıcak yüzeyler, yüksek akım, yangın; yüksek ses (~100 dB) → kulak koruması. Danışman gözetimi ve okul laboratuvarı şart; TÜBİTAK kamu güvenliği kuralına dikkat. Güç kaynağı temini belirsiz.

## İlk pilot
Danışman gözetiminde boru + ızgara + ısıtıcıyla "şarkı" elde edilebiliyor mu?

## Kaynaklar
[Heckl (IOA)](https://www.ioa.org.uk/system/files/publications/M%20HECKL%20ACTIVE%20CONTROL%20OF%20THE%20NOISE%20OF%20A%20RIJKE%20TUBE.pdf) · [PolyU tezi](https://theses.lib.polyu.edu.hk/handle/200/1993) · [Lund tezi](https://lup.lub.lu.se/student-papers/record/8847995) · [Georgia Tech](https://nldlab.gatech.edu/w/images/5/51/Rijke_Mitchell_Passarelli.pdf) · [Radyal jetlerle bastırma](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10470196/)
