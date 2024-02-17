import pygame

WIDTH = 800
HEIGHT = 600

BLACK = pygame.color.Color(0, 0, 0)
WHITE = pygame.color.Color(255, 255, 255)

OBJECTS = []

SHOW_STATS = True

WIN = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.RESIZABLE)

def load_image(path):
    return pygame.image.load(path).convert_alpha()

OBSERVER_IMAGE = load_image("observer.png")
