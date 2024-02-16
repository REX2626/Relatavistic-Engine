import pygame

WIDTH = 800
HEIGHT = 600

BLACK = pygame.color.Color(0, 0, 0)

OBJECTS = []

SHOW_STATS = True

WIN = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.RESIZABLE)

def load_image(path):
    return pygame.image.load(path).convert_alpha()

PLAYER_SHIP = load_image("player_ship.png")
