# Generated by Django 4.2.2 on 2023-08-16 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Catalog", "0010_remove_product_image_productimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.CharField(
                blank=True, max_length=2000, verbose_name="Описание"
            ),
        ),
    ]
