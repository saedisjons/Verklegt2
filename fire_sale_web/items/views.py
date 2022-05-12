from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from items.forms.item_forms import ItemCreateForm, ItemUpdateForm
from items.models import Item, ItemImage, Categories, CategoryItems, ItemOffer


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
    context = {'items': Item.objects.all().order_by('name'), 'categories': Categories.objects.all()}
    return render(request, 'items/index.html', context)


def category_all_pages(request):
    return {'allCategories': Categories.objects.all()}

#/items/3
def get_item_by_id(request, id):
    return render(request, 'items/item_details.html', {
        'item': get_object_or_404(Item, pk=id)
    })


def get_item_by_category(request, id):
    return render(request, 'items/item_category_details.html', {
        'items': Item.objects.all().filter(category=id),
        'categories': Categories.objects.get(id=id).name
    })

@login_required
def create_item(request):
    if request.method == "POST":
        form = ItemCreateForm(data=request.POST)
        if form.is_valid():
            item = form.save()
            item_image = ItemImage(image=request.POST['image'], item=item)
            item_image.save()
            categories = Categories(name=request.POST['category'])
            category_items = CategoryItems(category=categories, item=item)
            category_items.save()
            return redirect("items-index")
    else:
        form = ItemCreateForm()
    return render(request, 'items/create_item.html', {
       'form': form
    })

@login_required
def delete_item(request, id):
    context = {}
    item = get_object_or_404(Item, id=id)
    if request.method == "POST":
        item.delete()
        return redirect('items-index')
    return render(request, 'items/delete_item.html', context)

@login_required
def update_item(request, id):
    instance = get_object_or_404(Item, pk=id)
    if request.method == "POST":
        form = ItemUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            item = form.save()
            item_image = ItemImage(image=request.POST['image'], item=item)
            item_image.save()
            return get_item_by_id(request, id)
    else:
        form = ItemUpdateForm(instance=instance)
    return render(request, 'items/update_item.html', {
        'form': form,
        'id': id
    })

def make_offer(request, id):
    context = {}
    buyer = request.user.id
    if buyer == None:
        return redirect('login')
    else:
        item = get_object_or_404(Item, id=id)
        if request.method == "POST":
            offer = request.POST['offer']
            # check if number is valid (not empty and no spaces before or after)
            if not offer.strip():
                offer = ItemOffer(item=item, buyer=buyer, offer=offer)
                offer.save()
                return render(request, 'items/item_details.html', {})
            else:
                messages.success(request, ('Seems Like There Was An Error...'))
        return render(request, 'items/make_offer.html', context)