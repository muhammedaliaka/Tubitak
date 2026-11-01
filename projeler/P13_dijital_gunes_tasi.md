# P13 — Dijital Güneş Taşı: Güneş Bulutun Arkasındayken Gökyüzü Polarizasyonuyla Yön Bulmak

> **Tek cümle:** Rayleigh saçılmasının gökyüzünde oluşturduğu polarizasyon desenini telefon + polarizörle ölçüp güneş görünmezken yönü bulmak ve doğruluğu Viking güneş taşı (kalsit) ve insan gözüyle karşılaştırmak.
> **Aile:** Optik · **Yazılım payı:** ~%60 · **Yeni harcama (tahmin):** ~10–50 USD · **Yapay zekâ:** gerekmez (karşılaştırma isteğe bağlı)
> **Ayrıntı:** `fikir-havuzu-v2/DERIN_INCELEME.md` §4

## Neden ilginç
Manyetik pusula şehirde bozulur, GNSS parazitlenebilir; gökyüzü bedava bir referanstır. Viking hikâyesi güçlü.

## Araştırma soruları ve hipotezler
- **H1:** Telefon + polarizörle açık gökte güneş azimutu belirli bir hata sınırında bulunur.
- **H2:** Hata bulutlulukla artar; artış İstanbul kış koşullarında ölçülür.
- **H3:** Dijital yöntem kalsit güneş taşı + insan gözünden daha doğrudur (ya da değildir).

## Fizik
Rayleigh saçılması, Stokes parametreleri, polarizasyon derecesi/açısı, çift kırılma (kalsit), güneş efemerisi.

## Deneyler
E1 polarizör açısına göre cos² yasası · E2 açık gökte azimut kestirimi vs efemeris · E3 bulutluluk sınıfına göre hata · E4 kalsitle insan gözü ölçümü · E5 fizik modeli vs ML karşılaştırması.

## Donanım
**Yeni:** polarizör film, kalsit (İzlanda spatı), isteğe bağlı servo. **Mevcut:** telefon, Arduino, ekran, laptop.

## Yapay zekâ gerekli mi?
Hayır; bulutlu gökte fizik modeli yetmezse ML (Evren) denenir.

## Öncül → kama
**Öncül:** Horváth grubu (ELTE): açık gökte ≤ 3° net hata; kapalı gökte kalsit ~6°, kordiyerit ~10°, turmalin ~17° (2016); 1.080 gökyüzü durumu modeli (2017); Aix-Marseille ~30 € kameralı yön sensörü; Heriot-Watt fotodiyot halkası; Photonics 2024 (±2°).
**Kama (zayıf-orta):** İstanbul kış bulutunda telefon + kalsit + göz karşılaştırması.

## Etkileyici gösteri
Güneş görünmezken telefonun kuzeyi göstermesi; Viking taşıyla canlı karşılaştırma.

## Savunma anlatısı
GNSS'siz ve manyetiksiz yön bulma.

## Riskler
**Kasım–Aralık İstanbul'da bulut ve yağmur** → ölçüm günü azlığı. Kentsel yansımalar.

## İlk pilot (sıfır maliyet)
Polarize güneş gözlüğüyle gökyüzünün 3 açıda fotoğrafı; parlaklık açıyla değişiyor mu?

## Kaynaklar
[Royal Society Open Science 2016](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4736922/) · [ELTE Viking sentezi](https://arago.elte.hu/sites/default/files/VikingSynthesis_ProcA.pdf) · [Aix-Marseille](https://ism.univ-amu.fr/doc/hal-04521170/_1) · [Heriot-Watt](https://researchportal.hw.ac.uk/en/publications/celestial-compass-sensor-mimics-the-insect-eye-for-navigation-und/) · [Photonics 2024](https://doaj.org/article/0ab7060b95fa45a985212577dfd2ba26)
