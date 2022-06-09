import pygame
import sys
from pygame.locals import *

from src.components.Navbar import Navbar
from src.components.Button import Button
from src.components.ImageField import ImageField
from .Measurements import Measurements as meas

from src.pages.character_profile.CharacterProfile import CharacterProfile
from src.pages.settings.Settings import Settings
from src.pages.armor_shop.ArmorShop import ArmorShop
from src.pages.magic_shop.MagicShop import MagicShop
from src.pages.weapon_shop.WeaponShop import WeaponShop
from src.pages.tavern.Tavern import Tavern
from src.pages.arena.Arena import Arena


def CityMap(screen, mainClock, user):

    showHand = False
    running = True
    swapHero = False

    img_map = ImageField(meas.img_map['x'], meas.img_map['y'],
                         meas.img_map['width'], meas.img_map['height'],
                         meas.img_map['img_path'], screen)

    bt_marketplace = Button(meas.bt_marketplace['color'],
                            meas.bt_marketplace['x'], meas.bt_marketplace['y'],
                            meas.bt_marketplace['width'], meas.bt_marketplace['height'],
                            screen, text=meas.bt_marketplace['text'],
                            font=meas.bt_marketplace['font'], border_radius=meas.bt_marketplace['border_radius'])

    bt_arena = Button(meas.bt_arena['color'],
                            meas.bt_arena['x'], meas.bt_arena['y'],
                            meas.bt_arena['width'], meas.bt_arena['height'],
                            screen, text=meas.bt_arena['text'],
                            font=meas.bt_arena['font'], border_radius=meas.bt_arena['border_radius'])

    bt_weaponShop = Button(meas.bt_weaponShop['color'],
                            meas.bt_weaponShop['x'], meas.bt_weaponShop['y'],
                            meas.bt_weaponShop['width'], meas.bt_weaponShop['height'],
                            screen, text=meas.bt_weaponShop['text'],
                            font=meas.bt_weaponShop['font'], border_radius=meas.bt_weaponShop['border_radius'])

    bt_magicShop = Button(meas.bt_magicShop['color'],
                            meas.bt_magicShop['x'], meas.bt_magicShop['y'],
                            meas.bt_magicShop['width'], meas.bt_magicShop['height'],
                            screen, text=meas.bt_magicShop['text'],
                            font=meas.bt_magicShop['font'], border_radius=meas.bt_magicShop['border_radius'])

    bt_armorShop = Button(meas.bt_armorShop['color'],
                            meas.bt_armorShop['x'], meas.bt_armorShop['y'],
                            meas.bt_armorShop['width'], meas.bt_armorShop['height'],
                            screen, text=meas.bt_armorShop['text'],
                            font=meas.bt_armorShop['font'], border_radius=meas.bt_armorShop['border_radius'])

    bt_tavern = Button(meas.bt_tavern['color'],
                            meas.bt_tavern['x'], meas.bt_tavern['y'],
                            meas.bt_tavern['width'], meas.bt_tavern['height'],
                            screen, text=meas.bt_tavern['text'],
                            font=meas.bt_tavern['font'], border_radius=meas.bt_tavern['border_radius'])

    displayedContent = [
        img_map,
        bt_marketplace, bt_arena, bt_weaponShop, bt_magicShop, bt_armorShop, bt_tavern
    ]

    navbar = Navbar(screen)
    hero = user.currentHero
    hero.gen_eq()

    while running:
        screen.fill((255, 255, 255))
        if showHand:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for elem in displayedContent:
            elem.draw()

        navbar.draw()

        mx, my = pygame.mouse.get_pos()

        # HOVER EVENTS
        if bt_marketplace.rect.collidepoint((mx, my)):
            bt_marketplace.onHoverOn()
            showHand = True
        elif bt_arena.rect.collidepoint((mx, my)):
            bt_arena.onHoverOn()
            showHand = True
        elif bt_weaponShop.rect.collidepoint((mx, my)):
            bt_weaponShop.onHoverOn()
            showHand = True
        elif bt_magicShop.rect.collidepoint((mx, my)):
            bt_magicShop.onHoverOn()
            showHand = True
        elif bt_armorShop.rect.collidepoint((mx, my)):
            bt_armorShop.onHoverOn()
            showHand = True
        elif bt_tavern.rect.collidepoint((mx, my)):
            bt_tavern.onHoverOn()
            showHand = True
        else:
            bt_marketplace.onHoverOff()
            bt_arena.onHoverOff()
            bt_weaponShop.onHoverOff()
            bt_magicShop.onHoverOff()
            bt_armorShop.onHoverOff()
            bt_tavern.onHoverOff()
            showHand = False

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
                    # HANDLE NAVBAR BUTTONS
                    # CHARACTER PROFILE
                    if navbar.bt_profile.rect.collidepoint(event.pos):
                        CharacterProfile(screen, mainClock, user)
                        hero.gen_eq()
                        break

                    # SETTINGS
                    if navbar.bt_settings.rect.collidepoint(event.pos):
                        Settings(screen, mainClock)
                        hero.gen_eq()
                        break

                    # SWAP HERO
                    if navbar.bt_swap_hero.rect.collidepoint(event.pos):
                        user.deselect_hero()
                        running = False
                        swapHero = True
                        break

                    # LOGOUT
                    if navbar.bt_logout.rect.collidepoint(event.pos):
                        user.logout()
                        running = False
                        break


                    # HANDLE CITY PLACES
                    if bt_armorShop.rect.collidepoint(event.pos):
                        ArmorShop(screen, mainClock, user)
                        hero.gen_eq()
                        break

                    if bt_magicShop.rect.collidepoint(event.pos):
                        MagicShop(screen, mainClock, user)
                        hero.gen_eq()
                        break

                    if bt_weaponShop.rect.collidepoint(event.pos):
                        WeaponShop(screen, mainClock, user)
                        hero.gen_eq()
                        break

                    if bt_tavern.rect.collidepoint(event.pos):
                        Tavern(screen, mainClock, user)
                        hero.gen_eq()
                        break

                    if bt_arena.rect.collidepoint(event.pos):
                        Arena(screen, mainClock, user)
                        hero.gen_eq()
                        break

        pygame.display.update()
        mainClock.tick(60)

    return swapHero