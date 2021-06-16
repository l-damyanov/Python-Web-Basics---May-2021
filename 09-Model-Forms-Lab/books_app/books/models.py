from django.core.validators import MinValueValidator
from django.db import models


class Book(models.Model):
    title = models.CharField(
        max_length=20,
    )
    pages = models.IntegerField(
        validators=(
            MinValueValidator(1),
        ),
    )
    description = models.CharField(
        max_length=100,
    )
    author = models.CharField(
        max_length=20,
    )
