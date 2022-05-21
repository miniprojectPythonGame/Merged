import string
from typing import List

from api.game_classes.properties.enums import Quality, ItemType
from api.game_classes.properties.statistics import Statistics
from api.web.WebService import connect_to_db, disconnect_from_db


class Item:
    def __init__(self, name: string, price: int, description: string, statistics: Statistics, for_class: string,
                 item_id: int or None, available: int, quality: Quality):
        self.quality = quality
        self.price = price
        self.name = name
        self.description = description
        self.statistics = statistics
        self.for_class = for_class
        self.item_id = item_id
        self.available = available

    @classmethod
    def add_item_to_db(cls, item, min_lvl: int = 1):
        result = None
        conn, cursor = connect_to_db()
        with conn:
            try:
                cursor.execute("call add_item(%s,%s,%s,%s,%s,1::SMALLINT,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    item.quality.value, item.name, item.price, item.description, item.for_class, item.item_type.value,
                    min_lvl,
                    item.statistics.strength, item.statistics.intelligence, item.statistics.dexterity,
                    item.statistics.constitution,
                    item.statistics.luck, item.statistics.persuasion, item.statistics.trade, item.statistics.leadership,
                    item.statistics.protection, item.statistics.initiative))
                conn.commit()
                cursor.execute("select item_id from items order by item_id desc limit 1")
                result = cursor.fetchone()[0]
            except Exception as error:
                print(error)
            finally:
                return result

    @classmethod
    def add_item_to_hero_storage(cls, hero_id, item_id):
        transaction_status = None
        try:
            conn, cursor = connect_to_db()
            cursor.execute("call add_to_storage(%s,%s)", (hero_id, item_id))
            conn.commit()
            disconnect_from_db(conn, cursor)
            transaction_status = True
        except Exception as error:
            print(error)
            transaction_status = False
        finally:
            return transaction_status

    @classmethod
    def build_item(cls, item_id: int, item_info: List, available: int = 1):
        newStats = Statistics(item_info[7],
                              item_info[8],
                              item_info[9],
                              item_info[10],
                              item_info[11],
                              item_info[12],
                              item_info[13],
                              item_info[14],
                              item_info[15],
                              item_info[16],
                              )

        item_type = item_info[4]
        args = (newStats,
                item_info[0],
                item_info[1],
                item_info[2], item_info[6], item_id, available,
                Quality.get_quality(item_info[17]))

        item_dict = {
            ItemType.Belt: Belt,
            ItemType.Boots: Boots,
            ItemType.Breastplate: Breastplate,
            ItemType.Gloves: Gloves,
            ItemType.Headgear: Headgear,
            ItemType.LuckyItem: LuckyItem,
            ItemType.Necklace: Necklace,
            ItemType.Ring: Ring,
            ItemType.Steed: Steed,
            ItemType.PrimaryWeapon: PrimaryWeapon,
            ItemType.SecondaryWeapon: SecondaryWeapon,
            ItemType.PotionPeriod: PotionPeriod,
            ItemType.PotionPermanent: PotionPermanent,
        }

        return item_dict[ItemType(item_type)](*args)

    @classmethod
    def all_info_select(cls, item_id: int):
        select = "SELECT I.name,I.price,I.description,I.only_treasure,I.item_type_id,I.min_lvl,I.for_class," \
                 "s.strength,s.intelligence,s.dexterity,s.constitution,s.luck,s.persuasion,s.trade,s.leadership," \
                 "s.protection,s.initiative,i.quality FROM items I JOIN statistics s on s.statistics_id = I.statistics_id" \
                 " WHERE I.item_id = " + str(item_id)
        return select

    def __str__(self):
        return f'----------------------\n' \
               f'name:{self.name}\n' \
               f'price:{self.price}\n' \
               f'description:{self.description}\n' \
               f'item_id:{self.item_id}\n' \
               f'\n----------------------\n' \
               f'quality:{self.quality.name}\n' \
               f'\n----------------------\n' \
               f'{self.statistics}'


class Belt(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id, available, quality):
        Item.__init__(self, name, price, description, statistics, for_class, item_id, available, quality)
        self.item_type = ItemType.Belt


class Boots(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id, available, quality):
        Item.__init__(self, name, price, description, statistics, for_class, item_id, available, quality)
        self.item_type = ItemType.Boots


class Breastplate(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id, available, quality):
        Item.__init__(self, name, price, description, statistics, for_class, item_id, available, quality)
        self.item_type = ItemType.Breastplate


class Gloves(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id, available, quality):
        Item.__init__(self, name, price, description, statistics, for_class, item_id, available, quality)
        self.item_type = ItemType.Gloves


class Headgear(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id, available, quality):
        Item.__init__(self, name, price, description, statistics, for_class, item_id, available, quality)
        self.item_type = ItemType.Headgear


class LuckyItem(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id, available, quality):
        Item.__init__(self, name, price, description, statistics, for_class, item_id, available, quality)
        self.item_type = ItemType.LuckyItem


class Necklace(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id, available, quality):
        Item.__init__(self, name, price, description, statistics, for_class, item_id, available, quality)
        self.item_type = ItemType.Necklace


class Ring(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id, available, quality):
        Item.__init__(self, name, price, description, statistics, for_class, item_id, available, quality)
        self.item_type = ItemType.Ring


class Steed(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id, available, quality,
                 additionalStorage=0):
        Item.__init__(self, name, price, description, statistics, for_class, item_id, available, quality)
        self.additionalStorage = additionalStorage  # in slots
        self.item_type = ItemType.Steed


class PrimaryWeapon(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id, available, quality):
        Item.__init__(self, name, price, description, statistics, for_class, item_id, available, quality)
        if for_class == "w":
            self.min_dmg = statistics.strength * 15
        elif for_class == "a":
            self.min_dmg = statistics.dexterity * 15
        elif for_class == "m":
            self.min_dmg = statistics.intelligence * 15
        else:
            self.min_dmg = statistics.strength * 5 + statistics.dexterity * 5 + statistics.intelligence * 5

        self.max_dmg = self.min_dmg * 10 * statistics.luck
        self.item_type = ItemType.PrimaryWeapon


class SecondaryWeapon(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id, available, quality):
        Item.__init__(self, name, price, description, statistics, for_class, item_id, available, quality)
        self.item_type = ItemType.SecondaryWeapon


class PotionPeriod(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id, available, quality,
                 periodInDays=7):
        Item.__init__(self, name, price, description, statistics, for_class, item_id, available, quality)
        self.periodInDays = periodInDays
        self.item_type = ItemType.PotionPeriod

    def use(self):
        pass


class PotionPermanent(Item):
    def __init__(self, statistics: Statistics, name, price, description, for_class, item_id, available, quality):
        Item.__init__(self, name, price, description, statistics, for_class, item_id, available, quality)
        self.item_type = ItemType.PotionPermanent

    def use(self):
        pass
