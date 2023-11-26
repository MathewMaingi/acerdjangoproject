from django.db import models

# Create your models here.
# Table for employee details.
class employee(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=10)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.firstname+" "+self.lastname
class product(models.Model):
    productid = models.IntegerField(default=8)
    productname = models.CharField(max_length=50)
    productprice = models.IntegerField(default=0)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.productname

class Member(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField()
    username =models.CharField(max_length=15)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.firstname+""+self.lastname

class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.TextField()
    origin = models.CharField(max_length=50, default='Kenya')
    color = models.CharField(max_length=50, default='White')
    #image = models.ImageField()

    def __str__(self):
        return  self.name
class ImageModel(models.Model):
    image = models.ImageField(upload_to='(images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.title