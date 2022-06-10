from src.globals.const_values import *
from src.components.ColorSchemes import ColorSchemes

from src.globals.const_values import CATEGORY_ICONS

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
    category_button_size = 60
    category_button_padding = 20
    default_color = ColorSchemes()
    magic_shop_category_offset = round(2.3*category_button_padding) + category_button_size

    bt_return = BT_RETURN

    ig_item_size = 80
    ig_item_padding = 10
    ig_cols = 4
    ig_amount = 20
    ig_rows = round(ig_amount / ig_cols)
    ig_button_height = 30

    # LABEL: Page
    label_page = {
        'text': 'Magic shop',
        'x': margin,
        'y': 20,
        'anchor': 'topleft',
        'font': header_primary_font,
        'color': text_color,
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
    bt_showPotionPeriod = {
        "x": margin,
        "y": margin,
        "width": category_button_size,
        "height": category_button_size,
        "path_white": CATEGORY_ICONS['magic']['potionperiod']['path_white'],
        "path_gray": CATEGORY_ICONS['magic']['potionperiod']['path_gray'],
    }

    # BUTTON: Show rings in offer
    bt_showRings = {
        "x": margin + category_button_padding + category_button_size,
        "y": margin,
        "width": category_button_size,
        "height": category_button_size,
        "path_white": CATEGORY_ICONS['magic']['ring']['path_white'],
        "path_gray": CATEGORY_ICONS['magic']['ring']['path_gray'],
    }

    # BUTTON: Show necklaces in offer
    bt_showNecklaces = {
        "x": margin + 2*category_button_padding + 2*category_button_size,
        "y": margin,
        "width": category_button_size,
        "height": category_button_size,
        "path_white": CATEGORY_ICONS['magic']['necklace']['path_white'],
        "path_gray": CATEGORY_ICONS['magic']['necklace']['path_gray'],
    }

    # BUTTON: Show necklaces in offer
    bt_showPotionPermanent = {
        "x": margin + 3*category_button_padding + 3*category_button_size,
        "y": margin,
        "width": category_button_size,
        "height": category_button_size,
        "path_white": CATEGORY_ICONS['magic']['potionpermanent']['path_white'],
        "path_gray": CATEGORY_ICONS['magic']['potionpermanent']['path_gray'],
    }

    # BUTTON: Show necklaces in offer
    bt_showLuckyItem = {
        "x": margin + 4 * category_button_padding + 4 * category_button_size,
        "y": margin,
        "width": category_button_size,
        "height": category_button_size,
        "path_white": CATEGORY_ICONS['magic']['luckyitem']['path_white'],
        "path_gray": CATEGORY_ICONS['magic']['luckyitem']['path_gray'],
    }

    # BUTTON: Show necklaces in offer
    bt_showLuckyItems = {
        "x": bt_showNecklaces['x'] + magic_shop_category_offset,
        "y": margin,
        "width": category_button_size,
        "height": category_button_size,
        "path_white": CATEGORY_ICONS['magic']['luckyitem']['path_white'],
        "path_gray": CATEGORY_ICONS['magic']['luckyitem']['path_gray'],
    }

    # BUTTON: Show necklaces in offer
    bt_showPotionPermanent = {
        "x": bt_showLuckyItems['x'] + magic_shop_category_offset,
        "y": margin,
        "width": category_button_size,
        "height": category_button_size,
        "path_white": CATEGORY_ICONS['magic']['potionpermanent']['path_white'],
        "path_gray": CATEGORY_ICONS['magic']['potionpermanent']['path_gray'],
    }

    # SWITCH_CARDS: eq <-> statistics <-> backpack
    sc_eq_stat_bp = {
        "x": window_width - (ig_item_size * (ig_cols + 1) + ig_item_padding * ig_cols) - margin,
        "y": margin,
        "width": ig_item_size * (ig_cols + 1) + ig_item_padding * ig_cols,
        "height": ig_button_height + 10 + ig_item_size * ig_rows + ig_item_padding * (ig_rows - 1),
        "font": text_font,
        "color": ColorSchemes(),
        "switch_height": ig_button_height,
    }

    c_backpack = {
        "x": window_width - (ig_item_size * (ig_cols + 1) + ig_item_padding * ig_cols) - margin,
        "y": margin,
        "width": ig_item_size * (ig_cols + 1) + ig_item_padding * ig_cols,
        "height": ig_button_height + 10 + ig_item_size * ig_rows + ig_item_padding * (ig_rows - 1),
    }

    # ITEM_GRID: backpack
    ig_backpack = {
        "x": window_width - (ig_item_size * ig_cols + ig_item_padding * (ig_cols - 1)) - margin,
        "y": margin + sc_eq_stat_bp['switch_height'] + 10,
        "item_size": ig_item_size,
        "item_padding": ig_item_padding,
        "cols": ig_cols,
        "amount": ig_amount,
    }

    # BUTTON: backpack
    buttons_backpack = {
        "x": window_width - (ig_item_size * (ig_cols + 1) + ig_item_padding * ig_cols) - margin,
        "y": ig_backpack['y'],
        "width": ig_item_size,
        "height": ig_item_size,
        "padding": ig_item_padding,
        "path_white": BACKPACK_ICONS["path_white"],
        "path_gray": BACKPACK_ICONS["path_gray"],
    }

    c_stats = {
        "x": window_width - (ig_item_size * (ig_cols + 1) + ig_item_padding * ig_cols) - margin,
        "y": margin,
        "width": ig_item_size * (ig_cols + 1) + ig_item_padding * ig_cols,
        "height": ig_button_height + 10 + ig_item_size * ig_rows + ig_item_padding * (ig_rows - 1),
    }

    labels_stats = STATS_NAMES

    label_stat_header = {
        "font": header_tertiary_font,
        "color": text_color,
        "x": window_width - (ig_item_size * (ig_cols + 1) + ig_item_padding * ig_cols) - margin,
        "y": round(margin * 1.75),
        "height": 25,
        "padding": 15,
        "anchor": "topleft",
    }

    label_stat_values = {
        "font": header_tertiary_font,
        "color": stat_color,
        "x": window_width - margin,
        "y": round(margin * 1.75),
        "height": 25,
        "padding": 15,
        "anchor": "topright",
    }

    # CHARACTER_EQUIPMENT: -//-
    ce_characterEqPreview = {
        "x": window_width - (ig_item_size * (ig_cols + 1) + ig_item_padding * ig_cols) - margin,
        "y": round(margin * 1.5),
        "font": text_font,
        "colors": default_color,
    }

    # ITEM_GRID: shop offer
    ig_items = {
        "x": margin,
        "y": margin + category_button_padding + category_button_size,
        "item_size": 70,
        "item_padding": 9,
        "cols": 4,
        "amount": 20,
    }

    # LABEL: Gold
    label_gold = {
        'x': margin,
        'y': window_height - (margin - 10),
        'anchor': 'topleft',
        'font': header_tertiary_font,
        'color': text_color,
    }