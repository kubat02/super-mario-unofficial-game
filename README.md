# Super Mario Bros - Python Edition

Klasik Super Mario Bros oyununun Python/Pygame ile yapılmış versiyonu.

## 📁 Proje Yapısı

```
├── main.py           # Ana giriş noktası
├── game.py           # Oyun döngüsü ve ana mantık
├── player.py         # Mario karakteri
├── enemies.py        # Düşman karakterleri (Goomba, Koopa)
├── objects.py        # Platformlar, bloklar, coinler
├── level.py          # Level yapısı ve builder
├── camera.py         # Kamera sistemi
├── renderer.py       # Çizim fonksiyonları
└── config.py         # Sabitler ve ayarlar
```

## 🎮 Nasıl Çalıştırılır

```bash
python main.py
```

## 🛠️ Geliştirme

### Yeni Düşman Eklemek

`enemies.py` dosyasında yeni bir class oluştur:

```python
class YeniDusman(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, 'yeni_dusman')
```

`renderer.py`'de çizim fonksiyonu ekle:

```python
def draw_yeni_dusman(surface, x, y, frame):
    # Çizim kodu
    pass
```

### Yeni Level Eklemek

`level.py` dosyasında yeni bir method oluştur:

```python
def build_level_2(self):
    # Level verisi
    level_data = [
        ('platform', 100, 400, 200, 32),
        # ... daha fazla obje
    ]
    
    for obj in level_data:
        self._create_object(obj)
```

### Yeni Obje Tipi Eklemek

1. `objects.py`'de yeni class oluştur
2. `level.py`'de `_create_object()` methoduna ekle
3. `renderer.py`'de çizim fonksiyonu ekle (gerekiyorsa)

### Ayarları Değiştirmek

`config.py` dosyasındaki sabitleri değiştir:

```python
PLAYER_SPEED = 7  # Daha hızlı hareket
JUMP_STRENGTH = -20  # Daha yüksek zıplama
GRAVITY = 1.0  # Daha güçlü yerçekimi
```

## 📝 Obje Tipleri

Level'de kullanılabilecek objeler:

- `platform` - Platform (x, y, width, height)
- `question` - Soru bloğu (x, y)
- `brick` - Tuğla (x, y)
- `pipe` - Boru (x, y, height)
- `goomba` - Goomba düşmanı (x, y)
- `koopa` - Koopa düşmanı (x, y)
- `coin` - Altın (x, y)

## 🎯 Özellikler

- ✅ Modüler yapı
- ✅ Kolay genişletilebilir
- ✅ Temiz kod organizasyonu
- ✅ Yorum satırları
- ✅ Class-based tasarım
- ✅ Ayrılmış dosya yapısı

## 🚀 Gelecek Geliştirmeler İçin Fikirler

- Powerup sistemi (mantar, ateş çiçeği)
- Ses efektleri ve müzik
- Çoklu level sistemi
- Kaydetme/yükleme
- Boss savaşları
- Yeni düşman tipleri
- Özel bloklar ve etkiler
