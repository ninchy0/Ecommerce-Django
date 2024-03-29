from home.models import *
from django.db import models

# Create your models here.
class Cart(models.Model):
    username = models.CharField(max_length=500)
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    slug = models.CharField(max_length=300)
    quantity = models.IntegerField(default=1)
    total = models.IntegerField()
    checkout = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=400)
    subject = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self):
        return self.name


class Checkout(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.CharField(max_length=300)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.f_name} {self.l_name}'