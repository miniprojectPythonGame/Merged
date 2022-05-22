from enum import Enum
from random import randint

from api.game_classes.properties.enums import StatisticsEnum


class Statistics:
    def __init__(self, strength=0, intelligence=0, dexterity=0, constitution=0, luck=0, persuasion=0, trade=0,
                 leadership=0,
                 protection=0, initiative=0):
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.constitution = constitution
        self.luck = luck

        self.protection = protection

        self.hp = constitution * 100

        self.persuasion = persuasion
        self.trade = trade
        self.leadership = leadership
        self.initiative = initiative

    @classmethod
    def genItemStatistics(cls, different_stats_amount: int, points_to_use: int):
        stats = Statistics()
        stats_dict = {StatisticsEnum.STRENGTH.value: 0, StatisticsEnum.INTELLIGENCE.value: 0,
                      StatisticsEnum.DEXTERITY.value: 0, StatisticsEnum.CONSTITUTION.value: 0,
                      StatisticsEnum.PROTECTION.value: 0, StatisticsEnum.PERSUASION.value: 0,
                      StatisticsEnum.TRADE.value: 0, StatisticsEnum.LEADERSHIP.value: 0,
                      StatisticsEnum.INITIATIVE.value: 0}

        chosen_stats = []
        while len(chosen_stats) < different_stats_amount:
            x = randint(0, 8)
            if x not in chosen_stats:
                chosen_stats.append(x)

        for i in range(points_to_use):
            stat_to_update = randint(0, different_stats_amount - 1)
            update_dict = {chosen_stats[stat_to_update]: stats_dict.get(chosen_stats[stat_to_update]) + 1}
            stats_dict.update(update_dict)

        if StatisticsEnum.STRENGTH.value in chosen_stats:
            stats.strength += stats_dict.get(StatisticsEnum.STRENGTH.value)
        if StatisticsEnum.INTELLIGENCE.value in chosen_stats:
            stats.intelligence += stats_dict.get(StatisticsEnum.INTELLIGENCE.value)
        if StatisticsEnum.DEXTERITY.value in chosen_stats:
            stats.dexterity += stats_dict.get(StatisticsEnum.DEXTERITY.value)
        if StatisticsEnum.CONSTITUTION.value in chosen_stats:
            stats.constitution += stats_dict.get(StatisticsEnum.CONSTITUTION.value)
        if StatisticsEnum.PROTECTION.value in chosen_stats:
            stats.protection += stats_dict.get(StatisticsEnum.PROTECTION.value)
        if StatisticsEnum.PERSUASION.value in chosen_stats:
            stats.persuasion += stats_dict.get(StatisticsEnum.PERSUASION.value)
        if StatisticsEnum.TRADE.value in chosen_stats:
            stats.trade += stats_dict.get(StatisticsEnum.TRADE.value)
        if StatisticsEnum.LEADERSHIP.value in chosen_stats:
            stats.leadership += stats_dict.get(StatisticsEnum.LEADERSHIP.value)
        if StatisticsEnum.INITIATIVE.value in chosen_stats:
            stats.initiative += stats_dict.get(StatisticsEnum.INITIATIVE.value)

        return stats

    def setFightStatistics(self, freeDevelopmentPoints):
        for i in range(0, freeDevelopmentPoints):
            rand_num = randint(0, 4)
            if rand_num == 0:
                self.strength += 1
            elif rand_num == 1:
                self.intelligence += 1
            elif rand_num == 2:
                self.dexterity += 1
            elif rand_num == 3:
                self.constitution += 1
            else:
                self.luck += 1

        self.protection = randint(0, 50)
        self.hp = self.constitution * 100

    def __str__(self):
        return f'strength: {self.strength}\n' \
               f'intelligence:{self.intelligence}\n' \
               f'dexterity:{self.dexterity}\n' \
               f'constitution:{self.constitution}\n' \
               f'luck:{self.luck}\n' \
               f'persuasion:{self.persuasion}\n' \
               f'trade:{self.trade}\n' \
               f'leadership:{self.leadership}\n' \
               f'protection:{self.protection}\n' \
               f'initiative:{self.initiative}\n' \
               f'hp:{self.hp}'

    def __add__(self, other):
        strength = self.strength + other.strength
        intelligence = self.intelligence + other.intelligence
        dexterity = self.dexterity + other.dexterity
        constitution = self.constitution + other.constitution
        luck = self.luck + other.luck

        protection = self.protection + other.protection

        persuasion = self.persuasion + other.persuasion
        trade = self.trade + other.trade
        leadership = self.leadership + other.leadership
        initiative = self.initiative + other.initiative

        return Statistics(strength, intelligence, dexterity, constitution, luck, persuasion, trade,
                          leadership,
                          protection, initiative)

    def __sub__(self, other):
        strength = self.strength - other.strength
        intelligence = self.intelligence - other.intelligence
        dexterity = self.dexterity - other.dexterity
        constitution = self.constitution - other.constitution
        luck = self.luck - other.luck

        protection = self.protection - other.protection

        persuasion = self.persuasion - other.persuasion
        trade = self.trade - other.trade
        leadership = self.leadership - other.leadership
        initiative = self.initiative - other.initiative

        return Statistics(strength, intelligence, dexterity, constitution, luck, persuasion, trade,
                          leadership,
                          protection, initiative)
