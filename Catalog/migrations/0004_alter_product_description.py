# Generated by Django 4.2.2 on 2023-07-21 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Catalog", "0003_rename_available_product_preorder"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.CharField(blank=True, max_length=250),
        ),
    ]