import pygame

from api.game_classes.properties.enums import Quality

pygame.init()

from src.components.ItemGrid import ItemGrid
from src.components.ColorSchemes import ColorSchemes

from api.game_classes.objects.items.item import ItemType

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
SMALL_FONT = pygame.font.Font(FONT, 16)

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

CLASS_ICONS = {
    "warrior": {
        "gray": '../images/class_icons/warrior_gray.png',
        "white": '../images/class_icons/warrior_white.png',
    },
    "mage": {
        "gray": '../images/class_icons/mage_gray.png',
        "white": '../images/class_icons/mage_white.png',
    },
    "archer": {
        "gray": '../images/class_icons/archer_gray.png',
        "white": '../images/class_icons/archer_white.png',
    },
}

EQ_PLACEHOLDERS = {
    "headgear": '../images/icons/headgear_placeholder.png',
    "breastplate": '../images/icons/breastplate_placeholder.png',
    "gloves": '../images/icons/gloves_placeholder.png',
    "boots": '../images/icons/boots_placeholder.png',
    "belt": '../images/icons/belt_placeholder.png',
    "necklace": '../images/icons/necklace_placeholder.png',
    "ring": '../images/icons/ring_placeholder.png',
    "luckyitem": '../images/icons/luckyitem_placeholder.png',
    "potionperiod": '../images/icons/potionperiod_placeholder.png',
    "potionpermanent": '../images/icons/potionpermanent_placeholder.png',
    "primary_weapon": '../images/icons/primary_weapon_placeholder.png',
    "secondary_weapon": '../images/icons/secondary_weapon_placeholder.png',
}

CATEGORY_ICONS = {
    "armor": {
        "headgear": {
            "path_white": '../images/item_type_icons/armor/headgear_white.png',
            "path_gray": '../images/item_type_icons/armor/headgear_gray.png',
        },
        "breastplate": {
            "path_white": '../images/item_type_icons/armor/breastplate_white.png',
            "path_gray": '../images/item_type_icons/armor/breastplate_gray.png',
        },
        "gloves": {
            "path_white": '../images/item_type_icons/armor/gloves_white.png',
            "path_gray": '../images/item_type_icons/armor/gloves_gray.png',
        },
        "boots": {
            "path_white": '../images/item_type_icons/armor/boots_white.png',
            "path_gray": '../images/item_type_icons/armor/boots_gray.png',
        },
        "belt": {
            "path_white": '../images/item_type_icons/armor/belt_white.png',
            "path_gray": '../images/item_type_icons/armor/belt_gray.png',
        }
    },
    "magic": {
        "luckyitem": {
            "path_white": '../images/item_type_icons/magic/luckyitem_white.png',
            "path_gray": '../images/item_type_icons/magic/luckyitem_gray.png',
        },
        "necklace": {
            "path_white": '../images/item_type_icons/magic/necklace_white.png',
            "path_gray": '../images/item_type_icons/magic/necklace_gray.png',
        },
        "ring": {
            "path_white": '../images/item_type_icons/magic/ring_white.png',
            "path_gray": '../images/item_type_icons/magic/ring_gray.png',
        },
        "potionperiod": {
            "path_white": '../images/item_type_icons/magic/potionperiod_white.png',
            "path_gray": '../images/item_type_icons/magic/potionperiod_gray.png',
        },
        "potionpermanent": {
            "path_white": '../images/item_type_icons/magic/potionpermanent_white.png',
            "path_gray": '../images/item_type_icons/magic/potionpermanent_gray.png',
        }
    },
    "weapon": {
        "primaryweapon": {
            "path_white": '../images/item_type_icons/weapon/primaryweapon_white.png',
            "path_gray": '../images/item_type_icons/weapon/primaryweapon_gray.png',
        },
        "secondaryweapon": {
            "path_white": '../images/item_type_icons/weapon/secondaryweapon_white.png',
            "path_gray": '../images/item_type_icons/weapon/secondaryweapon_gray.png',
        }
    }
}

BACKPACK_ICONS = {
    "path_white": '../images/item_type_icons/backpack/backpack_white.png',
    "path_gray": '../images/item_type_icons/backpack/backpack_gray.png',
}

