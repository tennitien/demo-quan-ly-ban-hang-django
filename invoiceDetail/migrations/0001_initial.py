# Generated by Django 4.2.5 on 2023-09-21 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("product", "0001_initial"),
        ("invoice", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CTHD",
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
                ("SL", models.IntegerField(default=0)),
                (
                    "MASP",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.sanpham",
                    ),
                ),
                (
                    "SOHD",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="invoice.hoadon"
                    ),
                ),
            ],
        ),
    ]
