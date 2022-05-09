from django.db import models


# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=255)
    fullName = models.CharField(max_length=255)
    year_of_start = models.DateTimeField()

    def __str__(self):
        return self.fullName


class UserImage(models.Model):
    image = models.CharField(max_length=9999)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.image