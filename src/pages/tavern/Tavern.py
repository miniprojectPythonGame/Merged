import pygame
import sys
from pygame.locals import *

from src.components.Button import Button
from src.components.Label import Label
from src.components.ListElement import ListElement

from .Measurements import Measurements as meas

from src.components.ScrollableList import ScrollableList

from src.globals.const_values import getDifficulty


def Tavern(screen, mainClock, user):
    showHand = False
    isRunning = True

    quest_list = user.currentHero.quests.quest_list

    label_page = Label(meas.label_page['text'], meas.label_page['font'], meas.label_page['color'], screen,
                       meas.label_page['x'], meas.label_page['y'], meas.label_page['anchor'])

    bt_return = Button(meas.bt_return['color'], meas.bt_return['x'], meas.bt_return['y'],
                       meas.bt_return['width'], meas.bt_return['height'], screen,
                       path=meas.bt_return['path'])

    list_elements = []
    for quest in quest_list:
        difficulty = getDifficulty(quest.difficulty)
        list_elements.append(ListElement(meas.le_general['x'],
                                         meas.le_general['y'] + 0 * meas.list_element_padding + 0 * meas.list_element_height,
                                         meas.le_general['width'], meas.le_general['height'],
                                         meas.le_general['colors'], screen, quest.name, difficulty,
                                         meas.le_general['property_name'], "12",
                                         object=quest))

    sl_heroes = ScrollableList(meas.sl_quests['x'], meas.sl_quests['y'], screen, list_elements,
                               meas.list_element_height, meas.list_element_padding)

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

        sl_heroes.draw()

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

                # SCROLL
                if event.button == 4:
                    sl_heroes.onScrollUp()
                    break

                elif event.button == 5:
                    sl_heroes.onScrollDown()
                    break

        pygame.display.update()
        mainClock.tick(60)
