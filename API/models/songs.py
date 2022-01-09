from django.db import models

from .artists import Artist
from .albums import Album


class Song(models.Model):
    track_number = models.IntegerField(null=False)
    song_name = models.CharField(null=False, max_length=255)
    length = models.IntegerField(help_text="In seconds")
    bpm = models.IntegerField(null=False)
    is_explicit = models.BooleanField(default=False)
    streams = models.IntegerField(null=False, default=0)
    participants = models.ManyToManyField("Artist")
    album = models.ForeignKey("Album", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"

    def __str__(self):
        return f"{self.song_name}"
