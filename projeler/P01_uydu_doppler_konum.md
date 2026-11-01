# P01 — Sputnik'ten TRANSIT'e: Uydu Doppler Kaymasıyla Kağıthane'den GNSS'siz Konum Bulma

> **Tek cümle:** Alçak yörünge uydusunun radyo sinyalindeki Doppler kaymasını ucuz bir SDR ile ölçüp, önce bilinen konumdan yörüngeyi düzeltmek (Sputnik 1957), sonra yörüngeyi bilerek kendi konumumuzu bulmak (TRANSIT 1958).
> **Aile:** Radyo/SDR · **Yazılım payı:** ~%75 · **Yeni harcama (tahmin, doğrulanmadı):** ~60–100 USD · **Yapay zekâ:** gerekmez
> **Ayrıntı:** `fikir-havuzu-v2/DERIN_INCELEME.md` §1 ve `fikir-havuzu-v2/doppler_konum_sim.py`

## Neden ilginç
GNSS parazitlenince ya da aldatılınca konum kaybolur. Uydu Doppler'i bağımsız ikinci bir konum kaynağıdır. Hikâyesi güçlü: ilk uydu navigasyon sistemi TRANSIT tam olarak bu fikirden doğdu (APL Technical Digest).

## Araştırma soruları ve hipotezler
- **H1:** RTL-SDR + tel dipol ile Kağıthane'den alçak yörünge uydusunun Doppler eğrisi konum için yeterli doğrulukla ölçülebilir (eşik pilot sonrası).
- **H2 (Sputnik yönü):** Bilinen konumdan ölçülen eğri, TLE yörüngesinin yörünge boyu zamanlama hatasını düzeltir.
- **H3 (TRANSIT yönü):** Konum tek geçişte km, çok geçişte yüzlerce m mertebesinde bulunur.
- **H4:** Alıcı osilatör kayması bilinirse tek geçişteki büyük hatalar belirgin azalır.

## Fizik
Doppler olayı (Δf = −(f₀/c)·dρ/dt), kütle çekimi ve çembersel hareket (v = √(GM/r)), Dünya'nın dönmesi, kristal osilatörün sıcaklık kayması, en küçük kareler ve hata yayılımı.

## Deneyler
E1 ilk geçiş kaydı ve Doppler eğrisi · E2 bilinen konumla yörünge düzeltme · E3 konum kestirimi (telefon GNSS'i referans) · E4 osilatör kaymasının etkisi (sıcaklık, kalibrasyon) · E5 farklı uydu sinyallerinin karşılaştırması.

## Benzetim kanıtı (sentetik)
1 Hz frekans gürültüsünde medyan / P90 hata: tek geçiş 190 m / 3,4 km; kayma biliniyorsa 107 m / 0,46 km; 3 geçiş + 1 km TLE hatası ~0,7 / 1,4 km. Yayımlanmış Orbcomm sonuçlarıyla (782–1.687 m) aynı mertebe.

## Donanım
**Yeni:** RTL-SDR V4 + dipol seti, FM bant durdurucu filtre (İstanbul'daki güçlü FM yayınları için). **Mevcut:** laptop, Arduino/ESP32 (sıcaklık kaydı).

## Yapay zekâ gerekli mi?
Hayır. FFT ile frekans kestirimi ve doğrusal olmayan en küçük kareler yeterli.

## Öncül → kama
**Öncül:** RTL-SDR + dipolle Orbcomm Doppler konumlama içeren patent başvurusu; Orbcomm 2B hata 1.687 m → 782 m (NSF); çok takımyıldızlı ~132 m (Sensors 2020); iki uydulu doğruluk analizi (arXiv 2026).
**Kama (bulamadım):** Sputnik + TRANSIT iki yönü tek ucuz kurulumda, hata bütçesinin deneyle ayrıştırılması, ucuz uydu sinyallerinin kıyası, İstanbul'dan açık veri.

## Etkileyici gösteri
Uydu geçerken hoparlörde yükselip alçalan ıslık; ekranda her saniye daralan konum elipsi; sonunda harita üzerinde Kağıthane.

## Savunma anlatısı
GNSS'siz konum (TRANSIT bir donanma sistemiydi).

## Riskler
2026'da hangi uyduların yayın yaptığı doğrulanamadı (NOAA-19 için kaynaklar çelişkili; Orbcomm OG2 durumu bulunamadı) → pilotun ilk işi. FM girişimi, kentsel ufuk, modülasyonlu sinyalde taşıyıcı kestirimi.

## İlk pilot (sınav sonrası, 2 gün)
İki geçiş kaydet, spektrogramda Doppler eğrisini çiz, frekans gürültüsünü ölç (1–10 Hz civarı → uygulanabilir).

## Kaynaklar
[APL – Guier](https://secwww.jhuapl.edu/techdigest/Content/techdigest/pdf/V02-N01/02-01-Guier.pdf) · [Orbcomm patent](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11960018) · [NSF yayını](https://par.nsf.gov/servlets/purl/10413009) · [arXiv 2026](https://arxiv.org/pdf/2607.10241) · [rtl-sdr.com Orbcomm](https://www.rtl-sdr.com/tag/orbcomm/) · [WMO NOAA-19](https://space.oscar.wmo.int/satellites/view/noaa_19)
