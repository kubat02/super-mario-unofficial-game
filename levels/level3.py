"""
Level 3 tasarımı
Yapay zekaya bu seviyeyi oluşturmasını söyleyebilirsiniz
"""

# Obje tipleri ve parametreleri:
# - 'platform': (x, y, genişlik, yükseklik)
# - 'question': (x, y) - soru bloğu
# - 'brick': (x, y) - tuğla
# - 'pipe': (x, y, yükseklik)
# - 'goomba': (x, y) - düşman
# - 'koopa': (x, y) - kaplumbağa düşman
# - 'coin': (x, y) - altın


LEVEL_DATA = [
    # Başlangıç - Power-up test
    ('platform', 300, 500, 300, 32),
    ('mushroom', 350, 450),  # Super Mushroom - büyük Mario
    ('goomba_stationary', 450, 464),
    ('goomba', 520, 464),
    
    # Fire Flower test
    ('platform', 700, 400, 200, 32),
    ('fireflower', 750, 350),  # Fire Flower - SPACE ile ateş at!
    ('koopa_stationary', 800, 364),
    ('koopa_stationary', 850, 364),
    ('coin', 825, 330),
    
    # Star test
    ('platform', 1000, 480, 250, 32),
    ('star', 1100, 430),  # Yıldız - 10 saniye yenilmezlik
    ('goomba', 1050, 444),  # Normal goomba
    ('goomba_stationary', 1120, 444),  # Yerinde duran
    ('koopa', 1190, 444),  # Normal koopa
    ('coin', 1100, 410),
    ('coin', 1150, 410),
    
    # Boru ve düşmanlar
    ('pipe', 1400, 490, 70),
    ('goomba_stationary', 1500, 524),
    ('question', 1550, 400),
    
    # Platform atlama bölümü
    ('platform', 1700, 480, 100, 32),
    ('platform', 1850, 420, 100, 32),
    ('platform', 2000, 360, 100, 32),
    ('koopa_stationary', 1730, 444),
    ('goomba', 1880, 384),
    ('koopa_stationary', 2030, 324),
    ('coin', 1760, 430),
    ('coin', 1910, 370),
    ('coin', 2060, 310),
    
    # Tuğla bloklar ve yerinde düşmanlar
    ('brick', 2200, 500),
    ('brick', 2232, 500),
    ('brick', 2264, 500),
    ('brick', 2232, 468),
    ('question', 2232, 436),
    ('goomba_stationary', 2216, 464),
    
    # Yüksek platform challenge
    ('platform', 2450, 350, 180, 32),
    ('goomba_stationary', 2480, 314),
    ('goomba_stationary', 2530, 314),
    ('koopa', 2580, 314),
    ('coin', 2500, 280),
    ('coin', 2540, 280),
    ('coin', 2580, 280),
    
    # Boru ormanı
    ('pipe', 2750, 490, 70),
    ('pipe', 2900, 460, 100),
    ('pipe', 3050, 430, 130),
    ('goomba', 2820, 524),
    ('goomba_stationary', 2970, 524),
    ('koopa_stationary', 3120, 524),
    
    # Platform serisi
    ('platform', 3300, 480, 80, 32),
    ('platform', 3450, 420, 80, 32),
    ('platform', 3600, 360, 80, 32),
    ('platform', 3750, 420, 80, 32),
    ('goomba_stationary', 3330, 444),
    ('koopa', 3480, 384),
    ('goomba_stationary', 3630, 324),
    ('koopa_stationary', 3780, 384),
    ('coin', 3360, 410),
    ('coin', 3510, 350),
    ('coin', 3660, 290),
    ('coin', 3810, 350),
    
    # Soru blokları
    ('question', 3950, 400),
    ('question', 3982, 350),
    ('question', 4014, 300),
    ('question', 4046, 350),
    ('question', 4078, 400),
    ('goomba', 4000, 524),
    
    # Son platform challenge
    ('platform', 4250, 500, 120, 32),
    ('platform', 4420, 450, 120, 32),
    ('platform', 4590, 400, 120, 32),
    ('goomba_stationary', 4280, 464),
    ('koopa_stationary', 4290, 464),
    ('goomba', 4450, 414),
    ('koopa', 4620, 364),
    
    # Final bölgesi
    ('brick', 4800, 500),
    ('brick', 4832, 500),
    ('brick', 4864, 500),
    ('brick', 4832, 468),
    ('question', 4832, 436),
    
    ('platform', 4950, 480, 250, 32),
    ('goomba_stationary', 5000, 444),
    ('goomba', 5050, 444),
    ('koopa_stationary', 5100, 444),
    ('koopa', 5150, 444),
    ('coin', 5020, 410),
    ('coin', 5070, 410),
    ('coin', 5120, 410),
    ('coin', 5170, 410),
    
    # Son tuğla grubu
    ('brick', 5300, 500),
    ('brick', 5332, 468),
    ('brick', 5364, 436),
    ('brick', 5396, 404),
]
