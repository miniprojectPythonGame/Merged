from .ImageField import ImageField
from .Label import Label
from .PropertyBar import PropertyBar
from .ItemBox import ItemBox

from src.globals.const_values import *


class CharacterEquipment:
    def __init__(self, x, y, font, color, character_ref, screen):
        self.x = x
        self.y = y
        self.font = font
        self.color = color
        self.character_ref = character_ref
        self.screen = screen
        self.character = self.initateEquipment()

    def draw(self):
        for key in self.character:
            self.character[key].draw()

    def getColor(self, object):
        fill_colors = ColorSchemes()

        if object is None:
            return None

        if object['type'] == 'legendary':
            return fill_colors.legendary

        if object['type'] == "epic":
            return fill_colors.epic

        if object['type'] == "common":
            return fill_colors.common

    def initateEquipment(self):
        # CONST SIZE RELATIONS
        itembox_size = 110
        itembox_padding = 20
        itembox_offset = 20
        itembox_border_radius = 5
        property_bar_height = 30
        avatar_size_factor = 0.7

        avatar_width = round(AVATAR_FULL_WIDTH * avatar_size_factor)
        avatar_height = round(AVATAR_FULL_HEIGHT * avatar_size_factor)

        x = self.x
        y = self.y

        label_name = Label(self.character_ref['name'],
                           self.font, self.color.text_color, self.screen,
                           x + itembox_size + itembox_padding,
                           y)

        img_avatar = ImageField(x + itembox_size + itembox_padding,  # x
                                y + itembox_padding,  # y
                                avatar_width,
                                avatar_height,
                                self.character_ref['img_full'], self.screen)

        pb_level = PropertyBar(x + itembox_size + itembox_padding,  # x
                               y + itembox_padding + avatar_height,  # y
                               avatar_width, property_bar_height,
                               self.character_ref['exp'] / self.character_ref['expToNextLvl'],
                               "Level " + str(self.character_ref['level']),
                               self.font, self.color.primary, self.color.level, self.screen)

        pb_health = PropertyBar(x + itembox_size + itembox_padding,  # x
                                y + itembox_padding + avatar_height + property_bar_height,  # y
                                avatar_width, property_bar_height, 1,
                                str(self.character_ref['health']) + " HP",
                                self.font, self.color.primary, self.color.health, self.screen)

        ib_helmet = ItemBox(x,
                            y + itembox_padding,
                            itembox_size, itembox_size, self.screen,
                            path=EQ_PLACEHOLDERS['helmet'], offset=itembox_offset,
                            border_radius=itembox_border_radius)

        ib_chestplate = ItemBox(x,  # x
                                y + 2 * itembox_padding + itembox_size,  # y
                                itembox_size, itembox_size, self.screen,
                                path=EQ_PLACEHOLDERS['chestplate'], offset=itembox_offset,
                                border_radius=itembox_border_radius)

        ib_gloves = ItemBox(x,  # x
                            y + 3 * itembox_padding + 2 * itembox_size,  # y
                            itembox_size, itembox_size, self.screen,
                            path=EQ_PLACEHOLDERS['gloves'], offset=itembox_offset,
                            border_radius=itembox_border_radius)

        ib_boots = ItemBox(x,
                           y + 4 * itembox_padding + 3 * itembox_size,  # y,
                           itembox_size, itembox_size, self.screen,
                           path=EQ_PLACEHOLDERS['boots'], offset=itembox_offset,
                           border_radius=itembox_border_radius)

        ib_belt = ItemBox(x + 2 * itembox_padding + itembox_size + avatar_width,  # x,
                          y + itembox_padding,  # y
                          itembox_size, itembox_size, self.screen,
                          path=EQ_PLACEHOLDERS['belt'], offset=itembox_offset,
                          fill=self.getColor(self.character_ref['eq']['belt']),
                          border_radius=itembox_border_radius,
                          isActive=False)

        ib_necklace = ItemBox(x + 2 * itembox_padding + itembox_size + avatar_width,  # x,
                              y + 2 * itembox_padding + itembox_size,  # y
                              itembox_size, itembox_size, self.screen,
                              path=EQ_PLACEHOLDERS['necklace'], offset=itembox_offset,
                              border_radius=itembox_border_radius)

        ib_ring = ItemBox(x + 2 * itembox_padding + itembox_size + avatar_width,  # x,
                          y + 3 * itembox_padding + 2 * itembox_size,  # y
                          itembox_size, itembox_size, self.screen,
                          path=EQ_PLACEHOLDERS['ring'], offset=itembox_offset,
                          border_radius=itembox_border_radius)

        ib_artefact = ItemBox(x + 2 * itembox_padding + itembox_size + avatar_width,  # x,
                              y + 4 * itembox_padding + 3 * itembox_size,  # y,
                              itembox_size, itembox_size, self.screen,
                              path=EQ_PLACEHOLDERS['artefact'], offset=itembox_offset,
                              border_radius=itembox_border_radius)

        ib_sword = ItemBox(x + itembox_size + itembox_padding,  # x
                           y + avatar_height + 2 * itembox_padding + 2 * property_bar_height,  # y
                           itembox_size, itembox_size, self.screen,
                           path=EQ_PLACEHOLDERS['sword'], offset=itembox_offset,
                           border_radius=itembox_border_radius)

        ib_shield = ItemBox(x + itembox_padding + avatar_width,  # x
                            y + avatar_height + 2 * itembox_padding + 2 * property_bar_height,  # y
                            itembox_size, itembox_size, self.screen,
                            path=EQ_PLACEHOLDERS['shield'], offset=itembox_offset,
                            border_radius=itembox_border_radius)

        return {
            "label_name": label_name,
            "img_avatar": img_avatar,
            "pb_level": pb_level,
            "pb_health": pb_health,
            "ib_helmet": ib_helmet,
            "ib_chestplate": ib_chestplate,
            "ib_gloves": ib_gloves,
            "ib_boots": ib_boots,
            "ib_belt": ib_belt,
            "ib_necklace": ib_necklace,
            "ib_ring": ib_ring,
            "ib_artefact": ib_artefact,
            "ib_sword": ib_sword,
            "ib_shield": ib_shield,
        }
