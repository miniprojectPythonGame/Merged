import pygame
import sys
from pygame.locals import *

from frontend.src.components.Button import Button
from frontend.src.components.Label import Label
from frontend.src.components.CharacterEquipment import CharacterEquipment
from frontend.src.components.ItemGrid import ItemGrid
from frontend.src.components.Scrollbar import Scrollbar

from .Measurements import Measurements as meas

from frontend.src.globals.mock_data import weapon_shop, character_2


def WeaponShop(screen, mainClock):

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
                        screen, weapon_shop[category_active])

    showHand = False
    isRunning = True
    category_active = 'swords'


    label_page = Label(meas.label_page['text'], meas.label_page['font'], meas.label_page['color'], screen,
                       meas.label_page['x'], meas.label_page['y'], meas.label_page['anchor'])

    bt_return = Button(meas.bt_return['color'], meas.bt_return['x'], meas.bt_return['y'],
                       meas.bt_return['width'], meas.bt_return['height'], screen,
                       path=meas.bt_return['path'])

    bt_showSwords = Button(meas.bt_class_active['color'],
                        meas.bt_showSwords['x'], meas.bt_showSwords['y'],
                        meas.bt_showSwords['width'], meas.bt_showSwords['height'], screen,
                        path=meas.bt_showSwords['path_white'],
                        image_ofset=meas.bt_class_active['image_offset'],
                        border_radius=meas.bt_class_active['border_radius'])

    bt_showShields = Button(meas.bt_class_inactive['color'],
                        meas.bt_showShields['x'], meas.bt_showShields['y'],
                        meas.bt_showShields['width'], meas.bt_showShields['height'], screen,
                        path=meas.bt_showShields['path_white'],
                        image_ofset=meas.bt_class_inactive['image_offset'],
                        border_radius=meas.bt_class_inactive['border_radius'])

    bt_showHammers = Button(meas.bt_class_inactive['color'],
                        meas.bt_showHammers['x'], meas.bt_showHammers['y'],
                        meas.bt_showHammers['width'], meas.bt_showHammers['height'], screen,
                        path=meas.bt_showHammers['path_white'],
                        image_ofset=meas.bt_class_inactive['image_offset'],
                        border_radius=meas.bt_class_inactive['border_radius'])

    bt_showBows = Button(meas.bt_class_inactive['color'],
                        meas.bt_showBows['x'], meas.bt_showBows['y'],
                        meas.bt_showBows['width'], meas.bt_showBows['height'], screen,
                        path=meas.bt_showBows['path_white'],
                        image_ofset=meas.bt_class_inactive['image_offset'],
                        border_radius=meas.bt_class_inactive['border_radius'])

    bt_showDaggers = Button(meas.bt_class_inactive['color'],
                        meas.bt_showDaggers['x'], meas.bt_showDaggers['y'],
                        meas.bt_showDaggers['width'], meas.bt_showDaggers['height'], screen,
                        path=meas.bt_showDaggers['path_white'],
                        image_ofset=meas.bt_class_inactive['image_offset'],
                        border_radius=meas.bt_class_inactive['border_radius'])

    ce_characterEqPreview = CharacterEquipment(meas.ce_characterEqPreview['x'],
                                               meas.ce_characterEqPreview['y'],
                                               meas.ce_characterEqPreview['font'],
                                               meas.ce_characterEqPreview['colors'],
                                               character_2,
                                               screen)

    sb_offerScrollbar = Scrollbar(meas.sb_offerScrollbar['x'], meas.sb_offerScrollbar['y'],
                                  meas.sb_offerScrollbar['width'], meas.sb_offerScrollbar['height'],
                                  meas.sb_offerScrollbar['height_scroll'], screen,
                                  border=meas.sb_offerScrollbar['border'],
                                  border_radius=meas.sb_offerScrollbar['border_radius'])

    label_gold = Label("Gold: " + str(character_2['gold']), meas.label_gold['font'],
                       meas.label_gold['color'], screen, meas.label_gold['x'],
                       meas.label_gold['y'], meas.label_gold['anchor'])

    category_buttons = [
        ('swords', meas.bt_showSwords['path_white'],
            meas.bt_showSwords['path_gray'], bt_showSwords),
        ('shields', meas.bt_showShields['path_white'],
            meas.bt_showShields['path_gray'], bt_showShields),
        ('hammers', meas.bt_showHammers['path_white'],
            meas.bt_showHammers['path_gray'], bt_showHammers),
        ('bows', meas.bt_showBows['path_white'],
            meas.bt_showBows['path_gray'], bt_showBows),
        ('daggers', meas.bt_showDaggers['path_white'],
            meas.bt_showDaggers['path_gray'], bt_showDaggers),
    ]

    displayedContent = [
        label_page, bt_return, ce_characterEqPreview, sb_offerScrollbar, label_gold
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
