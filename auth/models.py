from django.db import models


class User(models.Model):
    username = models.CharField(primary_key=True,max_length=25)
    password = models.CharField(max_length=12)
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    bid = models.IntegerField()
    pass
