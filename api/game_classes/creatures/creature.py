import string

from api.game_classes.creatures.fightClasses import choseClass


class Creature:
    def __init__(self, name: string, className: string, lvl: int, strength: int = 0, intelligence: int = 0,
                 dexterity: int = 0,
                 constitution: int = 0, luck: int = 0, persuasion: int = 0, trade: int = 0, leadership: int = 0,
                 protection: int = 0,
                 initiative: int = 0, freeDevelopmentPts: int = 0):
        self.name = name
        self.fight_class = choseClass(className, strength, intelligence, dexterity,
                                      constitution, luck, persuasion, trade, leadership, protection,
                                      initiative)
        self.lvl = lvl
        self.freeDevelopmentPoints = freeDevelopmentPts

    def strongAgainstOtherClass(self, other):
        if type(other).__name__ == 'Warrior':
            return self.fight_class.statistics.strength * 2
        if type(other).__name__ == 'Mage':
            return self.fight_class.statistics.intelligence * 2
        if type(other).__name__ == 'Archer':
            return self.fight_class.statistics.dexterity * 2
