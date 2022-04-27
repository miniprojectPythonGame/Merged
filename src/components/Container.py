import pygame

from src.components.Button import Button
from src.components.ColorSchemes import ColorSchemes

from src.globals.const_values import FONT

class Container:
    def __init__(self, x, y, width, height, components):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.components = components

    def draw(self):
        for component in self.components:
            component.draw()