from django.db import models


class Profile(models.Model):
    budget = models.IntegerField()
    first_name = models.CharField(
        max_length=15,
    )
    last_name = models.CharField(
        max_length=15,
    )


class Expense(models.Model):
    title = models.CharField(
        max_length=50,
    )
    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()
