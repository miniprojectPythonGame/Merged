import pygame

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

class InputField:
    def __init__(self, x, y, width, height, border, colors,
                 screen, placeholder='None', max_length=10, isPassword=False, isNumeric=False):
        self.rect = pygame.Rect(x, y, width, height)
        self.padding = round(height * 0.2)
        self.border = border
        self.font = pygame.font.Font(None, height - self.padding)
        self.color_active = colors.active
        self.color_inactive = colors.inactive
        self.color_text = colors.text_color
        self.active = False
        self.color = self.color_inactive
        self.screen = screen
        self.placeholder = placeholder
        self.text = ''
        self.visibleText = placeholder
        self.isPassword = isPassword
        self.isNumeric = isNumeric
        self.max_length = max_length
        self.isEmpty = True
        self.text_surface = self.font.render(self.visibleText, True, colors.text_color)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect, self.border)
        self.text_surface = self.font.render(self.visibleText, True, self.color_text)
        self.screen.blit(self.text_surface, (self.rect.x + self.padding, self.rect.y + (1.4 * self.padding)))

    def appendText(self, character):
        if self.isEmpty and not self.isNumeric:
            self.text = ''
            self.visibleText = ''
            self.isEmpty = False

        if len(self.text) < self.max_length:
            if self.isPassword:
                self.text += character
                self.visibleText += '*'

            elif self.isNumeric:
                if character in digits:
                    if self.isEmpty:
                        self.text = ''
                        self.visibleText = ''
                        self.isEmpty = False

                    self.text += character
                    self.visibleText = self.text

            else:
                self.text += character
                self.visibleText = self.text

    def subtractText(self):
        self.text = self.text[:-1]
        self.visibleText = self.visibleText[:-1]

        if len(self.text) == 0:
            self.isEmpty = True
            self.visibleText = self.placeholder

    def reset(self):
        self.text = ''
        self.visibleText = self.placeholder
        self.isEmpty = True

    def activate(self):
        self.active = True
        self.color = self.color_active

    def deactivate(self):
        self.active = False
        self.color = self.color_inactive