import string
from enum import Enum
from typing import List

from api.game_classes.creatures.bot import Bot
from api.game_classes.objects.items.item import Item


class Difficulty(Enum):
    EASY = 1
    INTERMEDIATE = 2
    HARD = 3


class Quest:
    def __init__(self, difficulty: Difficulty, treasure: Item, description: string, name: string, enemy: Bot):
        self.treasure = treasure
        self.difficulty = difficulty
        self.description = description
        self.name = name
        self.enemy = enemy


class QuestList:
    def __init__(self, hero_id: int, hero_lvl: int):
        self.hero_id = hero_id
        self.hero_lvl = hero_lvl
        self.quest_list: List[Quest] = []

    def __load_quests(self):
        pass  # TODO add procedure in db to get the quests and map it here
