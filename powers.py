"""
Mario özel yetenekler sistemi
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


class PlayerPowerState:
    """Oyuncunun güç durumu"""
    
    def __init__(self):
        self.current_power = PowerUpType.NONE
        self.star_timer = 0  # Yıldız süresi (frame cinsinden)
        self.fire_cooldown = 0  # Ateş topu cooldown
        
    def set_power(self, power_type):
        """Güç ayarla"""
        if power_type == PowerUpType.STAR:
            # Yıldız geçici - 10 saniye
            self.star_timer = 600  # 10 saniye * 60 FPS
        else:
            self.current_power = power_type
    
    def update(self):
        """Her frame güncelle"""
        # Yıldız süresini azalt
        if self.star_timer > 0:
            self.star_timer -= 1
        
        # Ateş cooldown
        if self.fire_cooldown > 0:
            self.fire_cooldown -= 1
    
    def is_invincible(self):
        """Yenilmez mi?"""
        return self.star_timer > 0
    
    def is_super(self):
        """Büyük Mario mu?"""
        return self.current_power >= PowerUpType.SUPER
    
    def is_fire(self):
        """Ateş Mario mu?"""
        return self.current_power == PowerUpType.FIRE
    
    def can_shoot_fire(self):
        """Ateş topu atabilir mi?"""
        return self.is_fire() and self.fire_cooldown == 0
    
    def shoot_fire(self):
        """Ateş topu at"""
        if self.can_shoot_fire():
            self.fire_cooldown = 30  # 0.5 saniye cooldown
            return True
        return False
    
    def take_damage(self):
        """Hasar al"""
        if self.is_invincible():
            return False  # Hasar almadı
        
        if self.current_power == PowerUpType.FIRE:
            self.current_power = PowerUpType.SUPER
            return False  # Can kaybetmedi, sadece küçüldü
        elif self.current_power == PowerUpType.SUPER:
            self.current_power = PowerUpType.NONE
            return False  # Can kaybetmedi, sadece küçüldü
        else:
            return True  # Can kaybetti


class Fireball(pygame.sprite.Sprite):
    """Ateş topu"""
    
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface((12, 12))
        self.image.fill((255, 100, 0))  # Turuncu
        pygame.draw.circle(self.image, (255, 200, 0), (6, 6), 6)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 8 * direction
        self.vel_y = -2
        self.alive = True
        self.lifetime = 120  # 2 saniye
        
    def update(self, platforms):
        """Güncelle"""
        if not self.alive:
            return
        
        self.lifetime -= 1
        if self.lifetime <= 0:
            self.alive = False
            self.kill()
            return
        
        # Hareket
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        # Yerçekimi
        self.vel_y += 0.3
        
        # Zemine çarptığında zıplar
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = -4  # Zıpla
                else:
                    self.alive = False
                    self.kill()
                    break
