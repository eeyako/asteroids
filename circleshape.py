from __future__ import annotations
from abc import abstractmethod
import pygame

# Base class for game objects


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # type: (float, float, float) -> None
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    @abstractmethod
    def draw(self, screen):
        # type: (pygame.Surface) -> None
        pass

    @abstractmethod
    def update(self, dt):
        # type: (float) -> None
        pass

    def is_colliding(self, other):
        # type: (CircleShape) -> bool
        distance = self.position.distance_to(other.position)
        return distance < self.radius + other.radius
