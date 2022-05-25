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
    white = pygame.Color('white')
    label_padding = 35
    list_element_width = 650
    list_element_height = 60
    list_element_padding = 15
    default_color = ColorSchemes()

    plane_padding = 15
    title_padding = 60
    header_padding = 30

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
        "width": list_element_width,
        "height": list_element_height,
        "colors": default_color,
        "property_name": "Level: ",
    }

    sl_quests = {
        "x": margin,
        "y": margin,
    }

    # PLANE: background
    p_background = {
        "color": default_color.inactive,
        "x": window_width - (margin + (window_width - (3 * margin + list_element_width))),
        "y": margin,
        "width": window_width - (3 * margin + list_element_width),
        "height": window_height - 2 * margin,
    }

    # LABEL: quest title
    lb_quest_title = {
        'x': p_background['x'] + plane_padding,
        'y': p_background['y'] + plane_padding,
        'anchor': 'topleft',
        'font': header_secondary_font,
        'color': white,
    }

    # LABEL: difficulty
    lb_difficulty_header = {
        'x': p_background['x'] + plane_padding,
        'y': p_background['y'] + plane_padding + title_padding,
        'anchor': 'topleft',
        'font': text_font,
        'color': white,
    }

    # LABEL: min level
    lb_min_level_header = {
        'x': p_background['x'] + plane_padding,
        'y': p_background['y'] + plane_padding + title_padding + header_padding,
        'anchor': 'topleft',
        'font': text_font,
        'color': white,
    }

    # BUTTON: fight
    bt_fight = {
        "color": ColorSchemes(inactive="#aaaaaa", text_secondary_color="#ffffff"),
        'x': p_background['x'] + plane_padding,
        'y': p_background['y'] + p_background['height'] - (plane_padding + 40),
        "width": p_background['width'] - 2 * plane_padding,
        "height": 40,
        "text": 'Fight',
        "border-radius": 10,
    }