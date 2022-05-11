import string

from api.game_classes.creatures.creature import Creature


class Bot(Creature):
    def __init__(self, bot_name: string, bot_class: string or None, description: string, is_friendly: True or False,
                 image_id: int, lvl: int or None = None):
        Creature.__init__(self, bot_name, bot_class, lvl)
        self.description = description
        self.image_id = image_id
        self.is_friendly = is_friendly
        if not is_friendly:
            self.fight_class.statistics.setFightStatistics(lvl * 4)

    def __str__(self):
        return '\n----------------------\nName: ' + self.name + '\nbot_class: ' + \
               str(self.fight_class) + '\ndescription: ' + self.description  + \
               '\nstatistics: ' + str(self.fight_class.statistics) + '\n----------------------\n' + str(self.freeDevelopmentPoints)
