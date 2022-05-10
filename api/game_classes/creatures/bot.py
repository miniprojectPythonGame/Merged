import string

from api.game_classes.creatures.creature import Creature


class Bot(Creature):
    def __init__(self, bot_name: string, bot_class: string or None, description: string, is_friendly: True or False,
                 image_id: int, lvl: int or None = None):
        Creature.__init__(self, bot_name, bot_class, lvl)
        self.description = description
        self.image_id = image_id
        if not is_friendly:
            self.freeDevelopmentPoints = lvl * 4
            self.fight_class.statistics.setFightStatistics(self.freeDevelopmentPoints)
