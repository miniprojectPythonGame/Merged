import pygame

from .Button import Button
from .Label import Label
from .ColorSchemes import ColorSchemes

from src.globals.const_values import LIST_TITLE_FONT, LIST_SUBTITLE_FONT


class ListElement():
    def __init__(self, x, y, width, height, colors, screen,
                 title='', subtitle='', property_name='', property_value='', img_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colors = colors
        self.screen = screen
        self.title = title
        self.subtitle = subtitle
        self.property_name = property_name
        self.property_value = property_value
        self.img_path = img_path
        self.rect = pygame.Rect(x, y, width, height)
        self.title_label = Label(title, LIST_TITLE_FONT, colors.white,
                                 screen, x + 10, y + 10, "topleft")
        self.subtitle_label = Label(subtitle.capitalize(), LIST_SUBTITLE_FONT, self.setColor(colors, subtitle),
                                    screen, x + 10, y + height - 30, "topleft")
        self.property_name_label = Label(property_name, LIST_SUBTITLE_FONT, colors.white,
                                         screen, x + 400, y + 14, "topleft")
        self.property_value_label = Label(str(property_value), LIST_SUBTITLE_FONT, colors.gray_light,
                                          screen, x + 400, y + height - 30, "topleft")
        self.button = Button(ColorSchemes(inactive='#222222'), x + width - 120, y + 10, 110, height - 20,
                             screen, 'Open', LIST_TITLE_FONT,
                             border_radius=10)

    def draw(self):
        pygame.draw.rect(self.screen, self.colors.secondary, self.rect)
        self.title_label.draw()
        self.subtitle_label.draw()
        self.property_name_label.draw()
        self.property_value_label.draw()
        self.button.draw()

    def setColor(self, colors, subtitle):
        if subtitle == 'easy':
            return colors.easy
        if subtitle == 'intermediate':
            return colors.intermediate
        if subtitle == 'hard':
            return colors.hard

        return colors.white
