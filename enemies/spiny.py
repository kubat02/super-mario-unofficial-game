"""
Spiny - Diken topu düşman (üstüne basamazsın!)
"""
import pygame
from .base import Enemy


class Spiny(Enemy):
    """Spiny - Dikenleri var, ezilmez! Sadece ateş topuyla öldürülebilir"""
    
    def __init__(self, x, y, stationary=False):
        super().__init__(x, y, 'spiny', stationary)
    
    def stomp(self):
        """Spiny ezilmez! Dikenleri var - Mario hasar alır"""
        return 'no_stomp'  # Öldürülemez, ters tepki (hasar al)
    
    def _render(self):
        """Spiny çiz - kırmızı diken topu"""
        self.image.fill((0, 0, 0, 0))
        
        # Gövde (kırmızı kabuk) - 28x28'e sığdır
        pygame.draw.ellipse(self.image, (200, 0, 0), (2, 6, 24, 18))
        
        # Dikenler (siyah) - 28x28'e uygun pozisyonlar
        spike_positions = [
            (6, 4), (14, 2), (22, 4),  # Üst dikenler
            (4, 12), (24, 12),  # Yan dikenler
        ]
        
        for spike_x, spike_y in spike_positions:
            pygame.draw.polygon(self.image, (50, 50, 50), [
                (spike_x, spike_y),
                (spike_x - 3, spike_y + 6),
                (spike_x + 3, spike_y + 6)
            ])
        
        # Gözler (beyaz-kırmızı, kızgın bakış)
        eye_y = 12
        if self.direction == -1:
            # Sola bakıyor
            pygame.draw.circle(self.image, (255, 255, 255), (8, eye_y), 3)
            pygame.draw.circle(self.image, (255, 0, 0), (7, eye_y), 1)
        else:
            # Sağa bakıyor
            pygame.draw.circle(self.image, (255, 255, 255), (20, eye_y), 3)
            pygame.draw.circle(self.image, (255, 0, 0), (21, eye_y), 1)
