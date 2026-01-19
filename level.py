"""
Level yapısı ve level builder
"""
from objects import *
from enemies import Goomba, Koopa, PiranhaPlant, BulletBill, Spiny, Lakitu
from powers import PowerUp, PowerUpType, Mushroom, FireFlower, Star
import importlib


class Level:
    """Oyun seviyesi"""
    
    def __init__(self):
        self.platforms = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.question_blocks = pygame.sprite.Group()
        self.pipes = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()  # Güç objeleri
        self.all_sprites = pygame.sprite.Group()
        self.flag = None
        self.theme = 'overworld'  # Level teması: 'overworld', 'underground', 'castle', vb.
        self.background_color = SKY_BLUE  # Arkaplan rengi
    
    def load_level(self, world_number=1, level_number=1):
        """Belirtilen world ve seviyeyi yükle"""
        # World ve level kontrolü
        try:
            # Yeni world sistemi: levels.worldX.levelY
            level_module = importlib.import_module(f'levels.world{world_number}.level{level_number}')
            level_data = level_module.LEVEL_DATA
        except (ImportError, ModuleNotFoundError):
            # Eğer bulunamazsa, eski sistemi dene (geriye dönük uyumluluk)
            try:
                level_module = importlib.import_module(f'levels.level{level_number}')
                level_data = level_module.LEVEL_DATA
            except (ImportError, ModuleNotFoundError):
                print(f"World {world_number}, Level {level_number} bulunamadı! Varsayılan level yükleniyor.")
                # Varsayılan basit level
                level_data = [
                    ('platform', 400, 528, 200, 32),
                    ('question', 500, 400),
                    ('goomba', 450, 496),
                ]
                level_module = None
        
        # Tema bilgisini yükle (varsa)
        if level_module and hasattr(level_module, 'LEVEL_THEME'):
            self.theme = level_module.LEVEL_THEME
            self._apply_theme()
        else:
            self.theme = 'overworld'
            self.background_color = SKY_BLUE
        
        # Zemin oluştur
        for i in range(0, LEVEL_WIDTH, 32):
            platform = Platform(i, 560, 32, 40, 'ground')
            self.platforms.add(platform)
            self.all_sprites.add(platform)
        
        # Seviye objelerini oluştur
        for obj in level_data:
            self._create_object(obj)
        
        # Bayrak
        self.flag = Flag(5700, 240)
        self.all_sprites.add(self.flag)
    
    def _apply_theme(self):
        """Temaya göre arkaplan rengini ayarla"""
        theme_colors = {
            'overworld': SKY_BLUE,  # Bahçe/dış mekan - klasik mavi gökyüzü
            'underground': (20, 20, 20),  # Yeraltı - karanlık
            'underwater': (0, 50, 100),  # Su altı - koyu mavi
            'castle': (40, 20, 20),  # Kale - karanlık kırmızımsı
            'snow': (200, 220, 255),  # Kar - açık mavi-beyaz
        }
        self.background_color = theme_colors.get(self.theme, SKY_BLUE)
        
    def build_level_1(self):
        """Level 1'i oluştur - geriye dönük uyumluluk için"""
        self.load_level(1)
    
    def _create_object(self, obj_data):
        """Obje oluştur"""
        obj_type = obj_data[0]
        
        if obj_type == 'platform':
            obj = Platform(obj_data[1], obj_data[2], obj_data[3], obj_data[4])
            self.platforms.add(obj)
            self.all_sprites.add(obj)
            
        elif obj_type == 'question':
            obj = QuestionBlock(obj_data[1], obj_data[2], self.coins, self.all_sprites, 'coin', self.powerups)
            self.question_blocks.add(obj)
            self.blocks.add(obj)
            self.platforms.add(obj)
            self.all_sprites.add(obj)
        
        elif obj_type == 'question_mushroom':
            # Mantar içeren soru bloğu
            obj = QuestionBlock(obj_data[1], obj_data[2], self.coins, self.all_sprites, 'mushroom', self.powerups)
            self.question_blocks.add(obj)
            self.blocks.add(obj)
            self.platforms.add(obj)
            self.all_sprites.add(obj)
        
        elif obj_type == 'question_fireflower':
            # Fire Flower içeren soru bloğu
            obj = QuestionBlock(obj_data[1], obj_data[2], self.coins, self.all_sprites, 'fire_flower', self.powerups)
            self.question_blocks.add(obj)
            self.blocks.add(obj)
            self.platforms.add(obj)
            self.all_sprites.add(obj)
        
        elif obj_type == 'question_star':
            # Star içeren soru bloğu
            obj = QuestionBlock(obj_data[1], obj_data[2], self.coins, self.all_sprites, 'star', self.powerups)
            self.question_blocks.add(obj)
            self.blocks.add(obj)
            self.platforms.add(obj)
            self.all_sprites.add(obj)
            
        elif obj_type == 'brick':
            obj = Brick(obj_data[1], obj_data[2])
            self.blocks.add(obj)
            self.platforms.add(obj)
            self.all_sprites.add(obj)
            
        elif obj_type == 'pipe':
            obj = Pipe(obj_data[1], obj_data[2], obj_data[3])
            self.pipes.add(obj)
            self.blocks.add(obj)
            self.platforms.add(obj)
            self.all_sprites.add(obj)
            
        elif obj_type == 'goomba':
            # Stationary parametresi varsa kullan
            stationary = obj_data[3] if len(obj_data) > 3 else False
            obj = Goomba(obj_data[1], obj_data[2], stationary)
            self.enemies.add(obj)
            self.all_sprites.add(obj)
            
        elif obj_type == 'goomba_stationary':
            # Yerinde duran goomba (kısa yol)
            obj = Goomba(obj_data[1], obj_data[2], stationary=True)
            self.enemies.add(obj)
            self.all_sprites.add(obj)
            
        elif obj_type == 'koopa':
            # Stationary parametresi varsa kullan
            stationary = obj_data[3] if len(obj_data) > 3 else False
            obj = Koopa(obj_data[1], obj_data[2], stationary)
            self.enemies.add(obj)
            self.all_sprites.add(obj)
            
        elif obj_type == 'koopa_stationary':
            # Yerinde duran koopa (kısa yol)
            obj = Koopa(obj_data[1], obj_data[2], stationary=True)
            self.enemies.add(obj)
            self.all_sprites.add(obj)
        
        elif obj_type == 'piranha':
            # Piranha Plant - boru yüksekliği opsiyonel
            pipe_height = obj_data[3] if len(obj_data) > 3 else 64
            obj = PiranhaPlant(obj_data[1], obj_data[2], pipe_height)
            self.enemies.add(obj)
            self.all_sprites.add(obj)
        
        elif obj_type == 'bullet_bill':
            # Bullet Bill - yön opsiyonel (default: -1 sola)
            direction = obj_data[3] if len(obj_data) > 3 else -1
            obj = BulletBill(obj_data[1], obj_data[2], direction)
            self.enemies.add(obj)
            self.all_sprites.add(obj)
        
        elif obj_type == 'spiny':
            # Spiny - stationary opsiyonel
            stationary = obj_data[3] if len(obj_data) > 3 else False
            obj = Spiny(obj_data[1], obj_data[2], stationary)
            self.enemies.add(obj)
            self.all_sprites.add(obj)
        
        elif obj_type == 'lakitu':
            # Lakitu - player referansı gerekli (update sırasında verilecek)
            obj = Lakitu(obj_data[1], obj_data[2], player_ref=None, enemy_group=self.enemies)
            self.enemies.add(obj)
            self.all_sprites.add(obj)
            
        elif obj_type == 'coin':
            obj = Coin(obj_data[1], obj_data[2])
            self.coins.add(obj)
            self.all_sprites.add(obj)
        
        elif obj_type == 'mushroom':
            # Super Mushroom
            obj = Mushroom(obj_data[1], obj_data[2])
            self.powerups.add(obj)
            self.all_sprites.add(obj)
        
        elif obj_type == 'fireflower':
            # Fire Flower
            obj = FireFlower(obj_data[1], obj_data[2])
            self.powerups.add(obj)
            self.all_sprites.add(obj)
        
        elif obj_type == 'star':
            # Star
            obj = Star(obj_data[1], obj_data[2])
            self.powerups.add(obj)
            self.all_sprites.add(obj)
    
    def update(self):
        """Level'i güncelle"""
        # Düşmanları güncelle - birbirleriyle çarpışmaları için tüm düşman listesini ver
        platforms_and_blocks = list(self.platforms) + list(self.blocks)
        enemy_list = list(self.enemies)
        
        for enemy in self.enemies:
            enemy.update(platforms_and_blocks, enemy_list)
        
        for coin in self.coins:
            coin.update()
        
        for qblock in self.question_blocks:
            qblock.update()
        
        for powerup in self.powerups:
            powerup.update(platforms_and_blocks)
