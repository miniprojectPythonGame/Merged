import string

from api.game_classes.properties.statistics import Statistics


class Archer:
    def __init__(self, strength: int, intelligence: int, dexterity: int, constitution: int, luck: int, persuasion: int,
                 trade: int, leadership: int, protection: int,
                 initiative: int):
        self.statistics = Statistics(strength, intelligence, dexterity, constitution, luck, persuasion, trade,
                                     leadership, protection, initiative)
        # self.statistics = Statistics(1, 2, 7, 6, 4, 0, 0, 0)
        self.baseDmg = self.statistics.dexterity * 3 + 5

    def __str__(self):
        return 'Archer'


class Mage:
    def __init__(self, strength: int, intelligence: int, dexterity: int, constitution: int, luck: int, persuasion: int,
                 trade: int, leadership: int, protection: int,
                 initiative: int):
        self.statistics = Statistics(strength, intelligence, dexterity, constitution, luck, persuasion, trade,
                                     leadership, protection, initiative)

        # self.statistics = Statistics(6, 1, 2, 8, 3, 0, 0, 0)
        self.baseDmg = self.statistics.strength * 3 + 5

    def __str__(self):
        return 'Mage'


class Warrior:
    def __init__(self, strength: int, intelligence: int, dexterity: int, constitution: int, luck: int, persuasion: int,
                 trade: int, leadership: int, protection: int,
                 initiative: int):
        # self.statistics = Statistics(1, 8, 1, 4, 6, 0, 0, 0)
        self.statistics = Statistics(strength, intelligence, dexterity, constitution, luck, persuasion, trade,
                                     leadership, protection, initiative)
        self.baseDmg = self.statistics.dexterity * 3 + 5

    def __str__(self):
        return 'Warrior'


def choseClass(className: string, strength: int = 0, intelligence: int = 0, dexterity: int = 0,
               constitution: int = 0, luck: int = 0, persuasion: int = 0, trade: int = 0, leadership: int = 0,
               protection: int = 0,
               initiative: int = 0):

    args = (strength, intelligence, dexterity,
            constitution, luck, persuasion, trade, leadership, protection,
            initiative)

    class_dict = {'a': Archer, 'w': Warrior, 'm': Mage}
    return class_dict[className](*args)
