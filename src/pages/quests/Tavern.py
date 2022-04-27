import pygame
import sys
from pygame.locals import *

from src.components.Button import Button
from src.components.Label import Label
from src.components.ListElement import ListElement

from .Measurements import Measurements as meas

from src.globals.mock_data import tavern_quests


def Tavern(screen, mainClock):
    showHand = False
    isRunning = True

    label_page = Label(meas.label_page['text'], meas.label_page['font'], meas.label_page['color'], screen,
                       meas.label_page['x'], meas.label_page['y'], meas.label_page['anchor'])

    bt_return = Button(meas.bt_return['color'], meas.bt_return['x'], meas.bt_return['y'],
                       meas.bt_return['width'], meas.bt_return['height'], screen,
                       path=meas.bt_return['path'])

    quests = []
    i = 0
    for quest in tavern_quests:
        quests.append(ListElement(meas.le_general['x'],
                                  meas.le_general['y'] + i*meas.list_element_padding + i*meas.list_element_height,
                                  meas.le_general['width'], meas.le_general['height'],
                                  meas.le_general['colors'], screen, quest['name'], quest['difficulty'],
                                  meas.le_general['property_name'], quest['min_level']))
        i += 1

    displayedContent = [
        label_page, bt_return,
    ]

    while isRunning:
        screen.fill((255, 255, 255))
        if showHand:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for elem in displayedContent:
            elem.draw()

        for quest in quests:
            quest.draw()

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
                # LEFT CLICK
                if event.button == 1:
                    # HANDLE RETURN BUTTON
                    if bt_return.rect.collidepoint(event.pos):
                        isRunning = False
                        print("Redirecting: ArmorShop.py -> CityMap.py")

        pygame.display.update()
        mainClock.tick(60)
