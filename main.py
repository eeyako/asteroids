import os
import sys

import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape  # noqa: F401
from constants import (
    PLAYER_RADIUS,
    SCREEN_HEIGHT,
    SCREEN_POS_X,
    SCREEN_POS_Y,
    SCREEN_WIDTH,
)
from player import Player
from shot import Shot


def main():
    os.environ["SDL_VIDEO_WINDOW_POS"] = f"{SCREEN_POS_X},{SCREEN_POS_Y}"
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create groups
    updateables = pygame.sprite.Group()  # type: list[CircleShape]
    drawables = pygame.sprite.Group()  # type: list[CircleShape]
    asteroids = pygame.sprite.Group()  # type: list[CircleShape]
    shots = pygame.sprite.Group()  # type: list[CircleShape]

    # Assign containers
    AsteroidField.containers = (updateables,)
    Asteroid.containers = (asteroids, updateables, drawables)
    Shot.containers = (shots, updateables, drawables)
    Player.containers = (updateables, drawables)

    # Initialize objects
    AsteroidField()
    player = Player(
        x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2, radius=PLAYER_RADIUS
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color="black")

        for updatable in updateables:
            updatable.update(dt=dt)

        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.is_colliding(shot):
                    asteroid.split()
                    shot.kill()

        for drawable in drawables:
            drawable.draw(screen=screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
