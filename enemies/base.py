"""
Düşman base class
"""
import pygame
from config import ENEMY_SPEED


class Enemy(pygame.sprite.Sprite):
    """Tüm düşmanlar için base class"""
    
    def __init__(self, x, y, enemy_type='goomba', stationary=False):
        super().__init__()
        self.enemy_type = enemy_type
        self.stationary = stationary  # Yerinde mi yoksa hareket ediyor mu
        self.image = pygame.Surface((28, 28), pygame.SRCALPHA)  # Biraz küçük - geçitlerden geçebilsin
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y + 4  # Yere daha iyi oturmak için biraz aşağı
        self.original_x = x  # Başlangıç pozisyonu (yerinde durma için)
        self.vel_x = -ENEMY_SPEED if not stationary else ENEMY_SPEED
        self.vel_y = 0  # Dikey hız (yerçekimi için)
        self.direction = -1
        self.frame = 0
        self.alive = True
        self.on_ground = False
        self.sway_distance = 20  # Yerinde sallanma mesafesi
        
    def update(self, platforms, other_enemies=None):
        """Her frame'de güncelle"""
        if not self.alive:
            return
            
        self.frame += 1
        
        if self.stationary:
            # Yerinde sağ-sol sallanma (yerçekimi yok)
            self.rect.x += self.vel_x
            
            # Başlangıç noktasından çok uzaklaştıysa yön değiştir
            if self.rect.x < self.original_x - self.sway_distance:
                self.vel_x = ENEMY_SPEED
                self.direction = 1
            elif self.rect.x > self.original_x + self.sway_distance:
                self.vel_x = -ENEMY_SPEED
                self.direction = -1
        else:
            # Normal hareket - Mario gibi
            # Yerçekimi
            self.vel_y += 0.5
            if self.vel_y > 15:
                self.vel_y = 15
            
            # Yatay hareket
            self.rect.x += self.vel_x
            
            # Diğer düşmanlarla çarpışma
            if other_enemies:
                for enemy in other_enemies:
                    if enemy != self and enemy.alive and self.rect.colliderect(enemy.rect):
                        # Birbirlerine çarptılar - yön değiştir
                        if self.vel_x < 0:
                            self.rect.left = enemy.rect.right
                            self.vel_x = ENEMY_SPEED
                            self.direction = 1
                        else:
                            self.rect.right = enemy.rect.left
                            self.vel_x = -ENEMY_SPEED
                            self.direction = -1
            
            # Platform yatay çarpışması
            for platform in platforms:
                if self.rect.colliderect(platform.rect):
                    # Sadece yandan çarpışmayı kontrol et (üstten/alttan değil)
                    if abs(self.rect.bottom - platform.rect.top) > 5:
                        if self.vel_x < 0 and self.rect.left < platform.rect.right:
                            self.rect.left = platform.rect.right
                            self.vel_x = ENEMY_SPEED
                            self.direction = 1
                        elif self.vel_x > 0 and self.rect.right > platform.rect.left:
                            self.rect.right = platform.rect.left
                            self.vel_x = -ENEMY_SPEED
                            self.direction = -1
            
            # Dikey hareket (yerçekimi)
            self.rect.y += self.vel_y
            
            # Platform dikey çarpışması (zemin kontrolü)
            self.on_ground = False
            for platform in platforms:
                if self.rect.colliderect(platform.rect):
                    if self.vel_y > 0:  # Düşüyorsa
                        self.rect.bottom = platform.rect.top
                        self.vel_y = 0
                        self.on_ground = True
                    elif self.vel_y < 0:  # Yukarı çıkıyorsa
                        self.rect.top = platform.rect.bottom
                        self.vel_y = 0
        
        # Düşmanı çiz
        self._render()
    
    def _render(self):
        """Düşmanı çiz - override edilmeli"""
        pass
    
    def stomp(self):
        """Düşman ezildi"""
        self.alive = False
        self.kill()
        return 'kill'
