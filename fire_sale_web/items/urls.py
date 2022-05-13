from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="items-index"),
    path('<int:id>', views.get_item_by_id, name="item-details"),
    path('create_item', views.create_item, name="create_item"),
    path('delete_item/<int:id>', views.delete_item, name="delete_item"),
    path('update_item/<int:id>', views.update_item, name="update_item"),
    path('item_category/<int:id>', views.get_item_by_category, name="item_category"),
    path('my_items/<int:id>', views.get_item_by_user_id, name="my_items")
]
