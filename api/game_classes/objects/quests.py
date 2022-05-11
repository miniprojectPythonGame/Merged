import string
from typing import List

from api.game_classes.creatures.bot import Bot
from api.game_classes.properties.enums import Difficulty
from api.game_classes.properties.statistics import Statistics
from api.game_classes.objects.items.item import Item, Quality
from api.web.WebService import connect_to_db, disconnect_from_db


class Quest:
    def __init__(self, quest_id: int, difficulty: Difficulty, treasure: Item or None, description: string, name: string,
                 enemy: Bot):
        self.quest_id = quest_id
        self.treasure = treasure
        self.difficulty = difficulty
        self.description = description
        self.name = name
        self.enemy = enemy

    def __str__(self):
        return '----------------------\nName: ' + self.name + '\ndescription: ' + self.description + '\ndifficulty: ' + str(
            self.difficulty) + '\nenemy: ' + str(self.enemy) + '\n----------------------\n' + 'Treasure:\n' + str(self.treasure)


class QuestList:
    def __init__(self, hero_id: int, hero_lvl: int):
        self.hero_id = hero_id
        self.hero_lvl = hero_lvl
        self.quest_list: List[Quest] = []
        self.__load_quests()

    def __load_quests(self):
        conn, cursor = connect_to_db()
        cursor.execute(
            "SELECT bot_id,difficulty,min_lvl,quest_id,name,description,gold_reward,exp_reward,difficulty,treasure_id from quests where min_lvl <= %s",
            (self.hero_lvl,))
        result = cursor.fetchall()
        for line in result:
            cursor.execute("select bot_name,bot_class,description,image_id from bots where bot_id = %s", (line[0],))
            bot_data = cursor.fetchall()[0]
            new_bot: Bot = Bot(bot_data[0], bot_data[1], bot_data[2], False, bot_data[3],
                               line[2] + Difficulty.get_bot_lvl_advantage(line[1]))
            treasure_item: Item or None = None
            if line[9] is not None:
                cursor.execute(
                    "select image_id,name,description,item_type_id,for_class,price from treasures where treasure_id = %s",
                    (line[9],))
                item_data = cursor.fetchall()[0]
                quality: Quality = Quality.get_quality_from_difficulty(Difficulty.get_difficulty(line[1]))
                stats_and_points = Quality.get_different_stats_and_points_for_quality(quality)
                stats: Statistics = Statistics.genItemStatistics(stats_and_points[0], stats_and_points[1])
                treasure_item = Item(item_data[1], item_data[5], item_data[2], stats,
                                     item_data[4], None, 1, quality)

            new_quest: Quest = Quest(line[3], Difficulty.get_difficulty(line[1]), treasure_item, line[5], line[4],
                                     new_bot)
            self.quest_list.append(new_quest)
        disconnect_from_db(conn, cursor)


q = QuestList(20, 1)
for quest in q.quest_list:
    print(quest)
