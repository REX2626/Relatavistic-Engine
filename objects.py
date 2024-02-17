import pygame
import constants as CONST
from vector import Vector

class Object():
    __slots__ = ("mass", "position", "velocity")
    def __init__(self, mass: float, position: Vector, velocity: Vector) -> None:
        self.mass = mass
        self.position = position
        self.velocity = velocity

    def update(self) -> None:
        # Apply velocity to position
        # As the time per tick is small, we assume a == 0
        # S = ut + 1/2 at^2 can be approximated to:
        # S = ut
        self.position += self.velocity * CONST.SECONDS_PER_TICK

    def draw(self) -> None:
        # Radius is proportional to the square root of mass
        radius = self.mass**0.5
        pygame.draw.circle(CONST.WIN, CONST.GREY, (self.position + CONST.MIDPOINT()).tuple(), radius)
