"""
Level 4 - World 1-4: Lav Mağarası (Underground with Lava)
Tehlikeli yeraltı mağarası - sıcak lav ve ateş
"""

# Level teması
LEVEL_THEME = 'castle'  # Karanlık kale/mağara teması

LEVEL_DATA = [
    # Başlangıç - dikkatli ilerleme
    ('platform', 250, 500, 100, 32),
    ('platform', 400, 480, 100, 32),
    ('goomba', 410, 444),
    
    # Tuğla engellerle atlama
    ('brick', 600, 450),
    ('brick', 632, 450),
    ('brick', 664, 450),
    ('brick', 632, 400),
    ('question', 632, 350),
    
    ('platform', 800, 500, 120, 32),
    ('koopa_stationary', 840, 464),
    ('coin', 850, 430),
    
    # Dar geçit
    ('brick', 1000, 350),
    ('brick', 1032, 350),
    ('brick', 1064, 350),
    ('brick', 1096, 350),
    ('brick', 1128, 350),
    ('brick', 1160, 350),
    ('platform', 1050, 500, 80, 32),
    ('goomba', 1060, 464),
    
    # Lav üzerinde platformlar
    ('platform', 1300, 480, 80, 32),
    ('platform', 1450, 450, 80, 32),
    ('platform', 1600, 420, 80, 32),
    ('platform', 1750, 450, 80, 32),
    ('koopa', 1310, 444),
    ('goomba', 1610, 384),
    
    # Soru blokları
    ('question', 2100, 400),
    ('question', 2132, 350),
    ('fireflower', 2132, 320),
    
    # Zorlu platform atlama
    ('platform', 2350, 500, 70, 32),
    ('platform', 2500, 450, 70, 32),
    ('platform', 2650, 400, 70, 32),
    ('platform', 2800, 350, 70, 32),
    ('goomba', 2360, 464),
    ('koopa', 2660, 364),
    ('coin', 2380, 450),
    ('coin', 2530, 400),
    
    # Tuğla labirent
    ('brick', 3150, 500),
    ('brick', 3182, 500),
    ('brick', 3214, 500),
    ('brick', 3150, 400),
    ('brick', 3214, 400),
    ('question', 3182, 350),
    
    # Zikzak platformlar
    ('platform', 3750, 450, 80, 32),
    ('platform', 3900, 380, 80, 32),
    ('platform', 4050, 450, 80, 32),
    ('platform', 4200, 380, 80, 32),
    ('koopa', 3760, 414),
    ('goomba', 3910, 344),
    ('koopa', 4060, 414),
    
    # Soru bloğu kulesi
    ('question', 4550, 500),
    ('question', 4550, 450),
    ('question', 4550, 400),
    ('brick', 4582, 500),
    ('brick', 4582, 450),
    
    # Son zorlu bölüm
    ('platform', 4750, 480, 70, 32),
    ('platform', 4900, 420, 70, 32),
    ('platform', 5050, 360, 70, 32),
    ('koopa', 4760, 444),
    ('goomba', 4910, 384),
    ('koopa', 5060, 324),
    
    # Final - çıkış
    ('brick', 5550, 450),
    ('brick', 5582, 450),
    ('question', 5582, 400),
    ('star', 5582, 370),  # Yıldız ödülü!
]
