from django.core.management.base import BaseCommand
import csv
import os

from django.conf import settings

from ...models import Membership

memberships_file_path = "API/csvs/memberships.csv"
membership_file = os.path.join(settings.BASE_DIR, memberships_file_path)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--id")
        parser.add_argument("--cost")
        parser.add_argument("--membership_name")
        parser.add_argument("--membership_description")
        parser.add_argument("--duration")

    def handle(self, *args, **options):
        with open(membership_file, "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                membership = Membership()
                membership.id = row[0]
                membership.cost = row[1]
                membership.membership_name = row[2]
                membership.membership_description = row[3]
                membership.duration = row[4]
                membership.save()
