"""
Level 1 - World 1-1: Bahçeli Klasik Alan (Overworld)
Mario'nun başlangıç macerası - yeşil tepeler, borular ve güneşli gökyüzü
"""

# Level teması
LEVEL_THEME = 'overworld'  # Klasik bahçe teması

# Obje tipleri ve parametreleri:
# - 'platform': (x, y, genişlik, yükseklik)
# - 'question': (x, y) - soru bloğu (coin verir)
# - 'question_mushroom': (x, y) - soru bloğu (MANTAR verir! Mantar çıkınca hareket eder!)
# - 'brick': (x, y) - tuğla
# - 'pipe': (x, y, yükseklik)
# - 'goomba': (x, y) - normal düşman (hareket eder)
# - 'goomba_stationary': (x, y) - yerinde duran düşman (sağ-sol sallanır)
# - 'koopa': (x, y) - kaplumbağa düşman (hareket eder)
# - 'koopa_stationary': (x, y) - yerinde duran kaplumbağa (sağ-sol sallanır)
# - 'coin': (x, y) - altın
# - 'mushroom': (x, y) - Super Mushroom (büyük Mario) - doğrudan yerleştirilmiş
# - 'fireflower': (x, y) - Fire Flower (ateş Mario, SPACE ile ateş topu at!)
# - 'star': (x, y) - Yıldız (10 saniye yenilmezlik)
#
# YENİ ÖZELLİKLER:
# 1. ↑ TUŞU: Zıplama + Düşman ezdiğinizde basılı tutarsanız daha yüksek zıplarsınız!
# 2. SPACE TUŞU: Özel güç kullan (Fire Flower ile ateş topu at!)
# 3. 'goomba_stationary' ve 'koopa_stationary' yerinde sağ-sol sallanan düşmanlar!
# 4. 'question_mushroom': Soru bloğundan MANTAR çıkar! Mantar yerçekimi etkisiyle yere düşer ve hareket eder!


LEVEL_DATA = [
    # Başlangıç - ilk mantar!
    ('question_mushroom', 300, 350),  # İlk mantar burada!
    ('question', 332, 350),
    ('question', 364, 350),
    ('brick', 332, 250),
    ('pipe', 450, 490, 70),
    ('goomba', 600, 524),
    ('goomba', 700, 524),
    
    # Platform bölümü
    ('platform', 900, 500, 160, 32),
    ('coin', 920, 450),
    ('coin', 950, 450),
    ('coin', 980, 450),
    ('coin', 1010, 450),
    
    ('question_mushroom', 1100, 350),  # Mantar burada!
    ('brick', 1132, 350),
    ('question', 1164, 350),
    ('brick', 1132, 250),
    ('koopa', 1300, 524),
    ('pipe', 1450, 460, 100),
    
    # Merdiven platformlar
    ('brick', 1650, 500),
    ('brick', 1682, 500),
    ('brick', 1750, 450),
    ('brick', 1782, 450),
    ('brick', 1850, 400),
    ('brick', 1882, 400),
    
    # Yüksek platform
    ('platform', 2000, 350, 200, 32),
    ('goomba', 2050, 314),
    ('goomba', 2150, 314),
    ('coin', 2070, 280),
    ('coin', 2100, 280),
    ('coin', 2130, 280),
    
    # Soru blokları
    ('question', 2300, 350),
    ('question_mushroom', 2332, 300),  # Mantar!
    ('question', 2364, 250),
    ('question', 2396, 300),
    ('question', 2428, 350),
    
    ('pipe', 2550, 490, 70),
    ('koopa', 2700, 524),
    
    # Platform atlama
    ('platform', 2850, 480, 100, 32),
    ('platform', 3000, 420, 100, 32),
    ('platform', 3150, 360, 100, 32),
    ('coin', 2880, 430),
    ('coin', 3030, 370),
    ('coin', 3180, 310),
    
    # Tuğla duvar
    ('brick', 3350, 500),
    ('brick', 3382, 500),
    ('brick', 3414, 500),
    ('brick', 3350, 468),
    ('brick', 3382, 468),
    ('brick', 3414, 468),
    ('brick', 3382, 436),
    ('question', 3382, 404),
    
    # Düşman grubu
    ('goomba', 3550, 524),
    ('goomba', 3600, 524),
    ('koopa', 3700, 524),
    ('pipe', 3850, 410, 150),
    
    # Son platformlar
    ('platform', 4050, 500, 80, 32),
    ('platform', 4180, 450, 80, 32),
    ('platform', 4310, 400, 80, 32),
    ('platform', 4440, 350, 80, 32),
    ('goomba', 4060, 464),
    ('koopa', 4320, 364),
    
    ('question', 4600, 350),
    ('question', 4632, 350),
    ('question', 4664, 350),
    ('coin', 4616, 280),
    ('coin', 4648, 280),
    
    ('pipe', 4800, 460, 100),
    
    # Final
    ('platform', 4950, 500, 400, 32),
    ('goomba', 5000, 464),
    ('goomba', 5100, 464),
    ('goomba', 5200, 464),
    ('coin', 5050, 430),
    ('coin', 5100, 400),
    ('coin', 5150, 400),
    ('coin', 5200, 430),
    
    ('brick', 5400, 500),
    ('brick', 5432, 468),
    ('brick', 5464, 436),
    ('brick', 5496, 404),
]
