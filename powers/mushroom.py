"""
Super Mushroom - Mario'yu büyütür
"""
import pygame
from .base import PowerUp, PowerUpType


class Mushroom(PowerUp):
    """Super Mushroom - Mario'yu büyütür"""
    
    def __init__(self, x, y):
        super().__init__(x, y, PowerUpType.SUPER)
    
    def draw(self, screen, camera_x=0):
        """Mantar çiz"""
        if self.collected:
            return
        
        draw_x = self.rect.x - camera_x
        draw_y = self.rect.y
        
        # Mantar başı (kırmızı-beyaz)
        pygame.draw.ellipse(screen, (255, 0, 0), (draw_x, draw_y, 32, 24))
        # Beyaz noktalar
        pygame.draw.circle(screen, (255, 255, 255), (draw_x + 10, draw_y + 10), 4)
        pygame.draw.circle(screen, (255, 255, 255), (draw_x + 22, draw_y + 10), 4)
        # Mantar gövdesi (beyaz)
        pygame.draw.rect(screen, (255, 255, 220), (draw_x + 10, draw_y + 20, 12, 12))
