from backend.src.game_classes.objects.items.item import Item


class SoldItem(Item):
    def __init__(self, name, price, description, ownerUID, amount, onlyTreasure=False):
        Item.__init__(self, name, price, description, onlyTreasure)
        self.ownerUID = ownerUID
        self.amount = amount
