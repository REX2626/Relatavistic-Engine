import pygame
pygame.init()

import sys
from time import perf_counter
import constants as CONST
from vector import Vector
from observer import Observer
import stats

pygame.display.set_caption("Relatavistic Engine")


def draw_window():
    CONST.WIN.fill(CONST.BLACK)

    for object in CONST.OBJECTS:
        object.draw()

    if CONST.SHOW_STATS:
        stats.draw_stats()

    CONST.WIN.blit(CONST.OBSERVER_IMAGE, (CONST.MIDPOINT() - Vector(*CONST.OBSERVER_IMAGE.get_size())/2).tuple())

    pygame.display.update()


def update_objects():
    for object in CONST.OBJECTS:
        object.update()


def handle_user_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F3:
                CONST.SHOW_STATS = not CONST.SHOW_STATS

            elif event.key == pygame.K_SPACE:
                Observer.accelerate()

            elif event.key == pygame.K_UP:
                CONST.THRUST_FORCE *= 2

            elif event.key == pygame.K_DOWN:
                CONST.THRUST_FORCE /= 2

        elif event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                CONST.PIXELS_PER_METER *= 2
            else:
                CONST.PIXELS_PER_METER /= 2


def quit():
    pygame.quit()
    sys.exit()



def main():
    while True:
        start_time = perf_counter()

        handle_user_input()
        update_objects()
        draw_window()

        # Wait for tick to finish
        while perf_counter() < start_time + CONST.SECONDS_PER_TICK:
            pass


if __name__ == "__main__":
    main()
