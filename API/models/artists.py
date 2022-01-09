from django.db import models


class Artist(models.Model):
    artist_name = models.CharField(max_length=255, null=False)
    artist_image = models.ImageField(upload_to="artists/")
    origin = models.CharField(blank=False, max_length=100)
    language = models.CharField(blank=True, max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists"

    def __str__(self):
        return f"{self.artist_name}"
