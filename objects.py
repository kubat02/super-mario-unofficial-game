"""
Oyun objeleri - platformlar, bloklar, coinler
"""
import pygame
from config import *
from renderer import *


class Platform(pygame.sprite.Sprite):
    """Platform"""
    
    def __init__(self, x, y, width, height, block_type='ground'):
        super().__init__()
        self.block_type = block_type
        self.image = pygame.Surface((width, height))
        if block_type == 'ground':
            self.image.fill(GREEN)
            for i in range(0, width, 16):
                pygame.draw.rect(self.image, (0, 180, 0), (i, 0, 8, 8))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Coin(pygame.sprite.Sprite):
    """Altın"""
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((24, 24), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.frame = 0
        
    def update(self):
        self.frame += 1
        self.image.fill((0, 0, 0, 0))
        draw_coin(self.image, 0, 0, self.frame)


class QuestionBlock(pygame.sprite.Sprite):
    """Soru işareti bloğu"""
    
    def __init__(self, x, y, coin_group=None, all_sprites_group=None):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.active = True
        self.frame = 0
        self.coin_group = coin_group
        self.all_sprites_group = all_sprites_group
        
    def update(self):
        self.frame += 1
        self.image.fill((0, 0, 0, 0))
        draw_question_block(self.image, 0, 0, self.frame, self.active)
    
    def hit(self):
        """Bloğa vuruldu"""
        if self.active:
            self.active = False
            # Coin spawn
            if self.coin_group is not None and self.all_sprites_group is not None:
                coin = Coin(self.rect.x, self.rect.y - 40)
                self.coin_group.add(coin)
                self.all_sprites_group.add(coin)
            return True
        return False


class Brick(pygame.sprite.Sprite):
    """Tuğla bloğu"""
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        draw_brick(self.image, 0, 0)


class Pipe(pygame.sprite.Sprite):
    """Boru"""
    
    def __init__(self, x, y, height):
        super().__init__()
        self.image = pygame.Surface((64, height + 12), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - 8
        self.image.fill((0, 0, 0, 0))
        draw_pipe(self.image, 0, 8, height)


class Flag(pygame.sprite.Sprite):
    """Bayrak (level sonu)"""
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((48, 320), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        draw_flag(self.image, 0, 0)
