import pygame
from collections.abc import Callable
import constants as CONST
from observer import Observer
from objects import Object
from vector import Vector

font = pygame.font.SysFont("consolas", 20)
INDENT = 8

class Stat():
    __slots__ = ("text", "get_value")
    def __init__(self, text: str, get_value: Callable[[], str | int]) -> None:
        self.text = text
        self.get_value = get_value

    def draw(self, position: tuple[int, int]) -> int:
        label = font.render(f"{self.text}: {self.get_value():,}", True, CONST.WHITE)
        CONST.WIN.blit(label, position)
        return label.get_height()

class ObjectStat(Stat):
    def draw(self, object: Object, position: tuple[int, int]) -> int:
        label = font.render(f"{self.text}: {self.get_value(object):,}", True, CONST.WHITE)
        position = (CONST.WIN.get_width() - label.get_width() - position[0], position[1])
        CONST.WIN.blit(label, position)
        return label.get_height()

stats = [
    Stat("Tick Rate", lambda: CONST.TICK_RATE),
    Stat("Meters per Pixel", lambda: 1 / CONST.PIXELS_PER_METER),
    Stat("Mass", lambda: Observer.mass),
    Stat("Potential Energy", lambda: Observer.energy),
    Stat("Force of Thrusters", lambda: CONST.THRUST_FORCE)
]

object_stats = [
    ObjectStat("Rest Mass", lambda obj: obj.mass),
    ObjectStat("Mass", lambda obj: obj.mass / (1 - (abs(obj.velocity) / CONST.SPEED_OF_LIGHT)**2)**0.5),
    ObjectStat("Position", lambda obj: obj.position),
    ObjectStat("Velocity", lambda obj: obj.velocity),
    ObjectStat("Speed", lambda obj: abs(obj.velocity))
]

def draw_stats() -> None:
    # Draw observer stats
    height = INDENT
    for stat in stats:
        label_height = stat.draw((INDENT, height))
        height += label_height

    # Draw stats for object that mouse is hovering over
    mouse = Vector(*pygame.mouse.get_pos())
    mouse -= CONST.MIDPOINT()
    mouse /= CONST.PIXELS_PER_METER
    for object in CONST.OBJECTS:
        if mouse.dist_to(object.position) < 20 / CONST.PIXELS_PER_METER:
            height = INDENT
            for stat in object_stats:
                label_height = stat.draw(object, (INDENT, height))
                height += label_height

            break
