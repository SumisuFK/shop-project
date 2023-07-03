# Generated by Django 4.2.2 on 2023-07-02 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=250)),
                ("image", models.ImageField(upload_to="Catalog/images/")),
                ("image2", models.ImageField(blank=True, upload_to="Catalog/images/")),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("available", models.BooleanField(default=True)),
            ],
        ),
    ]
