from .Label import Label

from src.globals.const_values import pygame, \
    STATS_NAMES, \
    TEXT_FONT, \
    SMALL_FONT

from api.game_classes.objects.items.item import Quality

from .ColorSchemes import ColorSchemes


class PopupItem:
    def __init__(self, width, height, screen, isVisible=False):
        self.x = None
        self.y = None
        self.width = width
        self.height = height
        self.screen = screen
        self.name = None
        self.quality = None
        self.statistics = None
        self.isVisible = isVisible
        self.color = ColorSchemes()

    def draw(self):
        if self.isVisible and self.name != 'empty':
            name = Label(self.name, TEXT_FONT, self.color.white,
                         self.screen, self.x + 10, self.y + 10)
            quality = Label(self.quality, SMALL_FONT, self.secondary_color,
                            self.screen, self.x + 10, self.y + 23)

            stat_headers = []
            stat_values = []
            statistics = [
                self.statistics.strength,
                self.statistics.intelligence,
                self.statistics.dexterity,
                self.statistics.constitution,
                self.statistics.luck,
                self.statistics.persuasion,
                self.statistics.trade,
                self.statistics.leadership,
                self.statistics.protection,
                self.statistics.initiative,
            ]

            for i in range(len(STATS_NAMES)):
                stat_headers.append(
                    Label(STATS_NAMES[i], SMALL_FONT, self.color.gray_light, self.screen,
                          self.x + 10 + (i % 2) * 100,
                          self.y + 40 + (i % round(len(STATS_NAMES)/2)) * 12)
                )
                stat_values.append(
                    Label(str(statistics[i]), SMALL_FONT, self.secondary_color, self.screen,
                          self.x + 10 + ((i % 2) + 1) * 100 - 25,
                          self.y + 40 + (i % round(len(STATS_NAMES) / 2)) * 12)
                )

            rect = pygame.Rect(self.x, self.y, self.width, self.height)
            pygame.draw.rect(self.screen, self.color.primary, rect)
            pygame.draw.rect(self.screen, self.secondary_color, rect, 1, 5)
            name.draw()
            quality.draw()
            for i in range(len(stat_headers)):
                stat_headers[i].draw()
                stat_values[i].draw()

    def setItem(self, x, y, name, quality, statistics):
        self.x = x
        self.y = y
        self.name = name
        self.getColor(quality)
        self.statistics = statistics

    def setVisible(self, mode):
        self.isVisible = mode

    def getColor(self, quality):
        if quality == Quality.COMMON.value:
            self.quality = 'common'
            self.secondary_color = self.color.common

        elif quality == Quality.EPIC.value:
            self.quality = 'epic'
            self.secondary_color = self.color.epic

        elif quality == Quality.LEGENDARY.value:
            self.quality = 'legendary'
            self.secondary_color = self.color.legendary

        else:
            self.quality = 'empty'
            self.secondary_color = self.color.white