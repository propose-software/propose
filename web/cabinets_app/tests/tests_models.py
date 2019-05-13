from django.test import TestCase
from ..models import (
    Material, Hardware, Labor, Account,
    Project, Cabinet, Drawer, Specification, Room
)
from .tests_data import (
    get_material_info, get_hardware_info, get_labor_info,
    get_account_info, get_project_info, get_spec_info, get_room_info,
    get_cabinet_info, get_drawer_info,
)


class MaterialTest(TestCase):

    def test_material_class(self):
        self.assertTrue(Material)

    def test_material_instance(self):
        material = Material.objects.create(**get_material_info())
        self.assertIsInstance(material, Material)

    def test_material_fields(self):
        material_info = get_material_info()
        material = Material.objects.create(**material_info)
        self.assertEqual(material_info['name'], material.name)
        self.assertEqual(material_info['description'], material.description)
        self.assertEqual(material_info['thickness'], material.thickness)
        self.assertEqual(material_info['width'], material.width)
        self.assertEqual(material_info['length'], material.length)
        self.assertEqual(material_info['sheet_cost'], material.sheet_cost)
        self.assertEqual(material_info['waste_factor'], material.waste_factor)
        self.assertEqual(material_info['markup'], material.markup)


class HardwareTest(TestCase):

    def test_hardware_class(self):
        self.assertTrue(Hardware)

    def test_hardware_instance(self):
        hardware = Hardware.objects.create(**get_hardware_info())
        self.assertIsInstance(hardware, Hardware)

    def test_hardware_fields(self):
        hardware_info = get_hardware_info()
        hardware = Hardware.objects.create(**hardware_info)
        self.assertEqual(hardware_info['name'], hardware.name)
        self.assertEqual(hardware_info['cost_per'], hardware.cost_per)
        self.assertEqual(hardware_info['unit_type'], hardware.unit_type)
        self.assertEqual(hardware_info['markup'], hardware.markup)


class LaborTest(TestCase):

    def test_labor_class(self):
        self.assertTrue(Labor)

    def test_labor_instance(self):
        labor = Labor.objects.create(**get_labor_info())
        self.assertIsInstance(labor, Labor)

    def test_labor_fields(self):
        labor_info = get_labor_info()
        labor = Labor.objects.create(**labor_info)
        self.assertEqual(labor_info['item_name'], labor.item_name)
        self.assertEqual(labor_info['minutes'], labor.minutes)
        self.assertEqual(labor_info['unit_type'], labor.unit_type)


class AccountTest(TestCase):

    def test_account_class(self):
        self.assertTrue(Account)

    def test_account_instance(self):
        account = Account.objects.create(**get_account_info())
        self.assertIsInstance(account, Account, 'wah!')

    def test_account_fields(self):
        account_info = get_account_info()
        account = Account.objects.create(**account_info)
        self.assertEqual(account_info['name'], account.name)
        self.assertEqual(
            account_info['billing_address'], account.billing_address)
        self.assertEqual(account_info['billing_phone'], account.billing_phone)
        self.assertEqual(account_info['billing_email'], account.billing_email)
        self.assertEqual(account_info['contact_name'], account.contact_name)
        self.assertEqual(account_info['discount'], account.discount)


class ProjectTest(TestCase):

    def test_project_class(self):
        self.assertTrue(Project)

    def test_project_instance(self):
        project = Project.objects.create(**get_project_info())
        self.assertIsInstance(project, Project)

    def test_project_has_account(self):
        project = Project.objects.create(**get_project_info())
        self.assertEqual(project.account.name, 'Foo, Inc.')

    def test_project_fields(self):
        project_info = get_project_info()
        project = Project.objects.create(**project_info)
        self.assertEqual(project_info['name'], project.name)
        self.assertEqual(project_info['account'], project.account)
        self.assertEqual(
            project_info['physical_address'], project.physical_address)
        self.assertEqual(project_info['site_contact'], project.site_contact)
        self.assertEqual(project_info['contact_phone'], project.contact_phone)
        self.assertEqual(project_info['contact_email'], project.contact_email)
        self.assertEqual(project_info['hourly_rate'], project.hourly_rate)

    def test_project_account_has_multiple_projects(self):
        one_project = Project.objects.create(**get_project_info())
        other_project_info = get_project_info(one_project.account)
        other_project = Project.objects.create(**other_project_info)
        self.assertEqual(len(one_project.account.projects.all()), 2)


