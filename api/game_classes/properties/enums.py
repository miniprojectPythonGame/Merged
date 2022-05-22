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
        return {1: 1, 2: 3, 3: 7}.get(difficulty)

    @classmethod
    def get_gold_and_exp_from_difficulty(cls, difficulty: int):
        return {1: (3, 70), 2: (6, 150), 3: (20, 250)}.get(difficulty)


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


class StatisticsEnum(Enum):
    STRENGTH = 0
    INTELLIGENCE = 1
    DEXTERITY = 2
    CONSTITUTION = 3
    PROTECTION = 4
    PERSUASION = 5
    TRADE = 6
    LEADERSHIP = 7
    INITIATIVE = 8


class ItemType(Enum):
    Belt = 0
    Boots = 1
    Breastplate = 2
    Gloves = 3
    Headgear = 4
    LuckyItem = 5
    Necklace = 6
    Ring = 7
    Steed = 8
    PrimaryWeapon = 9
    SecondaryWeapon = 10
    PotionPeriod = 11
    PotionPermanent = 12

    item_type_dict = {0: Belt,
                      1: Boots,
                      2: Breastplate,
                      3: Gloves,
                      4: Headgear,
                      5: LuckyItem,
                      6: Necklace,
                      7: Ring,
                      8: Steed,
                      9: PrimaryWeapon,
                      10: SecondaryWeapon,
                      11: PotionPeriod,
                      12: PotionPermanent}
