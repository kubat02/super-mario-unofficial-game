"""
Bullet Bill - Hızlı mermi düşman
"""
import pygame
from .base import Enemy


class BulletBill(Enemy):
    """Bullet Bill - Hızlı, düz uçan mermi"""
    
    def __init__(self, x, y, direction=-1):
        super().__init__(x, y, 'bullet_bill', stationary=False)
        self.direction = direction
        self.vel_x = 6 * direction  # Hızlı hareket
        self.vel_y = 0  # Yerçekimi yok
        self.ignore_gravity = True
    
    def update(self, platforms, other_enemies=None):
        """Düz uçar, yerçekimi etkilemez"""
        if not self.alive:
            return
        
        self.frame += 1
        
        # Sadece yatay hareket
        self.rect.x += self.vel_x
        
        # Duvarlardan geçer, sadece platform varsa öl
        # (normalde ekran dışına çıkınca ölmeli)
        
        self._render()
    
    def _render(self):
        """Bullet Bill çiz"""
        self.image.fill((0, 0, 0, 0))
        
        # Gövde (siyah mermi) - 28x28'e sığdır
        pygame.draw.ellipse(self.image, (40, 40, 40), (0, 2, 28, 24))
        
        # Burun (gri)
        if self.direction == -1:
            # Sola bakan
            pygame.draw.polygon(self.image, (100, 100, 100), [
                (0, 14), (10, 4), (10, 24)
            ])
        else:
            # Sağa bakan
            pygame.draw.polygon(self.image, (100, 100, 100), [
                (28, 14), (18, 4), (18, 24)
            ])
        
        # Kollar (animasyonlu)
        arm_offset = 2 if (self.frame // 10) % 2 == 0 else -2
        pygame.draw.rect(self.image, (40, 40, 40), (6, 22 + arm_offset, 6, 4))
        pygame.draw.rect(self.image, (40, 40, 40), (16, 22 + arm_offset, 6, 4))
        
        # Gözler (beyaz, kırmızı pupil)
        if self.direction == -1:
            pygame.draw.circle(self.image, (255, 255, 255), (18, 10), 4)
            pygame.draw.circle(self.image, (255, 0, 0), (17, 10), 2)
        else:
            pygame.draw.circle(self.image, (255, 255, 255), (10, 10), 4)
            pygame.draw.circle(self.image, (255, 0, 0), (11, 10), 2)
