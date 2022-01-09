from django.db import models


class Genre(models.Model):
    genre_name = models.CharField(null=False, max_length=110)
    genre_image = models.ImageField(null=True)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return f"{self.genre_name}"
