from django.db import models
from users.models import User

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.FloatField()
    on_sale = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=False)

    def __str__(self):
        return self.name

class ItemImage(models.Model):
    image = models.CharField(max_length=9999)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.image


class CategoryItems(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=None,blank=True)

    def __str__(self):
        return self.item
