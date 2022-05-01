import pygame

pygame.init()

from src.components.ColorSchemes import ColorSchemes

# WINDOW SIZE
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SIZE_FACTOR = 0.6

# FONTS
# TITLE_FONT = pygame.font.SysFont('calibri', 100)
FONT = None
TITLE_FONT = pygame.font.Font(FONT, 100)
HEADER_PRIMARY_FONT = pygame.font.Font(FONT, 55)
HEADER_SECONDARY_FONT = pygame.font.Font(FONT, 40)
HEADER_TERTIARY_FONT = pygame.font.Font(FONT, 30)
TEXT_FONT = pygame.font.Font(FONT, 23)
INPUT_FONT = pygame.font.Font(FONT, 30)
LIST_TITLE_FONT = pygame.font.Font(FONT, 32)
LIST_SUBTITLE_FONT = pygame.font.Font(FONT, 25)

# ACCOUNT PROPERTIES
NICKNAME_LENGTH = 38
PASSWORD_LENGTH = 38

# IMAGES SIZES
AVATAR_FULL_WIDTH = 357
AVATAR_FULL_HEIGHT = 500
AVATAR_RECT_SIZE = 480

# MAP IMAGE SIZE
MAP_SIZE_FACTOR = 0.6
MAP_WIDTH = 2048
MAP_HEIGHT = 1536

# BUTTON: Return
BT_RETURN_SIZE = 40
BT_RETURN_PADDING = 10
BT_RETURN = {
    "color": ColorSchemes('white', 'white'),
    "x": round(SCREEN_WIDTH * SIZE_FACTOR) - BT_RETURN_PADDING - BT_RETURN_SIZE,
    "y": BT_RETURN_PADDING,
    "width": BT_RETURN_SIZE,
    "height": BT_RETURN_SIZE,
    "path": '../images/icons/return.png',
}

EQ_PLACEHOLDERS = {
    "headgear": '../images/icons/headgear_placeholder.png',
    "breastplate": '../images/icons/breastplate_placeholder.png',
    "gloves": '../images/icons/gloves_placeholder.png',
    "boots": '../images/icons/boots_placeholder.png',
    "belt": '../images/icons/belt_placeholder.png',
    "necklace": '../images/icons/necklace_placeholder.png',
    "ring": '../images/icons/ring_placeholder.png',
    "lucky_item": '../images/icons/lucky_item_placeholder.png',
    "primary_weapon": '../images/icons/primary_weapon_placeholder.png',
    "secondary_weapon": '../images/icons/secondary_weapon_placeholder.png',
}

AVATARS = {
    'warrior': [
        {
            "full": '../images/characters/warrior_1.jpg',
            "rect": '../images/characters/warrior_1_rect.jpg',
        },
        {
            "full": '../images/characters/warrior_2.jpg',
            "rect": '../images/characters/warrior_2_rect.jpg',
        },
        {
            "full": '../images/characters/warrior_3.jpg',
            "rect": '../images/characters/warrior_3_rect.jpg',
        },
    ],
    'mage': [
        {
            "full": '../images/characters/mage_1.jpg',
            "rect": '../images/characters/mage_1_rect.jpg',
        },
        {
            "full": '../images/characters/mage_2.jpg',
            "rect": '../images/characters/mage_2_rect.jpg',
        },
        {
            "full": '../images/characters/mage_3.jpg',
            "rect": '../images/characters/mage_3_rect.jpg',
        },
    ],
    'archer': [
        {
            "full": '../images/characters/archer_1.jpg',
            "rect": '../images/characters/archer_1_rect.jpg',
        },
        {
            "full": '../images/characters/archer_2.jpg',
            "rect": '../images/characters/archer_2_rect.jpg',
        },
        {
            "full": '../images/characters/archer_3.jpg',
            "rect": '../images/characters/archer_3_rect.jpg',
        },
    ]
}

CREATE_NEW_CHARACTER = {
    'name': 'Create',
    'spec': '',
    'level': 0,
    'img': '../images/characters/create_new.png',
}

INVENTORY_SHIFT = 11

def getFullAvatarPath(className, number):
    return '../images/characters/' + className + '_' + number + '.jpg'


def getRectAvatarPath(className, number):
    return '../images/characters/' + className + '_' + number + '_rect.jpg'

