from django.test import TestCase
from .models import (
    Material, Hardware, Labor, Account,
    Project, Cabinet, Drawer, Specification, Room
)


def get_material_info():
    """ Return dict for easy creation of Material instance
    e.g. material = Material.objects.create(**get_material_info)
    """
    return {
        'name': 'Select Cherry',
        'description': '3/4 A1 Select Cherry Plywood',
        'thickness': 0.75,
        'width': 48,
        'length': 96,
        'sheet_cost': 120,
        'waste_factor': 0.15,
        'markup': 0.2
    }


def get_account_info():
    """
    Return dictionary for easy creation of Account
    E.g. account = Account(**get_account_info())
    You can get fancy with this where you pass in
    custom values, etc.
    """
    return {
        'name': 'Foo, Inc.',
        'billing_address': '123 Bar Lane',
        'billing_phone': '206-123-4567',
        'billing_email': 'foo@bar.baz',
        'contact_name': 'Foo Bar',
        'discount': .00
    }


def get_project_info(account=None):
    """
    Return dictionary for easy creation of Project
    E.g. project = Project(**get_project_info())
    You can get fancy with this where you pass in
    custom values, etc.
    """
    if not account:
        account = Account.objects.create(**get_account_info())
    return {
        'name': 'remodel',
        'account': account,
        'physical_address': '123 Foo Bar Lane',
        'site_contact': 'Cookie Monster',
        'contact_phone': '123-456-7890',
        'contact_email': 'cookie@monster.com',
        'hourly_rate': 22.50
    }


def get_spec_info(project=None, int_material=None, ext_material=None):
    """ Return dictionary for easy creation of Specification
    e.g. spec = Specification.objects.create(**get_spec_info())
    """
    if not project:
        project = Project.objects.create(**get_project_info())
    if not int_material:
        int_material = Material.objects.create(**get_material_info())
    if not ext_material:
        ext_material = Material.objects.create(**get_material_info())
    return {
        'project': project,
        'interior_material': int_material,
        'exterior_material': ext_material,
        'name': 'Dark Cherry'
    }


def get_room_info(project=None):
    """ Return a dictionary for easy creation of Room objects
    """
    if not project:
        project = Project.objects.create(**get_project_info())
    return {
        'name': 'Kitchen',
        'project': project
    }


def get_cabinet_info(project=None, spec=None, room=None):
    """ Return dictionary for easy creation of Cabinet
    E.g. cabinet = Cabinet.objects.create(**get_cabinet_info())
    """
    if not project:
        project = Project.objects.create(**get_project_info())
    if not spec:
        spec = Specification.objects.create(**get_spec_info())
    if not room:
        room = Room.objects.create(**get_room_info())
    return {
        'project': project,
        'specification': spec,
        'room': room,
        'cabinet_number': 1,
        'width': 9,
        'height': 31,
        'depth': 24,
        'number_of_doors': 1,
        'number_of_shelves': 3,
        'finished_interior': False,
        'finished_left_end': False,
        'finished_right_end': False,
        'finished_top': False,
        'finished_bottom': False
    }


def get_drawer_info(cabinet=None, material=None):
    """ Return dictionary for easy creation of Drawer
    E.g. drawer = Drawer.objects.create(**get_cabinet_info())
    """
    if not cabinet:
        cabinet = Cabinet.objects.create(**get_cabinet_info())
    if not material:
        material = Material.objects.create(**get_material_info())
    return {
        'cabinet': cabinet,
        'height': 8,
        'material': material
    }

def get_hardware_info():
    ''' Return dictionary for easy creation of Hardware
    E.g. hardware = Hardware.objects.create(**get_hardware_info())
    '''
    return {
       'name': 'Blum 110+ Hinge',
       'cost_per': 2.75,
       'unit_type': 'each',
       'markup': .2,
    }



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

    def test_spec_project_has_many_specs(self):
        spec_one = Specification.objects.create(**get_spec_info())
        spec_two_info = get_spec_info(spec_one.project)
        spec_two = Specification.objects.create(**spec_two_info)
        self.assertEqual(len(spec_one.project.specifications.all()), 2)


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
