import pygame


class QuestPreview():
    def __init__(self, x, y, width, height, colors, screen,
                 title, description, min_level, difficulty, min_gold, max_gold, treasure):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colors = colors
        self.screen = screen
        self.title = title
        self.description = description
        self.min_level = min_level
        self.difficulty = difficulty
        self.min_gold = min_gold
        self.max_gold = max_gold
        self.treasure = treasure
        self.rect_background = pygame.Rect(x, y, width, height)
        

    def draw(self):
        pygame.draw.rect(self.screen, self.colors.secondary, self.rect_background)


    def setColor(self, colors, subtitle):
        if subtitle == 'easy':
            return colors.easy
        if subtitle == 'intermediate':
            return colors.intermediate
        if subtitle == 'hard':
            return colors.hard

        return colors.white
