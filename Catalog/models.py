from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=2000, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Цена')
    preorder = models.BooleanField(default=True, verbose_name='Предзаказ')
    size = models.CharField(max_length=10, choices=(('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')), default='S')

class ProductImage(models.Model):
    image = models.ImageField(upload_to='Catalog/images/', verbose_name='Фото', null=True)
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    
    