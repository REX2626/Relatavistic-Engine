import constants as CONST
from vector import Vector
class Observer():
    mass = 100
    energy = 100

    @classmethod
    def accelerate(cls) -> None:
        # Using F = ma
        # a = F / m
        force = Vector(0, 1000)
        acceleration = force / cls.mass

        for object in CONST.OBJECTS:
            # v = u + at
            object.velocity += acceleration * CONST.SECONDS_PER_TICK
