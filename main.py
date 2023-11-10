import pygame 

pygame.init()

#BACKGROUND
background = pygame.image.load('background.png')

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540

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

pygame.quit()

