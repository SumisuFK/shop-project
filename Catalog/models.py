from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='Catalog/images/')
    image2 = models.ImageField(upload_to='Catalog/images/', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default='0')
    available = models.BooleanField(default=True)