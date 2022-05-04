from items.models import Item


class ItemLogic:

    def getItem():
        for item in Item.objects.raw('SELECT * FROM items_item'):
            return item
