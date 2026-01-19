"""
Piranha Plant - Borulardan çıkan tehlikeli bitki
"""
import pygame
from .base import Enemy


class PiranhaPlant(Enemy):
    """Piranha Plant - Borulardan çıkar, ezilmez!"""
    
    def __init__(self, x, y, pipe_height=64):
        super().__init__(x, y, 'piranha', stationary=True)
        self.pipe_height = pipe_height
        self.pipe_top_y = y  # Borunun üst noktası
        self.hide_y = y + 32  # Saklandığı yer (borunun içi)
        self.show_y = y - 32  # Göründüğü yer (borunun üstü)
        self.rect.y = self.hide_y  # Başlangıçta saklanmış
        
        self.state = 'hiding'  # hiding, emerging, showing, retreating
        self.state_timer = 0
        self.hide_duration = 60  # 1 saniye
        self.show_duration = 90  # 1.5 saniye
        self.emerge_speed = 1.5
        
        self.vel_x = 0  # Piranha Plant hareket etmez
        self.vel_y = 0
    
    def update(self, platforms, other_enemies=None):
        """Piranha Plant davranışı - yukarı aşağı hareket"""
        if not self.alive:
            return
        
        self.frame += 1
        self.state_timer += 1
        
        if self.state == 'hiding':
            # Saklanmış, bekliyor
            if self.state_timer >= self.hide_duration:
                self.state = 'emerging'
                self.state_timer = 0
        
        elif self.state == 'emerging':
            # Borudan çıkıyor
            if self.rect.y > self.show_y:
                self.rect.y -= self.emerge_speed
            else:
                self.rect.y = self.show_y
                self.state = 'showing'
                self.state_timer = 0
        
        elif self.state == 'showing':
            # Tamamen dışarıda, bekliyor
            if self.state_timer >= self.show_duration:
                self.state = 'retreating'
                self.state_timer = 0
        
        elif self.state == 'retreating':
            # Boruya geri giriyor
            if self.rect.y < self.hide_y:
                self.rect.y += self.emerge_speed
            else:
                self.rect.y = self.hide_y
                self.state = 'hiding'
                self.state_timer = 0
        
        self._render()
    
    def stomp(self):
        """Piranha Plant ezilmez! Üstüne atlayınca da hasar alırsın"""
        return 'no_stomp'  # Öldürülemez
    
    def _render(self):
        """Piranha Plant çiz"""
        self.image.fill((0, 0, 0, 0))
        
        # Gövde (yeşil)
        pygame.draw.rect(self.image, (0, 180, 0), (10, 0, 12, 32))
        
        # Kafa (kırmızı, animasyonlu ağız)
        mouth_open = (self.frame // 10) % 2 == 0
        
        # Üst çene
        pygame.draw.ellipse(self.image, (200, 0, 0), (4, -8, 24, 20))
        
        # Alt çene (ağız açıksa aşağıda)
        if mouth_open:
            pygame.draw.ellipse(self.image, (180, 0, 0), (4, 12, 24, 18))
        else:
            pygame.draw.ellipse(self.image, (180, 0, 0), (4, 8, 24, 18))
        
        # Dişler (beyaz)
        pygame.draw.rect(self.image, (255, 255, 255), (8, 8, 3, 6))
        pygame.draw.rect(self.image, (255, 255, 255), (14, 8, 3, 6))
        pygame.draw.rect(self.image, (255, 255, 255), (20, 8, 3, 6))
        
        # Noktalar (beyaz)
        if not mouth_open:
            pygame.draw.circle(self.image, (255, 255, 255), (12, 2), 2)
            pygame.draw.circle(self.image, (255, 255, 255), (20, 2), 2)
