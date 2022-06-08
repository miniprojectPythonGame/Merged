import string
from datetime import datetime, timedelta

from api.game_classes.creatures.creature import Creature
from api.game_classes.events.battle import Battle
from api.game_classes.objects.buildings.cityGuilds import CityGuilds
from api.game_classes.objects.buildings.guild import Guild
from api.game_classes.objects.buildings.market import Market
from api.game_classes.objects.buildings.shops import ArmourShop, Stable, WeaponShop, MagicShop, MercenaryShop

from api.game_classes.objects.items.eq import Eq
from api.game_classes.objects.items.item import Item
from api.game_classes.objects.quests import QuestList, Quest
from api.game_classes.properties.enums import ShopType

from api.web.WebService import *


class Hero(Creature):
    def __init__(self, avatar_id: int, name: string, className: string, gold: int = 0, strength: int = 0,
                 intelligence: int = 0,
                 dexterity: int = 0,
                 constitution: int = 0, luck: int = 0, persuasion: int = 0, trade: int = 0, leadership: int = 0,
                 protection: int = 0,
                 initiative: int = 0, lvl: int = 0, exp: int = 0, expToNextLvl: int = 0, freeDevelopmentPts: int = 4,
                 hero_id: int or None = None,
                 statistics_id: int or None = None):

        Creature.__init__(self, name, className, lvl, strength, intelligence, dexterity,
                          constitution, luck, persuasion, trade, leadership, protection,
                          initiative, freeDevelopmentPts)

        self.avatar_id = avatar_id
        self.hero_id = hero_id

        self.eq = None
        # self.eq = Eq(hero_id, className, gold)

        self.statistics_id = statistics_id

        self.lvl = lvl
        self.exp = exp
        self.expToNextLvl = expToNextLvl

        self.messages = None  # TODO to implement for notifications after buying selling or fights

        self.quests = None
        # self.quests = QuestList(self.hero_id, self.lvl)

        self.armourShop = None
        # self.armourShop = ArmourShop(hero_id)

        self.magicShop = None
        # self.magicShop = MagicShop(hero_id)

        self.weaponShop = None
        # self.weaponShop = WeaponShop(hero_id)

        # TODO not implemented in frontend but in waiting
        self.market = None
        self.stable = None

        # TODO just not implemented
        self.guild = Guild(hero_id)  # TODO to be done in the future
        self.cityGuilds = CityGuilds(hero_id)  # TODO to be done in the future
        self.mercenaryShop = MercenaryShop(hero_id)  # TODO to be done in the future

    def __str__(self):
        return f'avatar_id:{self.avatar_id}\n' \
               f'hero_id:{self.hero_id}\n' \
               f'name:{self.name}\n' \
               f'gold:{self.eq.gold}\n' \
               f'exp:{self.exp}\n' \
               f'exp_to_next_lvl:{self.expToNextLvl}\n' \
               f'lvl:{self.lvl}\n' \
               f'class:{self.fight_class}\n' \
               f'\n-----------------------\n' \
               f'{self.fight_class.statistics}' \
               f'\n-----------------------\n' \
               f'{self.eq.gearStatistics}' \
               f'\n-----------------------\n'

    def add_exp(self, exp_to_add):
        self.exp += exp_to_add
        try:
            conn, cursor = connect_to_db()
            with conn:
                cursor.execute("CALL add_exp(%s ,%s )", (self.hero_id, exp_to_add))
                if self.exp >= self.expToNextLvl:
                    self.__updateAfterLvlUp()
                    # TODO add some message for the user
                return True
        except Exception as error:
            print(error)
            return False

    def add_to_statistics(self, statistic_name):
        if self.freeDevelopmentPoints > 0:
            self.freeDevelopmentPoints -= 1

            if statistic_name == 'strength':
                self.fight_class.statistics.strength += 1
            elif statistic_name == 'intelligence':
                self.fight_class.statistics.intelligence += 1
            elif statistic_name == 'dexterity':
                self.fight_class.statistics.dexterity += 1
            elif statistic_name == 'constitution':
                self.fight_class.statistics.constitution += 1
            elif statistic_name == 'luck':
                self.fight_class.statistics.luck += 1
            elif statistic_name == 'protection':
                self.fight_class.statistics.protection += 1
            elif statistic_name == 'persuasion':
                self.fight_class.statistics.persuasion += 1
            elif statistic_name == 'trade':
                self.fight_class.statistics.trade += 1
            elif statistic_name == 'leadership':
                self.fight_class.statistics.leadership += 1
            elif statistic_name == 'initiative':
                self.fight_class.statistics.initiative += 1

            try:
                conn, cursor = connect_to_db()
                with conn:
                    statistics_update = "UPDATE statistics SET " + statistic_name + " = " + statistic_name + " + 1 WHERE statistics_id = " + \
                                        str(self.statistics_id)
                    cursor.execute(statistics_update)

                    heroes_update = "UPDATE heroes SET free_development_pts = free_development_pts - 1 WHERE hero_id = " + \
                                    str(self.hero_id)
                    cursor.execute(heroes_update)

                    return True
            except Exception as error:
                print(error)
                return False

        return False

    def __updateAfterLvlUp(self):
        try:
            conn, cursor = connect_to_db()
            with conn:
                cursor.execute("SELECT exp_next_lvl from heroes where hero_id = %s", (self.hero_id,))
                self.expToNextLvl = cursor.fetchone()[0]
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
        """
        :param enemy: Hero class instance
        :return: (battle_logs,winner.hero_id) - battle logs look like list of such tuples (<hero_id of hero that attacked>,<dmg dealt>) and winner.hero_id is self-explanatory
        """
        return Battle.hero_vs_hero(self, enemy)

    def get_statistics(self):
        return self.fight_class.statistics + self.eq.gearStatistics

    def update_model_from_db(self):
        pass  # TODO - get whole current hero model in order to synchronize the game

    def add_to_buy_now_items(self, item_slot_id: int, price: int):
        item: Item or None = self.eq.itemSlots[item_slot_id]
        if item is not None and item.available == 1:
            self.market.add_to_buy_now_items(item, price)
            item.available = 0
            return True
        return False

    def add_to_auctioned_items(self, item_slot_id: int, price: int,
                               auction_end_date: datetime = datetime.now() + timedelta(days=7)):
        item: Item or None = self.eq.itemSlots[item_slot_id]
        if item is not None and item.available == 1:
            self.market.add_to_auctioned_items(item, price, auction_end_date)
            item.available = 0
            return True
        return False

    def buy_now_item(self, id_in_list: int):
        item_price: int = self.market.buy_now_items[id_in_list].price
        if self.eq.gold >= item_price:
            self.market.buy_now_item(id_in_list)
            self.eq.gold -= item_price
            return True
        return False

    def place_bet(self, id_in_list: int, bet: int):
        if self.eq.gold >= bet > self.market.auctioned_items[id_in_list].current_price:
            return self.market.place_bet(id_in_list, bet)
        return False

    def fight_with_bot_from_quest(self, quest_id_in_list: int):
        quest: Quest = self.quests.quest_list[quest_id_in_list]
        battle_logs, creature_id = Battle.hero_vs_bot(self, quest.enemy)
        if creature_id == -1:  # bot won - he does not have hero_id so -1 is returned
            return False
        else:
            item_id = Item.add_item_to_db(quest.treasure)
            Item.add_item_to_hero_storage(self.hero_id, item_id)
            quest.treasure.item_id = item_id
            self.eq.add_to_storage(quest.treasure)
            _, exp, gold = quest.add_prizes(self.hero_id, self.lvl)
            self.eq.gold += gold
            self.add_exp(exp)
            return True

    def get_gold(self):
        conn, cursor = connect_to_db()
        with conn:
            cursor.execute("SELECT gold from heroes where hero_id = %s", (self.hero_id,))
        gold = cursor.fetchone()[0]
        return gold

    def gen_quests(self):
        self.quests = QuestList(self.hero_id, self.lvl)

    def gen_armour_shop(self):
        self.armourShop = ArmourShop(self.hero_id)

    def gen_magic_shop(self):
        self.magicShop = MagicShop(self.hero_id)

    def gen_weapon_shop(self):
        self.weaponShop = WeaponShop(self.hero_id)

    def gen_market(self):
        self.market = Market(self.hero_id)

    def gen_stable(self):
        self.stable = Stable(self.hero_id)

    def gen_eq(self):
        self.eq = Eq(self.hero_id, self.fight_class, self.get_gold())
