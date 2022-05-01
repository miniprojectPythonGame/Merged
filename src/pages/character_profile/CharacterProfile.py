import pygame
import sys
from pygame.locals import *

from src.components.Label import Label
from src.components.Button import Button
from src.components.CharacterEquipment import CharacterEquipment
from src.components.ItemGrid import ItemGrid
from src.components.PopupItem import PopupItem
from src.components.SwitchCards import SwitchCards
from src.components.Container import Container

from api.game_classes.objects.items.item import ItemType

from .Measurements import Measurements as meas

from src.globals.const_values import INVENTORY_SHIFT


def CharacterProfile(screen, mainClock, user):
    def reloadButtons(buttons_list, current_active):
        newButtons = []

        for i in range(len(buttons_list)):
            if i == current_active:
                buttons_list[i].colorSchemes = meas.bt_class_active['color']
                buttons_list[i].color = meas.bt_class_active['color'].inactive
                buttons_list[i].path = meas.buttons_backpack['path_white']
                buttons_list[i].image = buttons_list[i].makeImage(meas.buttons_backpack['path_white'],
                                                                  meas.bt_class_active['image_offset'])
                buttons_list[i].border_radius = meas.bt_class_active['border_radius']
            else:
                buttons_list[i].colorSchemes = meas.bt_class_inactive['color']
                buttons_list[i].color = meas.bt_class_inactive['color'].inactive
                buttons_list[i].path = meas.buttons_backpack['path_gray']
                buttons_list[i].image = buttons_list[i].makeImage(meas.buttons_backpack['path_gray'],
                                                                  meas.bt_class_inactive['image_offset'])
                buttons_list[i].border_radius = meas.bt_class_inactive['border_radius']

            newButtons.append(buttons_list[i])

        return newButtons

    def reloadItemGrid(current_backpack):
        return ItemGrid(meas.ig_backpack['x'], meas.ig_backpack['y'],
                        meas.ig_backpack['item_size'], meas.ig_backpack['item_padding'],
                        meas.ig_backpack['cols'], meas.ig_backpack['amount'], screen,
                        character['backpacks'][current_backpack], active=active_item['from'] - INVENTORY_SHIFT)

    def getItemCategory(item_type):
        armors = ['belt', 'boots', 'breastplate', 'gloves', 'headgear']
        magic = ['luckyitem', 'necklace', 'ring', 'sceptre']

        if item_type in armors:
            return "armor"

        if item_type in magic:
            return "magic"

        return "weapon"

    def getEqItem(item):
        item_type = str(type(item).__name__).lower()

        if item:
            result = {
                "name": item.name,
                "img_path": '../images/items/' + getItemCategory(item_type) + '/' + item_type + '.png',
                "type": 'common',
            }
        else:
            result = {
                "name": "empty",
                "img_path": "../images/icons/add_item.png",
                "type": "empty",
            }

        return result

    def getEqItemByType(items, expected_type):
        item_type = str(type(items[expected_type]).__name__).lower()

        if items[expected_type]:
            result = {
                "name": items[expected_type].name,
                "img_path": '../images/items/' + getItemCategory(item_type) + '/' + item_type + '.png',
                "type": 'common',
            }
        else:
            result = {
                "name": "empty",
                "img_path": "../images/icons/add_item.png",
                "type": "empty",
            }

        return result

    def resetActiveItem():
        return {
            "from": -1,
            "to": -1
        }

    def setActiveItem(index):
        if active_item['from'] == -1:
            active_item['from'] = index
            return False

        if active_item['to'] == -1:
            active_item['to'] = index
            return True

        return None

    def reloadCharacterBackpacks():
        character['backpacks'] = [
            [getEqItem(hero.eq.itemSlots[i]) for i in range(INVENTORY_SHIFT, len(hero.eq.itemSlots))]
        ]

    def reloadCharacterEQ():
        character['eq'] = {
            "headgear": getEqItemByType(hero.eq.itemSlots, ItemType.Headgear.value),
            "breastplate": getEqItemByType(hero.eq.itemSlots, ItemType.Breastplate.value),
            "gloves": getEqItemByType(hero.eq.itemSlots, ItemType.Gloves.value),
            "boots": getEqItemByType(hero.eq.itemSlots, ItemType.Boots.value),
            "necklace": getEqItemByType(hero.eq.itemSlots, ItemType.Necklace.value),
            "belt": getEqItemByType(hero.eq.itemSlots, ItemType.Belt.value),
            "ring": getEqItemByType(hero.eq.itemSlots, ItemType.Ring.value),
            "lucky_item": getEqItemByType(hero.eq.itemSlots, ItemType.LuckyItem.value),
        }

    def reloadStatistics():
        statistics = hero.get_statistics()
        character['statistics'] = {
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
        new_stats_values = [Label(str(character['statistics'][meas.labels_stats[i]]), meas.label_stat_values['font'],
                                  meas.label_stat_values['color'], screen, meas.label_stat_values['x'],
                                  meas.label_stat_values['y'] + i * (
                                          meas.label_stat_values['height'] + meas.label_stat_values['padding']),
                                  meas.label_stat_values['anchor'])
                            for i in range(len(meas.labels_stats))]

        sc_eq_stat.components[1].components = stats_headers + new_stats_values

    def extractType(name):
        return ''.join(' '.join(name[3:].split('_')).title().split())

    def handleItemClick(index, current_item):
        if setActiveItem(index):
            hero.eq.swap_places(current_item['from'], current_item['to'])
            reloadCharacterBackpacks()
            reloadCharacterEQ()
            reloadStatistics()
            ce_characterEqPreview.reloadCharacter(character)
            print(user.currentHero.eq.gearStatistics)
            return resetActiveItem()
        else:
            return current_item

    running = True
    curr_item_in_popup = ''
    backpack_active = 0
    active_item = resetActiveItem()
    hero = user.currentHero
    statistics = hero.get_statistics()

    character = {
        'name': str(hero.name),
        'spec': str(hero.heroClass),
        'level': str(hero.lvl),
        'img_full': '../images/characters/' + str(hero.heroClass).lower() + '_' + str(
            hero.avatar_id) + '.jpg',
        "health": str(statistics.hp),
        "gold": str(hero.eq.gold),
        "exp": hero.exp,
        "expToNextLvl": hero.expToNextLvl,
        "eq": {
            "headgear": getEqItemByType(hero.eq.itemSlots, ItemType.Headgear.value),
            "breastplate": getEqItemByType(hero.eq.itemSlots, ItemType.Breastplate.value),
            "gloves": getEqItemByType(hero.eq.itemSlots, ItemType.Gloves.value),
            "boots": getEqItemByType(hero.eq.itemSlots, ItemType.Boots.value),
            "necklace": getEqItemByType(hero.eq.itemSlots, ItemType.Necklace.value),
            "belt": getEqItemByType(hero.eq.itemSlots, ItemType.Belt.value),
            "ring": getEqItemByType(hero.eq.itemSlots, ItemType.Ring.value),
            "lucky_item": getEqItemByType(hero.eq.itemSlots, ItemType.LuckyItem.value),
        },
        "backpacks": [
            [getEqItem(hero.eq.itemSlots[i]) for i in range(INVENTORY_SHIFT, len(hero.eq.itemSlots))]
        ],
        "statistics": {
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
    }

    label_page = Label(meas.label_page['text'], meas.label_page['font'], meas.label_page['color'],
                       screen, meas.label_page['x'], meas.label_page['y'], meas.label_page['anchor'])

    bt_return = Button(meas.bt_return['color'], meas.bt_return['x'], meas.bt_return['y'],
                       meas.bt_return['width'], meas.bt_return['height'], screen,
                       path=meas.bt_return['path'])

    ce_characterEqPreview = CharacterEquipment(meas.ce_characterEqPreview['x'],
                                               meas.ce_characterEqPreview['y'],
                                               meas.ce_characterEqPreview['font'],
                                               meas.ce_characterEqPreview['colors'],
                                               character,
                                               screen)

    ig_backpack = ItemGrid(meas.ig_backpack['x'], meas.ig_backpack['y'],
                           meas.ig_backpack['item_size'], meas.ig_backpack['item_padding'],
                           meas.ig_backpack['cols'], meas.ig_backpack['amount'], screen,
                           character['backpacks'][backpack_active], active=active_item['from'])

    buttons_backpack = [Button(meas.bt_class_active['color'],
                               meas.buttons_backpack['x'], meas.buttons_backpack['y'] +
                               i * (meas.buttons_backpack['height'] + meas.buttons_backpack['padding']),
                               meas.buttons_backpack['width'], meas.buttons_backpack['height'], screen,
                               path=meas.buttons_backpack['path_gray'],
                               image_ofset=meas.bt_class_active['image_offset'],
                               border_radius=meas.bt_class_active['border_radius'])
                        for i in range(len(character['backpacks']))]

    c_backpack = Container(meas.c_backpack['x'], meas.c_backpack['y'], meas.c_backpack['width'],
                           meas.c_backpack['height'], buttons_backpack + [ig_backpack])

    stats_headers = [
        Label(meas.labels_stats[i].capitalize(), meas.label_stat_header['font'], meas.label_stat_header['color'],
              screen, meas.label_stat_header['x'],
              meas.label_stat_header['y'] + i * (
                      meas.label_stat_header['height'] + meas.label_stat_header['padding']),
              meas.label_stat_header['anchor'])
        for i in range(len(meas.labels_stats))]

    stats_values = [Label(str(character['statistics'][meas.labels_stats[i]]), meas.label_stat_values['font'],
                          meas.label_stat_values['color'], screen, meas.label_stat_values['x'],
                          meas.label_stat_values['y'] + i * (
                                  meas.label_stat_values['height'] + meas.label_stat_values['padding']),
                          meas.label_stat_values['anchor'])
                    for i in range(len(meas.labels_stats))]

    c_stats = Container(meas.c_stats['x'], meas.c_stats['y'], meas.c_stats['width'], meas.c_stats['height'],
                        stats_headers + stats_values)

    sc_eq_stat = SwitchCards(meas.sc_eq_stat['x'], meas.sc_eq_stat['y'],
                             meas.sc_eq_stat['width'], meas.sc_eq_stat['height'], meas.sc_eq_stat['font'],
                             meas.sc_eq_stat['color'], screen, [c_backpack, c_stats], ['Items', 'Statistics'],
                             switch_height=meas.sc_eq_stat['switch_height'])

    ppi_itemDescription = PopupItem(0, 0, 100, 50, screen, '', meas.text_font)

    while running:
        screen.fill((255, 255, 255))
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        sc_eq_stat.components[0].components[-1] = reloadItemGrid(backpack_active)
        buttons_backpack = reloadButtons(buttons_backpack, backpack_active)

        label_page.draw()
        bt_return.draw()
        ce_characterEqPreview.draw()
        sc_eq_stat.draw()

        ppi_itemDescription.draw()

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
                        running = False
                        print("Redirecting: CharacterProfile.py -> CityMap.py")

                    # CARD SWITCH
                    for i in range(len(sc_eq_stat.buttons)):
                        if sc_eq_stat.buttons[i].rect.collidepoint(event.pos):
                            sc_eq_stat.current = i
                            break

                    # EQ
                    for key in ce_characterEqPreview.character:
                        if type(ce_characterEqPreview.character[key]).__name__ == "ItemBox":
                            if ce_characterEqPreview.character[key].rect.collidepoint(event.pos):
                                active_item = handleItemClick(ItemType[extractType(key)].value, active_item)
                                break

                    # ITEM GRID
                    c_backpack_elem = sc_eq_stat.components[0].components
                    for i in range(len(c_backpack_elem)):
                        # BACKPACKS
                        if type(c_backpack_elem[i]).__name__ == "Button":
                            if c_backpack_elem[i].rect.collidepoint(event.pos):
                                backpack_active = i
                                resetActiveItem()
                                break

                        # ACTIVATE ITEMS
                        else:
                            for j in range(len(c_backpack_elem[i].backpack_ref)):
                                if c_backpack_elem[i].backpack[j].rect.collidepoint(event.pos):
                                    active_item = handleItemClick(j + INVENTORY_SHIFT, active_item)
                                    break

                # RIGHT CLICK
                if event.button == 3:
                    for i in range(len(ig_backpack.backpack_ref)):
                        if ig_backpack.backpack[i].rect.collidepoint(event.pos):
                            if curr_item_in_popup == ig_backpack.backpack_ref[i]['name']:
                                ppi_itemDescription = PopupItem(0, 0, 200, 80, screen,
                                                                '', meas.text_font)
                            else:
                                print('Here: ', ig_backpack.backpack_ref[i]['name'])
                                x = min(mx, meas.window_width - 200)
                                y = min(my, meas.window_height - 80)
                                ppi_itemDescription = PopupItem(x, y, 200, 80, screen,
                                                                ig_backpack.backpack_ref[i]['name'],
                                                                meas.text_font,
                                                                isVisible=True)
                                curr_item_in_popup = ig_backpack.backpack_ref[i]['name']
                            break

        pygame.display.update()
        mainClock.tick(60)
