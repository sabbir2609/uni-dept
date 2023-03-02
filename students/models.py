import datetime

from django.db import models


class User(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),

    ]

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    nid = models.IntegerField(max_length=16)
    phone = models.IntegerField(max_length=11)
    birthdate = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name
