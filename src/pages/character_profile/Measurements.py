from src.globals.const_values import *
from src.components.ColorSchemes import ColorSchemes

# from src.globals.mock_data import character_2


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
    class_button_size = 60
    bar_colorScheme = ColorSchemes()

    bt_return = BT_RETURN

    ig_item_size = 70
    ig_item_padding = 10
    ig_cols = 4
    ig_amount = 20
    ig_rows = round(ig_amount / ig_cols)
    ig_button_height = 30

    # LABEL: Page
    label_page = {
        'text': 'Character profile',
        'x': window_width - margin,
        'y': 20,
        'anchor': 'topright',
        'font': header_primary_font,
        'color': text_color,
    }

    # CHARACTER_EQUIPMENT: -//-
    ce_characterEqPreview = {
        "x": margin,
        "y": margin - 30,
        "font": header_tertiary_font,
        "colors": bar_colorScheme,
    }

    sc_eq_stat = {
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
        "y": margin + sc_eq_stat['switch_height'] + 10,
        "item_size": 70,
        "item_padding": 10,
        "cols": 4,
        "amount": 24,
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

    labels_stats = [
        'strength', "intelligence", "dexterity", "constitution", "luck",
        "protection", "persuasion", "trade", "leadership", "initiative"
    ]

    label_stat_header = {
        "font": header_tertiary_font,
        "color": text_color,
        "x": window_width - (ig_item_size * (ig_cols + 1) + ig_item_padding * ig_cols) - margin,
        "y": round(margin * 1.5),
        "height": 25,
        "padding": 15,
        "anchor": "topleft",
    }

    label_stat_values = {
        "font": header_tertiary_font,
        "color": stat_color,
        "x": window_width - margin,
        "y": round(margin * 1.5),
        "height": 25,
        "padding": 15,
        "anchor": "topright",
    }