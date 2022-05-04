import string
from enum import Enum

from api.game_classes.objects.items.item import Item


class Difficulty(Enum):
    EASY = 1
    INTERMEDIATE = 2
    HARD = 3


class Quest:
    def __init__(self, difficulty: Difficulty, treasure: Item, description: string, name: string):
        self.treasure = treasure
        self.difficulty = difficulty
        self.description = description
        self.name = name
