from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from items.forms.item_forms import ItemCreateForm, ItemUpdateForm
from items.models import Item, ItemImage, ItemCategory


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET('search_filter')
        items = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.itemImage_set.first().image
        } for x in Item.objects.filter(name_icontains=search_filter)]
        return JsonResponse({ 'data': items })
    context = {'items': Item.objects.all().order_by('name'), 'categories': ItemCategory.objects.all()}
    return render(request, 'items/index.html', context)

#/items/3
@login_required
def get_item_by_id(request, id):
    return render(request, 'items/item_details.html', {
        'item': get_object_or_404(Item, pk=id)
    })

@login_required
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

@login_required
def delete_item(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('items-index')

@login_required
def update_item(request, id):
    instance = get_object_or_404(Item, pk=id)
    if request.method == "POST":
        form = ItemUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/items/item_details.html', id=id)
    else:
        form = ItemUpdateForm(instance=instance)
    return render(request, 'items/update_item.html', {
        'form': form,
        'id': id
    })

