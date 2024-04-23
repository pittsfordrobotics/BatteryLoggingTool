import pygame
from time import time


def do_stuff(surface):
    rect = pygame.Rect(0, 0, 255, 400)
    surface.fill(color=((time() * 1000 % 255), 0, time() * 1000 % 255), rect=rect)
    pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    surface1 = pygame.display.set_mode(size=(400, 400))
    while True:
        do_stuff(surface1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
