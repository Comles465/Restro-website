from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Restro(models.Model):
    firstnm=models.CharField(max_length=100)
    lastnm=models.CharField(max_length=100)
    email=models.EmailField()
    what=models.CharField(max_length=250)
    phone=PhoneNumberField(blank=True)
    message=models.TextField(null=True)
    
class Buff(models.Model):
    title=models.CharField(max_length=200)
    price=models.IntegerField()
    image=models.ImageField(upload_to='image')
    
class Chicken(models.Model):
    title=models.CharField(max_length=200)
    price=models.IntegerField()
    image=models.ImageField(upload_to='image')
    
class Veg(models.Model):
    title=models.CharField(max_length=200)
    price=models.IntegerField()
    image=models.ImageField(upload_to='image')