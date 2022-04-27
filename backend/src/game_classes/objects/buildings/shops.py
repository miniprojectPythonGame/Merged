from abc import ABC
from enum import Enum

from backend.src.game_classes.objects.items.item import ItemBuilder
from backend.src.web.WebService import connect_to_db, disconnect_from_db


class Shop(ABC):
    def __init__(self, hero_id):
        self.itemList = []
        self.hero_id = hero_id
        self.shop_name_in_db = ""

    def buyFromShop(self, item_slot_id: int, money: int):
        if money >= self.itemList[item_slot_id].price:
            try:
                conn, cursor = connect_to_db()
                call = "CALL sell_item_from_" + self.shop_name_in_db + "(%s,%s)"
                cursor.execute(call,
                               (self.hero_id, self.itemList[item_slot_id].item_id))
                conn.commit()

                select = "SELECT item_id from " + self.shop_name_in_db + " where hero_id = %s and item_slot_id = %s"

                cursor.execute(select, (self.hero_id, item_slot_id))

                new_id = cursor.fetchall()[0][0]
                print(new_id)
                bought_item = self.itemList[item_slot_id]
                print(self.itemList[item_slot_id].item_id)
                if new_id is not None:
                    cursor.execute(ItemBuilder.all_info_select(new_id))
                    self.itemList[item_slot_id] = ItemBuilder.build_item(self.itemList[item_slot_id].item_id,
                                                                         cursor.fetchall()[0])
                disconnect_from_db(conn, cursor)
                return bought_item
            except Exception as error:
                print(error)
                return False
        return False

    def get_shop_items(self):
        self.itemList = []
        try:
            conn, cursor = connect_to_db()
            select = "SELECT item_id from " + self.shop_name_in_db + " where hero_id = " + str(
                self.hero_id) + " order by item_slot_id desc;"
            cursor.execute(select)

            item_ids = cursor.fetchall()
            for i in item_ids:
                item_id = i[0]
                if item_id is not None:
                    cursor.execute(ItemBuilder.all_info_select(item_id))
                    self.itemList.append(ItemBuilder.build_item(item_id, cursor.fetchall()[0]))
            disconnect_from_db(conn, cursor)
        except Exception as error:
            print(error)

    def refresh(self):
        self.itemList = []
        try:
            conn, cursor = connect_to_db()
            call = "CALL refresh_" + self.shop_name_in_db + "_for_hero(" + str(self.hero_id) + ");"
            cursor.execute(call)
            conn.commit()
            disconnect_from_db(conn, cursor)
        except Exception as error:
            print(error)

        self.get_shop_items()

    def print(self):
        print(type(self).__name__)
        for i in self.itemList:
            print(i)


class ArmourShop(Shop):
    def __init__(self, hero_id):
        Shop.__init__(self, hero_id)
        self.shop_name_in_db = "armour_shop"
        self.get_shop_items()


class ShopType(Enum):
    ArmourShop = 0
    MagicShop = 1
    MercenaryShop = 2
    Stable = 3
    WeaponShop = 4


class MagicShop(Shop):
    def __init__(self, hero_id):
        Shop.__init__(self, hero_id)
        self.shop_name_in_db = "magic_shop"
        self.get_shop_items()


class MercenaryShop(Shop):
    def __init__(self, hero_id):
        Shop.__init__(self, hero_id)
        self.shop_name_in_db = "???"  # TODO add table in db later
        # self.get_shop_items()
        pass


class Stable(Shop):
    def __init__(self, hero_id):
        Shop.__init__(self, hero_id)
        self.shop_name_in_db = "steed_shop"
        self.get_shop_items()


class WeaponShop(Shop):
    def __init__(self, hero_id):
        Shop.__init__(self, hero_id)
        self.shop_name_in_db = "weapon_shop"
        self.get_shop_items()
