from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='Catalog/images/')
    image2 = models.ImageField(upload_to='Catalog/images/', blank=True)
    image3 = models.ImageField(upload_to='Catalog/images/', blank=True)
    image4 = models.ImageField(upload_to='Catalog/images/', blank=True)
    image5 = models.ImageField(upload_to='Catalog/images/', blank=True)
    image6 = models.ImageField(upload_to='Catalog/images/', blank=True)
    image7 = models.ImageField(upload_to='Catalog/images/', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    preorder = models.BooleanField(default=True)