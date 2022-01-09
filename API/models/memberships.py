from django.db import models


class Membership(models.Model):
    cost = models.IntegerField()
    membership_name = models.CharField(max_length=255, blank=False)
    membership_description = models.TextField()
    duration = models.IntegerField(help_text="In days")

    class Meta:
        verbose_name = "Membership"
        verbose_name_plural = "Memberships"

    def __str__(self):
        return f"{self.membership_name}"
