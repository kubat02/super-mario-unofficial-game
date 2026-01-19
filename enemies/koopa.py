"""
Koopa Troopa düşmanı
"""
import pygame
from .base import Enemy
from renderer import draw_koopa


class Koopa(Enemy):
    """Koopa Troopa - ezilince kabuk olur, tekrar ezilince ölür"""
    
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
            # Kabuk çiz (yeşil dörtgen) - 28x28'e sığdır
            pygame.draw.ellipse(self.image, (0, 200, 0), (2, 6, 24, 18))
            pygame.draw.ellipse(self.image, (200, 200, 0), (6, 8, 16, 14))
        else:
            draw_koopa(self.image, 2, 2, self.direction, self.frame)
