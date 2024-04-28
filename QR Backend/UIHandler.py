import pygame as pg
import pygame.display as display
import uiconstants as uic
import os


class UIHandler:
    def __init__(self):
        # ui construction (create buttons, labels, etc.)
        self.surface = display.set_mode(size=(uic.WINDOW_WIDTH, uic.WINDOW_HEIGHT))
        display.set_caption("BatteryLoggerTool v0.0.1")
        display.set_icon(pg.image.load(os.path.join("QR Backend", "blt-logo.png")))
        self.bg_rect = pg.Rect(0, 0, uic.WINDOW_WIDTH, uic.WINDOW_HEIGHT)
        self.surface.fill(color=uic.BG_COLOR, rect=self.bg_rect)
        self.btn1 = pg.Rect(50, 50, 100, 50)
        self.btns = [self.btn1]
        self.clicked = {str(self.btn1): False}
        self.surface.fill(color=(255, 255, 255), rect=self.btn1)
        print(str(self.btn1))

    def get_surface(self) -> pg.Surface:
        return self.surface

    def handle_click(self, btn: int):
        if pg.mouse.get_pressed()[0] and self.btn1.collidepoint(pg.mouse.get_pos()):
            if not self.clicked[str(self.btns[btn])]:
                self.clicked[str(self.btns[btn])] = True
                return True
        else:
            if self.clicked[str(self.btns[btn])]:
                self.clicked[str(self.btns[btn])] = False
            return False

    def do_stuff(self):
        """
        UI logic (handle button clicks, etc.) Meant to be called in the main loop.
        """
        if self.handle_click(0):
            print("Button 1 clicked")
