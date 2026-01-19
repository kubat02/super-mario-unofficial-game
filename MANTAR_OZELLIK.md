# 🍄 Mantar Soru Bloğu Özelliği

## ✨ Yeni Özellik: Mantarlar Soru Bloklarından Çıkıyor!

### 🎮 Nasıl Çalışır?

#### 1. **question_mushroom** - Yeni Blok Tipi
Artık level tasarımında iki tip soru bloğu var:
- `('question', x, y)` - Normal soru bloğu → **Coin verir** 💰
- `('question_mushroom', x, y)` - Özel soru bloğu → **MANTAR verir!** 🍄

#### 2. Klasik Mario Mantar Mekaniği
Mantarlar tam Mario oyunundaki gibi davranır:

**Bloktan Çıkış:**
1. Soru bloğuna alttan vurursunuz ↑
2. Mantar bloktan yukarı çıkar (spawn animasyonu)
3. Mantar blokun üstüne çıkar

**Hareket Mekanikleri:**
- ✅ **Yerçekimi etkisi**: Mantar yere düşer
- ✅ **Yatay hareket**: Mantar sağa veya sola doğru hareket eder
- ✅ **Duvar çarpması**: Duvara çarpınca yön değiştirir
- ✅ **Platform üzerinde**: Platformlarda yürür

**Yön Belirleme:**
- Mario **sağdan** vurursa → Mantar **sola** gider ⬅️
- Mario **soldan** vurursa → Mantar **sağa** gider ➡️

Bu sayede mantarı platformdan düşürmek daha zor olur!

### 🎯 Level 1 Güncellemeleri

**Mantar Konumları:**
```python
('question_mushroom', 300, 350)    # İlk mantar - hemen başta!
('question_mushroom', 1100, 350)   # İkinci mantar
('question_mushroom', 2332, 300)   # Üçüncü mantar
```

### 💡 Oyuncu İçin İpuçları

1. **İlk Mantar**: Oyunun başındaki ilk soru bloğu artık mantar veriyor! 🍄
2. **Dikkatli Vur**: Mantarın gideceği yönü düşün - platformdan düşmesin!
3. **Hızlı Yakala**: Mantar hareket ediyor, kaçırmadan topla!
4. **Yerçekimi**: Mantar yüksek yerden düşebilir, alt platformlara in

### 🔧 Teknik Detaylar

**PowerUp Sınıfı Güncellemeleri:**
```python
self.spawning = False  # Bloktan çıkış animasyonu
self.spawn_start_y = y
self.spawn_target_y = y - 32
```

**Spawn Animasyonu:**
- Mantar bloktan 2 piksel/frame hızla yukarı çıkar
- Spawn sırasında yerçekimi etki etmez
- Blokun üstüne çıkınca normal fizik başlar

**QuestionBlock Güncellemeleri:**
```python
content_type = 'coin' veya 'mushroom'
hit(player_direction)  # Mario'nun yönü
```

### 🎮 Kontrol

Hiçbir şey değişmedi! Sadece:
1. Soru bloğuna alttan vur (↑ + atlama)
2. Mantar çıkar ve hareket eder
3. Mantarı topla! 🍄

### 🏆 Sonuç

Artık tam bir Mario deneyimi! Mantarlar:
- ✅ Soru bloklarından çıkıyor
- ✅ Hareket ediyor
- ✅ Yerçekimi etkisi altında
- ✅ Duvarlara çarpıyor
- ✅ Platformlarda yürüyor
- ✅ Mario'nun vurduğu yönün tersine gidiyor

**Her soru bloğu mantar vermez!** Sadece `question_mushroom` tipleri mantar verir. 🎯
