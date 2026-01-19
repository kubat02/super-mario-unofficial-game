"""
Grafik çizim fonksiyonları
"""
import pygame
from config import *


def draw_mario(surface, x, y, direction, frame):
    """Animasyonlu Mario çizimi"""
    if direction == 1:  # Sağa bakıyor
        pygame.draw.rect(surface, RED, (x+8, y, 16, 8))
        pygame.draw.rect(surface, SKIN, (x+6, y+8, 20, 10))
        pygame.draw.rect(surface, BLACK, (x+16, y+10, 4, 4))
        pygame.draw.rect(surface, RED, (x+6, y-4, 22, 6))
        pygame.draw.rect(surface, WHITE, (x+12, y-2, 2, 2))
        pygame.draw.rect(surface, WHITE, (x+18, y-2, 2, 2))
        pygame.draw.rect(surface, RED, (x+8, y+18, 16, 10))
        pygame.draw.rect(surface, YELLOW, (x+14, y+20, 4, 4))
        pygame.draw.rect(surface, BLUE, (x+6, y+28, 8, 8))
        pygame.draw.rect(surface, BLUE, (x+18, y+28, 8, 8))
        pygame.draw.rect(surface, SKIN, (x+4, y+20, 4, 8))
        pygame.draw.rect(surface, SKIN, (x+24, y+20, 4, 8))
        pygame.draw.rect(surface, WHITE, (x+4, y+26, 4, 4))
        pygame.draw.rect(surface, WHITE, (x+24, y+26, 4, 4))
        
        if frame % 2 == 0:
            pygame.draw.rect(surface, BLUE, (x+6, y+36, 6, 8))
            pygame.draw.rect(surface, BLUE, (x+18, y+36, 6, 8))
        else:
            pygame.draw.rect(surface, BLUE, (x+8, y+36, 6, 8))
            pygame.draw.rect(surface, BLUE, (x+16, y+36, 6, 8))
        
        pygame.draw.rect(surface, BROWN, (x+4, y+44, 8, 4))
        pygame.draw.rect(surface, BROWN, (x+18, y+44, 8, 4))
    else:  # Sola bakıyor
        pygame.draw.rect(surface, RED, (x+8, y, 16, 8))
        pygame.draw.rect(surface, SKIN, (x+6, y+8, 20, 10))
        pygame.draw.rect(surface, BLACK, (x+12, y+10, 4, 4))
        pygame.draw.rect(surface, RED, (x+6, y-4, 22, 6))
        pygame.draw.rect(surface, WHITE, (x+12, y-2, 2, 2))
        pygame.draw.rect(surface, WHITE, (x+18, y-2, 2, 2))
        pygame.draw.rect(surface, RED, (x+8, y+18, 16, 10))
        pygame.draw.rect(surface, YELLOW, (x+14, y+20, 4, 4))
        pygame.draw.rect(surface, BLUE, (x+6, y+28, 8, 8))
        pygame.draw.rect(surface, BLUE, (x+18, y+28, 8, 8))
        pygame.draw.rect(surface, SKIN, (x+4, y+20, 4, 8))
        pygame.draw.rect(surface, SKIN, (x+24, y+20, 4, 8))
        pygame.draw.rect(surface, WHITE, (x+4, y+26, 4, 4))
        pygame.draw.rect(surface, WHITE, (x+24, y+26, 4, 4))
        
        if frame % 2 == 0:
            pygame.draw.rect(surface, BLUE, (x+6, y+36, 6, 8))
            pygame.draw.rect(surface, BLUE, (x+18, y+36, 6, 8))
        else:
            pygame.draw.rect(surface, BLUE, (x+8, y+36, 6, 8))
            pygame.draw.rect(surface, BLUE, (x+16, y+36, 6, 8))
        
        pygame.draw.rect(surface, BROWN, (x+4, y+44, 8, 4))
        pygame.draw.rect(surface, BROWN, (x+18, y+44, 8, 4))


def draw_goomba(surface, x, y, frame):
    """Goomba düşmanı çizimi"""
    pygame.draw.rect(surface, BROWN, (x+4, y+16, 24, 16))
    pygame.draw.ellipse(surface, BROWN, (x, y, 32, 20))
    
    if frame % 20 < 10:
        pygame.draw.rect(surface, WHITE, (x+8, y+8, 6, 6))
        pygame.draw.rect(surface, WHITE, (x+18, y+8, 6, 6))
        pygame.draw.rect(surface, BLACK, (x+10, y+10, 3, 3))
        pygame.draw.rect(surface, BLACK, (x+20, y+10, 3, 3))
    else:
        pygame.draw.rect(surface, WHITE, (x+6, y+8, 6, 6))
        pygame.draw.rect(surface, WHITE, (x+20, y+8, 6, 6))
        pygame.draw.rect(surface, BLACK, (x+8, y+10, 3, 3))
        pygame.draw.rect(surface, BLACK, (x+22, y+10, 3, 3))
    
    pygame.draw.rect(surface, BLACK, (x+8, y+6, 6, 2))
    pygame.draw.rect(surface, BLACK, (x+18, y+6, 6, 2))
    
    if frame % 10 < 5:
        pygame.draw.rect(surface, BROWN, (x+6, y+32, 8, 4))
        pygame.draw.rect(surface, BROWN, (x+18, y+32, 8, 4))
    else:
        pygame.draw.rect(surface, BROWN, (x+4, y+32, 8, 4))
        pygame.draw.rect(surface, BROWN, (x+20, y+32, 8, 4))


