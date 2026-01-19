"""
Level 2 - World 1-2: Yeraltı Mağarası (Underground)
Karanlık yeraltı tünelleri - alçak tavanlar ve sıkışık geçitler
"""

# Level teması
LEVEL_THEME = 'underground'  # Yeraltı teması

# Obje tipleri ve parametreleri:
# - 'platform': (x, y, genişlik, yükseklik)
# - 'question': (x, y) - soru bloğu
# - 'brick': (x, y) - tuğla
# - 'pipe': (x, y, yükseklik)
# - 'goomba': (x, y) - düşman
# - 'koopa': (x, y) - kaplumbağa düşman
# - 'coin': (x, y) - altın


LEVEL_DATA = [
    # Başlangıç alanı
    ('coin', 200, 450),
    ('coin', 250, 400),
    ('coin', 300, 350),
    
    # İlk engel grubu
    ('pipe', 400, 490, 70),
    ('goomba', 550, 524),
    ('question', 600, 350),
    ('brick', 632, 350),
    ('brick', 664, 350),
    
    # Platform atlama bölümü
    ('platform', 800, 480, 100, 32),
    ('platform', 950, 420, 100, 32),
    ('platform', 1100, 360, 100, 32),
    ('coin', 830, 430),
    ('coin', 980, 370),
    ('coin', 1130, 310),
    ('koopa', 1110, 324),
    
    # Soru blokları bölgesi
    ('question', 1300, 400),
    ('question', 1332, 350),
    ('question', 1364, 300),
    ('question', 1396, 350),
    ('question', 1428, 400),
    
    # Boru ve düşman grubu
    ('pipe', 1600, 460, 100),
    ('goomba', 1750, 524),
    ('goomba', 1800, 524),
    ('koopa', 1900, 524),
    
    # Yüksek platform challenge
    ('platform', 2100, 350, 150, 32),
    ('brick', 2120, 250),
    ('brick', 2152, 250),
    ('brick', 2184, 250),
    ('coin', 2136, 200),
    ('coin', 2168, 200),
    ('goomba', 2130, 314),
    
    # Tuğla merdiven
    ('brick', 2400, 500),
    ('brick', 2432, 468),
    ('brick', 2464, 436),
    ('brick', 2496, 404),
    ('brick', 2528, 372),
    ('question', 2528, 340),
    
    # Platform serisi
    ('platform', 2700, 480, 80, 32),
    ('platform', 2850, 420, 80, 32),
    ('platform', 3000, 360, 80, 32),
    ('platform', 3150, 420, 80, 32),
    ('platform', 3300, 480, 80, 32),
    ('coin', 2730, 430),
    ('coin', 2880, 370),
    ('coin', 3030, 310),
    ('coin', 3180, 370),
    ('coin', 3330, 430),
    
    # Boru ormanı
    ('pipe', 3500, 490, 70),
    ('pipe', 3650, 460, 100),
    ('pipe', 3800, 430, 130),
    ('pipe', 3950, 460, 100),
    ('pipe', 4100, 490, 70),
    ('goomba', 3720, 524),
    ('koopa', 3870, 524),
    ('goomba', 4020, 524),
    
    # Soru bloğu duvarı
    ('question', 4300, 450),
    ('question', 4332, 450),
    ('question', 4364, 450),
    ('question', 4300, 350),
    ('question', 4332, 350),
    ('question', 4364, 350),
    ('coin', 4316, 380),
    ('coin', 4348, 380),
    
    # Son platform challenge
    ('platform', 4550, 500, 100, 32),
    ('platform', 4700, 450, 100, 32),
    ('platform', 4850, 400, 100, 32),
    ('platform', 5000, 350, 100, 32),
    ('koopa', 4710, 414),
    ('goomba', 4860, 364),
    ('koopa', 5010, 314),
    
    # Final bölgesi
    ('brick', 5200, 500),
    ('brick', 5232, 500),
    ('brick', 5264, 500),
    ('brick', 5232, 468),
    ('question', 5232, 436),
    
    ('platform', 5400, 480, 200, 32),
    ('goomba', 5450, 444),
    ('goomba', 5500, 444),
    ('coin', 5470, 410),
    ('coin', 5500, 410),
    ('coin', 5530, 410),
]
