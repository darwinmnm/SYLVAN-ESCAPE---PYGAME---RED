import pygame
from src.obstacles import SpriteAnimation
import random

def load_random_obstacle(melon_filename, pumpkin_filename):
    obstacle_type = random.choice(["melon", "pumpkin"])
    x = 1080

    if obstacle_type == "melon":
        animation = SpriteAnimation(melon_filename)
    else:
        animation = SpriteAnimation(pumpkin_filename)

    return animation, obstacle_type, x

def main():
    pygame.init()

    width, height = 1080, 608
    screen = pygame.display.set_mode((width, height))
    background = pygame.image.load('background/background.png')
    floor = pygame.image.load('background/floor.png')
    pygame.display.set_caption('SYLVAN ESCAPE')

    melon_filename = 'asset/melon/animation_melon.png' 
    pumpkin_filename = 'asset/pumkin/animation_pumkin.png'

    animation, obstacle_type, x = load_random_obstacle(melon_filename, pumpkin_filename)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(background, (0, 0))
        screen.blit(floor, (-5, 75))

        animation.update()
        animation.draw(screen)

        if x <= -34:
            animation, obstacle_type, x = load_random_obstacle(melon_filename, pumpkin_filename)
        x -= 5

        pygame.display.flip()

        clock.tick(30)

if __name__ == "__main__":
    main()
