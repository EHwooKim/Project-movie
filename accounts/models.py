from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    preference = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='preferences',
        blank=True
    )
