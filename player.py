import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y, radius):
        # type: (float, float, float) -> None
        super().__init__(x, y, radius)
        self.rotation = 0
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90)
        right *= self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # type: (pygame.Surface) -> None
        pygame.draw.polygon(
            surface=screen,
            color='white',
            points=self.triangle(),
            width=2
        )

    def rotate(self, dt):
        # type: (float) -> None
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        # type: (float) -> None
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer > 0:
            return

        self.timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(
            x=self.position.x,
            y=self.position.y,
            radius=SHOT_RADIUS
        )
        velocity = pygame.Vector2(0, 1).rotate(self.rotation) * SHOT_SPEED
        shot.velocity = velocity

    def update(self, dt):
        # type: (float) -> None
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt=dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt=dt)
        if keys[pygame.K_w]:
            self.move(dt=dt)
        if keys[pygame.K_s]:
            self.move(dt=dt * -1)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.timer -= dt
