import pygame
import constants as CONST
from vector import Vector

class Object():
    __slots__ = ("mass", "position", "velocity")
    def __init__(self, mass: float, position: Vector, velocity: Vector) -> None:
        self.mass = mass
        self.position = position
        self.velocity = velocity

    def draw(self) -> None:
        pygame.draw.circle(CONST.WIN, CONST.GREY, (self.position + CONST.MIDPOINT()).tuple(), 10)
