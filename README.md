# Super Mario Bros - Python/Pygame

Klasik Super Mario'nun Python ile yaptığım versiyonu. Orijinal oyunun temel mekaniklerini uygulamaya çalıştım.

## Nasıl Oynanır

### Windows için direkt EXE
[Releases](https://github.com/kubat02/super-mario-unofficial-game/releases) kısmından SuperMario.exe'yi indir, çalıştır.

### Python ile
```bash
git clone https://github.com/kubat02/super-mario-unofficial-game.git
cd super-mario-unofficial-game
pip install pygame
python main.py
```

## Özellikler

**Koopa Kabuğu Sistemi**  
Koopa'ları ezince kabuk haline geliyorlar. Kabuğa dokunarak tekmeleyebilir ve düşmanlara çarptırabilirsin. Hareket eden kabuğa dikkat et, sana da zarar verir.

**Kombo Sistemi**  
Düşmanları art arda ezince puan artıyor: 100 → 200 → 400 → 800 → 1000+ puan

**Güç Türleri**
- Mantar: Büyük Mario
- Fire Flower: Ateş topu atabiliyorsun (SPACE)
- Yıldız: 10 saniye yenilmezlik

**Kontroller**
- Ok tuşları: Hareket ve zıplama
- SPACE: Ateş topu (Fire Flower ile)
- F: Uçma modu (test için)
- ↑ tuşunu düşman ezerken basılı tut: Ekstra yüksek zıplama

## Geliştirme

Kodda değişiklik yapmak istersen:

**Yeni level eklemek:** `levels/` klasöründe `level7.py` oluştur, `LEVEL_DATA` listesine objeleri ekle

**Düşman davranışı değiştirmek:** `enemies.py` içinde `update()` metodunu düzenle

**Oyun ayarları:** `config.py` dosyasındaki değerleri değiştir (hız, zıplama gücü vs.)

## Proje Yapısı
```
├── main.py          - Ana dosya
├── game.py          - Oyun döngüsü
├── player.py        - Mario
├── enemies.py       - Düşmanlar
├── objects.py       - Bloklar, platformlar
├── level.py         - Level yükleme
├── levels/          - Level dosyaları
└── config.py        - Ayarlar
```
