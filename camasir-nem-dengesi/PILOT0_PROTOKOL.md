# Pilot-0 Protokolü (Kapı 0) — 3 gün, elle kayıt

> Sınav haftalarından sonra, **16–18 Kasım** için. Amaç: ana plana (`PLAN.md`) para ve zaman harcamadan önce iki şeyi görmek: (1) asılı çamaşırın kütle–zaman eğrisi çıplak terazide okunabiliyor mu, (2) çamaşır odanın nemini ölçülebilir biçimde değiştiriyor mu?
> Bir kişi, bir oda yeter. Tüm sayılar aşağıda **model tahminidir (varsayımlı); eşik değildir.** Pilot-0'ın değeri önce tahmin, sonra gözlem karşılaştırmasıdır.

## Malzeme
- Dijital terazi (mutfak terazisi ≥ 5 kg kapasite, 1 g çözünürlük yeterli) + hafif plastik sepet (dara).
- Termo-higrometre (oda için; mümkünse ikincisi balkon/dış için). Fiyatı ucuzsa ikisini aynı anda yan yana koyup farkına bak (sensör ofseti).
- Aynı cins 2 büyük pamuk banyo havlusu, çamaşır makinesi, çamaşır askısı, saat/telefon kronometre.
- **Tam yük (5 kg kuru ≈ 7,6 kg ıslak) 5 kg'lık mutfak terazisini aşar;** bu yüzden pilotta yalnızca 2 havlu (≈1 kg kuru, ≈1,5 kg ıslak) kullanılır.

## Önce yap
1. Odanın boyunu×enini×yüksekliğini ölç → hacim (m³). Pencere türü, ısıtma türü (kombi/kalorifer/soba), kapı konumu not et.
2. Havluları makinede **her gün aynı programla** yıka ve aynı devirde sık (örneğin 1000 devir); sıkma biter bitmez tartıma gir (`t=0`).
3. Üç gün boyunca aynı oda, aynı ısıtma ayarı, **kapı kapalı**; deney sırasında bu odada duş/yemek/başka çamaşır olmasın (başka nem kaynağı yok).

## Üç gün
| Gün | Koşul | Ne yapılır |
|---|---|---|
| 1 | **Kontrol:** çamaşır yok, pencere kapalı | Oda sıcaklık/BN'sini aynı saatlerde (örn. 10:00–20:00) 30 dk'da bir kaydet |
| 2 | **Havlu, pencere kapalı** | Havluları askıya as; `t=0`'da ve sonra 30 dk'da bir (ilk 3 saat), sonra saatte bir tart. Her tartımda sıcaklık/BN yaz |
| 3 | **Havlu, pencere aralık (kanat yatık)** | Gün 2 ile aynı protokol; pencere aralığı sabit bırak |

**Tartım yöntemi:** Havluları askıdan alıp (dara edilmiş) sepete koy, kütleyi yaz, hemen aynı yere as. Tartım ≤ 30 sn sürsün. Havlular sabit kütleye gelene kadar (üst üste iki tartım aynı) devam et; son kütle ≈ kuru kütle (≈ %7 denge nemi içerir).

**Dışarı (balkon) nemi:** Gün başında ve her 2 saatte bir kısa bir ölçüm al (termo-higrometreyi 5 dk dışarıda bekletip oku). İstanbul'un Ocak/Şubat dış nemi için güvenilir kaynak bulamadığım için bu ölçüm gerçekten gerekli.

## Kayıt tablosu (her tartıma bir satır)
`tarih-saat | kütle (g) | oda sıcaklığı | oda BN (%) | balkon T/BN (varsa) | pencere (K/A) | kapı | ısıtma | not`

## Çözümleme (elektronik tabloda, 30 dk'lık iş)
1. Su kütlesi = kütle(t) − son kütle. Grafiği çiz: eğri önce yaklaşık doğrusal mı, sonra yavaşlıyor mu? Başlangıç hızı E₀ = −Δm/Δt (g/h).
2. Gün 2 ve Gün 3'te toplam su kaybı ≈ ıslak kütle − kuru kütle. Beklenen ~0,5 L civarı (model; RMC %52 kabulü).
3. Oda BN(t): Gün 2 ve 3'ü Gün 1 (kontrol) ile üst üste çiz. Çamaşırın etkisi = fark.
4. Model tahminiyle karşılaştır (aşağıda).

## Model tahmini (`sim_nem_dengesi.py`, İstanbul 6,8 °C, dış BN %78 varsayım, 30 m³ oda, 1–2 kg kuru havlu)
| Koşul | Tahmin edilen tepe oda BN | Tahmin edilen kuruma süresi |
|---|---|---|
| Pencere kapalı, 1 kg kuru | ~%65 → ~%79 (taban → tepe) | ~2,6 saat |
| Pencere kapalı, 2 kg kuru | ~%65 → ~%89 | ~7,8 saat |
| Pencere aralık, 2 kg kuru | tabana yakın (~%65) | ~3,7 saat |

**Uyarı:** Taban BN (%65) odanın hacmine, havalandırmasına ve diğer nem kaynaklarına çok bağlıdır; küçük odada (20 m³) modelin tabanı bile %80 çıkıyor. Bu yüzden Gün 1 (kontrol) şart ve **sayıları değil, yönü ve büyüklük mertebesini** karşılaştır.

## Kapı 0 (19 Kasım) kararı
- **Devam (#1 kesinleşir):** Kütle eğrisi temiz ve tek yönlü ve beklenen suyun yarısından fazlası tartılabiliyor; Gün 2'de oda BN'si Gün 1'e göre gözle görülür yükseliyor; Gün 3'te yükseliş belirgin biçimde küçük.
- **Duraksa/hayır:** Tartı gürültüsü eğriyi okunmaz kılıyor ya da çamaşırın BN etkisi görülmüyorsa → 22 Kasım'a kadar #2'ye geçmeyi (bitki ultrasonu) tartışın. Ana plan §11'deki zaman uyarısına bakın.
- Her iki durumda **sonucu olduğu gibi** yazın (başarısız deneme de rapora girer).

## Güvenlik ve kurallar
- Şebeke gerilimiyle uğraşılmaz; yalnızca pille çalışan terazi ve termo-higrometre kullanılır.
- Havluları askıya sallanma/düşme riski olmayacak biçimde asın; zeminin ıslanmasını önleyin.
- Raporda **sağlık iddiası yoktur**; yalnızca oda nemi, yoğuşma ve enerji ölçülür.
- Pilot-0 yalnızca kendi ve ailenizin evinde yapılır; başkasından veri alınmaz.
