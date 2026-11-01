# P12 — Ampulün Titremesi Kaydın Saatini Söyler: Şebeke Frekansıyla Video ve Ses Doğrulama

> **Tek cümle:** Şebeke frekansının (ENF) 50 Hz çevresindeki mikro dalgalanmalarını ampul ışığından ve sesten çıkarıp, kendi temassız referans kaydımızla eşleştirerek bir kaydın ne zaman çekildiğini ve kesilip kesilmediğini test etmek.
> **Aile:** Elektrik/sinyal · **Yazılım payı:** ~%85 · **Yeni harcama (tahmin):** ~0–30 USD · **Yapay zekâ:** gerekmez
> **Ayrıntı:** `fikir-havuzu-v2/DERIN_INCELEME.md` §3

## Neden ilginç
Yapay ses/görüntü çağında bağımsız fiziksel doğrulama. Türkiye Kıta Avrupası şebekesine bağlıysa (2010 deneme bağlantısı; KIT veri tabanında Türkiye bu alanda ölçüm noktası) Kağıthane'deki ampul Lizbon'dakiyle aynı ritimde titrer.

## Araştırma soruları ve hipotezler
- **H1:** Evdeki LED/ampullerin önemli kısmı ölçülebilir 100 Hz titreşim verir.
- **H2:** Video (rolling shutter) ve sesten çıkarılan ENF izi referansla eşleşir, zaman belirlenir.
- **H3:** WhatsApp/Telegram ses mesajında ENF harmonikleri sağ kalır ya da kalmaz (her iki sonuç da bulgu).

## Fizik
Alternatif akım, şebeke frekansı dinamiği (üretim–tüketim), ışık titreşimi, örnekleme ve aliasing, rolling shutter, Faraday indüksiyonu (temassız referans bobini).

## Deneyler
E1 fotodiyot + Arduino ile ampul titreşim ölçümü · E2 endüktif bobinle prize dokunmadan referans kaydı · E3 video/ses ENF çıkarımı · E4 mesajlaşma uygulaması testi · E5 KIT verisiyle yöntem doğrulaması.

## Donanım
**Yeni:** fotodiyot/op-amp, telefon toplama bobini. **Mevcut:** Arduino/ESP32, telefon, laptop. **Şebekeye doğrudan bağlantı yok.**

## Yapay zekâ gerekli mi?
Hayır.

## Öncül → kama
**Öncül:** UMD Min Wu laboratuvarı, Uludağ'dan Vatansever (rolling shutter ENF, 2019), harmonik tabanlı yöntemler, olay kameralarıyla ENF (CVPR 2023).
**Kama (bulamadım):** LED titreşiminin evlerde ölçümü + mesajlaşma uygulamalarında ENF'nin sağ kalması + Türkiye referansı.

## Etkileyici gösteri
Jüri önünde çekilen videonun dakikasını ampul titremesinden bulmak.

## Riskler
**LED titreşimi zayıf olabilir** (doğrudan test eden çalışma bulamadım) → E1 karar deneyi. Telefon videosunda gürültü ve aliasing.

## İlk pilot (sıfır maliyet)
Telefonun ağır çekim videosuyla 5 ampulü çek; parlaklıkta 100 Hz titreşim var mı?

## Kaynaklar
[KIT veri tabanı](https://arxiv.org/abs/2006.01771) · [Türkiye–Avrupa bağlantısı 2010](https://www.renewableenergyworld.com/power-grid/turkish-power-system-connected-with-european-grid/) · [Vatansever (Uludağ)](https://acikerisim.uludag.edu.tr/items/13b7142f-9d7b-4b16-9668-1003ca016515) · [Olaylardan ENF](https://arxiv.org/pdf/2305.02597) · [Ses iletişiminde ENF (Sensors 2025)](https://www.mdpi.com/1424-8220/25/12/3697)
