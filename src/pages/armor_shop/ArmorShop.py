import pygame
import sys
from pygame.locals import *

from src.components.Button import Button
from src.components.Label import Label
from src.components.CharacterEquipment import CharacterEquipment
from src.components.ItemGrid import ItemGrid
from src.components.Container import Container
from src.components.SwitchCards import SwitchCards

from .Measurements import Measurements as meas

from api.game_classes.objects.buildings.shops import ShopType

from src.globals.const_values import INVENTORY_SHIFT

from src.globals.const_values import \
    getCharacterForEQPreview, \
    reloadCharacterBackpacks, \
    reloadBackpackButtons, \
    getQuality, \
    getItemCategory

def ArmorShop(screen, mainClock, user):
    def reloadButtons(buttons_list, current_active):
        newButtons = []

        for name, path_white, path_gray, button in buttons_list:
            if current_active == name:
                button.colorSchemes = meas.bt_class_active['color']
                button.color = meas.bt_class_active['color'].inactive
                button.path = path_white
                button.image = button.makeImage(path_white, meas.bt_class_active['image_offset'])
                button.border_radius = meas.bt_class_active['border_radius']
            else:
                button.colorSchemes = meas.bt_class_inactive['color']
                button.color = meas.bt_class_inactive['color'].inactive
                button.path = path_gray
                button.image = button.makeImage(path_gray, meas.bt_class_inactive['image_offset'])
                button.border_radius = meas.bt_class_inactive['border_radius']

            newButtons.append((name, path_white, path_gray, button))

        return newButtons

    def sortItems(itemList):
        sorted = {
            "headgear": [],
            "breastplate": [],
            "gloves": [],
            "boots": [],
            "belt": []
        }

        for i in range(len(itemList)):
            item_type = str(itemList[i].item_type)[9:].lower()
            sorted[item_type].append({
                "name": itemList[i].name,
                "img_path": '../images/items/' + getItemCategory(item_type) + '/' + item_type + '.png',
                "type": getQuality(itemList[i].quality),
                "id": i,
            })

        return sorted

    def reloadItemGrid():
        return ItemGrid(meas.ig_items['x'], meas.ig_items['y'],
                        meas.ig_items['item_size'], meas.ig_items['item_padding'],
                        meas.ig_items['cols'], meas.ig_items['amount'],
                        screen, armor_shop[category_active])

    def handleBuyItem(item_id):
        hero.buy_from_shop(item_id, ShopType.ArmourShop.value)
        reloadCharacterBackpacks(character, hero)
        sc_eq_stat_bp.components[0].components[-1] = ItemGrid(meas.ig_backpack['x'], meas.ig_backpack['y'],
                           meas.ig_backpack['item_size'], meas.ig_backpack['item_padding'],
                           meas.ig_backpack['cols'], meas.ig_backpack['amount'], screen,
                           character['backpacks'][backpack_active])
        character['gold'] = hero.eq.gold
        label_gold = Label("Gold: " + str(character['gold']), meas.label_gold['font'],
                           meas.label_gold['color'], screen, meas.label_gold['x'],
                           meas.label_gold['y'], meas.label_gold['anchor'])
        return sortItems(hero.armourShop.itemList), label_gold

    def handleSellItem(item_id):
        hero.eq.sell_item_to_shop(item_id)
        reloadCharacterBackpacks(character, hero)
        sc_eq_stat_bp.components[0].components[-1] = ItemGrid(meas.ig_backpack['x'], meas.ig_backpack['y'],
                           meas.ig_backpack['item_size'], meas.ig_backpack['item_padding'],
                           meas.ig_backpack['cols'], meas.ig_backpack['amount'], screen,
                           character['backpacks'][backpack_active])
        character['gold'] = hero.eq.gold
        label_gold = Label("Gold: " + str(character['gold']), meas.label_gold['font'],
                           meas.label_gold['color'], screen, meas.label_gold['x'],
                           meas.label_gold['y'], meas.label_gold['anchor'])
        return label_gold

    showHand = False
    running = True
    category_active = 'headgear'
    backpack_active = 0
    hero = user.currentHero
    armor_shop = sortItems(hero.armourShop.itemList)

    character = getCharacterForEQPreview(hero)

    label_page = Label(meas.label_page['text'], meas.label_page['font'], meas.label_page['color'], screen,
                       meas.label_page['x'], meas.label_page['y'], meas.label_page['anchor'])

    bt_return = Button(meas.bt_return['color'], meas.bt_return['x'], meas.bt_return['y'],
                       meas.bt_return['width'], meas.bt_return['height'], screen,
                       path=meas.bt_return['path'])

    bt_showHeadgear = Button(meas.bt_class_active['color'],
                             meas.bt_showHeadgear['x'], meas.bt_showHeadgear['y'],
                             meas.bt_showHeadgear['width'], meas.bt_showHeadgear['height'], screen,
                             path=meas.bt_showHeadgear['path_white'],
                             image_ofset=meas.bt_class_active['image_offset'],
                             border_radius=meas.bt_class_active['border_radius'])

    bt_showBreastplates = Button(meas.bt_class_inactive['color'],
                                 meas.bt_showBreastplates['x'], meas.bt_showBreastplates['y'],
                                 meas.bt_showBreastplates['width'], meas.bt_showBreastplates['height'], screen,
                                 path=meas.bt_showBreastplates['path_white'],
                                 image_ofset=meas.bt_class_inactive['image_offset'],
                                 border_radius=meas.bt_class_inactive['border_radius'])

    bt_showGloves = Button(meas.bt_class_inactive['color'],
                           meas.bt_showGloves['x'], meas.bt_showGloves['y'],
                           meas.bt_showGloves['width'], meas.bt_showGloves['height'], screen,
                           path=meas.bt_showGloves['path_white'],
                           image_ofset=meas.bt_class_inactive['image_offset'],
                           border_radius=meas.bt_class_inactive['border_radius'])

    bt_showBoots = Button(meas.bt_class_inactive['color'],
                          meas.bt_showBoots['x'], meas.bt_showBoots['y'],
                          meas.bt_showBoots['width'], meas.bt_showBoots['height'], screen,
                          path=meas.bt_showBoots['path_white'],
                          image_ofset=meas.bt_class_inactive['image_offset'],
                          border_radius=meas.bt_class_inactive['border_radius'])

    bt_showBelts = Button(meas.bt_class_inactive['color'],
                          meas.bt_showBelts['x'], meas.bt_showBelts['y'],
                          meas.bt_showBelts['width'], meas.bt_showBelts['height'], screen,
                          path=meas.bt_showBelts['path_white'],
                          image_ofset=meas.bt_class_inactive['image_offset'],
                          border_radius=meas.bt_class_inactive['border_radius'])

    ce_characterEqPreview = CharacterEquipment(meas.ce_characterEqPreview['x'],
                                               meas.ce_characterEqPreview['y'],
                                               meas.ce_characterEqPreview['font'],
                                               meas.ce_characterEqPreview['colors'],
                                               character,
                                               screen, size='medium')

    label_gold = Label("Gold: " + str(character['gold']), meas.label_gold['font'],
                       meas.label_gold['color'], screen, meas.label_gold['x'],
                       meas.label_gold['y'], meas.label_gold['anchor'])

    category_buttons = [
        ('headgear', meas.bt_showHeadgear['path_white'],
         meas.bt_showHeadgear['path_gray'], bt_showHeadgear),
        ('breastplate', meas.bt_showBreastplates['path_white'],
         meas.bt_showBreastplates['path_gray'], bt_showBreastplates),
        ('gloves', meas.bt_showGloves['path_white'],
         meas.bt_showGloves['path_gray'], bt_showGloves),
        ('boots', meas.bt_showBoots['path_white'],
         meas.bt_showBoots['path_gray'], bt_showBoots),
        ('belt', meas.bt_showBelts['path_white'],
         meas.bt_showBelts['path_gray'], bt_showBelts),
    ]

    ig_backpack = ItemGrid(meas.ig_backpack['x'], meas.ig_backpack['y'],
                           meas.ig_backpack['item_size'], meas.ig_backpack['item_padding'],
                           meas.ig_backpack['cols'], meas.ig_backpack['amount'], screen,
                           character['backpacks'][backpack_active])

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

    sc_eq_stat_bp = SwitchCards(meas.sc_eq_stat_bp['x'], meas.sc_eq_stat_bp['y'],
                                meas.sc_eq_stat_bp['width'], meas.sc_eq_stat_bp['height'], meas.sc_eq_stat_bp['font'],
                                meas.sc_eq_stat_bp['color'], screen, [c_backpack, ce_characterEqPreview, c_stats], ['Backpack', 'Equipment', 'Statistics'],
                                switch_height=meas.sc_eq_stat_bp['switch_height'])

    displayedContent = [
        label_page, bt_return, sc_eq_stat_bp, label_gold
    ]

    while running:
        screen.fill((255, 255, 255))

        if showHand:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        category_buttons = reloadButtons(category_buttons, category_active)
        buttons_backpack = reloadBackpackButtons(buttons_backpack, backpack_active, meas)
        ig_items = reloadItemGrid()
        ig_items.draw()

        for elem in displayedContent:
            elem.draw()

        for name, path_white, path_gray, button in category_buttons:
            button.draw()

        mx, my = pygame.mouse.get_pos()

        # HOVER EVENTS
        if bt_showHeadgear.rect.collidepoint((mx, my)):
            bt_showHeadgear.onHoverOn()
            showHand = True
        elif bt_showBreastplates.rect.collidepoint((mx, my)):
            bt_showBreastplates.onHoverOn()
            showHand = True
        elif bt_showGloves.rect.collidepoint((mx, my)):
            bt_showGloves.onHoverOn()
            showHand = True
        elif bt_showBoots.rect.collidepoint((mx, my)):
            bt_showBoots.onHoverOn()
            showHand = True
        elif bt_showBelts.rect.collidepoint((mx, my)):
            bt_showBelts.onHoverOn()
            showHand = True
        else:
            bt_showHeadgear.onHoverOff()
            bt_showBreastplates.onHoverOff()
            bt_showGloves.onHoverOff()
            bt_showBoots.onHoverOff()
            bt_showBelts.onHoverOff()
            showHand = False

        for button in sc_eq_stat_bp.buttons:
            if button.rect.collidepoint((mx, my)):
                showHand = True
                break

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

                    # HANDLE CATEGORY BUTTONS
                    for name, path_white, path_gray, button in category_buttons:
                        if button.rect.collidepoint(event.pos):
                            category_active = name
                            break

                    # CARD SWITCH
                    for i in range(len(sc_eq_stat_bp.buttons)):
                        if sc_eq_stat_bp.buttons[i].rect.collidepoint(event.pos):
                            sc_eq_stat_bp.current = i
                            break

                    for item in ig_items.backpack:
                        if item.rect.collidepoint(event.pos):
                            armor_shop, displayedContent[3] = handleBuyItem(item.id)
                            break

                    c_backpack_elem = sc_eq_stat_bp.components[0].components
                    for i in range(len(c_backpack_elem)):
                        # BACKPACKS
                        if type(c_backpack_elem[i]).__name__ == "Button":
                            pass
                        #     if c_backpack_elem[i].rect.collidepoint(event.pos):
                        #         backpack_active = i
                        #         resetActiveItem()
                        #         break
                        #
                        # ACTIVATE ITEMS
                        else:
                            for j in range(len(c_backpack_elem[i].backpack_ref)):
                                if c_backpack_elem[i].backpack[j].rect.collidepoint(event.pos):
                                    displayedContent[3] = handleSellItem(j + INVENTORY_SHIFT)
                                    break



        pygame.display.update()
        mainClock.tick(60)






























