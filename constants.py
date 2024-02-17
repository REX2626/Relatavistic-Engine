import pygame
from vector import Vector
from universe import OBJECTS  # used by other files

WIDTH = 800
HEIGHT = 600

BLACK = pygame.color.Color(0, 0, 0)
GREY = pygame.color.Color(100, 100, 100)
WHITE = pygame.color.Color(255, 255, 255)

SHOW_STATS = True
TICK_RATE = 10
SECONDS_PER_TICK = 1 / TICK_RATE
THRUST_FORCE = 1

SPEED_OF_LIGHT = 299_792_458

WIN = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.RESIZABLE)
PIXELS_PER_METER = 1

def MIDPOINT():
    return Vector(*pygame.display.get_window_size())/2

def load_image(path):
    return pygame.image.load(path).convert_alpha()

OBSERVER_IMAGE = load_image("observer.png")
