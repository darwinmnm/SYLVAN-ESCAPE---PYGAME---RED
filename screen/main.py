import pygame, sys

pygame.init()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 608

#BACKGROUND
background = pygame.image.load('background/background.png')
floor = pygame.image.load('background/floor.png')

#SCREEN
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SYLVAN ESCAPE')


isGameRunning = True
while isGameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameRunning = False
    pygame.display.update()

    screen.blit(background, (0, 0))
    screen.blit(floor, (-5, 75))

pygame.quit()

