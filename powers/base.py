"""
PowerUp base class
"""
import pygame


class PowerUpType:
    """Güç türleri"""
    NONE = 0
    SUPER = 1  # Super Mushroom - Büyük Mario
    FIRE = 2   # Fire Flower - Ateş Mario
    STAR = 3   # Star - Yıldız (geçici yenilmezlik)


class PowerUp:
    """Güç objesi base class"""
    
    def __init__(self, x, y, power_type):
        self.rect = pygame.Rect(x, y, 32, 32)
        self.power_type = power_type
        self.vel_y = 0
        self.vel_x = 2  # Güçler sağa doğru hareket eder
        self.collected = False
        self.spawning = False  # Bloktan çıkış animasyonu
        self.spawn_start_y = y
        self.spawn_target_y = y - 32
        
    def update(self, platforms):
        """Güncelle"""
        if self.collected:
            return
        
        # Spawn animasyonu - bloktan yukarı çıkış
        if self.spawning:
            spawn_speed = 2
            if self.rect.y > self.spawn_target_y:
                self.rect.y -= spawn_speed
            else:
                self.rect.y = self.spawn_target_y
                self.spawning = False
            return  # Spawn sırasında yerçekimi yok
        
        # Yerçekimi
        self.vel_y += 0.5
        if self.vel_y > 10:
            self.vel_y = 10
        
        # Hareket
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        # Platform çarpışması
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                if self.vel_x > 0:
                    self.rect.right = platform.rect.left
                    self.vel_x = -2
                elif self.vel_x < 0:
                    self.rect.left = platform.rect.right
                    self.vel_x = 2
    
    def draw(self, screen, camera_x=0):
        """Çiz - override edilmeli"""
        pass
