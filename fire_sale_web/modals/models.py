from django.contrib.auth.models import User
from django.db import models
from items.views import Item
from users.views import Profile

class ItemOffer(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="item_owner")
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="item_buyer")
    offer = models.FloatField(blank=False)

