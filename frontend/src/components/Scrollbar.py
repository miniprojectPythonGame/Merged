from frontend.src.globals.const_values import *

class Scrollbar:
    def __init__(self, x, y, width, height, height_scroll, screen,
                 color_scroll=pygame.Color('#777777'),
                 color_background=pygame.Color('#aaaaaa'),
                 border=2, border_radius=0):
        self.x = x
        self.y = y
        self.x_scroll = x
        self.y_scroll = y
        self.width = width
        self.height = height
        self.height_scroll = height_scroll
        self.color_scroll = color_scroll
        self.color_background = color_background
        self.screen = screen
        self.border = border
        self.border_radius = border_radius
        self.rect_scroll = pygame.Rect(x, y, width, height_scroll)
        self.rect_background = pygame.Rect(x, y, width, height)

    def draw(self):
        pygame.draw.rect(self.screen, self.color_background, self.rect_background, 0, self.border_radius)
        pygame.draw.rect(self.screen, self.color_scroll, self.rect_scroll, 0, self.border_radius)

