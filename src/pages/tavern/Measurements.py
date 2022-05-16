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

    bt_return = BT_RETURN

    # LABEL: Page
    label_page = {
        'text': 'Tavern',
        'x': margin,
        'y': 20,
        'anchor': 'topleft',
        'font': header_primary_font,
        'color': text_color,
    }

    # LIST_ELEMENT: some bow
    le_general = {
        "x": margin,
        "y": margin,
        "width": 650,
        "height": 60,
        "colors": default_color,
        "property_name": "Level: ",
    }

    sl_quests = {
        "x": margin,
        "y": margin,
    }