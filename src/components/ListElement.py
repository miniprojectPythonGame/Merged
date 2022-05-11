import pygame

from .Button import Button
from .Label import Label
from .ColorSchemes import ColorSchemes
from .ImageField import ImageField

from src.globals.const_values import LIST_TITLE_FONT, LIST_SUBTITLE_FONT


class ListElement():
    def __init__(self, x, y, width, height, colors, screen,
                 title='', subtitle='', property_name='', property_value='', object=None, img_path=None):
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
        self.object = object
        self.img_path = img_path
        self.initialize()

    def initialize(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        if self.img_path is None:
            self.image = None
            self.title_label = Label(self.title, LIST_TITLE_FONT, self.colors.white,
                                     self.screen, self.x + 10, self.y + 10, "topleft")
            self.subtitle_label = Label(self.subtitle.capitalize(), LIST_SUBTITLE_FONT, self.setColor(self.colors, self.subtitle),
                                        self.screen, self.x + 10, self.y + self.height - 30, "topleft")
            self.property_name_label = Label(self.property_name, LIST_SUBTITLE_FONT, self.colors.white,
                                             self.screen, self.x + 400, self.y + 14, "topleft")
            self.property_value_label = Label(str(self.property_value), LIST_SUBTITLE_FONT, self.colors.gray_light,
                                              self.screen, self.x + 400, self.y + self.height - 30, "topleft")
            self.button = Button(ColorSchemes(inactive='#222222'), self.x + self.width - 120, self.y + 10, 110, self.height - 20,
                                 self.screen, 'Open', LIST_TITLE_FONT,
                                 border_radius=10)
        else:
            self.image = ImageField(self.x + 10, self.y + 10, self.height-20, self.height-20, self.img_path, self.screen)
            self.title_label = Label(self.title, LIST_TITLE_FONT, self.colors.white,
                                     self.screen, self.x + 10 + self.height, self.y + 10, "topleft")
            self.subtitle_label = Label(self.subtitle.capitalize(), LIST_SUBTITLE_FONT, self.setColor(self.colors, self.subtitle),
                                        self.screen, self.x + 10 + self.height, self.y + self.height - 30, "topleft")
            self.property_name_label = Label(self.property_name, LIST_SUBTITLE_FONT, self.colors.white,
                                             self.screen, self.x + 400 + self.height - 30, self.y + 14, "topleft")
            self.property_value_label = Label(str(self.property_value), LIST_SUBTITLE_FONT, self.colors.gray_light,
                                              self.screen, self.x + 400 + self.height - 30, self.y + self.height - 30, "topleft")
            self.button = Button(ColorSchemes(inactive='#222222'), self.x + self.width - 120, self.y + 10, 110, self.height - 20,
                                 self.screen, 'Open', LIST_TITLE_FONT,
                                 border_radius=10)

    def draw(self):
        pygame.draw.rect(self.screen, self.colors.secondary, self.rect)
        if self.image is not None:
            self.image.draw()

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

    def redraw(self):
        self.initialize()
        self.draw()