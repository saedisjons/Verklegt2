from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999, blank=True)
    name = models.CharField(max_length=255)
    fullName = models.CharField(max_length=255, blank=True)
    year_of_start = models.DateTimeField()

    def __str__(self):
        return self.fullName


class UserImage(models.Model):
    image = models.CharField(max_length=9999)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.image