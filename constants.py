import pygame
from objects import Object
from vector import Vector

WIDTH = 800
HEIGHT = 600

BLACK = pygame.color.Color(0, 0, 0)
GREY = pygame.color.Color(100, 100, 100)
WHITE = pygame.color.Color(255, 255, 255)

OBJECTS: list[Object] = [Object(10, Vector(100, 100), Vector(0, 0))]

SHOW_STATS = True

WIN = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.RESIZABLE)

def MIDPOINT():
    return Vector(*pygame.display.get_window_size())/2

def load_image(path):
    return pygame.image.load(path).convert_alpha()

OBSERVER_IMAGE = load_image("observer.png")
