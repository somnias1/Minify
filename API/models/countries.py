from django.db import models


class Country(models.Model):
    country_name = models.CharField(null=False, max_length=100)
    country_image = models.ImageField(null=True, upload_to="countries/")

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return f"{self.country_name}"
