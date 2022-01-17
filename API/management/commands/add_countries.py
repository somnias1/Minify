from django.core.management.base import BaseCommand
import csv
import os

from django.conf import settings

from ...models import Country

countries_file_path = "API/csvs/countries.csv"
country_file = os.path.join(settings.BASE_DIR, countries_file_path)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--id")
        parser.add_argument("--country_name")

    def handle(self, *args, **options):
        with open(country_file, "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                country = Country()
                country.id = row[0]
                country.country_name = row[1]
                country.save()
