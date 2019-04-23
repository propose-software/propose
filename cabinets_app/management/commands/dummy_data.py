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

        with open('dummy_hardware.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                p = Hardware(
                    name=row['\ufeffName'],
                    description=row['Description'],
                    cost_per=row['Cost_Per'],
                    unit_type=row['Unit'],
                    markup=row['Markup'],
                )
                p.save()

        with open('dummy_labor.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                p = Labor(
                    item_name=row['\ufeffItem_Name'],
                    minutes=row['Minutes'],
                    units=row['Units'],
                )
                p.save()

        with open('dummy_specs.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                project = Project.objects.get(name=row['Project'])
                int_mat = Material.objects.get(name=row['Int_Material'])
                ext_mat = Material.objects.get(name=row['Ext_Material'])
                p = Specification(
                    name=row['\ufeffName'],
                    project=project,
                    interior_material=int_mat,
                    exterior_material=ext_mat,
                )
                p.save()

        with open('dummy_cabinets.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                project = Project.objects.get(name=row['Project'])
                spec = Specification.objects.get(name=row['Spec'])
                p = Cabinet(
                    project=project,
                    room=row['Room'],
                    specification=spec,
                    cabinet_number=row['Cab_No'],
                    width=row['Width'],
                    height=row['Height'],
                    depth=row['Depth'],
                    number_of_doors=row['Num_Doors'],
                    number_of_shelves=row['Num_Shelves'],
                    finished_interior=row['Fin_Interior'],
                    finished_left_end=row['Fin_Left'],
                    finished_right_end=row['Fin_Right'],
                    finished_top=row['Fin_Top'],
                    finished_bottom=row['Fin_Bottom'],
                )
                p.save()

        with open('dummy_specs.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cabinet = Cabinet.objects.get(
                    project=row['Project'],
                    cabinet_numer=row['Cab_No']
                )
                material = Material.objects.get(name=row['Material'])
                p = Drawer(
                    cabinet=cabinet
                    height=row['Height'],
                    material=material,
                )
                p.save()
