"""
Fire Flower - Mario'ya ateş atma yeteneği verir
"""
import pygame
from .base import PowerUp, PowerUpType


class FireFlower(PowerUp):
    """Fire Flower - Ateş atma yeteneği"""
    
    def __init__(self, x, y):
        super().__init__(x, y, PowerUpType.FIRE)
        self.vel_x = 0  # Fire Flower hareket etmez
        self.frame = 0
    
    def update(self, platforms):
        """Fire Flower yerinde durur, sadece renk değişir"""
        if self.collected:
            return
        
        self.frame += 1
        
        # Spawn animasyonu varsa
        if self.spawning:
            spawn_speed = 2
            if self.rect.y > self.spawn_target_y:
                self.rect.y -= spawn_speed
            else:
                self.rect.y = self.spawn_target_y
                self.spawning = False
            return
        
        # Yerçekimi
        self.vel_y += 0.5
        if self.vel_y > 10:
            self.vel_y = 10
        
        self.rect.y += self.vel_y
        
        # Platform çarpışması
        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.vel_y > 0:
                self.rect.bottom = platform.rect.top
                self.vel_y = 0
    
    def draw(self, screen, camera_x=0):
        """Çiçek çiz (yanıp sönen renkler)"""
        if self.collected:
            return
        
        draw_x = self.rect.x - camera_x
        draw_y = self.rect.y
        
        # Renkler döngüsel değişir
        colors = [(255, 0, 0), (255, 128, 0), (255, 255, 0), (255, 0, 255)]
        color_index = (self.frame // 10) % len(colors)
        color = colors[color_index]
        
        # Çiçek gövdesi (yeşil)
        pygame.draw.rect(screen, (0, 200, 0), (draw_x + 14, draw_y + 16, 4, 16))
        
        # Çiçek yaprakları (4 yönlü)
        center_x = draw_x + 16
        center_y = draw_y + 12
        petal_size = 8
        
        # Üst
        pygame.draw.circle(screen, color, (center_x, center_y - petal_size), petal_size)
        # Alt
        pygame.draw.circle(screen, color, (center_x, center_y + petal_size), petal_size)
        # Sol
        pygame.draw.circle(screen, color, (center_x - petal_size, center_y), petal_size)
        # Sağ
        pygame.draw.circle(screen, color, (center_x + petal_size, center_y), petal_size)
        # Merkez
        pygame.draw.circle(screen, (255, 255, 0), (center_x, center_y), 5)
