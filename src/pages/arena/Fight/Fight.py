import time

import pygame
import sys
from pygame.locals import *

from src.components.Label import Label
from src.components.Button import Button
from src.components.ImageField import ImageField
from src.components.PropertyBar import PropertyBar

from .Measurements import Measurements as meas
from src.globals.const_values import getFullAvatarPath, STATS_NAMES, TEXT_FONT


def Fight(screen, mainClock, heroAttacker, heroDefender):
    def generatePreview(attacker, defender, y, x_header, x_attacker, x_defender, meas_header, meas_attacker,
                        meas_defender):
        stat_headers = []
        stat_values = []
        statistics = [
            [attacker.get_statistics().strength, defender.get_statistics().strength],
            [attacker.get_statistics().intelligence, defender.get_statistics().intelligence],
            [attacker.get_statistics().dexterity, defender.get_statistics().dexterity],
            [attacker.get_statistics().constitution, defender.get_statistics().constitution],
            [attacker.get_statistics().luck, defender.get_statistics().luck],
            [attacker.get_statistics().persuasion, defender.get_statistics().persuasion],
            [attacker.get_statistics().trade, defender.get_statistics().trade],
            [attacker.get_statistics().leadership, defender.get_statistics().leadership],
            [attacker.get_statistics().protection, defender.get_statistics().protection],
            [attacker.get_statistics().initiative, defender.get_statistics().initiative],
        ]

        for i in range(len(STATS_NAMES)):
            stat_headers.append(
                Label(STATS_NAMES[i], meas_header['font'], meas_header['color'], screen,
                      x_header,
                      y + i * meas_header['height'])
            )
            stat_values.append(
                Label(str(statistics[i][0]), meas_attacker['font'], meas_attacker['color'], screen,
                      x_attacker,
                      y + i * meas_attacker['height'])
            )
            stat_values.append(
                Label(str(statistics[i][1]), meas_defender['font'], meas_defender['color'], screen,
                      x_defender,
                      y + i * meas_defender['height'])
            )

        return stat_headers, stat_values

    def resolveAttack(heroID, damage, attacker, defender):
        if heroID == attacker['id']:
            defender['current_health'] -= damage
        else:
            attacker['current_health'] -= damage

    showHand = False
    running = True
    DELAY = 1

    battle_results = heroAttacker.init_fight_with_other_hero(heroDefender)
    battle_iterator = iter(battle_results[0])

    for strike in battle_results[0]:
        print(strike)

    attacker = {
        "id": heroAttacker.hero_id,
        "name": heroAttacker.name,
        "fight_class": str(heroAttacker.fight_class).lower(),
        "avatarID": heroAttacker.avatar_id,
        "max_health": heroAttacker.get_statistics().hp,
        "current_health": heroAttacker.get_statistics().hp,
    }

    defender = {
        "id": heroDefender.hero_id,
        "name": heroDefender.name,
        "fight_class": str(heroDefender.fight_class).lower(),
        "avatarID": heroDefender.avatar_id,
        "max_health": heroDefender.get_statistics().hp,
        "current_health": heroDefender.get_statistics().hp,
    }

    label_page = Label(meas.label_page['text'], meas.label_page['font'], meas.label_page['color'], screen,
                       meas.label_page['x'], meas.label_page['y'], meas.label_page['anchor'])

    bt_return = Button(meas.bt_return['color'], meas.bt_return['x'], meas.bt_return['y'],
                       meas.bt_return['width'], meas.bt_return['height'], screen,
                       path=meas.bt_return['path'])

    img_attacker = ImageField(meas.img_attacker['x'], meas.img_attacker['y'],
                              meas.img_attacker['width'], meas.img_attacker['height'],
                              path=getFullAvatarPath(attacker['fight_class'], attacker['avatarID']), screen=screen)

    label_attacker = Label(attacker['name'], meas.label_attacker['font'], meas.label_attacker['color'],
                           screen, meas.label_attacker['x'], meas.label_attacker['y'])

    img_defender = ImageField(meas.img_defender['x'], meas.img_defender['y'],
                              meas.img_defender['width'], meas.img_defender['height'],
                              path=getFullAvatarPath(defender['fight_class'], defender['avatarID']), screen=screen)

    label_defender = Label(defender['name'], meas.label_defender['font'], meas.label_defender['color'],
                           screen, meas.label_defender['x'], meas.label_defender['y'],
                           anchor=meas.label_defender['anchor'])

    stat_headers, stat_values = generatePreview(heroAttacker, heroDefender,
                                                meas.label_stat_header['y'],
                                                meas.label_stat_header['x'],
                                                meas.label_stat_values_attacker['x'],
                                                meas.label_stat_values_defender['x'],
                                                meas.label_stat_header,
                                                meas.label_stat_values_attacker,
                                                meas.label_stat_values_defender)

    pb_health_attacker = PropertyBar(meas.pb_health_attacker['x'], meas.pb_health_attacker['y'],
                                     meas.pb_health_attacker['width'], meas.pb_health_attacker['height'],
                                     attacker['current_health'] / attacker['max_health'],
                                     meas.pb_health_attacker['text'] + ": " + str(attacker['current_health']),
                                     meas.pb_health_attacker['font'], meas.pb_health_attacker['border_color'],
                                     meas.pb_health_attacker['fill_color'], screen)

    pb_health_defender = PropertyBar(meas.pb_health_defender['x'], meas.pb_health_defender['y'],
                                     meas.pb_health_defender['width'], meas.pb_health_defender['height'],
                                     defender['current_health'] / defender['max_health'],
                                     meas.pb_health_defender['text'] + ": " + str(defender['current_health']),
                                     meas.pb_health_defender['font'], meas.pb_health_defender['border_color'],
                                     meas.pb_health_defender['fill_color'], screen)

    bt_speedup = Button(meas.bt_speedup['color'], meas.bt_speedup['x'], meas.bt_speedup['y'],
                        meas.bt_speedup['width'], meas.bt_speedup['height'], screen,
                        path=meas.bt_speedup['path'])

    while running:
        screen.fill((255, 255, 255))

        if showHand:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        mx, my = pygame.mouse.get_pos()

        label_page.draw()

        img_attacker.draw()
        label_attacker.draw()

        img_defender.draw()
        label_defender.draw()

        pb_health_attacker.draw()
        pb_health_defender.draw()

        bt_speedup.draw()

        try:
            attack = next(battle_iterator)
            time.sleep(DELAY)
            resolveAttack(attack[0], attack[1], attacker, defender)

            pb_health_attacker.value = attacker['current_health'] / attacker['max_health']
            pb_health_attacker.text = meas.pb_health_attacker['text'] + ": " + str(attacker['current_health'])

            pb_health_defender.value = defender['current_health'] / defender['max_health']
            pb_health_defender.text = meas.pb_health_defender['text'] + ": " + str(defender['current_health'])

        except:
            bt_return.draw()

        for header in stat_headers:
            header.draw()

        for value in stat_values:
            value.draw()

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

                    if bt_speedup.rect.collidepoint(event.pos):
                        DELAY = 0
                        break

        pygame.display.update()
        mainClock.tick(60)
