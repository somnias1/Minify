from django.db import models
from datetime import date
from .songs import Song
from .users import User


class PlaylistSong(models.Model):
    song = models.ForeignKey(
        "Song", related_name="%(class)s_song", on_delete=models.CASCADE
    )
    playlist = models.ForeignKey(
        "Playlist", related_name="%(class)s_playlist", on_delete=models.CASCADE
    )
    added = models.DateField(auto_now=True)


class Playlist(models.Model):
    playlist_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    saved_song = models.ManyToManyField(
        "Song", through="PlaylistSong"
    )
    user = models.ForeignKey("User", related_name="%(class)s_user", on_delete =models.CASCADE)

    class Meta:
        verbose_name = "Playlist"
        verbose_name = "Playlists"

    def __str__(self):
        return f"{self.playlist_name}"
