from django.db import models

# Create your models here.

class Customer(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contact = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    cpassword = models.CharField(max_length=50)

class Queryt(models.Model):
    QueryEmail=models.CharField(max_length=200)
    Query=models.CharField(max_length=200)
    OrderId=models.CharField(max_length=200,null=True)