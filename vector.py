from __future__ import annotations

class Vector():
    __slots__ = ("x", "y")
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, multiplier: float) -> Vector:
        return Vector(self.x * multiplier, self.y * multiplier)

    def __truediv__(self, divisor: float) -> Vector:
        return Vector(self.x / divisor, self.y / divisor)

    def __abs__(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def tuple(self) -> tuple:
        return self.x, self.y

    def dist_to(self, other) -> float:
        return abs(other - self)

    def __format__(self, __format_spec: str) -> str:
        if __format_spec == ",":
            return f"({self.x:,}, {self.y:,})"
        else:
            raise TypeError

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
