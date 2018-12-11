import pygame
from data import items, walls
class Wall:
    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
        walls.append(self)
        self.img = pygame.image.load('wall.png')