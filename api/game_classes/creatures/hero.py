from datetime import datetime, timedelta
from math import floor
from random import randint

from api.game_classes.creatures.creature import Creature
from api.game_classes.events.battle import Battle
from api.game_classes.objects.buildings.cityGuilds import CityGuilds
from api.game_classes.objects.buildings.guild import Guild
from api.game_classes.objects.buildings.market import Market
from api.game_classes.objects.buildings.shops import ArmourShop, Stable, WeaponShop, MagicShop, MercenaryShop, ShopType

from api.game_classes.objects.items.eq import Eq
from api.game_classes.objects.items.item import Item

from api.web.WebService import *


class Hero(Creature):
    def __init__(self, avatar_id, name, className, gold=0, strength=None, intelligence=None,
                 dexterity=None,
                 constitution=None, luck=None, persuasion=None, trade=None, leadership=None, protection=None,
                 initiative=None, lvl=None, exp=None, expToNextLvl=None, freeDevelopmentPts=None, hero_id=None,
                 statistics_id=None):

        Creature.__init__(self, name, className, lvl, strength, intelligence, dexterity,
                          constitution, luck, persuasion, trade, leadership, protection,
                          initiative, freeDevelopmentPts)
        self.avatar_id = avatar_id
        self.hero_id = hero_id
        self.eq = Eq(hero_id, className, gold)
        self.statistics_id = statistics_id

        self.lvl = lvl
        self.exp = exp
        self.expToNextLvl = expToNextLvl

        self.messages = None  # TODO to implement for notifications after buying selling or fights

        self.armourShop = ArmourShop(hero_id)
        self.magicShop = MagicShop(hero_id)
        self.weaponShop = WeaponShop(hero_id)
        self.stable = Stable(hero_id)  # TODO to be done in the future
        self.guild = Guild(hero_id)  # TODO to be done in the future
        self.cityGuilds = CityGuilds(hero_id)  # TODO to be done in the future
        self.market = Market(hero_id)  # TODO to be done in the future
        self.mercenaryShop = MercenaryShop(hero_id)  # TODO to be done in the future

    def __str__(self):
        return "| avatar_id: " + str(self.avatar_id) + "| hero_id: " + str(
            self.hero_id) + "| Hero name: " + self.name + "| exp: " + str(self.exp) + \
               "| exp to next lvl: " + str(self.expToNextLvl) + "| lvl: " + str(self.lvl) + " | class: " + \
               str(self.heroClass) + " |\n-----------------------\n" + \
               str(self.heroClass.statistics) + "\n-----------------------\n" + \
               str(self.eq.gearStatistics) + "\n-----------------------\n"

    def addExp(self, expOfOther):
        exp_to_add = floor(expOfOther * randint(1, 26) / 100)
        self.exp += exp_to_add
        try:
            conn, cursor = connect_to_db()
            cursor.execute("CALL add_exp(%s ,%s )", (self.hero_id, exp_to_add))
            conn.commit()
            disconnect_from_db(conn, cursor)
            if self.exp >= self.expToNextLvl:
                self.__updateAfterLvlUp()
                # TODO add some message for the user
            return True
        except Exception as error:
            print("Email already exists " + str(error))
            return False

    def add_to_statistics(self, statistic_name):
        if self.freeDevelopmentPoints > 0:
            self.freeDevelopmentPoints -= 1

            if statistic_name == 'strength':
                self.heroClass.statistics.strength += 1
            elif statistic_name == 'intelligence':
                self.heroClass.statistics.intelligence += 1
            elif statistic_name == 'dexterity':
                self.heroClass.statistics.dexterity += 1
            elif statistic_name == 'constitution':
                self.heroClass.statistics.constitution += 1
            elif statistic_name == 'luck':
                self.heroClass.statistics.luck += 1
            elif statistic_name == 'protection':
                self.heroClass.statistics.protection += 1
            elif statistic_name == 'persuasion':
                self.heroClass.statistics.persuasion += 1
            elif statistic_name == 'trade':
                self.heroClass.statistics.trade += 1
            elif statistic_name == 'leadership':
                self.heroClass.statistics.leadership += 1
            elif statistic_name == 'initiative':
                self.heroClass.statistics.initiative += 1

            try:
                conn, cursor = connect_to_db()
                statistics_update = "UPDATE statistics SET " + statistic_name + " = " + statistic_name + " + 1 WHERE statistics_id = " + \
                                    str(self.statistics_id)
                cursor.execute(statistics_update)

                heroes_update = "UPDATE heroes SET free_development_pts = free_development_pts - 1 WHERE hero_id = " + \
                                str(self.hero_id)
                cursor.execute(heroes_update)

                conn.commit()
                disconnect_from_db(conn, cursor)
                return True
            except Exception as error:
                print(error)
                return False

        return False

    def __updateAfterLvlUp(self):
        try:
            conn, cursor = connect_to_db()
            cursor.execute("SELECT exp_next_lvl from heroes where hero_id = %s", (self.hero_id,))
            conn.commit()
            self.expToNextLvl = cursor.fetchall()[0][0]
            disconnect_from_db(conn, cursor)

            self.lvl += 1
            self.freeDevelopmentPoints += 4
            return True
        except Exception as error:
            print("Email already exists: " + str(error))
            return False

    def buy_from_shop(self, item_slot_id: int, shop_type: int):
        if shop_type == ShopType.ArmourShop.value:
            bought_item = self.armourShop.buyFromShop(item_slot_id, self.eq.gold)
            result = self.eq.add_item(bought_item)

            if result:
                print("Item successfully added!")
                return True
            else:
                print("Something went wrong!")
                return False

        if shop_type == ShopType.MagicShop.value:
            bought_item = self.magicShop.buyFromShop(item_slot_id, self.eq.gold)
            result = self.eq.add_item(bought_item)

            if result:
                print("Item successfully added!")
                return True
            else:
                print("Something went wrong!")
                return False

        if shop_type == ShopType.WeaponShop.value:
            bought_item = self.weaponShop.buyFromShop(item_slot_id, self.eq.gold)
            result = self.eq.add_item(bought_item)

            if result:
                print("Item successfully added!")
                return True
            else:
                print("Something went wrong!")
                return False

        if shop_type == ShopType.Stable.value:
            bought_item = self.stable.buyFromShop(item_slot_id, self.eq.gold)
            result = self.eq.add_item(bought_item)

            if result:
                print("Item successfully added!")
                return True
            else:
                print("Something went wrong!")
                return False
        if shop_type == ShopType.MercenaryShop.value:
            print("Not implemented!")
            return False
        print("Incorrect shop type")
        return False

    def init_fight_with_other_hero(self, enemy):
        # returns battle_logs,winner.hero_id
        return Battle.hero_vs_hero(self, enemy)

    def get_statistics(self):
        return self.heroClass.statistics + self.eq.gearStatistics

    def update_model_from_db(self):
        pass  # TODO - get whole current hero model in order to synchronize the game

    def add_to_buy_now_items(self, item_slot_id: int, price: int):
        item: Item = self.eq.itemSlots[item_slot_id]
        if item.available == 1:
            self.market.add_to_buy_now_items(item, price)
            item.available = 0
            return True
        return False

    def add_to_auctioned_items(self, item_slot_id: int, price: int,
                               auction_end_date: datetime = datetime.now() + timedelta(days=7)):
        item: Item = self.eq.itemSlots[item_slot_id]
        if item.available == 1:
            self.market.add_to_auctioned_items(item, price, auction_end_date)
            item.available = 0
            return True
        return False

    def buy_now_item(self, item_slot_id: int):
        item_price: int = self.market.buy_now_items[item_slot_id].price
        if self.eq.gold >= item_price:
            self.market.buy_now_item(item_slot_id)
            self.eq.gold -= item_price
            return True
        return False

    def place_bet(self, item_slot_id: int, bet: int):
        if self.eq.gold >= bet > self.market.auctioned_items[item_slot_id].current_price:
            return self.market.place_bet(item_slot_id, bet)
        return False
