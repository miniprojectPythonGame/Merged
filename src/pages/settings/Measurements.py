from src.globals.const_values import *


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
    white = pygame.Color('white')
    label_padding = 35
    class_button_size = 60

    bt_return = BT_RETURN

    # LABEL: Page
    label_page = {
        'text': 'Settings',
        'x': window_width - margin,
        'y': 20,
        'anchor': 'topright',
        'font': header_primary_font,
        'color': text_color,
    }