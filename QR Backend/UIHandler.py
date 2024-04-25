import pygame as pg
import os
import pygame.display as display
import uiconstants as uic


def init() -> pg.Surface:
    surface = display.set_mode(size=(uic.WINDOW_WIDTH, uic.WINDOW_HEIGHT))
    display.set_caption("BatteryLoggerTool v0.0.1")
    display.set_icon(pg.image.load(os.path.join("QR Backend", "blt-logo.png")))
    bg_rect = pg.Rect(0, 0, uic.WINDOW_WIDTH, uic.WINDOW_HEIGHT)
    surface.fill(color=uic.BG_COLOR, rect=bg_rect)
    return surface


def do_stuff(surface):
    rect = pg.Rect(0, 0, 255, 400)
    surface.fill(color=(255, 255, 255), rect=rect)
