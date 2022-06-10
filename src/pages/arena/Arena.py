import pygame
import sys
from pygame.locals import *

from .Fight.Fight import Fight

from src.components.Label import Label
from src.components.Button import Button
from src.components.ListElement import ListElement
from src.components.ScrollableList import ScrollableList
from src.components.ImageField import ImageField

from .Measurements import Measurements as meas

from src.globals.const_values import CLASS_ICONS,\
    AVATARS,\
    STATS_NAMES,\
    getFightClassName


def Arena(screen, mainClock, user):
    showHand = False
    running = True
    hero = user.currentHero
    user.get_enemy_heroes_min_info()
    allHeros = user.enemy_heroes_min_info
    activeHero = None

    def reloadStatistics(statistics):
        return {
            "strength": statistics.strength,
            "intelligence": statistics.intelligence,
            "dexterity": statistics.dexterity,
            "constitution": statistics.constitution,
            "luck": statistics.luck,
            "protection": statistics.protection,
            "persuasion": statistics.persuasion,
            "trade": statistics.trade,
            "leadership": statistics.leadership,
            "initiative": statistics.initiative,
        }

    def generateStats(statistics):
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

            result.append(
                Label(str(statistics[STATS_NAMES[n]]), meas.lb_stat_values['font'], meas.lb_stat_values['color'],
                      screen,
                      x + round(0.5 * meas.avatar_size) - meas.list_element_padding,
                      y,
                      meas.lb_stat_values['anchor']))

        return result

    def reloadPreview(activeHero):
        fight_class = str(activeHero.fight_class).lower()
        heroAvatar = activeHero.avatar_id - 1
        statistics = reloadStatistics(activeHero.get_statistics())

        img_hero = ImageField(meas.img_hero['x'], meas.img_hero['y'], meas.img_hero['width'], meas.img_hero['height'],
                              AVATARS[fight_class][heroAvatar]['rect'], screen)

        lb_name = Label(activeHero.name, meas.lb_name['font'], meas.lb_name['color'], screen,
                        meas.lb_name['x'], meas.lb_name['y'], meas.lb_name['anchor'])

        lb_stats_names = generateStats(statistics)

        bt_fight = Button(meas.bt_fight['color'], meas.bt_fight['x'], meas.bt_fight['y'],
                          meas.bt_fight['width'], meas.bt_fight['height'], screen,
                          meas.bt_fight['text'], meas.header_tertiary_font,
                          border_radius=meas.bt_fight['border-radius'])

        return img_hero, lb_name, lb_stats_names, bt_fight

    label_page = Label(meas.label_page['text'], meas.label_page['font'], meas.label_page['color'], screen,
                       meas.label_page['x'], meas.label_page['y'], meas.label_page['anchor'])

    bt_return = Button(meas.bt_return['color'], meas.bt_return['x'], meas.bt_return['y'],
                       meas.bt_return['width'], meas.bt_return['height'], screen,
                       path=meas.bt_return['path'])

    list_elements = []
    for key in allHeros.keys():
        fight_class = str(getFightClassName(allHeros[key][4])).lower()
        list_elements.append(ListElement(meas.le_general['x'],
                                         meas.le_general[
                                             'y'] + 0 * meas.list_element_padding + 0 * meas.list_element_height,
                                         meas.le_general['width'], meas.le_general['height'],
                                         meas.le_general['colors'], screen, allHeros[key][1], 'No guild',
                                         meas.le_general['property_name'], str(allHeros[key][3]),
                                         object=key,
                                         img_path=CLASS_ICONS[fight_class]['white']))

    sl_heroes = ScrollableList(meas.sl_heroes['x'], meas.sl_heroes['y'], screen, list_elements,
                               meas.list_element_height, meas.list_element_padding,
                               )

    img_hero = None
    lb_name = None
    lb_stats_names = None
    bt_fight = None


    while running:
        screen.fill((255, 255, 255))

        if showHand:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        mx, my = pygame.mouse.get_pos()

        label_page.draw()
        bt_return.draw()
        sl_heroes.draw()

        if activeHero is not None:
            img_hero.draw()
            lb_name.draw()
            for label in lb_stats_names:
                label.draw()
            bt_fight.draw()

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

                    if activeHero is not None and bt_fight.rect.collidepoint(event.pos):
                        Fight(screen, mainClock, hero, activeHero)

                        break

                    for heroLine in sl_heroes.list:
                        if heroLine.rect.collidepoint(event.pos):
                            user.choose_enemy_hero(heroLine.object)
                            activeHero = user.enemy_heroes[heroLine.object]

                            img_hero, lb_name, lb_stats_names, bt_fight = reloadPreview(activeHero)
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
