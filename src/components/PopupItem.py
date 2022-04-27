from .Label import Label

from src.globals.const_values import *


class PopupItem:
    def __init__(self, x, y, width, height, screen, name, font, isVisible=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.name = name
        self.font = font
        self.isVisible = isVisible
        self.rect = pygame.Rect(x, y, width, height)
        self.label_name = Label(name, font, pygame.Color('#333333'),
                                screen, x + 10, y + 10)

    def draw(self):
        if self.isVisible:
            pygame.draw.rect(self.screen, pygame.Color('#ffffff'),
                             self.rect)
            self.label_name.draw()
