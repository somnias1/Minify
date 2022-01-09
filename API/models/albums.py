from django.db import models
from datetime import date

from .artists import Artist
from .genres import Genre


class AlbumGenre(models.Model):
    genre = models.ForeignKey(
        "Genre", related_name="%(class)s_genre", on_delete=models.CASCADE
    )
    album = models.ForeignKey(
        "Album", related_name="%(class)s_album", on_delete=models.CASCADE
    )


class Album(models.Model):
    album_name = models.CharField(max_length=255, null=False)
    release_date = models.DateField(null=False)
    album_image = models.ImageField(null=True, blank=True, upload_to="albums/")
    genre = models.ManyToManyField("Genre", through="AlbumGenre")
    artist = models.ForeignKey(
        "Artist", related_name="%(class)s_artist", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"

    def __str__(self):
        return f"{self.album_name}"
