import pygame

from src.components.Button import Button
from src.components.ColorSchemes import ColorSchemes

from src.globals.const_values import FONT

class SwitchCards:
    def __init__(self, x, y, width, height, font, color, screen, components, descriptions, switch_height=25):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = font
        self.color = color
        self.screen = screen
        self.components = components
        self.descriptions = descriptions
        self.switch_height = switch_height
        self.current = 0
        self.buttons = self.generateButtons(len(components))

    def draw(self):
        self.buttons = self.generateButtons(len(self.components))

        for button in self.buttons:
            button.draw()

        self.components[self.current].draw()

    def generateButtons(self, size):
        buttons = []
        width = round(self.width / size)

        for i in range(size):
            if i == self.current:
                buttons.append(Button(ColorSchemes(), self.x + (width * i), self.y,
                          width, self.switch_height, self.screen,
                          self.descriptions[i], pygame.font.Font(FONT, round(self.switch_height * 0.75))))
            else:
                buttons.append(Button(ColorSchemes(), self.x + (width * i), self.y,
                          width, self.switch_height, self.screen,
                          self.descriptions[i], pygame.font.Font(FONT, round(self.switch_height * 0.75)), border=1))

        return buttons