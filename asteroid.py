import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        # type: (float, float, float) -> None
        super().__init__(x, y, radius)

    def draw(self, screen):
        # type: (pygame.Surface) -> None
        pygame.draw.circle(
            surface=screen,
            color='white',
            center=self.position,
            radius=self.radius,
            width=2
        )

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        old_radius = self.radius
        angle = random.uniform(20, 50)
        vel1 = self.velocity.rotate(angle)
        vel2 = self.velocity.rotate(-angle)
        for vel in [vel1, vel2]:
            Asteroid(
                x=self.position.x,
                y=self.position.y,
                radius=old_radius - ASTEROID_MIN_RADIUS
            ).velocity = vel * 1.2

    def update(self, dt):
        # type: (float) -> None
        self.position += self.velocity * dt
