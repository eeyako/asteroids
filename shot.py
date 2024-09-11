import pygame
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        # type: (float, float, float) -> None
        super().__init__(x, y, radius)

    def draw(self, screen):
        # type: (pygame.Surface) -> None
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=2,
        )

    def update(self, dt):
        # type: (float) -> None
        self.position += self.velocity * dt
