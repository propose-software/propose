from django.core.management.base import BaseCommand, CommandError
from cabinets_app.models import Project, Account
import csv


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('dummy_projects.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                account = Account.objects.get(name=row['Account'])
                p = Project(
                    name=row['\ufeffName'],
                    physical_address=row['Address'],
                    site_contact=row['Contact'],
                    contact_phone=row['Phone'],
                    contact_email=row['Email'],
                    hourly_rate=row['Rate'],
                    account=account,
                    )
                p.save()
