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

    default_color = ColorSchemes()

    bt_return = BT_RETURN

    # LABEL: Page
    label_page = {
        'text': 'Weapon shop',
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

    # SCROLLBAR: Shop offer scrollbar
    sb_offerScrollbar = {
        "x": margin,
        "y": margin + category_button_size + category_button_padding,
        "width": 15,
        "height": window_height - (2*margin + category_button_size + category_button_padding),
        "height_scroll": 200,
        "border": 0,
        "border_radius": 5,
    }

    # ITEM_GRID: shop offer
    ig_items = {
        "x": margin + sb_offerScrollbar['width'] + category_button_padding,
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

    # BUTTON: Show helmets in offer
    bt_showSwords = {
        "x": margin,
        "y": margin,
        "width": category_button_size,
        "height": category_button_size,
        "path_white": '../images/item_type_icons/weapon/sword_white.png',
        "path_gray": '../images/item_type_icons/weapon/sword_gray.png',
    }

    # BUTTON: Show chestplates in offer
    bt_showShields = {
        "x": margin + category_button_padding + category_button_size,
        "y": margin,
        "width": category_button_size,
        "height": category_button_size,
        "path_white": '../images/item_type_icons/weapon/shield_white.png',
        "path_gray": '../images/item_type_icons/weapon/shield_gray.png',
    }

    # BUTTON: Show gloves in offer
    bt_showHammers = {
        "x": margin + 2*category_button_padding + 2*category_button_size,
        "y": margin,
        "width": category_button_size,
        "height": category_button_size,
        "path_white": '../images/item_type_icons/weapon/hammer_white.png',
        "path_gray": '../images/item_type_icons/weapon/hammer_gray.png',
    }

    # BUTTON: Show boots in offer
    bt_showBows = {
        "x": margin + 3*category_button_padding + 3*category_button_size,
        "y": margin,
        "width": category_button_size,
        "height": category_button_size,
        "path_white": '../images/item_type_icons/weapon/bow_white.png',
        "path_gray": '../images/item_type_icons/weapon/bow_gray.png',
    }

    # BUTTON: Show belts in offer
    bt_showDaggers = {
        "x": margin + 4*category_button_padding + 4*category_button_size,
        "y": margin,
        "width": category_button_size,
        "height": category_button_size,
        "path_white": '../images/item_type_icons/weapon/dagger_white.png',
        "path_gray": '../images/item_type_icons/weapon/dagger_gray.png',
    }

    # LABEL: Gold
    label_gold = {
        'x': margin,
        'y': window_height - (margin - 10),
        'anchor': 'topleft',
        'font': header_tertiary_font,
        'color': text_color,
    }