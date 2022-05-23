import string
from abc import ABC
from typing import List

from api.game_classes.objects.items.item import Item
from api.web.WebService import connect_to_db


class Shop(ABC):
    def __init__(self, hero_id: int):
        self.itemList: List[Item] = []
        self.hero_id: int = hero_id
        self.shop_name_in_db: string = ""

    def buyFromShop(self, item_slot_id: int, money: int):
        if money >= self.itemList[item_slot_id].price:
            try:
                conn, cursor = connect_to_db()
                with conn:
                    call = "CALL sell_item_from_" + self.shop_name_in_db + "(%s,%s)"
                    cursor.execute(call,
                                   (self.hero_id, self.itemList[item_slot_id].item_id))
                    conn.commit()

                    select = "SELECT item_id from " + self.shop_name_in_db + " where hero_id = %s and item_slot_id = %s"

                    cursor.execute(select, (self.hero_id, item_slot_id))

                    new_id = cursor.fetchone()[0]
                    print(new_id)
                    bought_item = self.itemList[item_slot_id]
                    print(self.itemList[item_slot_id].item_id)
                    if new_id is not None:
                        cursor.execute(Item.all_info_select(new_id))
                        self.itemList[item_slot_id] = Item.build_item(self.itemList[item_slot_id].item_id,
                                                                      cursor.fetchone())
                    return bought_item
            except Exception as error:
                print(error)
                return False
        return False

    def get_shop_items(self):
        self.itemList = []
        try:
            conn, cursor = connect_to_db()
            with conn:
                select = "SELECT item_id from " + self.shop_name_in_db + " where hero_id = " + str(
                    self.hero_id) + " order by item_slot_id desc;"
                cursor.execute(select)

                item_ids = cursor.fetchall()
                for i in item_ids:
                    item_id = i[0]
                    if item_id is not None:
                        cursor.execute(Item.all_info_select(item_id))
                        self.itemList.append(Item.build_item(item_id, cursor.fetchall()[0]))
        except Exception as error:
            print(error)

    def refresh(self):
        self.itemList = []
        try:
            conn, cursor = connect_to_db()
            with conn:
                call = "CALL refresh_" + self.shop_name_in_db + "_for_hero(" + str(self.hero_id) + ");"
                cursor.execute(call)
        except Exception as error:
            print(error)

        self.get_shop_items()

    def __str__(self):
        items: string = f'{type(self).__name__}\n'
        for item in self.itemList:
            items += f'{item}\n'
        return items


class ArmourShop(Shop):
    def __init__(self, hero_id: int):
        Shop.__init__(self, hero_id)
        self.shop_name_in_db = "armour_shop"
        self.get_shop_items()


class MagicShop(Shop):
    def __init__(self, hero_id: int):
        Shop.__init__(self, hero_id)
        self.shop_name_in_db = "magic_shop"
        self.get_shop_items()


class MercenaryShop(Shop):
    def __init__(self, hero_id: int):
        Shop.__init__(self, hero_id)
        self.shop_name_in_db = "???"  # TODO add table in db later
        # self.get_shop_items()
        pass


class Stable(Shop):
    def __init__(self, hero_id: int):
        Shop.__init__(self, hero_id)
        self.shop_name_in_db = "steed_shop"
        self.get_shop_items()


class WeaponShop(Shop):
    def __init__(self, hero_id: int):
        Shop.__init__(self, hero_id)
        self.shop_name_in_db = "weapon_shop"
        self.get_shop_items()