class SpecificationTest(TestCase):

    def test_spec_class(self):
        self.assertTrue(Specification)

    def test_spec_instance(self):
        spec = Specification.objects.create(**get_spec_info())
        self.assertIsInstance(spec, Specification)

    def test_spec_has_project(self):
        spec = Specification.objects.create(**get_spec_info())
        self.assertEqual(spec.project.name, 'remodel')

    def test_spec_fields(self):
        spec_info = get_spec_info()
        spec = Specification.objects.create(**spec_info)
        self.assertEqual(spec_info['project'], spec.project)
        self.assertEqual(
            spec_info['interior_material'], spec.interior_material)
        self.assertEqual(
            spec_info['exterior_material'], spec.exterior_material)
        self.assertEqual(spec_info['name'], spec.name)
        self.assertEqual(spec_info['construction'], spec.construction)
        self.assertEqual(spec_info['catalog'], spec.catalog)
        self.assertEqual(spec_info['finish_level'], spec.finish_level)

    def test_spec_project_has_many_specs(self):
        spec_one = Specification.objects.create(**get_spec_info())
        spec_two_info = get_spec_info(spec_one.project)
        spec_two = Specification.objects.create(**spec_two_info)
        self.assertEqual(len(spec_one.project.specifications.all()), 2)


class RoomTest(TestCase):

    def test_room_class(self):
        self.assertTrue(Room)

    def test_room_instance(self):
        room = Room(**get_room_info())
        self.assertIsInstance(room, Room)

    def test_room_has_project(self):
        room = Room(**get_room_info())
        self.assertEqual(room.project.name, 'remodel')

    def test_room_fields(self):
        room_info = get_room_info()
        room = Room(**room_info)
        self.assertEqual(room_info['project'], room.project)
        self.assertEqual(room_info['name'], room.name)

    def test_room_project_has_many_rooms(self):
        room_one = Room.objects.create(**get_room_info())
        room_two_info = get_room_info(project=room_one.project)
        room_two = Room.objects.create(**room_two_info)
        self.assertEqual(len(room_one.project.rooms.all()), 2)


class CabinetTest(TestCase):

    def test_cabinet_class(self):
        self.assertTrue(Cabinet)

    def test_cabinet_instance(self):
        cabinet = Cabinet(**get_cabinet_info())
        self.assertIsInstance(cabinet, Cabinet)

    def test_cabinet_has_project_and_spec(self):
        cabinet = Cabinet(**get_cabinet_info())
        self.assertEqual(cabinet.project.name, 'remodel')
        self.assertEqual(cabinet.specification.name, 'Dark Cherry')

    def test_cabinet_fields(self):
        cabinet_info = get_cabinet_info()
        cabinet = Cabinet(**cabinet_info)
        self.assertEqual(cabinet_info['project'], cabinet.project)
        self.assertEqual(cabinet_info['specification'], cabinet.specification)
        self.assertEqual(cabinet_info['room'], cabinet.room)
        self.assertEqual(
            cabinet_info['cabinet_number'], cabinet.cabinet_number)
        self.assertEqual(cabinet_info['width'], cabinet.width)
        self.assertEqual(cabinet_info['height'], cabinet.height)
        self.assertEqual(cabinet_info['depth'], cabinet.depth)
        self.assertEqual(
            cabinet_info['number_of_doors'], cabinet.number_of_doors)
        self.assertEqual(
            cabinet_info['number_of_shelves'], cabinet.number_of_shelves)
        self.assertEqual(
            cabinet_info['finished_interior'], cabinet.finished_interior)
        self.assertEqual(
            cabinet_info['finished_left_end'], cabinet.finished_left_end)
        self.assertEqual(
            cabinet_info['finished_right_end'], cabinet.finished_right_end)
        self.assertEqual(cabinet_info['finished_top'], cabinet.finished_top)
        self.assertEqual(
            cabinet_info['finished_bottom'], cabinet.finished_bottom)

    def test_cabinet_project_has_many_cabinets(self):
        one_cabinet = Cabinet.objects.create(**get_cabinet_info())
        two_cabinet_info = get_cabinet_info(one_cabinet.project)
        two_cabinet = Cabinet.objects.create(**two_cabinet_info)
        self.assertEqual(len(one_cabinet.project.cabinets.all()), 2)

    def test_cabinet_drawers(self):
        cabinet = Cabinet.objects.create(**get_cabinet_info())
        drawer_one = Drawer.objects.create(**get_drawer_info(cabinet=cabinet))
        drawer_two_info = {
            'cabinet': cabinet,
            'height': 10,
            'material': Material.objects.create(**get_material_info())
        }
        drawer_two = Drawer.objects.create(**drawer_two_info)
        self.assertEqual(len(cabinet.drawers.all()), 2)
        self.assertEqual(cabinet.drawers.all()[0].height, 8)
        self.assertEqual(cabinet.drawers.all()[1].height, 10)
