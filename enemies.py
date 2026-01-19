"""
Düşman karakterleri
"""
import pygame
from config import ENEMY_SPEED
from renderer import draw_goomba, draw_koopa


class Enemy(pygame.sprite.Sprite):
    """Düşman base class"""
    
    def __init__(self, x, y, enemy_type='goomba', stationary=False):
        super().__init__()
        self.enemy_type = enemy_type
        self.stationary = stationary  # Yerinde mi yoksa hareket ediyor mu
        self.image = pygame.Surface((32, 32), pygame.SRCALPHA)  # 1 blok boyutu
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
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
        """Düşmanı çiz"""
        self.image.fill((0, 0, 0, 0))
        if self.enemy_type == 'goomba':
            draw_goomba(self.image, 0, 0, self.frame)
        elif self.enemy_type == 'koopa':
            draw_koopa(self.image, 0, 0, self.direction, self.frame)
    
    def _check_ground_ahead(self, platforms):
        """Kenardan düşmeyi engelle"""
        if self.vel_x < 0:
            check_x = self.rect.left - 10
        else:
            check_x = self.rect.right + 10
        
        check_y = self.rect.bottom + 10
        
        has_ground = False
        for platform in platforms:
            if (platform.rect.left < check_x < platform.rect.right and 
                platform.rect.top < check_y < platform.rect.bottom + 20):
                has_ground = True
                break
        
        if not has_ground:
            self.vel_x *= -1
            self.direction *= -1
    
    def stomp(self):
        """Düşman ezildi"""
        self.alive = False
        self.kill()


class Goomba(Enemy):
    """Goomba düşmanı"""
    
    def __init__(self, x, y, stationary=False):
        super().__init__(x, y, 'goomba', stationary)


class Koopa(Enemy):
    """Koopa Troopa düşmanı"""
    
    def __init__(self, x, y, stationary=False):
        super().__init__(x, y, 'koopa', stationary)
        self.in_shell = False  # Kabuk modunda mı
        self.shell_moving = False  # Kabuk hareket ediyor mu
        self.shell_speed = 8  # Kabuk hızı
    
    def stomp(self):
        """Koopa ezildi - kabuk moduna geç"""
        if not self.in_shell:
            # İlk eziliş - kabuk ol
            self.in_shell = True
            self.vel_x = 0
            self.shell_moving = False
            return 'shell'  # Kabuk haline geldi
        else:
            # Zaten kabuk - öldür
            self.alive = False
            self.kill()
            return 'kill'
    
    def kick_shell(self, direction):
        """Kabuğu tekmelendi - hızla hareket et"""
        if self.in_shell and not self.shell_moving:
            self.shell_moving = True
            self.vel_x = self.shell_speed * direction
            self.direction = direction
            return True
        return False
    
    def update(self, platforms, other_enemies=None):
        """Kabuk modu için özel update"""
        if not self.alive:
            return
        
        # Kabuk hareket ediyorsa
        if self.in_shell and self.shell_moving:
            self.frame += 1
            
            # Kabuk hareketi
            self.rect.x += self.vel_x
            
            # Duvarlardan sekmesi
            for platform in platforms:
                if self.rect.colliderect(platform.rect):
                    if self.vel_x < 0:
                        self.rect.left = platform.rect.right
                        self.vel_x = self.shell_speed
                        self.direction = 1
                    elif self.vel_x > 0:
                        self.rect.right = platform.rect.left
                        self.vel_x = -self.shell_speed
                        self.direction = -1
            
            # Diğer düşmanları öldür
            if other_enemies:
                for enemy in other_enemies:
                    if enemy != self and enemy.alive and self.rect.colliderect(enemy.rect):
                        enemy.alive = False
                        enemy.kill()
            
            # Yerçekimi (kabuk da düşer)
            self.vel_y += 0.5
            if self.vel_y > 15:
                self.vel_y = 15
            
            self.rect.y += self.vel_y
            
            # Zemin kontrolü
            for platform in platforms:
                if self.rect.colliderect(platform.rect) and self.vel_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
        elif self.in_shell and not self.shell_moving:
            # Hareketsiz kabuk - sadece yerçekimi
            self.vel_y += 0.5
            if self.vel_y > 15:
                self.vel_y = 15
            
            self.rect.y += self.vel_y
            
            for platform in platforms:
                if self.rect.colliderect(platform.rect) and self.vel_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
        else:
            # Normal hareket
            super().update(platforms, other_enemies)
    
    def _render(self):
        """Koopa'yı çiz"""
        self.image.fill((0, 0, 0, 0))
        if self.in_shell:
            # Kabuk çiz (yeşil dörtgen)
            pygame.draw.ellipse(self.image, (0, 200, 0), (4, 8, 24, 20))
            pygame.draw.ellipse(self.image, (200, 200, 0), (8, 10, 16, 16))
        else:
            draw_koopa(self.image, 0, 0, self.direction, self.frame)
