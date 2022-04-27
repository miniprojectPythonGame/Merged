import pygame
import sys
from pygame.locals import *

from frontend.src.components.Label import Label
from frontend.src.components.ImageField import ImageField
from frontend.src.components.InputField import InputField
from frontend.src.components.Button import Button
from frontend.src.components.CharacterPreview import CharacterPreview

from .Measurements import Measurements as meas
from frontend.src.globals.mock_data import warrior_avatars, mage_avatars, archer_avatars

def CreateCharacter(screen, mainClock):

    def generateAvatarsOfCurrentClass(currentClass):
        temp = []
        if currentClass == 'warrior':
            for i in range(len(warrior_avatars)):
                temp.append(ImageField(meas.images[i]['x'], meas.images[i]['y'],
                                         meas.images[i]['width'], meas.images[i]['height'],
                                         warrior_avatars[i]['rect'], screen))

        if currentClass == 'mage':
            for i in range(len(warrior_avatars)):
                temp.append(ImageField(meas.images[i]['x'], meas.images[i]['y'],
                                         meas.images[i]['width'], meas.images[i]['height'],
                                         mage_avatars[i]['rect'], screen))

        if currentClass == 'archer':
            for i in range(len(warrior_avatars)):
                temp.append(ImageField(meas.images[i]['x'], meas.images[i]['y'],
                                         meas.images[i]['width'], meas.images[i]['height'],
                                         archer_avatars[i]['rect'], screen))

        return temp

    def reloadPreviewBars(name, className, path):
        return CharacterPreview(meas.cp_createdCharacter['x'], meas.cp_createdCharacter['y'],
                           meas.cp_createdCharacter['width'], meas.cp_createdCharacter['height'],
                           meas.cp_createdCharacter['width']-80, meas.property_bar_height, name,
                           className.capitalize(), 1, path,
                           screen, meas.header_secondary_font)

    running = True
    curr_active = 'warrior'
    curr_avatarImage = warrior_avatars[0]['rect']

    label_page = Label(meas.label_page['text'], meas.label_page['font'], meas.label_page['color'], screen,
                       meas.label_page['x'], meas.label_page['y'], meas.label_page['anchor'])

    bt_return = Button(meas.bt_return['color'], meas.bt_return['x'], meas.bt_return['y'],
                       meas.bt_return['width'], meas.bt_return['height'], screen,
                       path=meas.bt_return['path'])

    # NAME SECTION
    label_name = Label(meas.label_name['text'], meas.label_name['font'], meas.label_name['color'], screen,
                       meas.label_name['x'], meas.label_name['y'], meas.label_name['anchor'])

    input_name = InputField(meas.input_name['x'], meas.input_name['y'],
                            meas.input_name['width'], meas.input_name['height'],
                            meas.input_name['border'], meas.input_name['color'],
                            screen, meas.input_name['placeholder'], meas.nickname_length)

    # CLASS SECTION
    label_class = Label(meas.label_class['text'], meas.label_class['font'], meas.label_class['color'], screen,
                        meas.label_class['x'], meas.label_class['y'], meas.label_class['anchor'])

    bt_warrior_active = Button(meas.bt_class_active['color'],
                        meas.bt_warrior['x'], meas.bt_warrior['y'],
                        meas.bt_warrior['width'], meas.bt_warrior['height'], screen,
                        path=meas.bt_warrior['path_white'],
                        image_ofset=meas.bt_class_active['image_offset'],
                        border_radius=meas.bt_class_active['border_radius'])

    bt_warrior_inactive = Button(meas.bt_class_inactive['color'],
                        meas.bt_warrior['x'], meas.bt_warrior['y'],
                        meas.bt_warrior['width'], meas.bt_warrior['height'], screen,
                        path=meas.bt_warrior['path_gray'],
                        image_ofset=meas.bt_class_inactive['image_offset'],
                        border_radius=meas.bt_class_inactive['border_radius'])

    bt_mage_active = Button(meas.bt_class_active['color'],
                     meas.bt_mage['x'], meas.bt_mage['y'],
                     meas.bt_mage['width'], meas.bt_mage['height'], screen,
                     path=meas.bt_mage['path_white'],
                     image_ofset=meas.bt_class_active['image_offset'],
                     border_radius=meas.bt_class_active['border_radius'])

    bt_mage_inactive = Button(meas.bt_class_inactive['color'],
                     meas.bt_mage['x'], meas.bt_mage['y'],
                     meas.bt_mage['width'], meas.bt_mage['height'], screen,
                     path=meas.bt_mage['path_gray'],
                     image_ofset=meas.bt_class_inactive['image_offset'],
                     border_radius=meas.bt_class_inactive['border_radius'])

    bt_archer_active = Button(meas.bt_class_active['color'],
                       meas.bt_archer['x'], meas.bt_archer['y'],
                       meas.bt_archer['width'], meas.bt_archer['height'], screen,
                       path=meas.bt_archer['path_white'],
                       image_ofset=meas.bt_class_active['image_offset'],
                       border_radius=meas.bt_class_active['border_radius'])

    bt_archer_inactive = Button(meas.bt_class_inactive['color'],
                       meas.bt_archer['x'], meas.bt_archer['y'],
                       meas.bt_archer['width'], meas.bt_archer['height'], screen,
                       path=meas.bt_archer['path_gray'],
                       image_ofset=meas.bt_class_inactive['image_offset'],
                       border_radius=meas.bt_class_inactive['border_radius'])

    # AVATARS SECTION
    label_avatar = Label(meas.label_avatar['text'], meas.label_avatar['font'], meas.label_avatar['color'], screen,
                         meas.label_avatar['x'], meas.label_avatar['y'], meas.label_avatar['anchor'])

    bt_create = Button(meas.bt_create['color'], meas.bt_create['x'], meas.bt_create['y'],
                      meas.bt_create['width'], meas.bt_create['height'], screen,
                      meas.bt_create['text'], meas.input_font)

    while running:
        screen.fill((255, 255, 255))

        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        label_page.draw()
        bt_return.draw()
        label_name.draw()
        input_name.draw()

        label_class.draw()
        if curr_active == 'warrior':
            bt_warrior_active.draw()
            bt_mage_inactive.draw()
            bt_archer_inactive.draw()

        if curr_active == 'mage':
            bt_warrior_inactive.draw()
            bt_mage_active.draw()
            bt_archer_inactive.draw()

        if curr_active == 'archer':
            bt_warrior_inactive.draw()
            bt_mage_inactive.draw()
            bt_archer_active.draw()

        label_avatar.draw()
        images = generateAvatarsOfCurrentClass(curr_active)
        for image in images:
            image.draw()

        cp_createdCharacter = reloadPreviewBars(input_name.text, curr_active, curr_avatarImage)
        cp_createdCharacter.draw()

        bt_create.draw()

        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                # Input name
                if input_name.active:
                    if event.key == K_BACKSPACE:
                        input_name.subtractText()
                    else:
                        input_name.appendText(event.unicode)

            if event.type == MOUSEBUTTONDOWN:
                # 'Name' input activate
                if input_name.rect.collidepoint(event.pos):
                    input_name.activate()
                else:
                    input_name.deactivate()

                # Pick 'warrior' class
                if bt_warrior_inactive.rect.collidepoint(event.pos):
                    curr_active = 'warrior'
                    curr_avatarImage = warrior_avatars[0]['rect']
                    print(curr_active)

                # Pick 'mage' class
                if bt_mage_inactive.rect.collidepoint(event.pos):
                    curr_active = 'mage'
                    curr_avatarImage = mage_avatars[0]['rect']
                    print(curr_active)

                # Pick 'archer' class
                if bt_archer_inactive.rect.collidepoint(event.pos):
                    curr_active = 'archer'
                    curr_avatarImage = archer_avatars[0]['rect']
                    print(curr_active)

                for image in images:
                    if image.rect.collidepoint(event.pos):
                        curr_avatarImage = image.path

                if bt_create.rect.collidepoint(event.pos):
                    running = False
                    print("Redirecting: CreateCharacter.py -> ChooseCharacter.py")

                # HANDLE RETURN BUTTON
                if bt_return.rect.collidepoint(event.pos):
                    running = False
                    print("Redirecting: CreateCharacter.py -> ChooseCharacter.py")


        pygame.display.update()
        mainClock.tick(60)
