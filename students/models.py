from django.db import models


class User(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),

    ]

    name = models.CharField(max_length=255, blank=False)
    address = models.CharField(max_length=255, blank=True)
    nid = models.CharField(max_length=17, help_text="Enter Your National ID")
    phone = models.CharField(max_length=14, help_text="eg: +8801700000000", blank=False)
    birthdate = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255, blank=False)
    code = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
