# Generated by Django 4.1.7 on 2023-03-02 08:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birthdate",
            field=models.DateField(),
        ),
    ]
