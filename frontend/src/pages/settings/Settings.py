import pygame
import sys
from pygame.locals import *

from frontend.src.components.Label import Label
from frontend.src.components.Button import Button

from .Measurements import Measurements as meas


def Settings(screen, mainClock):
    running = True

    label_page = Label(meas.label_page['text'], meas.label_page['font'], meas.label_page['color'], screen,
                       meas.label_page['x'], meas.label_page['y'], meas.label_page['anchor'])

    bt_return = Button(meas.bt_return['color'], meas.bt_return['x'], meas.bt_return['y'],
                       meas.bt_return['width'], meas.bt_return['height'], screen,
                       path=meas.bt_return['path'])

    while running:
        screen.fill((255, 255, 255))
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        label_page.draw()
        bt_return.draw()

        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                # HANDLE RETURN BUTTON
                if bt_return.rect.collidepoint(event.pos):
                    running = False
                    print("Redirecting: Settings.py -> CityMap.py")

        pygame.display.update()
        mainClock.tick(60)
