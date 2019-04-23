from django.core.management.base import BaseCommand, CommandError
from cabinets_app.models import Account
import csv


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('dummy_accounts.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                p = Account(
                    name=row['\ufeffName'],
                    billing_address=row['Address'],
                    billing_phone=row['Phone'],
                    billing_email=row['Email'],
                    contact_name=row['Contact'],
                    discount=row['Discount'],
                    )
                p.save()
