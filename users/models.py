from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=40, verbose_name='страна', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='Активация')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
