from src.globals.const_values import *
from src.globals.mock_data import *
from src.components.ColorSchemes import ColorSchemes


class Measurements:
    # WINDOW PARAMETERS
    size_factor = SIZE_FACTOR
    window_width = SCREEN_WIDTH * size_factor
    window_height = SCREEN_HEIGHT * size_factor
    margin = round(SCREEN_WIDTH * SIZE_FACTOR * 0.12 * 0.5)

    # ACCOUNT PROPERTIES
    nickname_length = NICKNAME_LENGTH
    password_length = PASSWORD_LENGTH

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

    # ARROW BUTTONS SIZE:
    abt_size = 60

    # CharacterPreview sizes:
    preview_size = 358
    property_bar_height = 35

    # Avatar thumbnails
    thumbnail_size = 90
    thumbnail_gap = round((round(window_width - (preview_size + 4 * margin)) - 5*thumbnail_size)/4)

    # CREATE BUTTON SIZE
    create_button_size = 60

    # LABEL: Page
    label_page = {
        'text': 'Create character',
        'x': window_width - margin,
        'y': 20,
        'anchor': 'topright',
        'font': header_primary_font,
        'color': text_color,
    }

    bt_return = BT_RETURN

    # RIGHT PANEL
    # IMAGE: Avatar preview
    cp_createdCharacter = {
        'x': window_width - margin - preview_size,
        'y': margin,
        'width': preview_size,
        'height': preview_size,
    }

    # LABEL: Currently typed name
    label_curr_name = {
        'text': 'Name',
        'x': cp_createdCharacter['x'],
        'y': cp_createdCharacter['height'] + cp_createdCharacter['y'] - 2 * property_bar_height,
        'anchor': 'topleft',
        'font': header_secondary_font,
        'color': text_color,
    }

    # LABEL: Currently picked class
    label_curr_class = {
        'text': '',
        'x': cp_createdCharacter['x'],
        'y': cp_createdCharacter['height'] + cp_createdCharacter['y'] - property_bar_height,
        'anchor': 'topleft',
        'font': header_secondary_font,
        'color': text_color,
    }

    # LEFT PANEL
    # LABEL: Character name
    label_name = {
        'text': 'Character name',
        'x': margin,
        'y': margin,
        'anchor': 'topleft',
        'font': header_secondary_font,
        'color': text_color,
    }

    # INPUT: Nickname
    input_name = {
        "padding": 5,
        "border": 2,
        "color": ColorSchemes(),
        "x": margin,
        "y": margin + label_padding,
        "width": round(window_width - (preview_size + 4 * margin)),
        "height": 50,
        "placeholder": 'Name',
    }

    # LABEL: Class
    label_class = {
        'text': 'Class',
        'x': margin,
        'y': margin + 150,
        'anchor': 'topleft',
        'font': header_secondary_font,
        'color': text_color,
    }

    # BUTTON (type): class active
    bt_class_active = {
        "color": ColorSchemes(inactive=pygame.Color('#333333')),
        "border_radius": 5,
        "image_offset": 5,
    }

    # BUTTON (type): class active
    bt_class_inactive = {
        "color": ColorSchemes(inactive=pygame.Color('white')),
        "border_radius": 5,
        "image_offset": 5,
    }

    # BUTTON: warrior
    bt_warrior = {
        "x": margin,
        "y": label_class['y'] + label_padding,
        "width": class_button_size,
        "height": class_button_size,
        "text": '',
        "path_white": '../images/class_icons/warrior_white.png',
        "path_gray": '../images/class_icons/warrior_gray.png',
    }

    # BUTTON: mage
    bt_mage = {
        "x": margin + label_padding + class_button_size,
        "y": label_class['y'] + label_padding,
        "width": class_button_size,
        "height": class_button_size,
        "text": '',
        "path_white": '../images/class_icons/mage_white.png',
        "path_gray": '../images/class_icons/mage_gray.png',
    }

    # BUTTON: archer
    bt_archer = {
        "x": margin + 2 * label_padding + 2 * class_button_size,
        "y": label_class['y'] + label_padding,
        "width": class_button_size,
        "height": class_button_size,
        "text": '',
        "path_white": '../images/class_icons/archer_white.png',
        "path_gray": '../images/class_icons/archer_gray.png',
    }

    # LABEL: Avatar
    label_avatar = {
        'text': 'Avatar',
        'x': margin,
        'y': margin + 300,
        'anchor': 'topleft',
        'font': header_secondary_font,
        'color': text_color,
    }


    # IMAGE: Avatar preview
    images = [
        {
            'x': margin,
            'y': label_avatar['y'] + label_padding,
            'width': thumbnail_size,
            'height': thumbnail_size,
        },
        {
            'x': margin + thumbnail_size + thumbnail_gap,
            'y': label_avatar['y'] + label_padding,
            'width': thumbnail_size,
            'height': thumbnail_size,
        },
        {
            'x': margin + 2*thumbnail_size + 2*thumbnail_gap,
            'y': label_avatar['y'] + label_padding,
            'width': thumbnail_size,
            'height': thumbnail_size,
        }
    ]

    # BUTTON: Create
    bt_create = {
        "color": ColorSchemes(),
        "x": cp_createdCharacter['x'],
        "y": window_height - margin - create_button_size,
        "width": cp_createdCharacter['width'],
        "height": create_button_size,
        "text": 'Create'
    }