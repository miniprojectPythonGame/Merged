
from api.game_classes.creatures.fightClasses import choseClass


class Creature:
    def __init__(self, name, className, lvl, strength=0, intelligence=0, dexterity=0,
                 constitution=0, luck=0, persuasion=0, trade=0, leadership=0, protection=0,
                 initiative=0, freeDevelopmentPts=0):
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

