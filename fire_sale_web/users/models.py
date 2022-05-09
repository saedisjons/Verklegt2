from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class User(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    userName = models.CharField(max_length=255)
    year_of_start = models.DateTimeField()
    profile_image = models.CharField(max_length=9999, blank=True)
    fullName = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.fullName


class UserImage(models.Model):
    image = models.CharField(max_length=9999)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.image