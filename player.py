"""
Oyuncu karakteri
"""
import pygame
from config import *
from renderer import draw_mario
from powers import PlayerPowerState


class Player(pygame.sprite.Sprite):
    """Mario oyuncu karakteri"""
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32), pygame.SRCALPHA)  # Küçük Mario - 1 blok
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.vel_x = 0
        self.on_ground = False
        self.lives = INITIAL_LIVES
        self.score = 0
        self.direction = 1  # 1 = sağ, -1 = sol
        self.frame = 0
        self.is_moving = False
        self.fly_mode = False  # Developer uçma modu
        self.power_state = PlayerPowerState()  # Güç durumu - başlangıçta küçük
        self.fireballs = pygame.sprite.Group()  # Ateş topları
        self.combo_count = 0  # Düşman ezme kombosu
        self.combo_timer = 0  # Kombo süresi
        self.is_dying = False  # Ölüm animasyonu
        self.death_jump_vel = 0  # Ölüm zıplaması
        self.invincibility_timer = 0  # Hasar sonrası yanıp sönme
        self._update_size()  # Boyutu güç durumuna göre ayarla
        
    def update(self, platforms, enemies, coins, blocks, level_width):
        """Her frame'de güncelle"""
        keys = pygame.key.get_pressed()
        
        # Ölüm animasyonu aktifse sadece onu oynat
        if self.is_dying:
            self._update_death_animation()
            return
        
        # Güç durumunu güncelle
        self.power_state.update()
        
        # Ateş toplarını güncelle
        self.fireballs.update(platforms)
        
        # Kombo timer azalt
        if self.combo_timer > 0:
            self.combo_timer -= 1
        else:
            self.combo_count = 0  # Süre doldu, komboyu sıfırla
        
        # Yanıp sönme timer
        if self.invincibility_timer > 0:
            self.invincibility_timer -= 1
        
        # Uçma modunda özel kontroller
        if self.fly_mode:
            self.vel_x = 0
            self.vel_y = 0
            self.is_moving = False
            
            fly_speed = PLAYER_SPEED * 2  # Uçarken daha hızlı
            
            if keys[pygame.K_LEFT]:
                self.vel_x = -fly_speed
                self.direction = -1
                self.is_moving = True
            if keys[pygame.K_RIGHT]:
                self.vel_x = fly_speed
                self.direction = 1
                self.is_moving = True
            if keys[pygame.K_UP]:
                self.vel_y = -fly_speed
                self.is_moving = True
            if keys[pygame.K_DOWN]:
                self.vel_y = fly_speed
                self.is_moving = True
            
            # Animasyon frame'i
            if self.is_moving:
                self.frame += 1
            else:
                self.frame = 0
            
            # Hareketi uygula (çarpışma kontrolü yok)
            self.rect.x += self.vel_x
            self.rect.y += self.vel_y
            
            # Level sınırları (sadece x ekseninde)
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > level_width:
                self.rect.right = level_width
            
            # Karakteri çiz
            self.image.fill((0, 0, 0, 0))
            draw_mario(self.image, 0, 0, self.direction, self.frame)
            return
        
        # Normal mod - orijinal kod
        # Yatay hareket
        self.vel_x = 0
        self.is_moving = False
        
        if keys[pygame.K_LEFT]:
            self.vel_x = -PLAYER_SPEED
            self.direction = -1
            self.is_moving = True
        if keys[pygame.K_RIGHT]:
            self.vel_x = PLAYER_SPEED
            self.direction = 1
            self.is_moving = True
        
        # Animasyon frame'i
        if self.is_moving:
            self.frame += 1
        else:
            self.frame = 0
            
        # Yatay hareketi uygula
        self.rect.x += self.vel_x
        
        # Level sınırları
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > level_width:
            self.rect.right = level_width
        
        # Yatay çarpışma kontrolü
        self._check_horizontal_collisions(platforms, blocks)
        
        # Yerçekimi
        self.vel_y += GRAVITY
        if self.vel_y > 15:
            self.vel_y = 15
            
        # Dikey hareketi uygula
        self.rect.y += self.vel_y
        
        # Dikey çarpışma kontrolü
        self.on_ground = False
        self._check_vertical_collisions(platforms, blocks)
        
        # Düşme kontrolü
        if self.rect.top > SCREEN_HEIGHT:
            self.die()
        
        # Karakteri çiz
        self.image.fill((0, 0, 0, 0))
        draw_mario(self.image, 0, 0, self.direction, self.frame)
    
    def _update_size(self):
        """Güç durumuna göre Mario'nun boyutunu güncelle"""
        old_bottom = self.rect.bottom
        old_centerx = self.rect.centerx
        
        if self.power_state.is_super():
            # Büyük Mario - 2 blok yüksekliğinde
            new_size = (32, 64)
        else:
            # Küçük Mario - 1 blok
            new_size = (32, 32)
        
        # Yeni boyutta surface oluştur
        self.image = pygame.Surface(new_size, pygame.SRCALPHA)
        
        # Rect'i güncelle ama pozisyonu koru
        old_rect = self.rect
        self.rect = self.image.get_rect()
        self.rect.centerx = old_centerx
        self.rect.bottom = old_bottom
    
    def use_power(self):
        """Space tuşu ile özel yetenek kullan"""
        if self.power_state.is_fire():
            # Ateş topu at
            if self.power_state.shoot_fire():
                from powers import Fireball
                fireball = Fireball(
                    self.rect.centerx,
                    self.rect.centery,
                    self.direction
                )
                self.fireballs.add(fireball)
                return True
        return False
    
    def collect_powerup(self, power_type):
        """Power-up topla ve boyutu güncelle"""
        old_power = self.power_state.current_power
        self.power_state.set_power(power_type)
        
        # Eğer güç değiştiyse boyutu güncelle
        if old_power != self.power_state.current_power or self.power_state.star_timer > 0:
            self._update_size()
    
    def take_damage(self):
        """Hasar al (düşman çarpması)"""
        # Zaten ölüyorsa veya yanıp sönüyorsa hasar alma
        if self.is_dying or self.invincibility_timer > 0:
            return
        
        # Güç varsa sadece güç kaybet
        if not self.power_state.take_damage():
            # Can kaybetmedi, sadece güç kaybetti - küçüldü
            self._update_size()  # Boyutu küçült
            self.invincibility_timer = 120  # 2 saniye yanıp sönme
            return
        
        # Gerçekten can kaybı - ölüm animasyonu başlat
        self.die()
            
    def die(self):
        """Öldü - Mario tarzı ölüm animasyonu"""
        self.lives -= 1
        self.is_dying = True
        self.death_jump_vel = -12  # Yukarı zıpla
        self.vel_x = 0
        self.vel_y = 0
    
    def add_score(self, points):
        """Skor ekle"""
        self.score += points
    
    def stomp_enemy(self, enemy):
        """Düşman ezildi - kombo sistemi"""
        # Kombo sayacını artır
        self.combo_count += 1
        self.combo_timer = 60  # 1 saniye içinde yeni ezme olmazsa sıfırla
        
        # Kombo puanı (her ezme daha fazla puan)
        combo_points = [100, 200, 400, 800, 1000, 2000, 4000, 8000]
        points_index = min(self.combo_count - 1, len(combo_points) - 1)
        points = combo_points[points_index]
        
        self.add_score(points)
        return points  # Ekranda göstermek için
                    
    def _check_horizontal_collisions(self, platforms, blocks):
        """Yatay çarpışmaları kontrol et"""
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_x > 0:
                    self.rect.right = platform.rect.left
                elif self.vel_x < 0:
                    self.rect.left = platform.rect.right
        
        for block in blocks:
            if self.rect.colliderect(block.rect):
                if self.vel_x > 0:
                    self.rect.right = block.rect.left
                elif self.vel_x < 0:
                    self.rect.left = block.rect.right
                    
    def _check_vertical_collisions(self, platforms, blocks):
        """Dikey çarpışmaları kontrol et"""
        # ÖNEMLİ: Önce blocks (özel davranışlı bloklar), sonra platforms
        
        for block in blocks:
            if self.rect.colliderect(block.rect):
                # Üstten mi alttan mı çarpıştığını anla
                overlap_top = self.rect.bottom - block.rect.top
                overlap_bottom = block.rect.bottom - self.rect.top
                
                if self.vel_y > 0 and overlap_top < overlap_bottom:
                    # Üstten düştü
                    self.rect.bottom = block.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0 and overlap_bottom < overlap_top:
                    # Alttan vurdu
                    if hasattr(block, 'hit'):
                        result = block.hit(self.direction)  # Mario'nun yönünü gönder
                        if result:
                            self.add_score(QUESTION_BLOCK_SCORE)
                    self.rect.top = block.rect.bottom
                    self.vel_y = 0
        
        for platform in platforms:
            # Blocks grubundaki platformları tekrar kontrol etme
            if platform in blocks:
                continue
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:
                    self.rect.top = platform.rect.bottom
                    self.vel_y = 0
    
    def _update_death_animation(self):
        """Mario tarzı ölüm animasyonu - yukarı zıplayıp aşağı düşme"""
        # Yukarı zıpla
        self.rect.y += self.death_jump_vel
        self.death_jump_vel += GRAVITY * 0.8  # Yerçekimi
        
        # Ekrandan çıktıysa animasyon bitti
        if self.rect.top > SCREEN_HEIGHT:
            self.is_dying = False
            # Respawn
            self.rect.x = 100
            self.rect.y = 100
            self.vel_y = 0
            self.vel_x = 0
            self.power_state.current_power = 0  # Küçük Mario'ya dön
            self._update_size()
            self.invincibility_timer = 180  # 3 saniye koruma
    
    def should_draw(self):
        """Yanıp sönme efekti için çizilmeli mi?"""
        if self.is_dying:
            return True  # Ölürken her zaman çiz
        if self.invincibility_timer > 0:
            # Yanıp sönme efekti
            return (self.invincibility_timer // 5) % 2 == 0
        return True
