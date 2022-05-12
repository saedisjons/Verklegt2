from django.urls import path
from . import views

urlpatterns = [
    path('contact_info', views.contact_info, name="contact_info"),
    path('payment_details', views.payment_details, name="payment_details"),
]
