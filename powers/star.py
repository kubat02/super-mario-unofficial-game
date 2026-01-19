"""
Star - Geçici yenilmezlik
"""
import pygame
import math
from .base import PowerUp, PowerUpType


class Star(PowerUp):
    """Star - 10 saniye yenilmezlik"""
    
    def __init__(self, x, y):
        super().__init__(x, y, PowerUpType.STAR)
        self.vel_x = 3  # Yıldız hızlı hareket eder
        self.vel_y = -5  # Başlangıçta yukarı zıplar
        self.frame = 0
    
    def update(self, platforms):
        """Yıldız sürekli zıplar"""
        if self.collected:
            return
        
        self.frame += 1
        
        # Spawn animasyonu
        if self.spawning:
            spawn_speed = 2
            if self.rect.y > self.spawn_target_y:
                self.rect.y -= spawn_speed
            else:
                self.rect.y = self.spawn_target_y
                self.spawning = False
                self.vel_y = -5  # Spawn sonrası yukarı zıpla
            return
        
        # Yerçekimi
        self.vel_y += 0.5
        if self.vel_y > 10:
            self.vel_y = 10
        
        # Hareket
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        # Platform çarpışması - zıpla
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = -5  # Zıpla
                if self.vel_x > 0:
                    self.rect.right = platform.rect.left
                    self.vel_x = -3
                elif self.vel_x < 0:
                    self.rect.left = platform.rect.right
                    self.vel_x = 3
    
    def draw(self, screen, camera_x=0):
        """Dönen renkli yıldız çiz"""
        if self.collected:
            return
        
        draw_x = self.rect.x - camera_x + 16
        draw_y = self.rect.y + 16
        
        # Dönen renkler
        colors = [(255, 255, 0), (255, 200, 0), (255, 255, 100), (255, 220, 50)]
        color = colors[(self.frame // 5) % len(colors)]
        
        # 5 köşeli yıldız çiz
        points = []
        num_points = 5
        outer_radius = 14
        inner_radius = 6
        
        for i in range(num_points * 2):
            angle = (i * math.pi / num_points) + (self.frame * 0.05)
            radius = outer_radius if i % 2 == 0 else inner_radius
            x = draw_x + math.cos(angle) * radius
            y = draw_y + math.sin(angle) * radius
            points.append((x, y))
        
        pygame.draw.polygon(screen, color, points)
        pygame.draw.polygon(screen, (255, 255, 255), points, 2)  # Beyaz kenar
