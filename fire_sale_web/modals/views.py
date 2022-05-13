from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView

# Create your views here.
from items.models import Item
from items.views import get_item_by_id
from users.models import Profile
from .models import ItemOffer
from .forms.modal_forms import OfferForm


def make_offer(request, id):
    context = {}
    item = get_object_or_404(Item, id=id)
    buyer = get_object_or_404(User, pk=request.user.id)
    owner = get_object_or_404(Profile, pk=item.user_id)
    if buyer != None:
        if request.method == "POST":
            offer_price = request.POST["offer"]
            offer = ItemOffer(item=item, buyer=buyer,owner=owner, offer=int(offer_price))
            offer.save()
            return get_item_by_id(request, id)
        return render(request, 'items/make_offer.html', context)
    else:
        return redirect('login')

class OfferFormView(FormView):
    template_name = "modals/home.html"
    form_class = OfferForm