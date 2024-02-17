import pygame
from collections.abc import Callable
import constants as CONST
from observer import Observer

font = pygame.font.SysFont("consolas", 20)
INDENT = 8

class Stat():
    __slots__ = ("text", "get_value")
    def __init__(self, text: str, get_value: Callable[[], str | int]) -> None:
        self.text = text
        self.get_value = get_value

    def draw(self, position: tuple[int, int]) -> int:
        label = font.render(f"{self.text}: {self.get_value()}", True, CONST.WHITE)
        CONST.WIN.blit(label, position)
        return label.get_height()

stats = [
    Stat("Mass", lambda: Observer.mass)
]

def draw_stats() -> None:
    height = INDENT
    for stat in stats:
        label_height = stat.draw((INDENT, height))
        height += label_height
