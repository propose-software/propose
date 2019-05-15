from ..models import (
    Material, Hardware, Labor, Account,
    Project, Cabinet, Drawer, Specification, Room
)
import factory
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    """ Create test User
    """
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


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


def get_labor_info():
    """ Return dictionary for ez creation on Labor,
    e.g. labor = Labor.objects.create(**get_labor_info())
    """
    return {
        'item_name': 'Cabinet',
        'minutes': 120,
        'unit_type': 'each'
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
        'name': 'Dark Cherry',
        'construction': 'Frameless',
        'catalog': 'Laminate',
        'finish_level': 'Unfinished'
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


def get_drawer_form_info(cabinet=None, material=None):
    """ Return dictionary for easy creation of drawer form POST data
    """
    if not cabinet:
        cabinet = Cabinet.objects.create(**get_cabinet_info())
    if not material:
        material = Material.objects.create(**get_material_info())
    return {
        'form-TOTAL_FORMS': 1,
        'form-INITIAL_FORMS': 0,
        'form-MIN_NUM_FORMS': 0,
        'form-MAX_NUM_FORMS': 1000,
        'cabinet': cabinet,
        'form-0-height': 8,
        'form-0-material': material.id,
        'form-0-id': ''
    }
