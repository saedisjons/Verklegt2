from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView

# Create your views here.
from items.models import Item
from items.views import get_item_by_id
from users.models import Profile
from .models import ItemOffer
from .forms.modal_forms import OfferForm

def form_test(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    context = {}
    buyer = get_object_or_404(User, pk=request.user.id)
    if is_ajax and buyer != None:
        if request.method == "POST":
            offer_price = request.POST['offer']
            item_id = request.POST['itemId']
            item = get_object_or_404(Item, id=item_id)
            owner = get_object_or_404(User, pk=item.user_id)
            offer = ItemOffer(item=item, buyer=buyer,owner=owner, offer=int(offer_price))
            offer.save()
            return get_item_by_id(request, item_id)
        return render(request, 'modals/modalsBase.html')
    else:
        return redirect('login')

#class OfferFormView(FormView):
 #   template_name = "modals/modalsBase.html"
  #  form_class = make_offer

def form_testt(request, *args, **kwargs):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    form = OfferForm()
    data = {}
    buyer = get_object_or_404(User, pk = request.user.id)
    if is_ajax:
        form = OfferForm(request.POST)
        if form.is_valid():
            data['offer'] = form.cleaned_data.get('offer')
            data['status'] = 'ok'
            data['buyer'] = buyer
            new_offer = ItemOffer(
                offer = data['offer'],
                buyer = data['buyer']
            )
            new_offer.save()
            return JsonResponse(data)
        else:
            data['status'] = 'error'
            return JsonResponse(data)
    context = {
        'form':form
    }
    return render(request, 'modals/modalsBase.html', context)