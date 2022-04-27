import pygame


class MultilineText:
    def __init__(self, text, font, color, surface, x, y, line_space, anchor='topleft'):
        self.text = text
        self.font = font
        self.color = color
        self.surface = surface
        self.x = x
        self.y = y
        self.line_space = line_space
        self.anchor = anchor

    def draw(self):
        offset = 0
        for text in self.text:
            text_obj = self.font.render(text, 1, self.color)
            rect = text_obj.get_rect()

            if self.anchor == 'topleft':
                rect.topleft = (self.x, self.y + offset)

            elif self.anchor == 'topright':
                rect.topright = (self.x, self.y + offset)

            else:
                print("Error")

            self.surface.blit(text_obj, rect)
            offset += self.line_space
