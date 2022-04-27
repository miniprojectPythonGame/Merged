from backend.src.game_classes.objects.items.soldItem import SoldItem


class Market:
    def __init__(self, hero_id):
        self.hero_id = hero_id
        self.soldItems = []

    def sellItem(self, name, price, description, ownerUID, amount):
        newSoldItem = SoldItem(self, name, price, description, ownerUID, amount)
        # TODO add pushing to database

    def showItemsSoldByUser(self, ownerUID):
        pass  # TODO get items from DB

    def stopSellingItem(self, itemID, ownerUID, amount):
        pass  # TODO stop selling amount of item: can be 2 from 10 or 3 from 3

    def buyItem(self, itemID):
        pass  # give money from buyer to seller and invoke stopSellingItem
