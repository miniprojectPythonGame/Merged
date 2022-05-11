import string
from enum import Enum
from typing import List

from api.game_classes.creatures.bot import Bot
from api.game_classes.objects.items.item import Item
from api.web.WebService import connect_to_db, disconnect_from_db


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
        return '----------------------\nName: ' + self.name + '\ndescription: ' + self.description + '\ndifficulty: ' + str(self.difficulty) + '\nenemy: ' + str(self.enemy) + '\n----------------------\n'


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
            if line[9] is not None:  # TODO to be implemented
                # TODO build item from treasure
                # TODO if the fight is won item should be created
                # TODO item should be transferred to hero's storage
                cursor.execute(
                    "select image_id,name,description,item_type_id,for_class from treasures where treasure_id = %s",
                    (line[9],))
                treasure_item = None  # TODO

            new_quest: Quest = Quest(line[3], Difficulty.get_difficulty(line[1]), treasure_item, line[5], line[4],
                                     new_bot)
            self.quest_list.append(new_quest)
        disconnect_from_db(conn, cursor)


q = QuestList(20, 1)
for quest in q.quest_list:
    print(quest)
