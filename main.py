import pygame
from player import Player
from wall import Wall
from weapon import Weapon
from levels import parse_level
from levels import Levels
from data import items, walls, screen

def run():
    pygame.init()  # choose a better size later
    clock = pygame.time.Clock()
    bg = pygame.image.load('background.png')

    player = Player()
    parse_level(Levels[1])
    running = True
    while running:
        clock.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
        # Move the player if an arrow key is pressed
        player.update_position()
        # Draw the scene
        screen.fill((0, 0, 0))
        for wall in walls:
            pygame.draw.rect(screen, (255, 255, 255), wall.rect)
            screen.blit(wall.img, (wall.rect.x, wall.rect.y))
        for item in items:
            pygame.draw.rect(screen, item.color, item.rect)
        player.player_update()
        pygame.display.flip()

run()