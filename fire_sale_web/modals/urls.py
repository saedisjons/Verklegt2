from django.urls import path
from . import views

app_name = 'modals'

urlpatterns = [
    #path('', views.OfferFormView.as_view(), name='modals'),
    path('', views.form_test, name='form_test')
    ]