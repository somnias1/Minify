from django.db import models

from .countries import Country


class Artist(models.Model):
    artist_name = models.CharField(max_length=255, null=False)
    artist_image = models.ImageField(null=True, blank=True, upload_to="artists/")
    origin = models.ForeignKey(
        "Country", related_name="%(class)s_country", on_delete=models.CASCADE
    )
    language = models.CharField(blank=True, max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists"

    def __str__(self):
        return f"{self.artist_name}"
