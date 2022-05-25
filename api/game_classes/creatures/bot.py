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
        return f'\n----------------------\n' \
               f'name:{self.name}\n' \
               f'fight_class:{self.fight_class}\n' \
               f'description:{self.description}\n' \
               f'statistics:{self.fight_class.statistics}'

    def get_statistics(self):
        return self.fight_class.statistics
