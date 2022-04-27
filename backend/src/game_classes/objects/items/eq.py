import random

from backend.src.game_classes.creatures.statistics import Statistics
from backend.src.game_classes.objects.items.item import ItemBuilder, Item
from backend.src.web.WebService import connect_to_db, disconnect_from_db


class Eq:
    def __init__(self, hero_id, className, gold):
        self.hero_id = hero_id
        self.itemSlots = [None] * 31
        self.gearStatistics = Statistics()
        self.className = className
        self.gold = gold
        self.get_storage()

    def __changeEqItem(self, in_eq, in_storage):
        if self.itemSlots[in_eq] is not None:
            self.gearStatistics -= self.itemSlots[in_eq].statistics

        self.itemSlots[in_eq], self.itemSlots[in_storage] = self.itemSlots[in_storage], self.itemSlots[in_eq]

        self.gearStatistics += self.itemSlots[in_eq].statistics

    def get_storage(self):
        try:
            conn, cursor = connect_to_db()
            cursor.execute(
                "SELECT i.item_id, i.item_type_id, s.item_slot_id,s.amount,s.available,i.for_class "
                "FROM storage s join items i on s.item_id = i.item_id where hero_id = %s;",
                (self.hero_id,))
            storage = cursor.fetchall()
            for item in storage:
                item_id = item[0]
                cursor.execute(
                    "SELECT I.name,I.price,I.description,I.only_treasure,I.item_type_id,I.min_lvl,I.for_class,s.strength,"
                    "s.intelligence,s.dexterity,s.constitution,s.luck,s.persuasion,s.trade,s.leadership,s.protection,s.initiative"
                    " FROM items I JOIN statistics s on s.statistics_id = I.statistics_id WHERE I.item_id = %s;",
                    (item_id,))

                self.itemSlots[item[2]] = ItemBuilder.build_item(item_id, cursor.fetchall()[0])
            disconnect_from_db(conn, cursor)
        except Exception as error:
            print(error)

    def swap_places(self, a, b):
        try:
            if self.__can_be_swapped(a, b):
                conn, cursor = connect_to_db()
                cursor.execute("call move_in_storage(%s,%s,%s)",
                               (self.hero_id, a,
                                b))
                conn.commit()
                if a <= 10:
                    self.__changeEqItem(a, b)
                elif b <= 10:
                    self.__changeEqItem(b, a)

                disconnect_from_db(conn, cursor)
        except Exception as error:
            print(error)

    def __can_be_swapped(self, a, b):
        if a > 10 and b > 10:
            return True
        if a <= 10 and self.itemSlots[b] is None:
            return True
        if b <= 10 and self.itemSlots[a] is None:
            return True
        if 10 >= a == self.itemSlots[b].get_code() and self.itemSlots[b].for_class in (None, self.className):
            return True
        if 10 >= b == self.itemSlots[a].get_code() and self.itemSlots[a].for_class in (None, self.className):
            return True
        return False

    def dump_item(self, itemSlots_id):
        item_id = self.itemSlots[itemSlots_id].item_id
        self.__remove_from_storage(itemSlots_id)
        try:
            conn, cursor = connect_to_db()
            if random.randint(0, 4) != 0:
                # you have 80% chance that duped item will be lost forever and will evaporate from existence,
                # but there still is a chance that someone will find it dumped and pick it up.
                cursor.execute("delete from items where item_id = %s;", (item_id,))
            conn.commit()
            disconnect_from_db(conn, cursor)
        except Exception as error:
            print(error)

    def __remove_from_storage(self, itemSlots_id):
        try:
            conn, cursor = connect_to_db()
            cursor.execute("CALL remove_from_storage(%s,%s)", (self.hero_id, itemSlots_id))
            conn.commit()
            disconnect_from_db(conn, cursor)
            self.itemSlots[itemSlots_id] = None
            return True
        except Exception as error:
            print(error)
            return False

    def sell_item(self, itemSlots_id):
        earned_money = self.itemSlots[itemSlots_id].price
        if self.__remove_from_storage(itemSlots_id):
            try:
                conn, cursor = connect_to_db()
                cursor.execute("update heroes set gold = gold + %s where hero_id = %s;", (earned_money, self.hero_id))
                conn.commit()
                disconnect_from_db(conn, cursor)
                self.gold += earned_money
                return True
            except Exception as error:
                print(error)
                return False
        return False

    def add_item(self, item: Item):
        if item is not False:
            try:
                conn, cursor = connect_to_db()
                cursor.execute("SELECT item_slot_id FROM storage where hero_id = %s and item_id = %s",
                               (self.hero_id, item.item_id))
                self.itemSlots[cursor.fetchall()[0][0]] = item
                disconnect_from_db(conn, cursor)
                self.gold -= item.price
                return True
            except Exception as error:
                print(error)
                return False
        return False
