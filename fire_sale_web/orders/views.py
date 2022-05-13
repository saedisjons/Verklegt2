import json

from django.shortcuts import render, redirect

from orders.models import OrderDetails, ContactInfo, PaymentDetails, Rating
from orders.forms.order_forms import ContactInfoForm, PaymentDetailsForm, RatingForm


# Create your views here.

def index(request, orderId):
    return render(request, 'orders/index.html', {
        'orderId': orderId
    })

def process_order(request):
    orderId = request.GET.get('orderId')
    return redirect('index', orderId=orderId)
    #contactForm = ContactInfoForm()
    #return render(request, 'orders/contact_info.html', {
    #    'form': contactForm,
    #    'orderId': orderId
    #})

def index(request, orderId):
    contactForm = ContactInfoForm()
    paymentForm = PaymentDetailsForm()
    ratingForm = RatingForm()
    orderDetails = OrderDetails.objects.get(pk=orderId)

    return render(request, 'orders/index.html', {
        'orderId': orderId,
        'item': orderDetails.item,
        'contactForm': contactForm,
        'paymentForm': paymentForm,
        'ratingForm': ratingForm
    })

def contact_info(request, orderId):
    if request.method == "POST":
        contactForm = ContactInfoForm(data=request.POST)
        contactForm.instance.user = request.user
        if contactForm.is_valid():
            contactInfo = contactForm.save()
            orderDetails = OrderDetails.objects.get(pk=orderId)
            orderDetails.contactInfo = contactInfo

            orderDetails.save()

            return redirect('payment_details', orderId=orderId)
            #paymentForm = PaymentDetailsForm()
            #return render(request, 'orders/payment_details.html', {
            #    'form': paymentForm,
            #    'orderId': orderId
            #})
    else:
        contactForm = ContactInfoForm()
        return render(request, 'orders/contact_info.html', {
           'form': contactForm,
            'orderId': orderId
        })


def payment_details(request, orderId):
    if request.method == "POST":
        paymentForm = PaymentDetailsForm(data=request.POST)
        paymentForm.instance.user = request.user
        if paymentForm.is_valid():
            paymentDetails = paymentForm.save()
            orderDetails = OrderDetails.objects.get(pk=orderId)
            orderDetails.payment = paymentDetails

            orderDetails.save()

            return redirect('review_order', orderId=orderId)
            #return render(request, 'orders/confirm_order.html', {
            #    'orderId': orderId
            #})
        else:
            payment = ""
    else:
        form = PaymentDetailsForm()
        return render(request, 'orders/payment_details.html', {
           'form': form,
            'orderId': orderId
        })

def review_order(request, orderId):
    orderDetails = OrderDetails.objects.get(pk=orderId)

    return render(request, 'orders/confirm_order.html', {
        'order': orderDetails
    })


def create_order(request, itemId, buyerId):
    order = OrderDetails.objects.create(
        item_id=itemId,
        buyer_id=buyerId
    )

def confirm_order(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body_unicode_split = body_unicode.split('&')
        bodyParams = dict(s.split('=') for s in body_unicode_split)

        orderId = bodyParams.get('orderId')
        order = OrderDetails.objects.get(pk=orderId)

        contactInfo = ContactInfo.objects.create(
            streetName=bodyParams.get('streetName'),
            houseNumber=bodyParams.get('houseNumber'),
            city=bodyParams.get('city'),
            country=bodyParams.get('country'),
            postCode=bodyParams.get('postCode'),
            user=request.user
        )

        paymentDetails = PaymentDetails.objects.create(
            nameOfCardH=bodyParams.get('nameOfCardHolder'),
            cardNum=bodyParams.get('cardNumber'),
            expDate=bodyParams.get('expirationDate'),
            cvv=bodyParams.get('cvv'),
            user=request.user
        )

        rating = Rating.objects.create(
            rating=bodyParams.get('rating'),
            userBeingRated_id=bodyParams.get('sellerId'),
            userGivingRating=request.user,
            order=order
        )

        order.contactInfo = contactInfo
        order.payment = paymentDetails

        order.confirmed = True

        order.save()

        return redirect('order_confirmed', order=order)









