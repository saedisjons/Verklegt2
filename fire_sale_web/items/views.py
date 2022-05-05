from django.shortcuts import render, get_object_or_404
from items.

# Create your views here.

def index(request):
   context = {'items': Item.objects.all().order_by('name')}
   return render(request, 'items/index.html', context)


def get_item_by_id(request, id):
   return render(request, 'items/item_details.html', {
      'item': get_object_or_404(Item, pk=id)
   })

def list_new_item(request):
   if request.method == 'POST':
      print(1)
   else:
      print((2))