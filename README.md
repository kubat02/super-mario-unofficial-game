# 🍄 Super Mario Bros - Python Edition

Klasik Super Mario Bros oyununun Python/Pygame ile yapılmış versiyonu.

## 🎮 Hemen Oyna!

### 💾 Windows İçin (Python Gerektirmez)

1. **[Releases](https://github.com/kubat02/super-mario-unofficial-game/releases)** sayfasına git
2. En son **SuperMario.exe** dosyasını indir
3. Çift tıkla ve oyna! 🎮

### 🐍 Python ile Çalıştırma

```bash
# Repository'yi klonla
git clone https://github.com/kubat02/super-mario-unofficial-game.git
cd super-mario-unofficial-game

# Bağımlılıkları yükle
pip install pygame

# Oyunu başlat
python main.py
```

## ⭐ Özellikler

### 🐢 Koopa Kabuğu Mekaniği
- Koopa'yı ezince kabuk haline gelir
- Kabuğa dokunarak tekmeleyip fırlatabilirsin
- Kabuk düşmanları öldürür - SÜPER KOMBO!
- Hareket eden kabuğa dikkat - can kaybedersin!

### 🔥 Kombo Sistemi
Art arda düşman ezince puan katlanıyor:
- 1. düşman: **100 puan**
- 2. düşman: **200 puan**
- 3. düşman: **400 puan**
- 8. düşman: **8000 puan!** 💰

### 💪 Güç Sistemleri
- **Super Mushroom** 🍄 - Büyük Mario
- **Fire Flower** 🌸 - Ateş topu at (SPACE tuşu)
- **Star** ⭐ - 10 saniye yenilmezlik

### 🎯 Kontroller
- **←/→**: Hareket
- **↑**: Zıplama (düşman üstünde basılı tut = süper zıplama!)
- **SPACE**: Özel güç (Fire Flower ile ateş topu)
- **F**: Uçma modu (Developer)

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
