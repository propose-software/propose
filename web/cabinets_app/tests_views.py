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

    def test_account_update_get(self):
        account = Account.objects.create(**get_account_info())
        url = '/account/' + str(account.id) + '/update'
        res = self.client.get(url, follow=True)
        self.assertIn(account.name.encode(), res.content)

    def test_account_update_post(self):
        account_info = get_account_info()
        account = Account.objects.create(**account_info)
        account_info['name'] = 'New Test Name'
        url = '/account/' + str(account.id) + '/update'
        res = self.client.post(url, account_info, follow=True)
        self.assertIn(account_info['name'].encode(), res.content)

    def test_account_delete_get(self):
        account = Account.objects.create(**get_account_info())
        url = '/account/' + str(account.id) + '/delete'
        res = self.client.get(url, follow=True)
        self.assertIn(account.name.encode(), res.content)

    def test_account_delete_post(self):
        account = Account.objects.create(**get_account_info())
        res = self.client.get('/', follow=True)
        self.assertIn(account.name.encode(), res.content)
        url = '/account/' + str(account.id) + '/delete'
        self.client.post(url)
        res = self.client.get('/', follow=True)
        self.assertNotIn(account.name.encode(), res.content)


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

    def test_material_create_get(self):
        res = self.client.get('/material', follow=True)
        self.assertIn(b'<h2>Create Material</h2>', res.content)

    def test_material_create_post(self):
        material_create = get_material_info()
        res = self.client.post('/material', material_create, follow=True)
        self.assertIn('<h2>Create Material</h2>', res.content.decode())

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

    def test_hardware_create_get(self):
        res = self.client.get('/hardware', follow=True)
        self.assertIn(b'<title>Create Hardware</title>', res.content)

    def test_hardware_create_post(self):
        hardware_create = get_hardware_info()
        res = self.client.post('/hardware', hardware_create, follow=True)
        self.assertIn('<h2>Create Hardware</h2>', res.content.decode())

    def test_hardware_list(self):
        hardware = Hardware.objects.create(**get_hardware_info())
        res = self.client.get('/hardware/' + str(hardware.id), follow=True)
        self.assertIn(hardware.name.encode(), res.content)

    def test_hardware_detail(self):
        hardware = Hardware.objects.create(**get_hardware_info())
        res = self.client.get('/hardware/' + str(hardware.id), follow=True)
        self.assertIn(hardware.name.encode(), res.content)
        self.assertIn(str(hardware.cost_per).encode(), res.content)
        self.assertIn(str(hardware.unit_type).encode(), res.content)
        self.assertIn(str(hardware.markup).encode(), res.content)


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
