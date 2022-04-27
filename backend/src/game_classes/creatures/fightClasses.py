from backend.src.game_classes.creatures.statistics import Statistics


class Archer:
    def __init__(self, strength, intelligence, dexterity, constitution, luck, persuasion, trade, leadership, protection,
                 initiative):
        self.statistics = Statistics(strength, intelligence, dexterity, constitution, luck, persuasion, trade,
                                     leadership, protection, initiative)
        # self.statistics = Statistics(1, 2, 7, 6, 4, 0, 0, 0)
        self.baseDmg = self.statistics.dexterity * 3

    def __str__(self):
        return 'Archer'


class Mage:
    def __init__(self, strength, intelligence, dexterity, constitution, luck, persuasion, trade, leadership, protection,
                 initiative):
        self.statistics = Statistics(strength, intelligence, dexterity, constitution, luck, persuasion, trade,
                                     leadership, protection, initiative)

        # self.statistics = Statistics(6, 1, 2, 8, 3, 0, 0, 0)
        self.baseDmg = self.statistics.strength * 3

    def __str__(self):
        return 'Mage'


class Warrior:
    def __init__(self, strength, intelligence, dexterity, constitution, luck, persuasion, trade, leadership, protection,
                 initiative):
        # self.statistics = Statistics(1, 8, 1, 4, 6, 0, 0, 0)
        self.statistics = Statistics(strength, intelligence, dexterity, constitution, luck, persuasion, trade,
                                     leadership, protection, initiative)
        self.baseDmg = self.statistics.dexterity * 3

    def __str__(self):
        return 'Warrior'


def choseClass(className, strength=None, intelligence=None, dexterity=None,
               constitution=None, luck=None, persuasion=None, trade=None, leadership=None, protection=None,
               initiative=None):
    if className == 'a':
        return Archer(strength, intelligence, dexterity,
                      constitution, luck, persuasion, trade, leadership, protection,
                      initiative)
    if className == 'w':
        return Warrior(strength, intelligence, dexterity,
                       constitution, luck, persuasion, trade, leadership, protection,
                       initiative)
    if className == 'm':
        return Mage(strength, intelligence, dexterity,
                    constitution, luck, persuasion, trade, leadership, protection,
                    initiative)
