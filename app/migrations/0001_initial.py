# Generated by Django 4.2.11 on 2024-05-03 04:08

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Restro",
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
                ("firstnm", models.CharField(max_length=100)),
                ("lastnm", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("what", models.CharField(max_length=250)),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, region=None
                    ),
                ),
                ("message", models.TextField(null=True)),
            ],
        ),
    ]
