import random

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    profile_image = models.ImageField(
        upload_to='profile_image/', blank=True, null=True
    )


class Place(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    code = models.IntegerField(
        default=random.randint(1000, 9999),
        unique=True,
        editable=False,
        null=False,
    )

    def __str__(self):
        return f"{self.latitude};{self.longitude}"
