import pygame
pygame.init()

import sys
import constants as CONST
from vector import Vector
import stats

pygame.display.set_caption("Relatavistic Engine")


def draw_window():
    CONST.WIN.fill(CONST.BLACK)

    for object in CONST.OBJECTS:
        object.draw()

    stats.draw_stats()

    CONST.WIN.blit(CONST.OBSERVER_IMAGE, (CONST.MIDPOINT() - Vector(*CONST.OBSERVER_IMAGE.get_size())/2).tuple())

    pygame.display.update()


def handle_user_input():
    pass


def quit():
    pygame.quit()
    sys.exit()



def main():
    while True:

        handle_user_input()
        draw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F3:
                    CONST.SHOW_STATS = not CONST.SHOW_STATS


if __name__ == "__main__":
    main()
