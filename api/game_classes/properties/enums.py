from enum import Enum


class Difficulty(Enum):
    EASY = 1
    INTERMEDIATE = 2
    HARD = 3

    @classmethod
    def get_difficulty(cls, difficulty: int):
        return {1: Difficulty.EASY, 2: Difficulty.INTERMEDIATE, 3: Difficulty.HARD}.get(difficulty)

    @classmethod
    def get_bot_lvl_advantage(cls, difficulty: int):
        return {1: 3, 2: 7, 3: 15}.get(difficulty)


class Quality(Enum):
    LEGENDARY = 1
    EPIC = 2
    COMMON = 3

    @classmethod
    def get_quality(cls, number: int):
        if number == 1:
            return Quality.LEGENDARY
        if number == 2:
            return Quality.EPIC
        if number == 3:
            return Quality.COMMON

    @classmethod
    def get_quality_from_difficulty(cls, diff: Difficulty):
        return {Difficulty.EASY: Quality.COMMON, Difficulty.INTERMEDIATE: Quality.EPIC,
                Difficulty.HARD: Quality.LEGENDARY}.get(diff)

    @classmethod
    def get_different_stats_and_points_for_quality(cls, quality):
        return {Quality.COMMON: (2, 5), Quality.EPIC: (3, 15), Quality.LEGENDARY: (5, 25)}.get(quality)
