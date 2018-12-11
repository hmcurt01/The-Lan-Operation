import pygame
from data import items, walls
class Weapon:
    def __init__(self, pos, color, weapon_type):
        self.rect = pygame.Rect(pos[0], pos[1], 8, 8)
        items.append(self)
        self.weapon_name = weapon_type
        self.color = color