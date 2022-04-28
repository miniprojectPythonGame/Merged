import pygame
import sys
from pygame.locals import *

from api.web.user import User
from src.components.InputField import InputField
from src.components.ImageField import ImageField
from src.components.Label import Label
from src.components.MultilineText import MultilineText
from src.components.Button import Button
from src.components.Checkbox import Checkbox

from src.pages.register_screen.RegisterScreen import RegisterScreen
from src.pages.choose_character.ChooseCharacter import ChooseCharacter

from .Measurements import Measurements as meas

def LoginScreen(screen, mainClock):

    user = User()

    # Function to validate input on Login
    def validate():
        if len(input_nickname.text) < 8:
            return False
        if len(input_password.text) < 8:
            return False
        return True

    image = ImageField(meas.graphic['x'], meas.graphic['y'],
                       meas.graphic['width'], meas.graphic['height'],
                       '../images/pages/login_screen/image_1.png', screen)

    logo = ImageField(meas.logo['x'], meas.logo['y'],
                       meas.logo['width'], meas.logo['height'],
                       '../images/logo_100x37.png', screen)

    label_login = Label(meas.label_login['text'], meas.title_font, meas.text_color, screen,
                        meas.label_login['x'], meas.label_login['y'], meas.label_login['anchor'])

    mt_description = MultilineText(meas.mt_desc['text'], meas.text_font, meas.text_color,
                                   screen, meas.mt_desc['x'], meas.mt_desc['y'],
                                   meas.mt_desc['line_height'], meas.mt_desc['anchor'])

    input_nickname = InputField(meas.input_nick['x'], meas.input_nick['y'],
                                meas.input_nick['width'], meas.input_nick['height'],
                                meas.input_nick['border'], meas.input_nick['color'],
                                screen, 'Nickname', meas.nickname_length)

    input_password = InputField(meas.input_pass['x'], meas.input_pass['y'],
                                meas.input_pass['width'], meas.input_pass['height'],
                                meas.input_pass['border'], meas.input_pass['color'],
                                screen, 'Password', meas.password_length, isPassword=True)

    cb_remember = Checkbox(meas.cb_remember['color'], meas.cb_remember['x'], meas.cb_remember['y'],
                           meas.cb_remember['width'], meas.cb_remember['height'], screen, meas.cb_remember['border'])

    label_remember = Label(meas.label_remember['text'], meas.header_tertiary_font, meas.text_color, screen,
                        meas.label_remember['x'], meas.label_remember['y'], meas.label_remember['anchor'])

    bt_login = Button(meas.bt_login['color'], meas.bt_login['x'], meas.bt_login['y'],
                      meas.bt_login['width'], meas.bt_login['height'], screen,
                      meas.bt_login['text'], meas.input_font)

    bt_signup = Button(meas.bt_signup['color'], meas.bt_signup['x'], meas.bt_signup['y'],
                      meas.bt_signup['width'], meas.bt_signup['height'], screen,
                      meas.bt_signup['text'], meas.header_tertiary_font, border=2)

    label_signup = Label(meas.label_signup['text'], meas.header_tertiary_font, meas.text_color, screen,
                        meas.label_signup['x'], meas.label_signup['y'], meas.label_signup['anchor'])

    while True:
        screen.fill((255, 255, 255))

        label_login.draw()
        mt_description.draw()
        image.draw()
        logo.draw()

        input_nickname.draw()
        input_password.draw()
        bt_login.draw()
        cb_remember.draw()
        label_remember.draw()
        label_signup.draw()
        bt_signup.draw()

        mx, my = pygame.mouse.get_pos()

        # HOVERS
        # Button login hover
        if bt_login.rect.collidepoint((mx, my)):
            bt_login.onHoverOn()
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            bt_login.onHoverOff()
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        # Button signup hover
        if bt_signup.rect.collidepoint((mx, my)):
            bt_signup.onHoverOn()
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            bt_signup.onHoverOff()
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        # EVENTS
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if input_nickname.active:
                    if event.key == K_BACKSPACE:
                        input_nickname.subtractText()
                    else:
                        input_nickname.appendText(event.unicode)

                if input_password.active:
                    if event.key == K_BACKSPACE:
                        input_password.subtractText()
                    else:
                        input_password.appendText(event.unicode)
            if event.type == MOUSEBUTTONDOWN:
                # if event.button == 1:
                #     click = True

                # 'Nickname' input
                if input_nickname.rect.collidepoint(event.pos):
                    input_nickname.activate()
                else:
                    input_nickname.deactivate()

                # 'Password' input
                if input_password.rect.collidepoint(event.pos):
                    input_password.activate()
                else:
                    input_password.deactivate()

                # 'Remember me' checkbox
                if cb_remember.rect.collidepoint(event.pos):
                    if cb_remember.isSelected:
                        cb_remember.deselect()
                    else:
                        cb_remember.select()

                # 'Login' button
                if bt_login.rect.collidepoint(event.pos):
                    print("Login: ", input_nickname.text, input_password.text, cb_remember.isSelected)
                    # For tests use:
                    if validate():
                        if user.login(input_nickname.text, input_password.text):
                            input_nickname.reset()
                            input_password.reset()
                            ChooseCharacter(screen, mainClock, user)
                        else:
                            print("Login fail")
                    else:
                        print("Validation fail")


                 # 'Sign up' button
                if bt_signup.rect.collidepoint(event.pos):
                    print("Redirect-> Register")
                    RegisterScreen(screen, mainClock, user)


        pygame.display.update()
        mainClock.tick(60)
