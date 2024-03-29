# Generated by Django 4.2.2 on 2023-07-21 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Catalog", "0004_alter_product_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.CharField(blank=True, max_length=250, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(upload_to="Catalog/images/", verbose_name="Фото"),
        ),
        migrations.AlterField(
            model_name="product",
            name="image2",
            field=models.ImageField(
                blank=True, upload_to="Catalog/images/", verbose_name="Фото2"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="image3",
            field=models.ImageField(
                blank=True, upload_to="Catalog/images/", verbose_name="Фото3"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="image4",
            field=models.ImageField(
                blank=True, upload_to="Catalog/images/", verbose_name="Фото4"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="image5",
            field=models.ImageField(
                blank=True, upload_to="Catalog/images/", verbose_name="Фото5"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="image6",
            field=models.ImageField(
                blank=True, upload_to="Catalog/images/", verbose_name="Фото6"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="image7",
            field=models.ImageField(
                blank=True, upload_to="Catalog/images/", verbose_name="Фото7"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="preorder",
            field=models.BooleanField(default=True, verbose_name="Предзаказ"),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(
                decimal_places=0, max_digits=10, verbose_name="Цена"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="title",
            field=models.CharField(max_length=100, verbose_name="Название"),
        ),
    ]
