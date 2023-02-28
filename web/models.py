
from django.db import models


# Create your models here.


class Subscription(models.Model):
    usertype = models.CharField(max_length=50)
    price = models.IntegerField()
    is_active = models.BooleanField()
    plan = models.CharField(max_length=25)

    def __str__(self):
        return self.usertype


class UserDetails(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    contact = models.CharField(max_length=12)
    subscription = models.ForeignKey(Subscription, related_name='subscription', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="img/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField(max_length=250, null=True)
    image = models.ImageField(upload_to="img/")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.description



