"""
Lakitu - Bulut üstünde uçar, Spiny yumurtaları atar
"""
import pygame
from .base import Enemy


class SpinyEgg(pygame.sprite.Sprite):
    """Spiny Yumurtası - düşünce Spiny'ye dönüşür"""
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((16, 16), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = 2  # Aşağı düşüyor
        self.alive = True
        self.hatched = False  # Yere çarptı mı?
        self._render()
    
    def update(self, platforms):
        """Yumurtayı güncelle"""
        if not self.alive or self.hatched:
            return
        
        # Düşüyor
        self.vel_y += 0.5
        if self.vel_y > 10:
            self.vel_y = 10
        
        self.rect.y += self.vel_y
        
        # Yere çarptı mı?
        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.vel_y > 0:
                self.rect.bottom = platform.rect.top
                self.hatched = True  # Spiny'ye dönüşecek
                break
    
    def _render(self):
        """Yumurta çiz (yeşil-beyaz noktalı)"""
        self.image.fill((0, 0, 0, 0))
        # Yeşil yumurta
        pygame.draw.ellipse(self.image, (0, 200, 0), (0, 0, 16, 16))
        # Beyaz noktalar
        pygame.draw.circle(self.image, (255, 255, 255), (5, 5), 2)
        pygame.draw.circle(self.image, (255, 255, 255), (11, 8), 2)
        pygame.draw.circle(self.image, (255, 255, 255), (8, 11), 2)


class Lakitu(Enemy):
    """Lakitu - Bulut üstünde uçar, Spiny yumurtası atar"""
    
    def __init__(self, x, y, player_ref=None, enemy_group=None):
        super().__init__(x, y, 'lakitu', stationary=False)
        self.vel_y = 0
        self.ignore_gravity = True  # Uçuyor
        self.hover_y = y  # Hedef yükseklik
        self.hover_speed = 0.5
        self.follow_distance = 200  # Mario'dan bu kadar uzakta takip eder
        self.throw_cooldown = 0
        self.throw_interval = 180  # 3 saniye (60 FPS * 3)
        self.eggs = []  # Attığı yumurtalar
        self.player_ref = player_ref  # Mario referansı
        self.enemy_group = enemy_group  # Düşman grubu (Spiny eklemek için)
        
        # Lakitu daha yavaş hareket eder
        self.vel_x = 1
    
    def update(self, platforms, other_enemies=None):
        """Lakitu davranışı - Mario'yu takip et, yumurta at"""
        if not self.alive:
            return
        
        self.frame += 1
        self.throw_cooldown -= 1
        
        # Mario'yu takip et (yatayda)
        if self.player_ref:
            player_x = self.player_ref.rect.x
            distance = self.rect.x - player_x
            
            # Mario'dan belirli mesafede kal
            if distance > self.follow_distance + 50:
                self.vel_x = -1.5  # Mario'ya yaklaş
                self.direction = -1
            elif distance < self.follow_distance - 50:
                self.vel_x = 1.5  # Mario'dan uzaklaş
                self.direction = 1
            else:
                self.vel_x = 0  # İdeal mesafede
        
        self.rect.x += self.vel_x
        
        # Yukarı aşağı sallanma (hover)
        hover_offset = (self.frame // 30) % 20 - 10
        self.rect.y = self.hover_y + hover_offset
        
        # Spiny yumurtası at
        if self.throw_cooldown <= 0 and self.player_ref:
            self._throw_egg(platforms)
            self.throw_cooldown = self.throw_interval
        
        # Yumurtaları güncelle
        for egg in self.eggs[:]:
            egg.update(platforms)
            if egg.hatched:
                # Spiny'ye dönüş!
                self._spawn_spiny(egg.rect.x, egg.rect.y, platforms)
                self.eggs.remove(egg)
            elif not egg.alive:
                self.eggs.remove(egg)
        
        self._render()
    
    def _throw_egg(self, platforms):
        """Spiny yumurtası at"""
        egg = SpinyEgg(self.rect.centerx - 8, self.rect.bottom)
        self.eggs.append(egg)
    
    def _spawn_spiny(self, x, y, platforms):
        """Yumurtadan Spiny çıkar"""
        if self.enemy_group:
            from .spiny import Spiny
            spiny = Spiny(x, y - 32)
            self.enemy_group.add(spiny)
    
    def stomp(self):
        """Lakitu ezilir - bulut kaybolur"""
        self.alive = False
        self.kill()
        return 'kill'
    
    def _render(self):
        """Lakitu çiz - bulut + gözlüklü Koopa"""
        self.image.fill((0, 0, 0, 0))
        
        # Bulut (beyaz)
        cloud_y = 12
        pygame.draw.ellipse(self.image, (255, 255, 255), (2, cloud_y, 12, 10))
        pygame.draw.ellipse(self.image, (255, 255, 255), (10, cloud_y - 2, 14, 12))
        pygame.draw.ellipse(self.image, (255, 255, 255), (18, cloud_y, 12, 10))
        
        # Lakitu (Koopa benzeri - yeşil gözlüklü)
        # Gövde
        pygame.draw.ellipse(self.image, (0, 200, 0), (10, 2, 12, 16))
        # Kabuk
        pygame.draw.ellipse(self.image, (255, 200, 0), (8, 8, 16, 12))
        
        # Gözlükler (siyah çerçeve, beyaz cam)
        pygame.draw.circle(self.image, (50, 50, 50), (13, 6), 3)
        pygame.draw.circle(self.image, (255, 255, 255), (13, 6), 2)
        pygame.draw.circle(self.image, (50, 50, 50), (19, 6), 3)
        pygame.draw.circle(self.image, (255, 255, 255), (19, 6), 2)
        
        # Gözlük çizgisi
        pygame.draw.line(self.image, (50, 50, 50), (16, 6), (16, 6), 2)
        
        # Balıkçı oltası (yumurta atarken sallanır)
        rod_swing = 2 if self.throw_cooldown > self.throw_interval - 10 else 0
        pygame.draw.line(self.image, (100, 50, 0), (20, 10), (24 + rod_swing, 16), 2)
    
    def get_eggs_for_collision(self):
        """Yumurtaları döndür (çarpışma testi için)"""
        return self.eggs
