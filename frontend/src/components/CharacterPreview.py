import pygame

from frontend.src.components.ImageField import ImageField

class CharacterPreview:
    def __init__(self, x, y, width, height, bar_width, bar_height,
                 name, class_name, level, imagePath, screen, font):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bar_width = bar_width
        self.bar_height = bar_height
        self.name = name
        self.class_name = class_name
        self.level = level
        self.screen = screen
        self.font = font
        self.rect = pygame.Rect(x, y, width, height + 2 * bar_height)
        self.image = ImageField(x, y, width, height, imagePath, screen)
        self.rect_border = pygame.Rect(x, y, width, height)

        self.rect_name = pygame.Rect(x + round((width - bar_width) / 2),
                                     y + height - bar_height - 10,
                                     bar_width, bar_height)
        self.text_name = self.font.render(self.name, 1, pygame.Color('white'))

        self.rect_class = pygame.Rect(x,
                                      y + height,
                                      width, bar_height)
        self.text_class = self.font.render(self.class_name, 1, pygame.Color('white'))

        self.rect_level = pygame.Rect(x,
                                      y + height + bar_height,
                                      width, bar_height)
        self.text_level = self.font.render('Level ' + str(self.level), 1, pygame.Color('white'))

    def draw(self):
        self.image.draw()
        pygame.draw.rect(self.screen, pygame.Color('gray14'), self.rect_border, 3)

        pygame.draw.rect(self.screen, pygame.Color('gray14'), self.rect_name, 0, 7)
        self.screen.blit(self.text_name,
                         (
                             self.x + (self.width - self.bar_width) / 2 + (
                                         self.bar_width - self.text_name.get_width()) / 2,
                             self.y + self.height - self.bar_height - 8 + (
                                     self.bar_height - self.text_name.get_height()) / 2))

        if self.class_name != '':
            pygame.draw.rect(self.screen, pygame.Color('gray14'), self.rect_class, 0)
            self.screen.blit(self.text_class,
                             (self.x + (self.width - self.text_class.get_width()) / 2,
                              self.y + self.height + (self.bar_height - self.text_class.get_height()) / 2))

            pygame.draw.rect(self.screen, pygame.Color('gray26'), self.rect_level, 0)
            self.screen.blit(self.text_level,
                             (self.x + (self.width - self.text_level.get_width()) / 2,
                              self.y + self.height + self.bar_height + (
                                      self.bar_height - self.text_level.get_height()) / 2))