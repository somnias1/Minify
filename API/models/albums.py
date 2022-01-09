from django.db import models
from datetime import date


class Album(models.Model):
    album_name = models.CharField(max_length=255, null=False)
    release_date = models.DateField(null=False)
    album_image = models.ImageField(upload_to="albums/")

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"

    def __str__(self):
        return f"{self.album_name}"
