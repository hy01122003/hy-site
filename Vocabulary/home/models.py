from django.db import models

# Create your models here.

class Account(models.Model):
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=20)
    FullName = models.CharField(max_length=30, default=" ")

