# Generated by Django 4.2.2 on 2023-08-05 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Catalog", "0008_remove_product_image_remove_product_image2_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(
                null=True, upload_to="Catalog/images/", verbose_name="Фото"
            ),
        ),
        migrations.DeleteModel(
            name="ProductImage",
        ),
    ]
