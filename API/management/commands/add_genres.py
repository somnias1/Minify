from django.core.management.base import BaseCommand
import csv
import os

from django.conf import settings

from ...models import Genre

genres_file_path = "API/csvs/genres.csv"
genre_file = os.path.join(settings.BASE_DIR, genres_file_path)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--id")
        parser.add_argument("--genre_name")

    def handle(self, *args, **options):
        with open(genre_file, "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                genre = Genre()
                genre.id = row[0]
                genre.genre_name = row[1]
                genre.save()
