from django.db import models


# Create your models here.
class Users(models.Model):
    fullname = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    yearofbirth = models.DateField(default=2)


def __str__(self):
    return self.fullname


class Products(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.CharField(max_length=200)
    product_quantity = models.IntegerField()

    def __str__(self):
        return self.product_name


class Member(models.Model):
    Username = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=30)

    def __str__(self):
        return self.Username


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name


class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
