import pygame


class PropertyBar:
    def __init__(self, x, y, width, height, value,
                 text, font, border_color, fill_color, screen, border=1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.value = value
        self.text = text
        self.font = font
        self.border_color = border_color
        self.fill_color = fill_color
        self.screen = screen
        self.border = border

    def draw(self):
        self.bar_border = pygame.Rect(self.x, self.y, self.width, self.height)
        self.bar_fill = pygame.Rect(self.x, self.y, round(self.width * self.value), self.height)

        pygame.draw.rect(self.screen, self.fill_color, self.bar_fill)
        pygame.draw.rect(self.screen, self.border_color, self.bar_border, self.border)

        if self.text != '':
            text = self.font.render(self.text, 1, self.border_color)
            self.screen.blit(text,
                             (self.x + (self.width / 2 - text.get_width() / 2),
                              self.y + (self.height / 2 - text.get_height() / 2) + self.height * 0.06))
