from backend.src.game_classes.creatures.creature import Creature


class Bot(Creature):
    def __init__(self, name, className, gold, gained_exp, lvl=1, dropped_item=None):
        Creature.__init__(self, name, className, lvl)
        self.heroClass.statistics.setFightStatistics(self.freeDevelopmentPoints)
        self.gold = gold
        self.dropped_item = dropped_item
        self.gained_exp = gained_exp
