# Generated by Django 4.2.2 on 2023-07-03 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Catalog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image3",
            field=models.ImageField(blank=True, upload_to="Catalog/images/"),
        ),
        migrations.AddField(
            model_name="product",
            name="image4",
            field=models.ImageField(blank=True, upload_to="Catalog/images/"),
        ),
        migrations.AddField(
            model_name="product",
            name="image5",
            field=models.ImageField(blank=True, upload_to="Catalog/images/"),
        ),
        migrations.AddField(
            model_name="product",
            name="image6",
            field=models.ImageField(blank=True, upload_to="Catalog/images/"),
        ),
        migrations.AddField(
            model_name="product",
            name="image7",
            field=models.ImageField(blank=True, upload_to="Catalog/images/"),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
