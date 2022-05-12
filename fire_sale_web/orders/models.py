from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class ContactInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    streetName = models.TextField(max_length=255)
    houseNumber = models.TextField(max_length=255)
    city = models.TextField(max_length=255)
    country = models.TextField(max_length=255)
    postCode = models.IntegerField()


class PaymentDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nameOfCardH = models.TextField(max_length=255)
    cardNum = models.IntegerField()
    expDate = models.DateField()
