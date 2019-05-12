import factory
from django.contrib.auth.models import User
from django.test import TestCase, Client
from .models import (
    Material, Hardware, Labor, Account,
    Project, Cabinet, Drawer, Specification, Room
)
from .tests_models import (
    get_material_info, get_hardware_info, get_labor_info,
    get_account_info, get_project_info, get_spec_info, get_room_info,
    get_cabinet_info, get_drawer_info,
)


class UserFactory(factory.django.DjangoModelFactory):
    """ Create test User
    """
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class TestMaterials(TestCase):

    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('12345')
        self.user.save()
        self.client = Client()
        self.client.login(
            username=self.user.username,
            password='12345'
        )

    def test_material_list(self):
        material = Material.objects.create(**get_material_info())
        res = self.client.get('/material/' + str(material.id), follow=True)
        self.assertIn(material.name.encode(), res.content)

    def test_material_detail(self):
        material = Material.objects.create(**get_material_info())
        res = self.client.get('/material/' + str(material.id), follow=True)
        self.assertIn(material.name.encode(), res.content)
        self.assertIn(material.description.encode(), res.content)
        self.assertIn(str(material.thickness).encode(), res.content)
        self.assertIn(str(material.width).encode(), res.content)
        self.assertIn(str(material.length).encode(), res.content)
        self.assertIn(str(material.sheet_cost).encode(), res.content)
        self.assertIn(str(material.waste_factor).encode(), res.content)
        self.assertIn(str(material.markup).encode(), res.content)

    def test_material_create_get(self):
        res = self.client.get('/material', follow=True)
        self.assertIn(b'<h2>Create Material</h2>', res.content)

    def test_material_create_post(self):
        material_info = get_material_info()
        res = self.client.post('/material/', material_info, follow=True)
        self.assertIn(material_info['name'], res.content.decode())
        self.assertIn(material_info['description'], res.content.decode())
        self.assertIn(str(material_info['thickness']), res.content.decode())
        self.assertIn(str(material_info['width']), res.content.decode())
        self.assertIn(str(material_info['length']), res.content.decode())
        self.assertIn(str(material_info['sheet_cost']), res.content.decode())
        self.assertIn(str(material_info['waste_factor']), res.content.decode())
        self.assertIn(str(material_info['markup']), res.content.decode())

    def test_material_update_get(self):
        material = Material.objects.create(**get_material_info())
        url = '/material/' + str(material.id) + '/update'
        res = self.client.get(url, follow=True)
        self.assertIn(material.name.encode(), res.content)

    def test_material_update_post(self):
        material_info = get_material_info()
        material = Material.objects.create(**material_info)
        material_info['name'] = 'New Material Name'
        material_info['description'] = 'New Description'
        material_info['thickness'] = 99
        material_info['width'] = 100
        material_info['length'] = 101
        url = '/material/' + str(material.id) + '/update'
        res = self.client.post(url, material_info, follow=True)
        self.assertIn(material_info['name'], res.content.decode())
        self.assertIn(material_info['description'], res.content.decode())
        self.assertIn(str(material_info['thickness']), res.content.decode())
        self.assertIn(str(material_info['width']), res.content.decode())
        self.assertIn(str(material_info['length']), res.content.decode())
        self.assertIn(str(material_info['sheet_cost']), res.content.decode())
        self.assertIn(str(material_info['waste_factor']), res.content.decode())
        self.assertIn(str(material_info['markup']), res.content.decode())

    def test_material_delete_get(self):
        material = Material.objects.create(**get_material_info())
        url = '/material/' + str(material.id) + '/delete'
        res = self.client.get(url, follow=True)
        self.assertIn(material.name.encode(), res.content)

    def test_material_delete_post(self):
        material = Material.objects.create(**get_material_info())
        res = self.client.get('/material/all', follow=True)
        self.assertIn(material.name.encode(), res.content)
        self.client.post('/material/' + str(material.id) + '/delete')
        res = self.client.get('/material/all', follow=True)
        self.assertNotIn(material.name.encode(), res.content)


