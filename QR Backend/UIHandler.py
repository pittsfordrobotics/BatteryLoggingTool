import random

import os
import pygame as pg
import pygame.display as display

import BatteryDB
import uiconstants as uic


class UIHandler:
    def __init__(self):
        pg.init()
        # ui construction (create buttons, labels, etc.)
        self.surface = display.set_mode(size=(uic.WINDOW_WIDTH, uic.WINDOW_HEIGHT))
        display.set_caption("BatteryLoggerTool v0.0.1")
        display.set_icon(pg.image.load(os.path.join("QR Backend", "blt-logo.png")))
        self.bg_rect = pg.Rect(0, 0, uic.WINDOW_WIDTH, uic.WINDOW_HEIGHT)
        self.surface.fill(color=uic.BG_COLOR, rect=self.bg_rect)
        self.btns = [
            pg.Rect(50, 50, 300, 300),
            pg.Rect(300, 300, 100, 100)
        ]
        for btn in self.btns:
            pg.draw.rect(self.surface, uic.BTN_COLOR, btn, border_radius=50)
        self.clicked = {0: False}
        self.batteries_db = BatteryDB.BatteryDB()
        print(self.batteries_db.batteries)

    def get_surface(self) -> pg.Surface:
        return self.surface

    def handle_click(self, btn: int) -> bool:
        """
        :param btn: an int value indicating the specified button's index in self.btns
        :return: a boolean indicating whether the button has been clicked
        """
        if pg.mouse.get_pressed()[0] and self.btns[btn].collidepoint(pg.mouse.get_pos()):
            if not self.clicked[btn]:
                self.clicked[btn] = True
                return True
        else:
            self.clicked[btn] = False
            return False

    def do_stuff(self):
        """
        UI logic (handle button clicks, etc.) Meant to be called in the main loop.
        """
        for btn in self.btns:
            if self.handle_click(self.btns.index(btn)):
                print(f"Button {self.btns.index(btn) + 1} clicked")
                pg.draw.rect(self.surface,
                             (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                             btn,
                             border_radius=50)

    def mainloop(self):
        self.do_stuff()
        pg.display.flip()
        if pg.event.get(pg.QUIT):
            pg.quit()
            exit()
