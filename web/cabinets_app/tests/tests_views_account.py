from django.test import TestCase, Client
from ..models import (
    Material, Hardware, Labor, Account, Project
)
from .tests_data import (
    get_material_info, get_hardware_info, get_labor_info,
    get_account_info, get_project_info, UserFactory
)


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