class TestHardware(TestCase):

    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('12345')
        self.user.save()
        self.client = Client()
        self.client.login(
            username=self.user.username,
            password='12345'
        )

    def test_hardware_list(self):
        hardware = Hardware.objects.create(**get_hardware_info())
        res = self.client.get('/hardware/' + str(hardware.id), follow=True)
        self.assertIn(hardware.name.encode(), res.content)

    def test_hardware_detail(self):
        hardware = Hardware.objects.create(**get_hardware_info())
        res = self.client.get('/hardware/' + str(hardware.id), follow=True)
        self.assertIn(hardware.name.encode(), res.content)
        self.assertIn(str(hardware.cost_per).encode(), res.content)
        self.assertIn(hardware.unit_type.encode(), res.content)
        self.assertIn(str(hardware.markup).encode(), res.content)

    def test_hardware_create_get(self):
        res = self.client.get('/hardware', follow=True)
        self.assertIn(b'<title>Create Hardware</title>', res.content)

    def test_hardware_create_post(self):
        hardware_info = get_hardware_info()
        res = self.client.post('/hardware/', hardware_info, follow=True)
        self.assertIn(hardware_info['name'], res.content.decode())
        self.assertIn(str(hardware_info['cost_per']), res.content.decode())
        self.assertIn(hardware_info['unit_type'], res.content.decode())
        self.assertIn(str(hardware_info['markup']), res.content.decode())

    def test_hardware_update_get(self):
        hardware = Hardware.objects.create(**get_hardware_info())
        url = '/hardware/' + str(hardware.id) + '/update'
        res = self.client.get(url, follow=True)
        self.assertIn(hardware.name.encode(), res.content)

    def test_hardware_update_post(self):
        hardware_info = get_hardware_info()
        hardware = Hardware.objects.create(**hardware_info)
        hardware_info['name'] = 'New Test Name'
        hardware_info['cost_per'] = 3.14
        hardware_info['unit_type'] = 'Set'
        hardware_info['markup'] = .33
        url = '/hardware/' + str(hardware.id) + '/update'
        res = self.client.post(url, hardware_info, follow=True)
        self.assertIn(hardware_info['name'], res.content.decode())
        self.assertIn(str(hardware_info['cost_per']), res.content.decode())
        self.assertIn(hardware_info['unit_type'], res.content.decode())
        self.assertIn(str(hardware_info['markup']), res.content.decode())

    def test_hardware_delete_get(self):
        hardware = Hardware.objects.create(**get_hardware_info())
        url = '/hardware/' + str(hardware.id) + '/delete'
        res = self.client.get(url, follow=True)
        self.assertIn(hardware.name.encode(), res.content)

    def test_hardware_delete_post(self):
        hardware = Hardware.objects.create(**get_hardware_info())
        res = self.client.get('/hardware/all', follow=True)
        self.assertIn(hardware.name.encode(), res.content)
        self.client.post('/hardware/' + str(hardware.id) + '/delete')
        res = self.client.get('/', follow=True)
        self.assertNotIn(hardware.name.encode(), res.content)


class TestLabor(TestCase):

    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('12345')
        self.user.save()
        self.client = Client()
        self.client.login(
            username=self.user.username,
            password='12345'
        )

    def test_labor_list(self):
        labor = Labor.objects.create(**get_labor_info())
        res = self.client.get('/labor/' + str(labor.id), follow=True)
        self.assertIn(labor.item_name.encode(), res.content)

    def test_labor_detail(self):
        labor = Labor.objects.create(**get_labor_info())
        res = self.client.get('/labor/' + str(labor.id), follow=True)
        self.assertIn(labor.item_name.encode(), res.content)
        self.assertIn(str(labor.minutes).encode(), res.content)
        self.assertIn(labor.unit_type.encode(), res.content)

    def test_labor_create_get(self):
        res = self.client.get('/labor', follow=True)
        self.assertIn(b'<title>Create Labor</title>', res.content)

    def test_labor_create_post(self):
        labor_info = get_labor_info()
        res = self.client.post('/labor/', labor_info, follow=True)
        self.assertIn(labor_info['item_name'], res.content.decode())
        self.assertIn(str(labor_info['minutes']), res.content.decode())

    def test_labor_update_get(self):
        labor = Labor.objects.create(**get_labor_info())
        url = '/labor/' + str(labor.id) + '/update'
        res = self.client.get(url, follow=True)
        self.assertIn(labor.item_name.encode(), res.content)

    def test_labor_update_post(self):
        labor_info = get_labor_info()
        labor = Labor.objects.create(**labor_info)
        labor_info['item_name'] = 'New Test Name'
        labor_info['minutes'] = 123
        url = '/labor/' + str(labor.id) + '/update'
        res = self.client.post(url, labor_info, follow=True)
        self.assertIn(labor_info['item_name'], res.content.decode())
        self.assertIn(str(labor_info['minutes']), res.content.decode())

    def test_labor_delete_get(self):
        labor = Labor.objects.create(**get_labor_info())
        url = '/labor/' + str(labor.id) + '/delete'
        res = self.client.get(url, follow=True)
        self.assertIn(labor.item_name.encode(), res.content)

    def test_labor_delete_post(self):
        labor = Labor.objects.create(**get_labor_info())
        res = self.client.get('/labor/all', follow=True)
        self.assertIn(labor.item_name.encode(), res.content)
        self.client.post('/labor/' + str(labor.id) + '/delete')
        res = self.client.get('/', follow=True)
        self.assertNotIn(labor.item_name.encode(), res.content)


