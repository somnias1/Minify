from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timedelta, date


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=86)
    USERNAME_FIELD = "username"

    email = models.EmailField(null=False)
    signup_date = models.DateField(auto_now=True)
    birth_Date = models.DateField(null=False)
    allow_explicit = models.BooleanField(default=False)
    foto_perfil = models.ImageField(
        null=True,
        blank=True,
        upload_to="users/",
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users/"

    def __str__(self):
        return f"{self.username}"
