
from api.game_classes.creatures.fightClasses import choseClass


class Creature:
    def __init__(self, name, className, lvl, strength=None, intelligence=None, dexterity=None,
                 constitution=None, luck=None, persuasion=None, trade=None, leadership=None, protection=None,
                 initiative=None, freeDevelopmentPts=None):
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

