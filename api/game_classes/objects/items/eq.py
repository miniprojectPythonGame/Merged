import random
import string

from api.game_classes.properties.statistics import Statistics
from api.game_classes.objects.items.item import Item
from api.web.WebService import connect_to_db


class Eq:
    def __init__(self, hero_id: int, className: string, gold: int):
        """
        :param hero_id: Identifier of hero in db

        :param className: Name of class of hero - 'a' for Archer, 'm' for Mage and 'w' for Warrior. Mainly used for checking whether an Item can be equipped

        :param gold: Heroes gold
        """
        self.hero_id = hero_id
        self.itemSlots: None or Item = [None] * 31  # indexes from 0 to 10 are Eq - the things that are equipped
        self.gearStatistics = Statistics()
        self.className = className
        self.gold = gold
        self.get_storage()

    def add_to_storage(self, item: Item):
        for i in range(11, len(self.itemSlots)):
            if self.itemSlots[i] is None:
                self.itemSlots[i] = item
                return

    def __changeEqItem(self, in_eq, in_storage):
        if self.itemSlots[in_eq] is not None:
            self.gearStatistics -= self.itemSlots[in_eq].statistics

        self.itemSlots[in_eq], self.itemSlots[in_storage] = self.itemSlots[in_storage], self.itemSlots[in_eq]

        if self.itemSlots[in_eq] is not None:
            self.gearStatistics += self.itemSlots[in_eq].statistics

    def get_storage(self):
        conn, cursor = connect_to_db()
        try:
            with conn:
                cursor.execute(
                    "SELECT i.item_id,s.available,s.item_slot_id,i.quality "
                    "FROM storage s join items i on s.item_id = i.item_id where hero_id = %s;",
                    (self.hero_id,))
                storage = cursor.fetchall()
                for item in storage:
                    item_id = item[0]
                    available = item[1]
                    item_slot_id = item[2]
                    cursor.execute(Item.all_info_select(item_id))

                    self.itemSlots[item_slot_id] = Item.build_item(item_id, cursor.fetchall()[0], available)

                    if item_slot_id <= 10:
                        self.gearStatistics += self.itemSlots[item_slot_id].statistics

        except Exception as error:
            print(error)

    def swap_places(self, a, b):
        try:
            if self.__can_be_swapped(a, b):
                conn, cursor = connect_to_db()
                with conn:
                    cursor.execute("call move_in_storage(%s,%s,%s)",
                                   (self.hero_id, a,
                                    b))
                    if a <= 10:
                        self.__changeEqItem(a, b)
                    elif b <= 10:
                        self.__changeEqItem(b, a)
                    else:
                        self.itemSlots[a], self.itemSlots[b] = self.itemSlots[b], self.itemSlots[a]

        except Exception as error:
            print(error)

    def __can_be_swapped(self, a: int, b: int):
        if a <= 10 and b <= 10:
            return False
        if a > 10 and b > 10:
            return True
        if a <= 10 and self.itemSlots[b] is None:
            return True
        if b <= 10 and self.itemSlots[a] is None:
            return True
        if 10 >= a == self.itemSlots[b].item_type.value and self.itemSlots[b].for_class in (None, self.className):
            return True
        if 10 >= b == self.itemSlots[a].item_type.value and self.itemSlots[a].for_class in (None, self.className):
            return True
        return False

    def dump_item(self, itemSlots_id):
        item_id = self.itemSlots[itemSlots_id].item_id
        self.__remove_from_storage(itemSlots_id)
        conn, cursor = connect_to_db()
        with conn:
            try:
                if random.randint(0, 4) != 0:
                    # you have 80% chance that duped item will be lost forever and will evaporate from existence,
                    # but there still is a chance that someone will find it dumped and pick it up.
                    cursor.execute("delete from items where item_id = %s;", (item_id,))
            except Exception as error:
                print(error)

    def __remove_from_storage(self, itemSlots_id):
        conn, cursor = connect_to_db()
        with conn:
            try:
                cursor.execute("CALL remove_from_storage(%s,%s)", (self.hero_id, itemSlots_id))
                self.itemSlots[itemSlots_id] = None
                return True
            except Exception as error:
                print(error)
                return False

    def sell_item_to_shop(self, itemSlots_id):
        earned_money = self.itemSlots[itemSlots_id].price
        if self.__remove_from_storage(itemSlots_id):
            conn, cursor = connect_to_db()
            with conn:
                try:
                    cursor.execute("update heroes set gold = gold + %s where hero_id = %s;",
                                   (earned_money, self.hero_id))
                    self.gold += earned_money
                    return True
                except Exception as error:
                    print(error)
                    return False
        return False

    def add_item(self, item: Item):
        if item is not False:
            try:
                self.add_to_storage(item)
                self.gold -= item.price
                return True
            except Exception as error:
                print(error)
                return False
        return False
