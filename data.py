import pygame
items = []
walls = []
screen = pygame.display.set_mode((800, 600))
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
def billboard(message, x, y):
    text = myfont.render(message, False, (255, 255, 255))
    screen.blit(text, (x, y))