"""
Goomba düşmanı
"""
from .base import Enemy
from renderer import draw_goomba


class Goomba(Enemy):
    """Goomba düşmanı - en basit düşman, ezilince ölür"""
    
    def __init__(self, x, y, stationary=False):
        super().__init__(x, y, 'goomba', stationary)
    
    def _render(self):
        """Goomba'yı çiz"""
        self.image.fill((0, 0, 0, 0))
        # 28x28 boyutuna sığdır (2px padding)
        draw_goomba(self.image, 2, 2, self.frame)
