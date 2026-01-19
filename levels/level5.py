"""
Level 5 - World 1-5: Bowser'ın Kalesi (Bowser's Castle) 
Büyük kötü adamın şatosu - karanlık, tehlikeli ve zorlu final seviyesi!
"""

# Level teması
LEVEL_THEME = 'castle'  # Kale teması - karanlık ve korkutucu

LEVEL_DATA = [
    # Kale girişi - tehlikeli başlangıç
    ('brick', 200, 500),
    ('brick', 232, 500),
    ('brick', 264, 500),
    ('goomba', 240, 464),
    
    # İlk platform
    ('platform', 400, 500, 150, 32),
    ('koopa_stationary', 450, 464),
    ('koopa_stationary', 490, 464),
    ('coin', 470, 430),
    
    # Tuğla labirent - sıkışık geçit
    ('brick', 650, 450),
    ('brick', 682, 450),
    ('brick', 714, 450),
    ('brick', 746, 450),
    ('brick', 650, 350),
    ('brick', 682, 350),
    ('brick', 714, 350),
    ('brick', 746, 350),
    ('goomba', 670, 414),
    ('koopa', 720, 414),
    
    # Yüksek platform challenge
    ('platform', 900, 400, 100, 32),
    ('platform', 1050, 350, 100, 32),
    ('goomba_stationary', 920, 364),
    ('koopa_stationary', 1070, 314),
    ('question', 975, 300),
    ('mushroom', 975, 270),
    
    # Tehlikeli atlama bölümü
    ('platform', 1250, 480, 80, 32),
    ('platform', 1400, 450, 80, 32),
    ('platform', 1550, 420, 80, 32),
    ('platform', 1700, 390, 80, 32),
    ('koopa', 1260, 444),
    ('goomba', 1410, 414),
    ('koopa', 1560, 384),
    ('goomba', 1710, 354),
    ('coin', 1280, 430),
    ('coin', 1430, 400),
    ('coin', 1580, 370),
    ('coin', 1730, 340),
    
    # Boru ve düşman ordusu
    ('pipe', 1900, 460, 100),
    ('goomba', 2050, 524),
    ('goomba', 2100, 524),
    ('koopa', 2150, 524),
    ('goomba', 2200, 524),
    ('koopa', 2250, 524),
    
    # Tuğla kule
    ('brick', 2450, 500),
    ('brick', 2482, 500),
    ('brick', 2450, 450),
    ('brick', 2482, 450),
    ('brick', 2450, 400),
    ('brick', 2482, 400),
    ('brick', 2450, 350),
    ('brick', 2482, 350),
    ('brick', 2466, 300),
    ('question', 2466, 250),
    ('fireflower', 2466, 220),  # Fire Flower - gerekli!
    
    # Soru blokları duvarı
    ('question', 2700, 450),
    ('question', 2732, 450),
    ('question', 2764, 450),
    ('question', 2700, 350),
    ('question', 2732, 350),
    ('question', 2764, 350),
    ('coin', 2716, 400),
    ('coin', 2748, 400),
    
    # Zorlu platform zinciri
    ('platform', 2950, 480, 70, 32),
    ('platform', 3100, 430, 70, 32),
    ('platform', 3250, 380, 70, 32),
    ('platform', 3400, 330, 70, 32),
    ('platform', 3550, 280, 70, 32),
    ('koopa_stationary', 2970, 444),
    ('goomba', 3120, 394),
    ('koopa_stationary', 3270, 344),
    ('goomba', 3420, 294),
    ('koopa', 3570, 244),
    
    # Kale iç kısım - karanlık koridor
    ('brick', 3750, 400),
    ('brick', 3782, 400),
    ('brick', 3814, 400),
    ('brick', 3846, 400),
    ('brick', 3878, 400),
    ('brick', 3910, 400),
    ('platform', 3780, 500, 120, 32),
    ('goomba', 3790, 464),
    ('koopa_stationary', 3830, 464),
    ('goomba', 3870, 464),
    
    # Platform atlama - lav üzerinde
    ('platform', 4100, 480, 80, 32),
    ('platform', 4250, 440, 80, 32),
    ('platform', 4400, 400, 80, 32),
    ('platform', 4550, 360, 80, 32),
    ('koopa', 4110, 444),
    ('goomba', 4260, 404),
    ('koopa', 4410, 364),
    ('goomba', 4560, 324),
    
    # Soru bloğu kulesi - son güçler
    ('question', 4750, 500),
    ('question', 4750, 450),
    ('question', 4750, 400),
    ('question', 4750, 350),
    ('question', 4750, 300),
    ('brick', 4782, 500),
    ('brick', 4782, 450),
    ('brick', 4782, 400),
    ('brick', 4782, 350),
    ('star', 4750, 270),  # Yıldız - final için gerekli!
    
    # Son meydan okuma - Bowser'a doğru
    ('platform', 4950, 480, 80, 32),
    ('platform', 5100, 420, 80, 32),
    ('platform', 5250, 480, 80, 32),
    ('platform', 5400, 420, 80, 32),
    ('koopa', 4960, 444),
    ('goomba', 4990, 444),
    ('koopa_stationary', 5110, 384),
    ('goomba', 5140, 384),
    ('koopa', 5260, 444),
    ('goomba', 5290, 444),
    ('koopa_stationary', 5410, 384),
    ('goomba', 5440, 384),
    
    # Final - Bowser'ın odası önü
    ('brick', 5600, 500),
    ('brick', 5632, 500),
    ('brick', 5664, 500),
    ('brick', 5600, 450),
    ('brick', 5632, 450),
    ('brick', 5664, 450),
    ('brick', 5632, 400),
    ('question', 5632, 350),
    
    # Zafere giden son yol
    ('platform', 5700, 500, 50, 32),
]
