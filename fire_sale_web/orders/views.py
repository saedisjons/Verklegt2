from django.shortcuts import render, redirect

from forms.contact_info_form import ContactInfoForm
from forms.payment_details_form import PaymentDetailsForm

# Create your views here.


def contact_info(request):
    if request.method == "POST":
        form = ContactInfoForm(data=request.POST)
        if form.is_valid():
            form.save()
            payment_details_form = PaymentDetailsForm()
            return render(request, 'orders/payment_details.html', {
                'form': form
            })
    else:
        form = ContactInfoForm()
        return render(request, 'orders/contact_info.html', {
           'form': form
        })


def payment_details(request):
    form = PaymentDetailsForm()
    return render(request, 'orders/payment_details.html', {
       'form': form
    })
