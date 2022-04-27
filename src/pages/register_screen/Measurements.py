from src.globals.const_values import *
from src.components.ColorSchemes import ColorSchemes


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
    input_height = 30
    input_margin = 15

    # IMAGE: graphic
    graphic = {
        'x': window_width - round(SCREEN_WIDTH * SIZE_FACTOR * 0.45),
        'y': 0,
        'width': round(SCREEN_WIDTH * SIZE_FACTOR * 0.45),
        'height': round(SCREEN_HEIGHT * SIZE_FACTOR),
    }

    # IMAGE: logo
    logo = {
        'x': 30,
        'y': 30,
        'width': logo_width,
        'height': logo_height,
    }

    # LABEL: Register
    label_login = {
        'text': 'Register',
        'x': margin + round((SCREEN_WIDTH * SIZE_FACTOR) - (graphic['width'] + 2 * margin)),
        'y': margin - 50,
        'anchor': 'topright',
    }

    # MultilineText: Description
    mt_desc = {
        'text': [
            'Praesent vel tellus accumsan nisl tincidunt.',
            'Pellentesque ullamcorper venenatis lorem et.',],
        'x': margin + round((SCREEN_WIDTH * SIZE_FACTOR) - (graphic['width'] + 2 * margin)),
        'y': margin + 30,
        'anchor': 'topright',
        'line_height': 20,
    }

    # INPUT: Nickname
    input_nick = {
        "padding": 5,
        "border": border,
        "color": ColorSchemes(),
        "x": margin,
        "y": margin + 90,
        "width": round((SCREEN_WIDTH * SIZE_FACTOR) - (graphic['width'] + 2 * margin)),
        "height": input_height,
    }

    # INPUT: Email
    input_email = {
        "padding": 5,
        "border": border,
        "color": ColorSchemes(),
        "x": margin,
        "y": input_nick['y'] + input_height + input_margin,
        "width": round((SCREEN_WIDTH * SIZE_FACTOR) - (graphic['width'] + 2 * margin)),
        "height": input_height,
    }

    # INPUT: Password
    input_pass = {
        "padding": 5,
        "border": border,
        "color": ColorSchemes(),
        "x": margin,
        "y": input_email['y'] + input_height + input_margin,
        "width": round((SCREEN_WIDTH * SIZE_FACTOR) - (graphic['width'] + 2 * margin)),
        "height": input_height,
    }

    # LABEL: Sex
    label_sex = {
        'text': 'Sex',
        "x": margin,
        "y": input_pass['y'] + input_height + input_margin,
        'anchor': 'topleft',
    }

    # LABEL: female sex
    label_female = {
        'text': 'female',
        "x": margin + input_nick['width'],
        "y": input_pass['y'] + input_height + input_margin,
        'anchor': 'topright',
    }

    # Checkbox: male sex
    cb_female = {
        "color": ColorSchemes(),
        "x": label_female['x'] - 100,
        "y": input_pass['y'] + input_height + input_margin,
        "width": 20,
        "height": 20,
        "border": border,
    }

    # LABEL: male sex
    label_male = {
        'text': 'male',
        "x": cb_female['x'] - 80,
        "y": input_pass['y'] + input_height + input_margin,
        'anchor': 'topleft',
    }

    # Checkbox: male sex
    cb_male = {
        "color": ColorSchemes(),
        "x": label_male['x'] - 30,
        "y": input_pass['y'] + input_height + input_margin,
        "width": 20,
        "height": 20,
        "border": border,
    }

    # LABEL: Age
    label_age = {
        'text': 'Age',
        "x": margin,
        "y": cb_male['y'] + input_height + input_margin,
        'anchor': 'topleft',
    }

    # INPUT: Password
    input_age = {
        "padding": 5,
        "border": border,
        "color": ColorSchemes(),
        "x": margin + input_nick['width'] - 211,
        "y": label_age['y'] - 5,
        "width": 211,
        "height": input_height,
    }

    # BUTTON: Register
    bt_register = {
        "color": ColorSchemes(),
        "x": margin,
        "y": margin + 310,
        "width": input_pass['width'],
        "height": 50,
        "text": 'Register'
    }

    # LABEL: Signin
    label_signup = {
        'text': 'Already registered?',
        'x': margin + input_nick['width'] - 120,
        'y': window_height - margin + 8,
        'anchor': 'topright',
    }

    # BUTTON: Signin
    bt_signup = {
        "color": ColorSchemes(),
        'x': margin + input_nick['width'] - 100,
        "y": window_height - margin,
        "width": 100,
        "height": 35,
        "text": 'Sign in'
    }