def draw_koopa(surface, x, y, direction, frame):
    """Koopa Troopa çizimi"""
    pygame.draw.ellipse(surface, GREEN, (x+2, y+8, 28, 24))
    pygame.draw.rect(surface, (0, 150, 0), (x+4, y+12, 24, 16))
    pygame.draw.circle(surface, YELLOW, (x+16, y+20), 8)
    pygame.draw.circle(surface, GREEN, (x+16, y+20), 5)
    
    if direction == 1:
        pygame.draw.rect(surface, YELLOW, (x+24, y+4, 12, 12))
        pygame.draw.rect(surface, BLACK, (x+30, y+8, 3, 3))
        pygame.draw.rect(surface, RED, (x+30, y+12, 4, 2))
    else:
        pygame.draw.rect(surface, YELLOW, (x-4, y+4, 12, 12))
        pygame.draw.rect(surface, BLACK, (x, y+8, 3, 3))
        pygame.draw.rect(surface, RED, (x-2, y+12, 4, 2))
    
    if frame % 10 < 5:
        pygame.draw.rect(surface, YELLOW, (x+4, y+30, 6, 6))
        pygame.draw.rect(surface, YELLOW, (x+22, y+30, 6, 6))
    else:
        pygame.draw.rect(surface, YELLOW, (x+2, y+30, 6, 6))
        pygame.draw.rect(surface, YELLOW, (x+24, y+30, 6, 6))


def draw_coin(surface, x, y, frame):
    """Animasyonlu coin çizimi"""
    width = abs(int(12 * pygame.math.Vector2(1, 0).rotate(frame * 6).x))
    if width < 2:
        width = 2
    pygame.draw.ellipse(surface, GOLD, (x+12-width//2, y, width, 24))
    pygame.draw.ellipse(surface, YELLOW, (x+12-width//2+2, y+2, max(1, width-4), 20))


def draw_brick(surface, x, y):
    """Tuğla bloğu çizimi"""
    pygame.draw.rect(surface, BRICK_RED, (x, y, 32, 32))
    pygame.draw.rect(surface, (200, 60, 60), (x+2, y+2, 28, 28))
    pygame.draw.line(surface, (100, 20, 20), (x, y+16), (x+32, y+16), 2)
    pygame.draw.line(surface, (100, 20, 20), (x+16, y), (x+16, y+16), 2)
    pygame.draw.line(surface, (100, 20, 20), (x+8, y+16), (x+8, y+32), 2)
    pygame.draw.line(surface, (100, 20, 20), (x+24, y+16), (x+24, y+32), 2)


def draw_question_block(surface, x, y, frame, active=True):
    """Soru işareti bloğu çizimi"""
    if active:
        pygame.draw.rect(surface, GOLD, (x, y, 32, 32))
        pygame.draw.rect(surface, YELLOW, (x+2, y+2, 28, 28))
        offset = 2 if (frame // 10) % 2 == 0 else 0
        pygame.draw.rect(surface, BROWN, (x+12, y+6-offset, 8, 4))
        pygame.draw.rect(surface, BROWN, (x+16, y+10-offset, 4, 4))
        pygame.draw.rect(surface, BROWN, (x+14, y+14-offset, 4, 4))
        pygame.draw.rect(surface, BROWN, (x+14, y+20-offset, 4, 4))
    else:
        pygame.draw.rect(surface, (100, 100, 100), (x, y, 32, 32))
        pygame.draw.rect(surface, (120, 120, 120), (x+2, y+2, 28, 28))


def draw_pipe(surface, x, y, height):
    """Boru çizimi"""
    pygame.draw.rect(surface, GREEN, (x, y, 64, height))
    pygame.draw.rect(surface, (0, 180, 0), (x+8, y, 48, height))
    pygame.draw.rect(surface, GREEN, (x-4, y-8, 72, 12))
    pygame.draw.rect(surface, (0, 120, 0), (x, y-6, 64, 8))
    pygame.draw.rect(surface, (0, 220, 0), (x+12, y, 4, height))


def draw_flag(surface, x, y):
    """Bayrak çizimi"""
    pygame.draw.rect(surface, WHITE, (x, y, 8, 300))
    for i in range(5):
        color = RED if i % 2 == 0 else WHITE
        pygame.draw.rect(surface, color, (x+8, y+i*12, 40, 12))
    pygame.draw.circle(surface, YELLOW, (x+4, y-8), 12)
