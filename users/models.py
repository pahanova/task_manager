from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Пользователь
    """
    REQUIRED_FIELDS = []

    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
