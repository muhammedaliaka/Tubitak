# P15 — Karadeniz Fırtınasını Kağıthane'den Duymak: Sismik Gürültüden Dalga Yüksekliği Tahmini

> **Tek cümle:** Kandilli'nin açık sismometre kayıtlarındaki mikrosismik gürültünün (0,1–0,5 Hz) şiddetinden Karadeniz/Marmara dalga yüksekliğini fizik modeliyle tahmin etmek ve dalga modeli verisiyle doğrulamak.
> **Aile:** Jeofizik/veri · **Yazılım payı:** ~%95 · **Yeni harcama:** 0 · **Yapay zekâ:** araştırma sorusunun parçası (fizik vs ML)

## Neden ilginç
Yer, denizdeki fırtınayı "duyar". Şamandıra olmayan yerlerde deniz durumunu sismometreden kestirmek.

## Araştırma soruları ve hipotezler
- **H1:** İstanbul ve Karadeniz kıyısı istasyonlarında ikincil mikrosismik tepe (dalga frekansının iki katı) dalga yüksekliğiyle korelasyon gösterir.
- **H2:** Kıyıya yakın istasyonlar daha fazla deniz durumu bilgisi taşır.
- **H3:** Fizik tabanlı regresyon, rastgele ormana (Remote Sensing 2020'de kullanılan yöntem) yakın sonuç verir; ML gerekli olmayabilir.

## Fizik
Okyanus dalgası dağılımı, Longuet-Higgins çift frekans mekanizması (karşıt dalgalar), Rayleigh yüzey dalgaları, spektral analiz, uzaklıkla sönüm.

## Analizler
A1 istasyon PSD ve tepe frekansları · A2 dalga verisiyle (model) korelasyon · A3 fizik regresyonu vs ML · A4 fırtına vaka çalışmaları · A5 kentsel gürültü (gündüz/gece) etkisi.

## Veri
**Doğrulanmadı:** Kandilli (KOERI) istasyon verilerine FDSN/EIDA üzerinden erişim; Karadeniz dalga modeli (ör. Copernicus Marine, kayıt gerekebilir). Pilotun ilk işi erişimi doğrulamak.

## Donanım
Gerekmez (laptop). İsteğe bağlı ucuz sensör bu frekanslarda yetersiz kalır.

## Yapay zekâ gerekli mi?
Fizik önce; ML yalnızca kazanç sağlarsa (H3).

## Öncül → kama
**Öncül:** Doğu Türkiye sismik ağıyla ikincil mikrosismik P dalgası çalışması; Remote Sensing 2020 (rastgele orman ile dalga yüksekliği); Doğu Sicilya istasyonlarıyla ~0,14–0,18 m hata; Kuzey Pasifik/Avrupa'da mikrosismik–dalga ilişkisinin sınırları.
**Kama (bulamadım):** Karadeniz + KOERI istasyonlarıyla dalga yüksekliği kestirimi.

## Etkileyici gösteri
Fırtına haritası ile Kağıthane'ye yakın sismometrenin spektrogramının aynı anda "kabarması".

## Savunma / kritik altyapı anlatısı
Deniz durumsal farkındalığı, kıyı tehlikeleri.

## Riskler
Veri erişimi; Karadeniz kapalı deniz (daha küçük dalgalar) ve kaynak karışıklığı (Akdeniz/Atlantik); fiziksel ürün payı düşük (tamamen yazılım).

## İlk pilot (sıfır maliyet)
Bir istasyonun bir haftalık verisini indirip spektrogram çiz; 0,1–0,5 Hz bandı fırtına günleriyle değişiyor mu?

## Kaynaklar
[Remote Sensing 2020](https://doaj.org/article/1908b34527184ce895261e138764aed9) · [Doğu Türkiye mikrosismik (HAL)](https://hal-insu.archives-ouvertes.fr/insu-00565200) · [Sicilya çalışması](https://www.iris.unict.it/handle/20.500.11769/418785) · [Kuzey Pasifik/Avrupa](https://eprints.soton.ac.uk/406178/2/2016JC012183.pdf)
