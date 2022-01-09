from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timedelta, date

from .memberships import Membership
from .queues import Queue
from .countries import Country
from .artists import Artist


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=86)
    USERNAME_FIELD = "username"

    email = models.EmailField(null=False)
    signup_date = models.DateField(auto_now=True)
    birth_date = models.DateField(null=False)
    country = models.ForeignKey(
        "Country", related_name="%(class)s_country", on_delete=models.CASCADE
    )
    user_image = models.ImageField(
        null=True,
        blank=True,
        upload_to="users/",
    )
    allow_explicit = models.BooleanField(default=False)
    membership = models.ForeignKey(
        "Membership", related_name="%(class)s_Membership", on_delete=models.CASCADE
    )

    queue = models.OneToOneField(
        "Queue", related_name="user_queue", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.username}"


class UserFollowing(models.Model):

    user = models.ForeignKey(
        "User", related_name="user_following", on_delete=models.CASCADE
    )
    artist = models.ForeignKey(
        "Artist", related_name="artist_followed", on_delete=models.CASCADE
    )
    followed = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "artist"], name="unique_followers")
        ]

        ordering = ["-followed"]

    def __str__(self):
        return f"{self.user} sigue a {self.artist}"
