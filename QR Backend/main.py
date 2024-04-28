import pygame as pg
import UIHandler

if __name__ == "__main__":
    pg.init()
    handler = UIHandler.UIHandler()
    while True:
        handler.do_stuff()
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
