from src.globals.const_values import *
from src.components.ColorSchemes import ColorSchemes

class Measurements:
    # WINDOW PARAMETERS
    size_factor = SIZE_FACTOR
    window_width = SCREEN_WIDTH * size_factor
    window_height = SCREEN_HEIGHT * size_factor
    margin = round(SCREEN_WIDTH * SIZE_FACTOR * 0.12 * 0.5)

    # FONTS: sizes
    title_font = TITLE_FONT
    header_primary_font = HEADER_PRIMARY_FONT
    header_secondary_font = HEADER_SECONDARY_FONT
    header_tertiary_font = HEADER_TERTIARY_FONT
    text_font = TEXT_FONT
    input_font = INPUT_FONT

    # FONTS: colors
    text_color = pygame.Color('gray26')
    stat_color = pygame.Color('#35848f')
    white = pygame.Color('white')
    label_padding = 35
    list_element_width = 650
    list_element_height = 60
    list_element_padding = 15
    hero_title_height = 20
    fight_button_height = 50
    default_color = ColorSchemes()

    avatar_size = 300
    avatar_offset = 100

    bt_return = BT_RETURN
    # LABEL: Page
    label_page = {
        'text': 'Arena fight',
        'x': margin,
        'y': 20,
        'anchor': 'topleft',
        'font': header_primary_font,
        'color': text_color,
    }

    label_attacker = {
        'x': margin,
        'y': margin,
        'anchor': 'topleft',
        'font': header_secondary_font,
        'color': text_color,
    }

    img_attacker = {
        'x': margin,
        'y': margin + 30,
        'width': round(AVATAR_FULL_WIDTH * 0.85),
        'height': round(AVATAR_FULL_HEIGHT * 0.85),
    }


    # DEFENDER
    label_defender = {
        'x': window_width - margin,
        'y': margin,
        'anchor': 'topright',
        'font': header_secondary_font,
        'color': text_color,
    }

    img_defender = {
        'x': window_width - (margin + round(AVATAR_FULL_WIDTH * 0.85)),
        'y': margin + 30,
        'width': round(AVATAR_FULL_WIDTH * 0.85),
        'height': round(AVATAR_FULL_HEIGHT * 0.85),
    }

    # COMMON
    label_stat_values_attacker = {
        "font": header_tertiary_font,
        "color": stat_color,
        "x": margin + img_attacker['width'] + 10,
        'y': margin + 30,
        "height": 30,
        "padding": 20,
        "anchor": "topright",
    }

    label_stat_header = {
        "font": header_tertiary_font,
        "color": text_color,
        "x": margin + img_attacker['width'] + 150,
        'y': margin + 30,
        "height": 30,
        "padding": 20,
        "anchor": "center",
    }

    label_stat_values_defender = {
        "font": header_tertiary_font,
        "color": stat_color,
        "x": window_width - (margin + img_defender['width'] + 20),
        'y': margin + 30,
        "height": 30,
        "padding": 20,
        "anchor": "topright",
    }

    pb_health_attacker = {
        'x': margin,
        'y': img_attacker['y'] + img_attacker['height'],
        'width': img_attacker['width'],
        'height': 40,
        'text': "HP",
        'font': text_font,
        'border_color': text_color,
        'fill_color': ColorSchemes().health,
    }

    pb_health_defender = {
        'x': window_width - (margin + round(AVATAR_FULL_WIDTH * 0.85)),
        'y': img_defender['y'] + img_defender['height'],
        'width': img_attacker['width'],
        'height': 40,
        'text': "HP",
        'font': text_font,
        'border_color': text_color,
        'fill_color': ColorSchemes().health,
    }

    bt_speedup = {
        "color": ColorSchemes('white', 'white'),
        "x": margin + img_attacker['width'] + 150,
        "y": window_height - (margin + 64),
        "width": 64,
        "height": 64,
        "path": '../images/icons/speedup_fight.png',
    }