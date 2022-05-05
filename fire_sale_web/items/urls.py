from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:800/items
    path('', views.index, name="users-index"),
]