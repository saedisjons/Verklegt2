from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.TextField(max_length=9999)

    def __str__(self):
        return self.user.username

class UserImage(models.Model):
    image = models.CharField(max_length=9999)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.image
