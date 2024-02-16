import pygame
import sys
import constants as CONST

pygame.display.set_caption("Relatavistic Engine")


def draw_window():
    CONST.WIN.fill(CONST.BLACK)

    for object in CONST.OBJECTS:
        object.draw()

    CONST.WIN.blit(CONST.PLAYER_SHIP, (CONST.WIDTH/2 - CONST.PLAYER_SHIP.get_width()/2, CONST.HEIGHT/2 - CONST.PLAYER_SHIP.get_height()/2))

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
