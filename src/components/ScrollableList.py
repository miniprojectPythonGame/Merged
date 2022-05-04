import pygame

from .ColorSchemes import ColorSchemes


class ScrollableList():
    def __init__(self, x, y, screen, elements, elem_height, elem_padding,
                 scroll_thickness=10, scroll_padding=10, visible=7, colors=ColorSchemes()):
        self.x = x
        self.y = y
        self.screen = screen
        self.elements = elements
        self.elem_height = elem_height
        self.elem_padding = elem_padding
        self.scroll_padding = scroll_padding
        self.scroll_range = len(self.elements)
        self.scroll_position = 0
        self.scroll_thickness = scroll_thickness
        self.visible = visible
        self.colors = colors
        self.list = self.initiateList()
        self.height = self.getHeight()
        self.drawScrollBar()

    def draw(self):
        pos = 0
        for i in range(self.scroll_position, self.scroll_position + self.visible):
            self.list[i].redraw()
            self.elements[i].y = self.getYPosition(pos)
            self.elements[i].x = self.x + self.scroll_thickness + self.scroll_padding
            pos += 1

        self.drawScrollBar()

    def initiateList(self):
        result = []
        pos = 0
        for i in range(self.scroll_position, self.scroll_range):
            self.elements[i].y = self.getYPosition(pos)
            self.elements[i].x += self.scroll_thickness + self.scroll_padding
            result.append(self.elements[pos])
            pos += 1

        return result

    def getYPosition(self, i):
        return self.y + i*self.elem_padding + i*self.elem_height

    def getHeight(self):
        return self.visible * self.elem_height + (self.visible - 1) * self.elem_padding

    def drawScrollBar(self):
        height = round((self.visible / self.scroll_range) * self.height)
        elem_height = round(round((self.visible / self.scroll_range) * self.height) / self.visible)
        y = self.y + self.scroll_position * elem_height
        rect = pygame.Rect(self.x, y, self.scroll_thickness, height)
        pygame.draw.rect(self.screen, self.colors.gray_light, rect, 0, 5)

    def onScrollUp(self):
        if self.scroll_position - 1 >= 0:
            self.scroll_position -= 1

    def onScrollDown(self):
        if self.scroll_position + 1 <= self.scroll_range - self.visible:
            self.scroll_position += 1
