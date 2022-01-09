from django.db import models
from .songs import Song
from datetime import datetime


class QueueOrder(models.Model):
    song = models.ForeignKey(
        "Song", related_name="%(class)s_song", on_delete=models.CASCADE
    )
    queue = models.ForeignKey(
        "Queue", related_name="%(class)s_queue", on_delete=models.CASCADE
    )
    added = models.DateTimeField(auto_now=True)


class Queue(models.Model):
    queued_song = models.ManyToManyField(
        "Song",
        through="QueueOrder",
        related_name="queued_song",
    )

    class Meta:
        verbose_name = "Queue"
        verbose_name_plural = "Queues"
