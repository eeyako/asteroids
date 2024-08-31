import os
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    os.environ['SDL_VIDEO_WINDOW_POS'] = f'{SCREEN_POS_X},{SCREEN_POS_Y}'
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)

    # Initialize objects
    AsteroidField()
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

        for each in updatable:
            each.update(dt=dt)

        for each in asteroids:
            if each.is_colliding(player):
                print('Game over!')
                sys.exit()

        for each in drawable:
            each.draw(screen=screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == '__main__':
    main()
