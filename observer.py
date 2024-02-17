import constants as CONST
from vector import Vector
class Observer():
    _mass = 100  # Mass not including potential energy
    energy = 10**20

    @classmethod
    @property
    def mass(cls) -> float:
        return cls._mass + cls.energy / CONST.SPEED_OF_LIGHT**2

    @classmethod
    def accelerate(cls) -> None:
        # Using F = ma
        # a = F / m
        # NOTE: this is non-relatavistic
        force = Vector(0, CONST.THRUST_FORCE)
        acceleration = force / cls.mass

        # v = u + at
        velocity = acceleration * CONST.SECONDS_PER_TICK

        for object in CONST.OBJECTS:
            # v = gamma*v0
            # need to multiply by gamma factor to take relatavistic effects into account
            gamma = 1 / (1 - (abs(object.velocity)/CONST.SPEED_OF_LIGHT)**2)**0.5
            object.velocity += velocity * gamma

        # When accelerating, the observer loses energy and mass
        # Energy lost = 1/2 mv^2
        energy_lost = 0.5 * cls.mass * abs(velocity)**2
        cls.energy -= energy_lost

        # Mass lost = energy lost / c^2
        cls.mass -= energy_lost / CONST.SPEED_OF_LIGHT**2
