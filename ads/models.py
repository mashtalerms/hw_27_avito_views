from django.db import models


class Ad(models.Model):                       # Ads model
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)


class Category(models.Model):               # Categories model
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
