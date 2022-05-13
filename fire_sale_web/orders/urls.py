from django.urls import path
from . import views

urlpatterns = [
    path('<int:orderId>', views.index, name="index"),
    path('contact_info/<int:orderId>', views.contact_info, name="contact_info"),
    path('payment_details/<int:orderId>', views.payment_details, name="payment_details"),
    path('process_order', views.process_order, name="process_order"),
    path('review_order/<int:orderId>', views.review_order, name="review_order"),
    path('confirm_order', views.confirm_order, name="confirm_order"),
    path('create_order/<int:itemId>/<int:buyerId>', views.create_order, name="create_order")
]
