"""
World 2 - Level 1 - Desert Start
"""

LEVEL_THEME = 'overworld'  # Değiştirebilirsin: 'underground', 'castle', 'snow'

LEVEL_DATA = [
    # Platformlar
    ('platform', 400, 528, 200, 32),
    ('platform', 700, 496, 128, 32),
    ('platform', 1000, 464, 160, 32),
    
    # Sorular ve bloklar
    ('question', 500, 400),
    ('question_mushroom', 600, 400),
    ('brick', 700, 400),
    
    # Düşmanlar
    ('goomba', 450, 496),
    ('koopa', 900, 432),
    
    # Borular
    ('pipe', 1200, 496, 64),
]
