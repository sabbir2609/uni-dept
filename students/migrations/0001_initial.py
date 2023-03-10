# Generated by Django 4.1.7 on 2023-03-02 08:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("name", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                ("nid", models.IntegerField(max_length=16)),
                ("phone", models.IntegerField(max_length=11)),
                ("birthdate", models.DateField(default=datetime.date)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")], max_length=1
                    ),
                ),
            ],
        ),
    ]
