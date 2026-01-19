"""
Level 6 - KOOPA KABUK ŞAMPİYONASI 🐢
Epic level tasarımı - Zorluk: Orta-Zor

YENİ MEKANİK: KOOPA KABUĞU!
- Koopa'yı ezince kabuk olur
- Kabuğa tekrar dokunarak tekmeleyebilirsin
- Kabuk hareket ederken diğer düşmanları öldürür
- Hareket eden kabuğa çarparsan can kaybedersin!

KOMBO SİSTEMİ:
- Düşmanları art arda ezince kombo puanı artar
- 100 → 200 → 400 → 800 → 1000 → 2000 → 4000 → 8000
- 1 saniye içinde yeni ezme yoksa kombo sıfırlanır

KONTROLLER:
- ↑: Zıplama (düşman üstünde basılı tutarsan süper zıplama!)
- SPACE: Özel güç (Fire Flower ile ateş topu)
"""

LEVEL_DATA = [
    # ===== BAŞLANGIÇ - ÖĞRETME BÖLÜMÜ =====
    ('question', 200, 400),
    ('coin', 250, 450),
    ('coin', 280, 450),
    ('coin', 310, 450),
    
    # İlk Koopa - kolay test
    ('koopa', 450, 524),
    ('brick', 550, 450),
    ('question', 582, 450),
    ('brick', 614, 450),
    
    # ===== PLATFORM ZİPLEME BÖLÜMÜ =====
    ('platform', 800, 500, 96, 32),
    ('coin', 820, 450),
    ('coin', 850, 450),
    ('coin', 880, 450),
    
    # Boşluk - düşme tehlikesi
    ('platform', 1000, 480, 96, 32),
    ('goomba', 1020, 450),
    
    ('platform', 1200, 460, 128, 32),
    ('koopa', 1220, 430),
    ('koopa', 1280, 430),
    
    # ===== KOOPA ARENA - KABUK USTALIĞI =====
    ('platform', 1400, 540, 400, 32),  # Geniş arena
    ('pipe', 1420, 476, 64),
    ('koopa', 1500, 510),
    ('koopa', 1600, 510),
    ('goomba', 1550, 510),
    ('goomba', 1650, 510),
    ('question', 1550, 440),  # Fire Flower için
    ('question', 1650, 440),
    ('brick', 1582, 380),
    ('brick', 1614, 380),
    ('coin', 1590, 330),
    ('coin', 1620, 330),
    
    # ===== HIZLI PLATFORM ATLAMA =====
    ('platform', 1850, 520, 64, 32),
    ('coin', 1870, 470),
    
    ('platform', 1970, 480, 64, 32),
    ('goomba', 1980, 450),
    
    ('platform', 2090, 440, 64, 32),
    ('koopa', 2100, 410),
    
    ('platform', 2210, 400, 96, 32),
    ('coin', 2230, 350),
    ('coin', 2260, 350),
    
    # ===== BORU VE DÜŞMAN ORDUSU =====
    ('pipe', 2400, 490, 70),
    ('pipe', 2550, 460, 100),
    ('goomba_stationary', 2500, 524),  # Yerinde sallanan
    ('koopa', 2650, 524),
    ('goomba', 2700, 524),
    ('koopa', 2750, 524),
    
    # Üst platform - güvenli geçiş
    ('platform', 2450, 360, 200, 32),
    ('coin', 2480, 310),
    ('coin', 2520, 310),
    ('coin', 2560, 310),
    ('coin', 2600, 310),
    ('question', 2540, 290),
    
    # ===== TUĞLA LABİRENT =====
    ('brick', 2850, 480),
    ('brick', 2882, 480),
    ('brick', 2914, 480),
    ('brick', 2946, 480),
    
    ('brick', 2850, 420),
    ('question', 2882, 420),
    ('question', 2914, 420),
    ('brick', 2946, 420),
    
    ('brick', 2850, 360),
    ('brick', 2882, 360),
    ('brick', 2914, 360),
    ('brick', 2946, 360),
    
    ('koopa_stationary', 2900, 524),  # Yerinde sallanan Koopa
    ('goomba', 2950, 524),
    
    # ===== YÜKSEK PLATFORM CHALLENGE =====
    ('platform', 3100, 460, 128, 32),
    ('koopa', 3120, 430),
    ('koopa', 3180, 430),
    
    ('platform', 3280, 380, 96, 32),
    ('coin', 3300, 330),
    ('coin', 3330, 330),
    
    ('platform', 3430, 300, 128, 32),
    ('question', 3450, 230),
    ('question', 3482, 230),
    ('question', 3514, 230),
    ('goomba', 3470, 270),
    ('goomba', 3520, 270),
    
    # İniş - dikkatli ol!
    ('platform', 3600, 380, 96, 32),
    ('koopa', 3620, 350),
    
    ('platform', 3750, 460, 96, 32),
    
    # ===== KOOPA KABUK CHALLENGE =====
    # Dar geçit - kabuğu kullan!
    ('platform', 3900, 540, 300, 32),
    ('brick', 3920, 480),
    ('brick', 3952, 480),
    ('brick', 3984, 480),
    ('brick', 4016, 480),
    ('brick', 4048, 480),
    ('brick', 4080, 480),
    ('brick', 4112, 480),
    ('brick', 4144, 480),
    ('brick', 4176, 480),
    
    ('koopa', 3920, 510),  # Bu kabuğu kullan!
    ('goomba', 3970, 510),
    ('goomba', 4020, 510),
    ('goomba', 4070, 510),
    ('koopa', 4120, 510),
    ('goomba', 4170, 510),
    
    ('coin', 3940, 440),
    ('coin', 3990, 440),
    ('coin', 4040, 440),
    ('coin', 4090, 440),
    ('coin', 4140, 440),
    
    # ===== FİNAL SPRINT =====
    ('platform', 4250, 500, 160, 32),
    ('pipe', 4280, 436, 64),
    ('question', 4350, 400),
    ('question', 4382, 400),
    
    ('platform', 4470, 480, 96, 32),
    ('koopa', 4490, 450),
    
    ('platform', 4620, 460, 128, 32),
    ('goomba', 4640, 430),
    ('koopa', 4690, 430),
    
    # Son platform öncesi - büyük boşluk!
    ('platform', 4800, 440, 64, 32),
    ('coin', 4820, 390),
    
    ('platform', 4920, 420, 96, 32),
    ('coin', 4950, 370),
    
    # ===== ZAFER PLATFORMU =====
    ('platform', 5100, 500, 200, 32),
    ('coin', 5130, 450),
    ('coin', 5160, 450),
    ('coin', 5190, 450),
    ('coin', 5220, 450),
    ('question', 5175, 400),
    
    # Final borular
    ('pipe', 5320, 436, 64),
    ('pipe', 5420, 460, 100),
]
