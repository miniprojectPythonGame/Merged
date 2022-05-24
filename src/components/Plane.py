import pygame

class Plane():
    def __init__(self, x, y, width, height, color, screen, border=0, border_radius=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.border = border
        self.border_radius = border_radius


    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect, self.border, self.border_radius)