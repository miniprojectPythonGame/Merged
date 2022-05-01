import pygame

from .ItemBox import ItemBox
from .ColorSchemes import ColorSchemes


class ItemGrid:
    def __init__(self, x, y, item_size, item_padding, cols, amount, screen, backpack_ref, active=-1):
        self.x = x
        self.y = y
        self.item_size = item_size
        self.item_padding = item_padding
        self.cols = cols
        self.amount = amount
        self.screen = screen
        self.active = active
        self.backpack_ref = backpack_ref
        self.backpack = self.initateBackpack()

    def draw(self):
        for item in self.backpack:
            item.draw()

    def initateBackpack(self):
        backpack = []
        x = self.x
        y = self.y
        ib_offset_placeholder = 20
        ib_offset_item = 10
        fill_colors = ColorSchemes()

        for i in range(len(self.backpack_ref)):
            if self.backpack_ref[i]['type'] == 'legendary':
                isActive = i == self.active
                backpack.append(
                    ItemBox(x, y, self.item_size, self.item_size, self.screen,
                            path=self.backpack_ref[i]['img_path'], offset=ib_offset_item,
                            fill=fill_colors.legendary, border_radius=5, isActive=isActive)
                )

            if self.backpack_ref[i]['type'] == 'epic':
                isActive = i == self.active
                backpack.append(
                    ItemBox(x, y, self.item_size, self.item_size, self.screen,
                            path=self.backpack_ref[i]['img_path'], offset=ib_offset_item,
                            fill=fill_colors.epic, border_radius=5, isActive=isActive)
                )

            if self.backpack_ref[i]['type'] == 'common':
                isActive = i == self.active
                backpack.append(
                    ItemBox(x, y, self.item_size, self.item_size, self.screen,
                            path=self.backpack_ref[i]['img_path'], offset=ib_offset_item,
                            fill=fill_colors.common, border_radius=5, isActive=isActive)
                )

            if self.backpack_ref[i]['type'] == 'empty':
                isActive = i == self.active
                backpack.append(
                    ItemBox(x, y, self.item_size, self.item_size, self.screen,
                            path=self.backpack_ref[i]['img_path'], offset=ib_offset_item,
                            fill=fill_colors.white, border_radius=5, isActive=isActive)
                )

            if i % self.cols == self.cols - 1:
                y += self.item_size + self.item_padding
                x = self.x
            else:
                x += self.item_size + self.item_padding

        return backpack
