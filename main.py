import pygame

pygame.display.set_caption("Relatavistic Engine")

WIDTH = 800
HEIGHT = 600

BLACK = pygame.color.Color(0, 0, 0)

OBJECTS = []

WIN = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.RESIZABLE)

def load_image(path):
    return pygame.image.load(path).convert_alpha()


PLAYER_SHIP = load_image("player_ship.png")


def draw_window():
    WIN.fill(BLACK)

    for object in OBJECTS:
        object.draw()

    WIN.blit(PLAYER_SHIP, (WIDTH/2 - PLAYER_SHIP.get_width()/2, HEIGHT/2 - PLAYER_SHIP.get_height()/2))

    pygame.display.update()


def handle_user_input():
    pass



def main():
    while True:

        handle_user_input()
        draw_window()


if __name__ == "__main__":
    main()
