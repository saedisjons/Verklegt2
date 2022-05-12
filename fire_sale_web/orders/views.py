from django.shortcuts import render, redirect
from forms.order_forms import ContactInfoForm, PaymentDetailsForm

# Create your views here.

def contact_info(request):
    if request.method == "POST":
        contactForm = ContactInfoForm(data=request.POST)
        if contactForm.is_valid():
            contactForm.save()
            paymentForm = PaymentDetailsForm()
            return render(request, 'orders/payment_details.html', {
                'form': paymentForm
            })
    else:
        contactForm = ContactInfoForm()
        return render(request, 'orders/contact_info.html', {
           'form': contactForm
        })


def payment_details(request):
    form = PaymentDetailsForm()
    return render(request, 'orders/payment_details.html', {
       'form': form
    })
