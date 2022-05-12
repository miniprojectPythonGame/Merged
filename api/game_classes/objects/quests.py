import string
from math import floor
from random import randint
from typing import List

from api.game_classes.creatures.bot import Bot
from api.game_classes.properties.enums import Difficulty
from api.game_classes.properties.statistics import Statistics
from api.game_classes.objects.items.item import Item, Quality, ItemType, Belt, Boots, Breastplate, Gloves, Headgear, \
    LuckyItem, Necklace, Ring, Steed, PrimaryWeapon, SecondaryWeapon, PotionPeriod, PotionPermanent
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

    def add_prizes(self, hero_id, hero_lvl):
        d_gold_mod, d_exp_mod = Difficulty.get_gold_and_exp_from_difficulty(self.difficulty.value)
        exp = floor(randint(50, 100) / 100 * hero_lvl * d_exp_mod)
        gold = floor(randint(50, 100) / 100 * hero_lvl * d_gold_mod)

        t_status = None
        try:
            conn, cursor = connect_to_db()
            cursor.execute("update heroes set gold = gold + %s where hero_id = %s;", (gold, hero_id))
            cursor.execute("update heroes set exp = exp + %s where hero_id = %s;", (exp, hero_id))
            conn.commit()
            disconnect_from_db(conn, cursor)
            t_status = True
        except Exception as error:
            print(error)
            t_status = False
        finally:
            return t_status

    def __str__(self):
        return '----------------------\nName: ' + self.name + '\ndescription: ' + self.description + '\ndifficulty: ' + str(
            self.difficulty) + '\nenemy: ' + str(self.enemy) + '\n----------------------\n' + 'Treasure:\n' + str(
            self.treasure)


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

                item_dict = {
                    ItemType.Belt.value: Belt(stats, item_data[1], item_data[5], item_data[2], item_data[4], None, 1,
                                              quality),
                    ItemType.Boots.value: Boots(stats, item_data[1], item_data[5], item_data[2], item_data[4], None, 1,
                                                quality),
                    ItemType.Breastplate.value: Breastplate(stats, item_data[1], item_data[5], item_data[2],
                                                            item_data[4], None, 1,
                                                            quality),
                    ItemType.Gloves.value: Gloves(stats, item_data[1], item_data[5], item_data[2], item_data[4], None,
                                                  1,
                                                  quality),
                    ItemType.Headgear.value: Headgear(stats, item_data[1], item_data[5], item_data[2], item_data[4],
                                                      None, 1,
                                                      quality),
                    ItemType.LuckyItem.value: LuckyItem(stats, item_data[1], item_data[5], item_data[2], item_data[4],
                                                        None, 1,
                                                        quality),
                    ItemType.Necklace.value: Necklace(stats, item_data[1], item_data[5], item_data[2], item_data[4],
                                                      None, 1,
                                                      quality),
                    ItemType.Ring.value: Ring(stats, item_data[1], item_data[5], item_data[2], item_data[4], None, 1,
                                              quality),
                    ItemType.Steed.value: Steed(stats, item_data[1], item_data[5], item_data[2], item_data[4], None, 1,
                                                quality),
                    ItemType.PrimaryWeapon.value: PrimaryWeapon(stats, item_data[1], item_data[5], item_data[2],
                                                                item_data[4], None, 1,
                                                                quality),
                    ItemType.SecondaryWeapon.value: SecondaryWeapon(stats, item_data[1], item_data[5], item_data[2],
                                                                    item_data[4], None, 1,
                                                                    quality),
                    ItemType.PotionPeriod.value: PotionPeriod(stats, item_data[1], item_data[5], item_data[2],
                                                              item_data[4], None, 1,
                                                              quality),
                    ItemType.PotionPermanent.value: PotionPermanent(stats, item_data[1], item_data[5], item_data[2],
                                                                    item_data[4], None, 1,
                                                                    quality)
                }

                treasure_item = item_dict.get(item_data[3])

            new_quest: Quest = Quest(line[3], Difficulty.get_difficulty(line[1]), treasure_item, line[5], line[4],
                                     new_bot)
            self.quest_list.append(new_quest)
        disconnect_from_db(conn, cursor)

# q = QuestList(20, 1)
# for quest in q.quest_list:
#     print(quest)
