import pygame

class ColorSchemes:
    def __init__(self,  active='lightskyblue3',
                        inactive='gray26',
                        text_color='gray26',
                        text_secondary_color='gray98'):
        self.active = pygame.Color(active)
        self.inactive = pygame.Color(inactive)
        self.text_color = pygame.Color(text_color)
        self.text_secondary_color = pygame.Color(text_secondary_color)
        self.primary = pygame.Color('#333333')
        self.secondary = pygame.Color('#555555')
        self.white = pygame.Color('white')
        self.black = pygame.Color('black')
        self.gray_light = pygame.Color('#cccccc')
        self.level = pygame.Color('#f29f46')
        self.health = pygame.Color('#49a644')
        self.legendary = pygame.Color('#edc161')
        self.epic = pygame.Color('#3680ad')
        self.common = pygame.Color('#95c4b2')
        self.easy = pygame.Color('#659e24')
        self.intermediate = pygame.Color('#d6733a')
        self.hard = pygame.Color('#e04643')
        self.attacker = pygame.Color('#013069')
        self.defender = pygame.Color('#690101')