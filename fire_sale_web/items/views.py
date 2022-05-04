from django.shortcuts import render
from items.models import Item
from items.itemLogic import ItemLogic

# Create your views here.
def index(request):
    items = ItemLogic.getItem()
    context = {'items': items}
    return render(request, 'items/index.html', context)