class TestAccounts(TestCase):

    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('12345')
        self.user.save()
        self.client = Client()
        self.client.login(
            username=self.user.username,
            password='12345'
        )

    def test_accounts_list(self):
        account = Account.objects.create(**get_account_info())
        res = self.client.get('/', follow=True)
        self.assertIn(account.name.encode(), res.content)

    def test_account_detail(self):
        account = Account.objects.create(**get_account_info())
        res = self.client.get('/account/' + str(account.id), follow=True)
        self.assertIn(account.name.encode(), res.content)
        self.assertIn(account.billing_address.encode(), res.content)
        self.assertIn(account.billing_phone.encode(), res.content)
        self.assertIn(account.billing_email.encode(), res.content)
        self.assertIn(account.contact_name.encode(), res.content)
        self.assertIn(str(account.discount).encode(), res.content)

    def test_account_create_get(self):
        res = self.client.get('/account', follow=True)
        self.assertIn(b'<h2>Create Account</h2>', res.content)

    def test_account_create_post(self):
        account_info = get_account_info()
        res = self.client.post('/account/', account_info, follow=True)
        self.assertIn(account_info['name'].encode(), res.content)
        self.assertIn(account_info['billing_address'].encode(), res.content)
        self.assertIn(account_info['billing_phone'].encode(), res.content)
        self.assertIn(account_info['billing_email'].encode(), res.content)
        self.assertIn(account_info['contact_name'].encode(), res.content)
        self.assertIn(str(account_info['discount']).encode(), res.content)

    def test_account_update_get(self):
        account = Account.objects.create(**get_account_info())
        url = '/account/' + str(account.id) + '/update'
        res = self.client.get(url, follow=True)
        self.assertIn(account.name.encode(), res.content)

    def test_account_update_post(self):
        account_info = get_account_info()
        account = Account.objects.create(**account_info)
        account_info['name'] = 'New Test Name'
        account_info['billing_address'] = '1600 Pennsylvania Ave.'
        account_info['discount'] = 0
        url = '/account/' + str(account.id) + '/update'
        res = self.client.post(url, account_info, follow=True)
        self.assertIn(account_info['name'].encode(), res.content)
        self.assertIn(account_info['billing_address'].encode(), res.content)
        self.assertIn(account_info['billing_phone'].encode(), res.content)
        self.assertIn(account_info['billing_email'].encode(), res.content)
        self.assertIn(account_info['contact_name'].encode(), res.content)
        self.assertIn(str(account_info['discount']).encode(), res.content)

    def test_account_delete_get(self):
        account = Account.objects.create(**get_account_info())
        url = '/account/' + str(account.id) + '/delete'
        res = self.client.get(url, follow=True)
        self.assertIn(account.name.encode(), res.content)

    def test_account_delete_post(self):
        account = Account.objects.create(**get_account_info())
        res = self.client.get('/', follow=True)
        self.assertIn(account.name.encode(), res.content)
        self.client.post('/account/' + str(account.id) + '/delete')
        res = self.client.get('/', follow=True)
        self.assertNotIn(account.name.encode(), res.content)


class TestProjects(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('12345')
        self.user.save()
        self.client = Client()
        self.client.login(
            username=self.user.username,
            password='12345'
        )

    def test_project_create_get(self):
        account = Account.objects.create(**get_account_info())
        url = '/account/' + str(account.id) + '/project'
        res = self.client.get(url, follow=True)
        check = '<h2>Create Project for {}</h2>'.format(account.name)
        self.assertIn(check.encode(), res.content)

    def test_project_create_post(self):
        project_info = get_project_info()
        res = self.client.post('/account/', project_info, follow=True)
        self.assertIn(project_info['name'].encode(), res.content)

    def test_project_detail(self):
        project = Project.objects.create(**get_project_info())
        res = self.client.get('/project/' + str(project.id) +
                              '/detail', follow=True)
        self.assertIn(project.name.encode(), res.content)
        self.assertIn(project.physical_address.encode(), res.content)
        self.assertIn(project.site_contact.encode(), res.content)
        self.assertIn(project.contact_phone.encode(), res.content)
        self.assertIn(project.contact_email.encode(), res.content)
        self.assertIn(str(project.hourly_rate).encode(), res.content)

    # def test_project_list():


class TestCabinets(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('12345')
        self.user.save()
        self.client = Client()
        self.client.login(
            username=self.user.username,
            password='12345'
        )
        pass
