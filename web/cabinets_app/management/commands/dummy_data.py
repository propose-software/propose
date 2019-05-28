from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from cabinets_app.models import (
    Company, Account, Material, Hardware, Labor,
    Project, Specification, Room, Cabinet, Drawer)
import csv


class Command(BaseCommand):
    def handle(self, *args, **options):

        Company.objects.all().delete()
        Account.objects.all().delete()
        Project.objects.all().delete()
        Material.objects.all().delete()
        Hardware.objects.all().delete()
        Labor.objects.all().delete()

        with open('dummy_data/dummy_companies.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                p = Company(
                    name=row['name'],
                    billing_address=row['billing_address'],
                    billing_phone=row['billing_phone'],
                    billing_email=row['billing_email'],
                    contact_name=row['contact_name'],
                )
                p.save()

        with open('dummy_data/dummy_accounts.csv') as f:
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

        with open('dummy_data/dummy_projects.csv') as f:
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

        with open('dummy_data/dummy_materials.csv') as f:
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
                    category=row['Category'],
                    mat_type=row['Type'],
                )
                p.save()

        with open('dummy_data/dummy_hardware.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                p = Hardware(
                    name=row['\ufeffName'],
                    cost_per=row['Cost_Per'],
                    unit_type=row['Unit'],
                    markup=row['Markup'],
                    category=row['Category'],
                    labor_minutes=row['Labor_Minutes'],
                )
                p.save()

        with open('dummy_data/dummy_labor.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                p = Labor(
                    item_name=row['\ufeffItem_Name'],
                    minutes=row['Minutes'],
                    unit_type=row['Units'],
                    category=row['Category'],
                )
                p.save()

        with open('dummy_data/dummy_specs.csv') as f:
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

        with open('dummy_data/dummy_rooms.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                project = Project.objects.get(name=row['Project'])
                p = Room(
                    project=project,
                    name=row['Room']
                )
                p.save()

        with open('dummy_data/dummy_cabinets.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                project = Project.objects.get(name=row['\ufeffProject'])
                spec = Specification.objects.filter(
                    name=row['Spec'],
                    project=project
                )[0]
                room = Room.objects.filter(
                    project=project,
                    name=row['Room']
                )[0]
                fin_int = True if row['Fin_Interior'] == 'True' else False
                fin_left = True if row['Fin_Interior'] == 'True' else False
                fin_right = True if row['Fin_Interior'] == 'True' else False
                fin_top = True if row['Fin_Interior'] == 'True' else False
                fin_bot = True if row['Fin_Interior'] == 'True' else False
                p = Cabinet(
                    project=project,
                    specification=spec,
                    room=room,
                    cabinet_number=row['Cab_No'],
                    width=row['Width'],
                    height=row['Height'],
                    depth=row['Depth'],
                    number_of_doors=row['Num_Doors'],
                    number_of_shelves=row['Num_Shelves'],
                    finished_interior=fin_int,
                    finished_left_end=fin_left,
                    finished_right_end=fin_right,
                    finished_top=fin_top,
                    finished_bottom=fin_bot,
                )
                p.save()

        with open('dummy_data/dummy_drawers.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                project = Project.objects.get(name=row['\ufeffProject'])
                cabinet = Cabinet.objects.filter(
                    project=project,
                    cabinet_number=row['Cab_No']
                )[0]
                material = Material.objects.get(name=row['Material'])
                p = Drawer(
                    cabinet=cabinet,
                    height=row['Height'],
                    material=material,
                )
                p.save()
