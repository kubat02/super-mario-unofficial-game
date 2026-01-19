"""
Kamera sistemi
"""
import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT


class Camera:
    """Oyuncu takip eden kamera"""
    
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
    
    def apply(self, entity):
        """Kamera offset'i uygula"""
        return entity.rect.move(-self.camera.x, 0)
    
    def update(self, target):
        """Oyuncuyu takip et"""
        x = target.rect.centerx - SCREEN_WIDTH // 3
        
        # Kamera sınırları
        x = max(0, x)
        x = min(x, self.width - SCREEN_WIDTH)
        
        self.camera = pygame.Rect(x, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
