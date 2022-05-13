from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from items.models import Item


class ContactInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    streetName = models.TextField(max_length=255)
    houseNumber = models.TextField(max_length=255)
    city = models.TextField(max_length=255)
    country = models.TextField(max_length=255)
    postCode = models.IntegerField()


class PaymentDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nameOfCardH = models.TextField(max_length=255)
    cardNum = models.TextField(max_length=255)
    expDate = models.DateField()
    cvv = models.TextField(max_length=255, default=None, blank=True, null=True)


class OrderDetails(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    payment = models.OneToOneField(PaymentDetails, null=True, blank=True, on_delete=models.DO_NOTHING)
    contactInfo = models.OneToOneField(ContactInfo, null=True, blank=True, on_delete=models.DO_NOTHING)
    rating = models.IntegerField(default=None, blank=True, null=True)
    confirmed = models.BooleanField(default=False)

class Rating(models.Model):
    userBeingRated = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_being_rated")
    userGivingRating = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_giving_rating")
    order = models.ForeignKey(OrderDetails, on_delete=models.CASCADE, related_name="order_rating")
    rating = models.IntegerField()