AVATARS = {
    'warrior': [
        {
            "full": '../images/characters/warrior_1.jpg',
            "rect": '../images/characters/warrior_1_rect.jpg'
        },
        {
            "full": '../images/characters/warrior_2.jpg',
            "rect": '../images/characters/warrior_2_rect.jpg'
        },
        {
            "full": '../images/characters/warrior_3.jpg',
            "rect": '../images/characters/warrior_3_rect.jpg'
        },
    ],
    'mage': [
        {
            "full": '../images/characters/mage_1.jpg',
            "rect": '../images/characters/mage_1_rect.jpg'
        },
        {
            "full": '../images/characters/mage_2.jpg',
            "rect": '../images/characters/mage_2_rect.jpg'
        },
        {
            "full": '../images/characters/mage_3.jpg',
            "rect": '../images/characters/mage_3_rect.jpg'
        },
    ],
    'archer': [
        {
            "full": '../images/characters/archer_1.jpg',
            "rect": '../images/characters/archer_1_rect.jpg',
        },
        {
            "full": '../images/characters/archer_2.jpg',
            "rect": '../images/characters/archer_2_rect.jpg'
        },
        {
            "full": '../images/characters/archer_3.jpg',
            "rect": '../images/characters/archer_3_rect.jpg'
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

STATS_NAMES = [
    'strength', "intelligence", "dexterity", "constitution", "luck",
    "protection", "persuasion", "trade", "leadership", "initiative"
]

def setActiveItem(index, active_item):
    if active_item['from'] == -1:
        active_item['from'] = index
        return False

    if active_item['to'] == -1:
        active_item['to'] = index
        return True

    return None

def resetActiveItem():
    return {
        "from": -1,
        "to": -1
    }
def getFightClassName(name):
    if name == 'w':
        return 'Warrior'
    if name == 'a':
        return 'Archer'
    if name == 'm':
        return 'Mage'
    return None

def getQuality(item_quality):
    return str(item_quality)[8:].lower()

def getDifficulty(quest_difficulty):
    return str(quest_difficulty)[11:].lower()

def reloadBackpackButtons(buttons_list, current_active, meas):
    newButtons = []

    for i in range(len(buttons_list)):
        if i == current_active:
            buttons_list[i].colorSchemes = meas.bt_class_active['color']
            buttons_list[i].color = meas.bt_class_active['color'].inactive
            buttons_list[i].path = meas.buttons_backpack['path_white']
            buttons_list[i].image = buttons_list[i].makeImage(meas.buttons_backpack['path_white'],
                                                              meas.bt_class_active['image_offset'])
            buttons_list[i].border_radius = meas.bt_class_active['border_radius']
        else:
            buttons_list[i].colorSchemes = meas.bt_class_inactive['color']
            buttons_list[i].color = meas.bt_class_inactive['color'].inactive
            buttons_list[i].path = meas.buttons_backpack['path_gray']
            buttons_list[i].image = buttons_list[i].makeImage(meas.buttons_backpack['path_gray'],
                                                              meas.bt_class_inactive['image_offset'])
            buttons_list[i].border_radius = meas.bt_class_inactive['border_radius']

        newButtons.append(buttons_list[i])

    return newButtons

def extractType(name):
    if name == 'ib_luckyitem':
        return 'LuckyItem'

    if name == 'ib_primaryweapon':
        return 'PrimaryWeapon'

    if name == 'ib_secondaryweapon':
        return 'SecondaryWeapon'

    print(''.join(' '.join(name[3:].split('_')).title().split()))
    return ''.join(' '.join(name[3:].split('_')).title().split())

def reloadItemGrid(character, backpack_active, meas, active_item, screen):
    return ItemGrid(meas.ig_backpack['x'], meas.ig_backpack['y'],
                    meas.ig_backpack['item_size'], meas.ig_backpack['item_padding'],
                    meas.ig_backpack['cols'], meas.ig_backpack['amount'], screen,
                    character['backpacks'][backpack_active], active=active_item['from'] - INVENTORY_SHIFT)

def reloadCharacterBackpacks(character, hero):
    character['backpacks'] = [
        [getEqItem(hero.eq.itemSlots[i]) for i in range(INVENTORY_SHIFT, len(hero.eq.itemSlots))]
    ]

def reloadCharacterEQ(character, hero):
    character['eq'] = {
        "headgear": getEqItemByType(hero.eq.itemSlots, ItemType.Headgear.value),
        "breastplate": getEqItemByType(hero.eq.itemSlots, ItemType.Breastplate.value),
        "gloves": getEqItemByType(hero.eq.itemSlots, ItemType.Gloves.value),
        "boots": getEqItemByType(hero.eq.itemSlots, ItemType.Boots.value),
        "necklace": getEqItemByType(hero.eq.itemSlots, ItemType.Necklace.value),
        "belt": getEqItemByType(hero.eq.itemSlots, ItemType.Belt.value),
        "ring": getEqItemByType(hero.eq.itemSlots, ItemType.Ring.value),
        "luckyitem": getEqItemByType(hero.eq.itemSlots, ItemType.LuckyItem.value),
        "primaryweapon": getEqItemByType(hero.eq.itemSlots, ItemType.PrimaryWeapon.value),
        "secondaryweapon": getEqItemByType(hero.eq.itemSlots, ItemType.SecondaryWeapon.value),
    }

def getItemCategory(item_type):
    armors = ['belt', 'boots', 'breastplate', 'gloves', 'headgear']
    magic = ['luckyitem', 'necklace', 'ring', 'potionperiod', 'potionpermanent']

    if item_type in armors:
        return "armor"

    if item_type in magic:
        return "magic"
    print("exit")
    return "weapon"

def getEqItem(item):
    item_type = str(type(item).__name__).lower()

    if item:
        result = {
            "name": item.name,
            "img_path": '../images/items/' + getItemCategory(item_type) + '/' + item_type + '.png',
            "type": getQuality(item.quality),
            "id": 0,
        }
    else:
        result = {
            "name": "empty",
            "img_path": "../images/icons/add_item.png",
            "type": "empty",
            "id": 0,
        }

    return result

def getEqItemByType(items, expected_type):
    item_type = str(type(items[expected_type]).__name__).lower()

    if items[expected_type]:
        result = {
            "name": items[expected_type].name,
            "img_path": '../images/items/' + getItemCategory(item_type) + '/' + item_type + '.png',
            "type": getQuality(items[expected_type].quality),
            "statistics": items[expected_type].statistics
        }
    else:
        result = {
            "name": "empty",
            "img_path": "../images/icons/add_item.png",
            "type": "empty",
            "statistics": "empty"
        }

    return result

def getCharacterForEQPreview(hero):
    return {
        'name': str(hero.name),
        'spec': str(hero.fight_class),
        'level': str(hero.lvl),
        'img_full': '../images/characters/' + str(hero.fight_class).lower() + '_' + str(
            hero.avatar_id) + '.jpg',
        "health": str(hero.get_statistics().hp),
        "gold": str(hero.eq.gold),
        "exp": hero.exp,
        "expToNextLvl": hero.expToNextLvl,
        "eq": {
            "headgear": getEqItemByType(hero.eq.itemSlots, ItemType.Headgear.value),
            "breastplate": getEqItemByType(hero.eq.itemSlots, ItemType.Breastplate.value),
            "gloves": getEqItemByType(hero.eq.itemSlots, ItemType.Gloves.value),
            "boots": getEqItemByType(hero.eq.itemSlots, ItemType.Boots.value),
            "necklace": getEqItemByType(hero.eq.itemSlots, ItemType.Necklace.value),
            "belt": getEqItemByType(hero.eq.itemSlots, ItemType.Belt.value),
            "ring": getEqItemByType(hero.eq.itemSlots, ItemType.Ring.value),
            "luckyitem": getEqItemByType(hero.eq.itemSlots, ItemType.LuckyItem.value),
            "primaryweapon": getEqItemByType(hero.eq.itemSlots, ItemType.PrimaryWeapon.value),
            "secondaryweapon": getEqItemByType(hero.eq.itemSlots, ItemType.SecondaryWeapon.value),
        },
        "backpacks": [
            [getEqItem(hero.eq.itemSlots[i]) for i in range(INVENTORY_SHIFT, len(hero.eq.itemSlots))]
        ],
        "statistics": {
            "strength": hero.get_statistics().strength,
            "intelligence": hero.get_statistics().intelligence,
            "dexterity": hero.get_statistics().dexterity,
            "constitution": hero.get_statistics().constitution,
            "luck": hero.get_statistics().luck,
            "protection": hero.get_statistics().protection,
            "persuasion": hero.get_statistics().persuasion,
            "trade": hero.get_statistics().trade,
            "leadership": hero.get_statistics().leadership,
            "initiative": hero.get_statistics().initiative,
        }
    }

def getFullAvatarPath(className, number):
    return '../images/characters/' + className + '_' + str(number) + '.jpg'

def getRectAvatarPath(className, number):
    return '../images/characters/' + className + '_' + str(number) + '_rect.jpg'

def getFullEnemyPath(className, number):
    return '../images/enemies/' + className + '_' + str(number) + '.jpg'

def getRectEnemyPath(className, number):
    return '../images/enemies/' + className + '_' + str(number) + '_rect.jpg'

def setColor(colors, subtitle):
    if subtitle == 'easy':
        return colors.easy
    if subtitle == 'intermediate':
        return colors.intermediate
    if subtitle == 'hard':
        return colors.hard
    return colors.white

def getQualityValue(color):
    fill_colors = ColorSchemes()

    if color == fill_colors.legendary:
        return Quality.LEGENDARY.value

    if color == fill_colors.epic:
        return Quality.EPIC.value

    if color == fill_colors.common:
        return Quality.COMMON.value

    return None