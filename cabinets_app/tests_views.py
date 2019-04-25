import factory
from django.contrib.auth.models import User
from django.test import TestCase, Client
from .models import (
    Material, Hardware, Labor, Account,
    Project, Cabinet, Drawer, Specification, Room
)
from .tests_models import (
    get_material_info, get_account_info, get_cabinet_info,
    get_drawer_info, get_material_info, get_project_info,
    get_spec_info
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
