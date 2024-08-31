import os
import pygame
from constants import *
from player import Player


def main():
    os.environ['SDL_VIDEO_WINDOW_POS'] = f'{SCREEN_POS_X},{SCREEN_POS_Y}'
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(
        x=SCREEN_WIDTH / 2,
        y=SCREEN_HEIGHT / 2,
        radius=PLAYER_RADIUS
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color='black')
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == '__main__':
    main()
