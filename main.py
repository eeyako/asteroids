import os
import pygame
from constants import *

def main():
    os.environ['SDL_VIDEO_WINDOW_POS'] = f'{SCREEN_POS_X},{SCREEN_POS_Y}'
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color='black')
        pygame.display.flip()


if __name__ == '__main__':
    main()