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
    category_button_size = 60
    category_button_padding = 20
    magic_shop_category_offset = round(2.3*category_button_padding) + category_button_size

    default_color = ColorSchemes()

    bt_return = BT_RETURN

    # LABEL: Page
    label_page = {
        'text': 'Magic shop',
        'x': margin,
        'y': 20,
        'anchor': 'topleft',
        'font': header_primary_font,
        'color': text_color,
    }

    # CHARACTER_EQUIPMENT: -//-
    ce_characterEqPreview = {
        "x": window_width - 510 - margin,
        "y": margin - 30,
        "font": header_tertiary_font,
        "colors": default_color,
    }

    # ITEM_GRID: shop offer
    ig_items = {
        "x": margin + category_button_padding,
        "y": margin + category_button_padding + category_button_size,
        "item_size": 80,
        "item_padding": 8,
        "cols": 4,
        "amount": 20,
    }

    # BUTTON (type): class inactive
    bt_class_active = {
        "color": ColorSchemes(inactive=pygame.Color('#333333')),
        "border_radius": 5,
        "image_offset": 7,
    }

    # BUTTON (type): class active
    bt_class_inactive = {
        "color": ColorSchemes(inactive=pygame.Color('white')),
        "border_radius": 5,
        "image_offset": 5,
    }

    # BUTTON: Show potions in offer
    bt_showPotions = {
        "x": margin,
        "y": margin,
        "width": category_button_size,
        "height": category_button_size,
        "path_white": '../images/item_type_icons/magic/potion_white.png',
        "path_gray": '../images/item_type_icons/magic/potion_gray.png',
    }

    # BUTTON: Show rings in offer
    bt_showRings = {
        "x": bt_showPotions['x'] + magic_shop_category_offset,
        "y": margin,
        "width": category_button_size,
        "height": category_button_size,
        "path_white": '../images/item_type_icons/magic/ring_white.png',
        "path_gray": '../images/item_type_icons/magic/ring_gray.png',
    }

    # BUTTON: Show necklaces in offer
    bt_showNecklaces = {
        "x": bt_showRings['x'] + magic_shop_category_offset,
        "y": margin,
        "width": category_button_size,
        "height": category_button_size,
        "path_white": '../images/item_type_icons/magic/necklace_white.png',
        "path_gray": '../images/item_type_icons/magic/necklace_gray.png',
    }

    # BUTTON: Show sceptres in offer
    bt_showSceptres = {
        "x": bt_showNecklaces['x'] + magic_shop_category_offset,
        "y": margin,
        "width": category_button_size,
        "height": category_button_size,
        "path_white": '../images/item_type_icons/magic/sceptre_white.png',
        "path_gray": '../images/item_type_icons/magic/sceptre_gray.png',
    }

    # LABEL: Gold
    label_gold = {
        'x': margin,
        'y': window_height - (margin - 10),
        'anchor': 'topleft',
        'font': header_tertiary_font,
        'color': text_color,
    }