from django.db import models

# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
class Buy(models.Model):
    product_name= models.CharField(max_length=255)
    price = models.CharField(max_length=20)
    email = models.EmailField()