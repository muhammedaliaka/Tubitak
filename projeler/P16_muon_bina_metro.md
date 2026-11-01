# P16 — Müonlarla Binanın ve Metronun İçini Görmek: Kağıthane'de Kozmik Işın Radyografisi

> **Tek cümle:** İki ucuz sintilatör + SiPM müon dedektörüyle apartman katlarında ve Kağıthane'de yeraltındaki M11 istasyonu ile viyadükteki M7 istasyonunda müon sayım hızını ölçüp, üstteki malzeme kalınlığını (beton/toprak) kestirmek.
> **Aile:** Parçacık fiziği · **Yazılım payı:** ~%55 · **Yeni harcama (tahmin, doğrulanmadı):** ~200–400 USD · **Yapay zekâ:** gerekmez

## Neden ilginç
Kozmik ışınlarla bir yapının içini "görmek"; görelilik (müonların yere ulaşması zaman genleşmesiyle açıklanır) lise fiziğinde.

## Araştırma soruları ve hipotezler
- **H1:** Müon hızı kat sayısı arttıkça (üstteki beton) azalır; azalma modelle uyumludur.
- **H2:** Açısal dağılım ~cos²θ'ya uyar.
- **H3:** Yeraltı (M11) ve yerüstü (M7) istasyon farkından üst örtü kalınlığı kestirilir.

## Fizik
Kozmik ışın sağanakları, müon ömrü ve zaman genleşmesi, maddede enerji kaybı, cos²θ, su eşdeğeri derinlik.

## Deneyler
E1 dedektör yapımı ve çakışma (coincidence) kalibrasyonu · E2 apartman katlarına göre hız · E3 açı taraması · E4 metro istasyonları (**izin şart**) · E5 basit model/Geant4 karşılaştırması.

## Donanım
**Yeni:** plastik sintilatör blokları, SiPM'ler, CosmicWatch tarzı PCB (yurtdışından üretim), lehimleme (SMD). **Mevcut:** Arduino, laptop.

## Yapay zekâ gerekli mi?
Hayır.

## Öncül → kama
**Öncül:** CosmicWatch (MIT, "Desktop Muon Detector"); Japonya'da bir lise 1–5. katlarda ölçüm; İtalya'da bir lise kat ölçümü; Boston metrosunda derinlik; 21 noktalı metro müon radyografisi (arXiv 2303.09819).
**Kama (zayıf):** İstanbul'da aynı semtte yeraltı/viyadük istasyon karşılaştırması; bina kat kalınlığı kestirimi.

## Etkileyici gösteri
Her kat inildikçe azalan "uzaydan gelen tıkırtılar".

## Savunma anlatısı
Müon tomografisi ile kargo/konteyner ve tünel/boşluk denetimi (genel bilgi, doğrulanmadı).

## Riskler
**En yüksek takvim riski:** parça temini 2–4 hafta (tahmin), SMD lehim, düşük sayım istatistiği (nokta başına saatler), metro izni ve güvenlik.

## İlk pilot
Donanım gelmeden yapılamaz. Bu yüzden sınav haftasında sipariş kararı gerekir.

## Kaynaklar
[Desktop Muon Detector (arXiv 1606.01196)](https://arxiv.org/pdf/1606.01196) · [Metro müon radyografisi](https://arxiv.org/pdf/2303.09819) · [Japon lise çalışması (JpGU 2021)](https://pub-files.atlas.jp/fs/public/jpgu2021/ver_2/abstract/en/O07-P46.pdf) · [İtalyan lise sunumu](https://agenda.centrofermi.it/event/343/contributions/2248/attachments/1013/1535/EEE_presentazione_27-05_definitiva.pdf)
