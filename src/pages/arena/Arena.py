import pygame
import sys
from pygame.locals import *

from src.components.Label import Label
from src.components.Button import Button
from src.components.ListElement import ListElement
from src.components.ScrollableList import ScrollableList
from src.components.ImageField import ImageField

from .Measurements import Measurements as meas

from src.globals.const_values import CLASS_ICONS, AVATARS, STATS_NAMES


def Arena(screen, mainClock, user):
    showHand = False
    running = True
    hero = user.currentHero

    def reloadStatistics():
        return {
            "strength": hero.get_statistics().strength,
            "intelligence": hero.get_statistics().intelligence,
            "dexterity": hero.get_statistics().dexterity,
            "constitution": hero.get_statistics().constitution,
            "luck": hero.get_statistics().luck,
            "protection": hero.get_statistics().protection,
            "persuasion": hero.get_statistics().persuasion,
            "trade": hero.get_statistics().trade,
            "leadership": hero.get_statistics().leadership,
            "initiative": hero.get_statistics().initiative,
        }

    def generateStats():
        result = []
        cols = 2
        rows = round(len(STATS_NAMES) / cols)
        width = meas.avatar_size / cols
        height = meas.hero_title_height

        for n in range(len(STATS_NAMES)):
            x = meas.lb_stat_names['x'] + (n % cols) * width
            y = meas.lb_stat_names['y'] + (n % rows) * height
            result.append(Label(STATS_NAMES[n], meas.lb_stat_names['font'], meas.lb_stat_names['color'], screen,
                                x, y, meas.lb_stat_names['anchor']))

            result.append(Label(str(statistics[STATS_NAMES[n]]), meas.lb_stat_values['font'], meas.lb_stat_values['color'], screen,
                                x + round(0.5 * meas.avatar_size) - meas.list_element_padding,
                                y,
                                meas.lb_stat_values['anchor']))


        return result

    label_page = Label(meas.label_page['text'], meas.label_page['font'], meas.label_page['color'], screen,
                       meas.label_page['x'], meas.label_page['y'], meas.label_page['anchor'])

    bt_return = Button(meas.bt_return['color'], meas.bt_return['x'], meas.bt_return['y'],
                       meas.bt_return['width'], meas.bt_return['height'], screen,
                       path=meas.bt_return['path'])

    statistics = reloadStatistics()

    list_elements = []
    for i in range(12):
        list_elements.append(ListElement(meas.le_general['x'],
                                         meas.le_general[
                                             'y'] + 0 * meas.list_element_padding + 0 * meas.list_element_height,
                                         meas.le_general['width'], meas.le_general['height'],
                                         meas.le_general['colors'], screen, 'Item #' + str(i), 'No guild',
                                         meas.le_general['property_name'], '29',
                                         img_path=CLASS_ICONS['archer']['white']))

    sl_heroes = ScrollableList(meas.sl_heroes['x'], meas.sl_heroes['y'], screen, list_elements,
                               meas.list_element_height, meas.list_element_padding)

    img_hero = ImageField(meas.img_hero['x'], meas.img_hero['y'], meas.img_hero['width'], meas.img_hero['height'],
                          AVATARS['warrior'][0]['rect'], screen)

    lb_name = Label(hero.name, meas.lb_name['font'], meas.lb_name['color'], screen,
                    meas.lb_name['x'], meas.lb_name['y'], meas.lb_name['anchor'])

    lb_stats_names = generateStats()

    bt_fight = Button(meas.bt_fight['color'], meas.bt_fight['x'], meas.bt_fight['y'],
                       meas.bt_fight['width'], meas.bt_fight['height'], screen,
                       meas.bt_fight['text'], meas.header_tertiary_font, border_radius=meas.bt_fight['border-radius'])

    displayedContent = [
        label_page, bt_return, sl_heroes, img_hero, lb_name, bt_fight
    ]
    displayedContent += lb_stats_names

    while running:
        screen.fill((255, 255, 255))

        if showHand:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for elem in displayedContent:
            elem.draw()

        mx, my = pygame.mouse.get_pos()

        # HOVER EVENTS
        # if bt_showHeadgear.rect.collidepoint((mx, my)):
        #     bt_showHeadgear.onHoverOn()
        #     showHand = True
        # elif bt_showBreastplates.rect.collidepoint((mx, my)):
        #     bt_showBreastplates.onHoverOn()
        #     showHand = True
        # elif bt_showGloves.rect.collidepoint((mx, my)):
        #     bt_showGloves.onHoverOn()
        #     showHand = True
        # elif bt_showBoots.rect.collidepoint((mx, my)):
        #     bt_showBoots.onHoverOn()
        #     showHand = True
        # elif bt_showBelts.rect.collidepoint((mx, my)):
        #     bt_showBelts.onHoverOn()
        #     showHand = True
        # else:
        #     bt_showHeadgear.onHoverOff()
        #     bt_showBreastplates.onHoverOff()
        #     bt_showGloves.onHoverOff()
        #     bt_showBoots.onHoverOff()
        #     bt_showBelts.onHoverOff()
        #     showHand = False

        # CLICK EVENTS
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
                        running = False
                        break

                # SCROLL
                if event.button == 4:
                    sl_heroes.onScrollUp()
                    break

                elif event.button == 5:
                    sl_heroes.onScrollDown()
                    break

        pygame.display.update()
        mainClock.tick(60)
