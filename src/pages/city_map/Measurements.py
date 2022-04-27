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
    class_button_size = 60
    default_color = ColorSchemes()

    # MAP SIZE
    img_map = {
        "x": -60,
        "y": -270,
        "width": MAP_WIDTH * MAP_SIZE_FACTOR,
        "height": MAP_HEIGHT * MAP_SIZE_FACTOR,
        "img_path": '../images/map.jpg',
    }

    # BUTTON: Go to marketplace
    bt_marketplace = {
        "color": default_color,
        "x": 220,
        "y": 140,
        "width": 100,
        "height": 30,
        "text": 'Marketplace',
        "font": text_font,
        "border_radius": 5,
    }

    # BUTTON: Go to arena
    bt_arena = {
        "color": default_color,
        "x": 300,
        "y": 200,
        "width": 80,
        "height": 30,
        "text": 'Arena',
        "font": text_font,
        "border_radius": 5,
    }

    # BUTTON: Go to weaponShop
    bt_weaponShop = {
        "color": default_color,
        "x": 150,
        "y": 250,
        "width": 110,
        "height": 30,
        "text": 'Weapon Shop',
        "font": text_font,
        "border_radius": 5,
    }

    # BUTTON: Go to magicShop
    bt_magicShop = {
        "color": default_color,
        "x": 400,
        "y": 350,
        "width": 100,
        "height": 30,
        "text": 'Magic Shop',
        "font": text_font,
        "border_radius": 5,
    }

    # BUTTON: Go to armorShop
    bt_armorShop = {
        "color": default_color,
        "x": 500,
        "y": 450,
        "width": 100,
        "height": 30,
        "text": 'Armor Shop',
        "font": text_font,
        "border_radius": 5,
    }

    # BUTTON: Go to tavern
    bt_tavern = {
        "color": default_color,
        "x": 600,
        "y": 200,
        "width": 80,
        "height": 30,
        "text": 'Tavern',
        "font": text_font,
        "border_radius": 5,
    }
