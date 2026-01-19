"""
Düşman karakterleri - modüler yapı
"""
from .base import Enemy
from .goomba import Goomba
from .koopa import Koopa
from .piranha import PiranhaPlant
from .bullet_bill import BulletBill
from .spiny import Spiny
from .lakitu import Lakitu, SpinyEgg

__all__ = ['Enemy', 'Goomba', 'Koopa', 'PiranhaPlant', 'BulletBill', 'Spiny', 'Lakitu', 'SpinyEgg']
