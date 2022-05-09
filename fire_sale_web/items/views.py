from django.shortcuts import render, get_object_or_404, redirect
from forms.item_forms import ItemCreateForm
from models import Item, ItemImage

# Create your views here.


def index(request):
    context = {'items': Item.objects.all().order_by('name')}
    return render(request, 'items/index.html', context)


def get_item_by_id(request, id):
    return render(request, 'items/item_details.html', {
        'item': get_object_or_404(Item, pk=id)
    })


def create_item(request):
    if request.method == "POST":
        form = ItemCreateForm(data=request.POST)
        if form.is_valid():
            item = form.save()
            item_image = ItemImage(image=request.POST['image'], item=item)
            item_image.save()
            return redirect("items-index")
    else:
        form = ItemCreateForm()
    return render(request, 'items/create_item.html', {
       'form': form
    })
