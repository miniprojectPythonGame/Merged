import pygame
import sys
from pygame.locals import *

from src.components.Button import Button
from src.components.Label import Label
from src.components.CharacterEquipment import CharacterEquipment
from src.components.ItemGrid import ItemGrid

from .Measurements import Measurements as meas

from src.globals.mock_data import magic_shop, character_2


def MagicShop(screen, mainClock):

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

    def reloadItemGrid(category_active):
        return ItemGrid(meas.ig_items['x'], meas.ig_items['y'],
                        meas.ig_items['item_size'], meas.ig_items['item_padding'],
                        meas.ig_items['cols'], meas.ig_items['amount'],
                        screen, magic_shop[category_active])

    showHand = False
    isRunning = True
    category_active = 'potions'


    label_page = Label(meas.label_page['text'], meas.label_page['font'], meas.label_page['color'], screen,
                       meas.label_page['x'], meas.label_page['y'], meas.label_page['anchor'])

    bt_return = Button(meas.bt_return['color'], meas.bt_return['x'], meas.bt_return['y'],
                       meas.bt_return['width'], meas.bt_return['height'], screen,
                       path=meas.bt_return['path'])

    bt_showPotions = Button(meas.bt_class_active['color'],
                        meas.bt_showPotions['x'], meas.bt_showPotions['y'],
                        meas.bt_showPotions['width'], meas.bt_showPotions['height'], screen,
                        path=meas.bt_showPotions['path_white'],
                        image_ofset=meas.bt_class_active['image_offset'],
                        border_radius=meas.bt_class_active['border_radius'])

    bt_showRings = Button(meas.bt_class_inactive['color'],
                        meas.bt_showRings['x'], meas.bt_showRings['y'],
                        meas.bt_showRings['width'], meas.bt_showRings['height'], screen,
                        path=meas.bt_showRings['path_white'],
                        image_ofset=meas.bt_class_inactive['image_offset'],
                        border_radius=meas.bt_class_inactive['border_radius'])

    bt_showNecklaces = Button(meas.bt_class_inactive['color'],
                        meas.bt_showNecklaces['x'], meas.bt_showNecklaces['y'],
                        meas.bt_showNecklaces['width'], meas.bt_showNecklaces['height'], screen,
                        path=meas.bt_showNecklaces['path_white'],
                        image_ofset=meas.bt_class_inactive['image_offset'],
                        border_radius=meas.bt_class_inactive['border_radius'])

    bt_showSceptres = Button(meas.bt_class_inactive['color'],
                        meas.bt_showSceptres['x'], meas.bt_showSceptres['y'],
                        meas.bt_showSceptres['width'], meas.bt_showSceptres['height'], screen,
                        path=meas.bt_showSceptres['path_white'],
                        image_ofset=meas.bt_class_inactive['image_offset'],
                        border_radius=meas.bt_class_inactive['border_radius'])

    ce_characterEqPreview = CharacterEquipment(meas.ce_characterEqPreview['x'],
                                               meas.ce_characterEqPreview['y'],
                                               meas.ce_characterEqPreview['font'],
                                               meas.ce_characterEqPreview['colors'],
                                               character_2,
                                               screen)

    label_gold = Label("Gold: " + str(character_2['gold']), meas.label_gold['font'],
                       meas.label_gold['color'], screen, meas.label_gold['x'],
                       meas.label_gold['y'], meas.label_gold['anchor'])

    category_buttons = [
        ('potions', meas.bt_showPotions['path_white'],
            meas.bt_showPotions['path_gray'], bt_showPotions),
        ('rings', meas.bt_showRings['path_white'],
            meas.bt_showRings['path_gray'], bt_showRings),
        ('necklaces', meas.bt_showNecklaces['path_white'],
            meas.bt_showNecklaces['path_gray'], bt_showNecklaces),
        ('sceptres', meas.bt_showSceptres['path_white'],
            meas.bt_showSceptres['path_gray'], bt_showSceptres),
    ]

    displayedContent = [
        label_page, bt_return, ce_characterEqPreview, label_gold
    ]

    while isRunning:
        screen.fill((255, 255, 255))
        if showHand:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        ig_items = reloadItemGrid(category_active)
        ig_items.draw()

        for elem in displayedContent:
            elem.draw()

        category_buttons = reloadButtons(category_buttons, category_active)

        for name, path_white, path_gray, button in category_buttons:
            button.draw()

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
                    # HANDLE CATEGORY BUTTONS
                    for name, path_white, path_gray, button in category_buttons:
                        if button.rect.collidepoint(event.pos):
                            category_active = name

                    # HANDLE RETURN BUTTON
                    if bt_return.rect.collidepoint(event.pos):
                        isRunning = False
                        print("Redirecting: ArmorShop.py -> CityMap.py")

        pygame.display.update()
        mainClock.tick(60)
