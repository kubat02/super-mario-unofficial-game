"""
Ana oyun class'ı
"""
import pygame
import sys
import os
from config import *
from player import Player
from camera import Camera
from level import Level


class Game:
    """Super Mario oyunu"""
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Super Mario Bros")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        self.running = True
        self.game_over = False
        self.level_complete = False
        self.frame_count = 0
        self.current_world = 1  # Mevcut world
        self.current_level = 1  # Mevcut level
        self.max_worlds = 8  # 8 world var
        self.world_levels = self._count_world_levels()  # Her world'deki level sayısı
        self.all_levels_complete = False  # Tüm seviyeler tamamlandı mı
        
        # Oyun bileşenleri
        self.player = None
        self.camera = None
        self.level = None
        
        self._initialize_game()
    
    def _count_world_levels(self):
        """Her world'deki level sayısını hesapla"""
        world_levels = {}
        levels_dir = os.path.join(os.path.dirname(__file__), 'levels')
        
        for world_num in range(1, self.max_worlds + 1):
            world_dir = os.path.join(levels_dir, f'world{world_num}')
            if os.path.exists(world_dir):
                level_count = 0
                for filename in os.listdir(world_dir):
                    if filename.startswith('level') and filename.endswith('.py'):
                        try:
                            level_num = int(filename.replace('level', '').replace('.py', ''))
                            if level_num > level_count:
                                level_count = level_num
                        except ValueError:
                            pass
                world_levels[world_num] = level_count if level_count > 0 else 1
            else:
                world_levels[world_num] = 1  # Varsayılan
        
        return world_levels
    
    def _initialize_game(self):
        """Oyunu başlat"""
        # Player oluştur (eğer yoksa)
        if self.player is None:
            self.player = Player(100, 400)
        else:
            # Mevcut player'ı resetle
            self.player.rect.x = 100
            self.player.rect.y = 400
            self.player.vel_x = 0
            self.player.vel_y = 0
            self.player.fly_mode = False
        
        # Level oluştur
        self.level = Level()
        try:
            self.level.load_level(self.current_world, self.current_level)
            print(f"World {self.current_world}, Level {self.current_level} yüklendi!")
        except Exception as e:
            print(f"World {self.current_world}, Level {self.current_level} yüklenemedi: {e}")
            # Eğer seviye bulunamazsa world 1 level 1'i yükle
            self.current_world = 1
            self.current_level = 1
            self.level.load_level(1, 1)
        
        # Lakitu'lara player referansı ata
        from enemies import Lakitu
        for enemy in self.level.enemies:
            if isinstance(enemy, Lakitu):
                enemy.player_ref = self.player
        
        # Kamera oluştur
        self.camera = Camera(LEVEL_WIDTH, SCREEN_HEIGHT)
    
    def run(self):
        """Ana oyun döngüsü"""
        while self.running:
            self.clock.tick(FPS)
            self.frame_count += 1
            
            self._handle_events()
            
            if not self.game_over:
                self._update()
            
            self._render()
    
    def _handle_events(self):
        """Event'leri işle"""
        keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                # UP tuşu - Zıplama
                if event.key == pygame.K_UP and not self.game_over and not self.level_complete:
                    if self.player.on_ground:
                        self.player.vel_y = JUMP_STRENGTH
                
                # SPACE tuşu - Özel güç kullan
                if event.key == pygame.K_SPACE and not self.game_over and not self.level_complete:
                    self.player.use_power()
                
                if event.key == pygame.K_r and (self.game_over or self.level_complete or self.all_levels_complete):
                    self._restart_game()
                
                # Ctrl+0 ile uçma modunu aç/kapat
                if event.key == pygame.K_0 and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                    self.player.fly_mode = not self.player.fly_mode
                    print(f"Developer Fly Mode: {'ON' if self.player.fly_mode else 'OFF'}")
    
    def _update(self):
        """Oyunu güncelle"""
        # Level tamamlandıktan sonra 2 saniye bekle ve sonraki levele geç
        if self.level_complete:
            if self.frame_count > FPS * 2:  # 2 saniye
                self._load_next_level()
            return
        
        # Player'ı güncelle
        self.player.update(
            self.level.platforms,
            self.level.enemies,
            self.level.coins,
            self.level.blocks,
            LEVEL_WIDTH
        )
        
        # Level'i güncelle
        self.level.update()
        
        # Kamerayı güncelle
        self.camera.update(self.player)
        
        # Coin toplama
        collected_coins = pygame.sprite.spritecollide(self.player, self.level.coins, True)
        for coin in collected_coins:
            self.player.add_score(COIN_SCORE)
        
        # PowerUp toplama
        collected_powerups = pygame.sprite.spritecollide(self.player, self.level.powerups, True)
        for powerup in collected_powerups:
            self.player.collect_powerup(powerup.power_type)  # Boyut güncelleme ile
            self.player.add_score(1000)  # PowerUp puanı
        
        # Düşman çarpışması
        enemy_hits = pygame.sprite.spritecollide(self.player, self.level.enemies, False)
        keys = pygame.key.get_pressed()
        for enemy in enemy_hits:
            if enemy.alive:
                # Lakitu yumurta çarpışması kontrol et
                if hasattr(enemy, 'get_eggs_for_collision'):
                    for egg in enemy.get_eggs_for_collision():
                        if egg.alive and self.player.rect.colliderect(egg.rect):
                            # Yumurtaya çarptı - hasar al
                            if not self.player.power_state.is_invincible():
                                self.player.take_damage()
                                egg.alive = False
                                if self.player.lives <= 0:
                                    self.game_over = True
                
                # Koopa kabuğu kontrolü
                if hasattr(enemy, 'in_shell') and enemy.in_shell:
                    # Hareketsiz kabuk - tekmeleme
                    if not enemy.shell_moving:
                        # Sağdan mı soldan mı vurduk?
                        if self.player.rect.centerx < enemy.rect.centerx:
                            enemy.kick_shell(1)  # Sağa tekmelendi
                        else:
                            enemy.kick_shell(-1)  # Sola tekmelendi
                        self.player.add_score(100)
                        continue
                    # Hareket eden kabuk - çarpıldı
                    elif enemy.shell_moving:
                        # Yenilmezse veya üstten basarsa kabuğu durdur
                        if self.player.power_state.is_invincible():
                            enemy.shell_moving = False
                            enemy.vel_x = 0
                            continue
                        elif self.player.vel_y > 0 and self.player.rect.bottom <= enemy.rect.centery:
                            enemy.shell_moving = False
                            enemy.vel_x = 0
                            if keys[pygame.K_UP]:
                                self.player.vel_y = -18
                            else:
                                self.player.vel_y = -10
                            points = self.player.stomp_enemy(enemy)
                            continue
                        else:
                            # Hareket eden kabuğa çarptı - hasar al
                            self.player.take_damage()
                            if self.player.lives <= 0:
                                self.game_over = True
                            continue
                
                # Yenilmezse düşmanı direkt öldür
                if self.player.power_state.is_invincible():
                    enemy.stomp()
                    self.player.add_score(ENEMY_STOMP_SCORE)
                # Üstüne basma
                elif self.player.vel_y > 0 and self.player.rect.bottom <= enemy.rect.centery:
                    result = enemy.stomp()
                    
                    # Piranha veya Spiny - ezilmez!
                    if result == 'no_stomp':
                        # Hasar al
                        self.player.take_damage()
                        if self.player.lives <= 0:
                            self.game_over = True
                    # Koopa kabuk oldu mu?
                    elif result == 'shell':
                        points = self.player.stomp_enemy(enemy)
                        # Yukarı tuşuna basılıysa daha yüksek zıpla
                        if keys[pygame.K_UP]:
                            self.player.vel_y = -18
                        else:
                            self.player.vel_y = -10
                    else:
                        # Normal düşman öldü
                        points = self.player.stomp_enemy(enemy)
                        if keys[pygame.K_UP]:
                            self.player.vel_y = -18
                        else:
                            self.player.vel_y = -10
                else:
                    # Çarpışma - hasar al
                    self.player.take_damage()
                    if self.player.lives <= 0:
                        self.game_over = True
        
        # Ateş topu - düşman çarpışması
        for fireball in self.player.fireballs:
            fireball_hits = pygame.sprite.spritecollide(fireball, self.level.enemies, False)
            for enemy in fireball_hits:
                if enemy.alive:
                    enemy.stomp()
                    fireball.alive = False
                    fireball.kill()
                    self.player.add_score(ENEMY_STOMP_SCORE)
        
        # Level tamamlama
        if self.player.rect.right >= self.level.flag.rect.left:
            if not self.level_complete:
                self.level_complete = True
                self.frame_count = 0  # Timer'ı resetle
    
    def _render(self):
        """Ekrana çiz"""
        # Level temasına göre arkaplan
        self.screen.fill(self.level.background_color)
        
        # Tüm sprite'ları çiz
        for sprite in self.level.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        
        # Lakitu yumurtalarını çiz
        from enemies import Lakitu
        for enemy in self.level.enemies:
            if isinstance(enemy, Lakitu) and hasattr(enemy, 'eggs'):
                for egg in enemy.eggs:
                    if egg.alive:
                        self.screen.blit(egg.image, self.camera.apply(egg))
        
        # PowerUp'ları çiz (draw metodu ile)
        camera_x = self.camera.camera.x
        for powerup in self.level.powerups:
            powerup.draw(self.screen, camera_x)
        
        # Player'ı çiz (yanıp sönme efekti ile)
        if self.player.should_draw():
            self.screen.blit(self.player.image, self.camera.apply(self.player))
        
        # Ateş toplarını çiz
        for fireball in self.player.fireballs:
            self.screen.blit(fireball.image, self.camera.apply(fireball))
        
        # UI çiz
        self._render_ui()
        
        pygame.display.flip()
    
    def _render_ui(self):
        """UI elementlerini çiz"""
        # Can ve skor
        lives_text = self.font.render(f"MARIO  x{self.player.lives}", True, WHITE)
        score_text = self.font.render(f"SCORE", True, WHITE)
        score_value = self.font.render(f"{self.player.score:06d}", True, WHITE)
        world_text = self.small_font.render(f"WORLD {self.current_world}-{self.current_level}", True, WHITE)
        
        self.screen.blit(lives_text, (20, 20))
        self.screen.blit(score_text, (SCREEN_WIDTH - 200, 20))
        self.screen.blit(score_value, (SCREEN_WIDTH - 200, 50))
        self.screen.blit(world_text, (SCREEN_WIDTH//2 - 50, 20))
        
        # Güç durumu göstergesi
        power_text = ""
        power_color = WHITE
        if self.player.power_state.is_invincible():
            power_text = "★ STAR ★"
            power_color = (255, 215, 0)
        elif self.player.power_state.is_fire():
            power_text = "🔥 FIRE"
            power_color = (255, 100, 0)
        elif self.player.power_state.is_super():
            power_text = "⬆ SUPER"
            power_color = (0, 255, 0)
        
        if power_text:
            power_display = self.small_font.render(power_text, True, power_color)
            self.screen.blit(power_display, (20, 60))
        
        # Uçma modu göstergesi
        if self.player.fly_mode:
            fly_text = self.small_font.render("FLY MODE (DEV)", True, (255, 255, 0))
            self.screen.blit(fly_text, (SCREEN_WIDTH//2 - 70, 45))
        
        # Game over mesajı
        if self.game_over:
            game_over_text = self.font.render("GAME OVER!", True, WHITE)
            restart_text = self.small_font.render("Press R to Restart", True, WHITE)
            self.screen.blit(game_over_text, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 50))
            self.screen.blit(restart_text, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2))
        
        # Level complete mesajı
        if self.level_complete:
            win_text = self.font.render("LEVEL COMPLETE!", True, WHITE)
            if self.current_level < self.max_level:
                next_text = self.small_font.render(f"Loading Level {self.current_level + 1}...", True, WHITE)
                self.screen.blit(win_text, (SCREEN_WIDTH//2 - 130, SCREEN_HEIGHT//2 - 50))
                self.screen.blit(next_text, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2))
            else:
                self.screen.blit(win_text, (SCREEN_WIDTH//2 - 130, SCREEN_HEIGHT//2 - 50))
        
        # Tüm seviyeler tamamlandı
        if self.all_levels_complete:
            congrats_text = self.font.render("ALL LEVELS COMPLETE!", True, (255, 215, 0))
            score_text = self.font.render(f"Final Score: {self.player.score}", True, WHITE)
            restart_text = self.small_font.render("Press R to Play Again", True, WHITE)
            self.screen.blit(congrats_text, (SCREEN_WIDTH//2 - 160, SCREEN_HEIGHT//2 - 70))
            self.screen.blit(score_text, (SCREEN_WIDTH//2 - 120, SCREEN_HEIGHT//2 - 20))
            self.screen.blit(restart_text, (SCREEN_WIDTH//2 - 110, SCREEN_HEIGHT//2 + 20))
    
    def _load_next_level(self):
        """Sonraki seviyeyi yükle (world sistemi)"""
        # Önce level'i arttır
        self.current_level += 1
        
        # Bu world'de bu level var mı?
        max_level_in_world = self.world_levels.get(self.current_world, 1)
        
        if self.current_level > max_level_in_world:
            # Bu world'ün levelleri bitti - sonraki world'e geç
            self.current_world += 1
            self.current_level = 1
            
            if self.current_world > self.max_worlds:
                # Tüm worldler tamamlandı!
                self.all_levels_complete = True
                self.level_complete = False
                print(f"Tüm {self.max_worlds} world tamamlandı! Oyunu bitirdin!")
                return
        
        # Sonraki world/level'i yükle
        self.level_complete = False
        self.frame_count = 0
        self._initialize_game()
        print(f"Yeni level: World {self.current_world}-{self.current_level}")
    
    def _restart_game(self):
        """Oyunu yeniden başlat"""
        self.game_over = False
        self.level_complete = False
        self.all_levels_complete = False
        self.frame_count = 0
        self.current_world = 1
        self.current_level = 1
        self.player = None  # Player'ı sıfırla
        self._initialize_game()
    
    def quit(self):
        """Oyundan çık"""
        pygame.quit()
        sys.exit()
