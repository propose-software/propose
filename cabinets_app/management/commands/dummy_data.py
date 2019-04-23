from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from cabinets_app.models import (Account, Project, Material,
    Specification, Cabinet, Hardware, Drawer, Labor)
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

        with open('dummy_materials.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                updated = timezone.now()
                p = Material(
                    name=row['\ufeffName'],
                    description=row['Description'],
                    thickness=row['Thickness'],
                    width=row['Width'],
                    length=row['Length'],
                    sheet_cost=row['Sheet_Cost'],
                    waste_factor=row['Waste_Factor'],
                    markup=row['Markup'],
                )
                p.save()
