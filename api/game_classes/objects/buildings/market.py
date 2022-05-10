import string
from datetime import datetime, timedelta
from typing import List

from api.game_classes.objects.items.item import Item, ItemType
from api.web.WebService import connect_to_db, disconnect_from_db


class BuyNowItem:
    def __init__(self, item: Item, seller_id: int, price: int):
        self.item = item
        self.seller_id = seller_id
        self.price = price

    def __str__(self):
        return '----------------------\nSeller_id: ' + str(self.seller_id) + '\nprice: ' + \
               str(self.price) + "\n" + str(self.item)


class AuctionedItem:
    def __init__(self, item: Item, seller_id: int, start_price: int, current_price: int, auction_end_date: datetime,
                 leader: int or None):
        self.item = item
        self.seller_id = seller_id
        self.start_price = start_price
        self.current_price = current_price
        self.auction_end_date = auction_end_date
        self.leader = leader

    def __str__(self):
        return '----------------------\nSeller_id: ' + str(self.seller_id) + '\nstart_price: ' + \
               str(self.start_price) + '\ncurrent_price: ' + str(self.current_price) + \
               '\nauction_end_date: ' + str(self.auction_end_date) + '\nleader_id: ' + str(self.leader) + "\n" + str(
            self.item)


class Filters:
    def __init__(self, name: string or None = None, item_type: List[int] or None = None, min_price: int or None = None,
                 max_price: int or None = None, for_class: List[string] or None = None):
        self.name = name
        self.item_type = item_type
        self.min_price = min_price
        self.max_price = max_price
        self.for_class = for_class


class Market:
    def __init__(self, hero_id):
        self.hero_id: int = hero_id
        self.buy_now_items = None
        self.auctioned_items = None
        self.filters = {}  # TODO IMPLEMENT ME
        self.__load_buy_now_items()
        self.__load_auctioned_items()
        self.filters = Filters()

    def __load_auctioned_items(self):
        transaction_status = None
        self.auctioned_items = []
        try:
            conn, cursor = connect_to_db()
            cursor.execute(
                "SELECT item_id,seller_id,start_price,current_price,auction_end_date,current_leader_id from auctioned_items")
            result: List = cursor.fetchall()

            for i in result:
                item_id = i[0]
                cursor.execute(Item.all_info_select(item_id))
                built_item: Item = Item.build_item(item_id, cursor.fetchall()[0])
                ai: AuctionedItem = AuctionedItem(built_item, i[1], i[2], i[3], i[4], i[5])
                self.auctioned_items.append(ai)

            disconnect_from_db(conn, cursor)
            transaction_status = True
        except Exception as error:
            transaction_status = False
            print(error)
        finally:
            return transaction_status

    def __load_buy_now_items(self):
        transaction_status = None
        self.buy_now_items = []
        try:
            conn, cursor = connect_to_db()
            cursor.execute(
                "SELECT item_id,seller_id,selling_price from buy_now_items")
            result: List = cursor.fetchall()

            for i in result:
                item_id = i[0]
                cursor.execute(Item.all_info_select(item_id))
                built_item: Item = Item.build_item(item_id, cursor.fetchall()[0])
                bni: BuyNowItem = BuyNowItem(built_item, i[1], i[2])
                self.buy_now_items.append(bni)

            disconnect_from_db(conn, cursor)
            transaction_status = True
        except Exception as error:
            transaction_status = False
            print(error)
        finally:
            return transaction_status

    def add_to_buy_now_items(self, item: Item, price: int):
        new = BuyNowItem(item, self.hero_id, price)
        transaction_status = None
        try:
            conn, cursor = connect_to_db()
            cursor.execute("call add_new_item_on_sale(%s,%s,%s,%s,%s);",
                           (item.item_id, self.hero_id, price, 'buy_now', None))
            conn.commit()
            disconnect_from_db(conn, cursor)
            transaction_status = True
            self.buy_now_items.append(new)
        except Exception as error:
            transaction_status = False
            print(error)
        finally:
            return transaction_status

    def add_to_auctioned_items(self, item: Item, price: int,
                               auction_end_date: datetime):
        new = AuctionedItem(item, self.hero_id, price, price, auction_end_date, None)
        transaction_status = None
        try:
            conn, cursor = connect_to_db()
            cursor.execute("call add_new_item_on_sale(%s,%s,%s,%s,%s);",
                           (item.item_id, self.hero_id, price, 'auction', auction_end_date))
            conn.commit()
            disconnect_from_db(conn, cursor)
            transaction_status = True
            self.auctioned_items.append(new)
        except Exception as error:
            transaction_status = False
            print(error)
        finally:
            return transaction_status

    def buy_now_item(self, id_in_list: int):
        transaction_status = None
        bni: BuyNowItem = self.buy_now_items[id_in_list]
        try:
            conn, cursor = connect_to_db()
            cursor.execute("call buy_now(%s,%s,%s);", (self.hero_id, bni.item.item_id, bni.seller_id))
            conn.commit()
            disconnect_from_db(conn, cursor)
            transaction_status = True
        except Exception as error:
            transaction_status = False
            print(error)
        finally:
            return bni if transaction_status else transaction_status

    def place_bet(self, id_in_list: int, bet: int):
        transaction_status = None
        ai: AuctionedItem = self.auctioned_items[id_in_list]
        try:
            conn, cursor = connect_to_db()
            cursor.execute("select place_bet(%s,%s,%s,%s)", (ai.item.item_id, ai.seller_id, bet, self.hero_id))
            transaction_status = True if cursor.fetchone()[0] == "SUCCESS" else False  # todo may not work
            conn.commit()
            disconnect_from_db(conn, cursor)
        except Exception as error:
            transaction_status = False
            print(error)
        finally:
            return transaction_status
