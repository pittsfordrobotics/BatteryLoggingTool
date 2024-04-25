import pygame as pg
import UIHandler

if __name__ == "__main__":
    pg.init()
    surface = UIHandler.init()
    while True:
        UIHandler.do_stuff(surface)
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
