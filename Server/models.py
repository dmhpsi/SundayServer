from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    info = models.CharField(max_length=500, default="")
    info_time = models.BigIntegerField(default=-1)
    contacts = models.CharField(max_length=500, default="")
    contacts_time = models.BigIntegerField(default=-1)


class Feed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=1000)
