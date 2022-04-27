from frontend.src.globals.const_values import *
from frontend.src.components.ColorSchemes import ColorSchemes


class Measurements:
    # WINDOW PARAMETERS
    size_factor = SIZE_FACTOR
    window_width = SCREEN_WIDTH * size_factor
    window_height = SCREEN_HEIGHT * size_factor
    margin = round(SCREEN_WIDTH * SIZE_FACTOR * 0.12)

    # ACCOUNT PROPERTIES
    nickname_length = NICKNAME_LENGTH
    password_length = PASSWORD_LENGTH

    # LOGO PARAMETERS
    logo_size_factor = 1
    logo_width = 100 * logo_size_factor
    logo_height = 37 * logo_size_factor

    # FONTS: sizes
    title_font = TITLE_FONT
    header_primary_font = HEADER_PRIMARY_FONT
    header_secondary_font = HEADER_SECONDARY_FONT
    header_tertiary_font = HEADER_TERTIARY_FONT
    text_font = TEXT_FONT
    input_font = INPUT_FONT

    # FONTS: colors
    text_color = pygame.Color('gray26')

    border = 1

    # left -> right
    # IMAGE: graphic
    graphic = {
        'x': 0,
        'y': 0,
        'width': round(window_width * 0.45),
        'height': round(window_height),
    }

    # IMAGE: logo
    logo = {
        'x': graphic['width'] + 30,
        'y': 30,
        'width': logo_width,
        'height': logo_height,
    }

    # LABEL: Login
    label_login = {
        'text': 'Login',
        'x': window_width - margin,
        'y': margin - 50,
        'anchor': 'topright',
    }

    # MultilineText: Description
    mt_desc = {
        'text': [
            'Lorem ipsum dolor sit amet, consectetur',
            'adipiscing elit. Duis porttitor diam tincidunt',
            'neque viverra blandit.'],
        'x': window_width - margin,
        'y': margin + 30,
        'anchor': 'topright',
        'line_height': 20,
    }

    # INPUT: Nickname
    input_nick = {
        "padding": 5,
        "border": border,
        "color": ColorSchemes(),
        "x": graphic['width'] + margin,
        "y": margin + 110,
        "width": round(window_width - (graphic['width'] + 2 * margin)),
        "height": 50,
    }

    # INPUT: Password
    input_pass = {
        "padding": 5,
        "border": border,
        "color": ColorSchemes(),
        "x": graphic['width'] + margin,
        "y": margin + 190,
        "width": round(window_width - (graphic['width'] + 2 * margin)),
        "height": 50,
    }

    # Checkbox: remember me
    cb_remember = {
        "color": ColorSchemes(),
        "x": graphic['width'] + margin,
        "y": margin + 258,
        "width": 30,
        "height": 30,
        "border": border,
    }

    # Label: remember me
    label_remember = {
        'text': 'Remember me',
        'x': cb_remember['x'] + cb_remember['width'] + 20,
        "y": margin + 264,
        'anchor': 'topleft',
    }

    # BUTTON: Login
    bt_login = {
        "color": ColorSchemes(),
        "x": graphic['width'] + margin,
        "y": margin + 305,
        "width": input_pass['width'],
        "height": input_pass['height'],
        "text": 'Login'
    }

    # LABEL: Signup
    label_signup = {
        'text': 'Need an account?',
        'x': window_width - margin - 110,
        'y': window_height - margin + 8,
        'anchor': 'topright',
    }

    # BUTTON: Signup
    bt_signup = {
        "color": ColorSchemes(),
        "x": window_width - margin - 100,
        "y": window_height - margin,
        "width": 100,
        "height": 35,
        "text": 'Sign up'
    }