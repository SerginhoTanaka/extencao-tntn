from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    score = models.IntegerField(default=0)
