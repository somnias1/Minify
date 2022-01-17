from django.core.management.base import BaseCommand
import csv
import os

from django.conf import settings

from ...models import Artist, Country

artists_file_path = "API/csvs/artists.csv"
artist_file = os.path.join(settings.BASE_DIR, artists_file_path)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--id")
        parser.add_argument("--artist_name")
        parser.add_argument("--origin")
        parser.add_argument("--language")
        parser.add_argument("--description")

    def handle(self, *args, **options):
        with open(artist_file, "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                artist = Artist()
                artist.id = row[0]
                artist.artist_name = row[1]
                artist.origin = Country.objects.get(id=row[2])
                artist.language = row[3]
                artist.description = row[4]
                artist.save()
