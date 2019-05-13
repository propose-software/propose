from django.test import TestCase, Client
from ..models import Account, Project
from .tests_data import get_account_info, get_project_info, UserFactory


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

    def test_project_home(self):
        project = Project.objects.create(**get_project_info())
        res = self.client.get('/project/' + str(project.id), follow=True)
        self.assertIn(project.name + ' Project Invoice', res.content.decode())

    def test_project_detail(self):
        project = Project.objects.create(**get_project_info())
        url = '/project/' + str(project.id) + '/detail'
        res = self.client.get(url, follow=True)
        self.assertIn(project.name.encode(), res.content)
        self.assertIn(project.physical_address.encode(), res.content)
        self.assertIn(project.site_contact.encode(), res.content)
        self.assertIn(project.contact_phone.encode(), res.content)
        self.assertIn(project.contact_email.encode(), res.content)
        self.assertIn(str(project.hourly_rate).encode(), res.content)

    def test_project_create_get(self):
        account = Account.objects.create(**get_account_info())
        url = '/account/' + str(account.id) + '/project'
        res = self.client.get(url, follow=True)
        check = '<h2>Create Project for {}</h2>'.format(account.name)
        self.assertIn(check.encode(), res.content)

    def test_project_create_post(self):
        project_info = get_project_info()
        url = '/account/' + str(project_info['account'].id) + '/project/'
        res = self.client.post(url, project_info, follow=True)
        self.assertIn(project_info['name'].encode(), res.content)
        self.assertIn(project_info['physical_address'].encode(), res.content)
        self.assertIn(project_info['site_contact'].encode(), res.content)
        self.assertIn(project_info['contact_phone'].encode(), res.content)
        self.assertIn(project_info['contact_email'].encode(), res.content)
        self.assertIn(str(project_info['hourly_rate']).encode(), res.content)
        self.assertTrue(Project.objects.get(name=project_info['name']))

    def test_project_update_get(self):
        project = Project.objects.create(**get_project_info())
        url = '/project/' + str(project.id) + '/update'
        res = self.client.get(url, follow=True)
        self.assertIn(project.name.encode(), res.content)

    def test_project_update_post(self):
        project_info = get_project_info()
        project = Project.objects.create(**project_info)
        project_info['name'] = 'The Best Project'
        project_info['physical_address'] = '1600 Pennsylvania Ave.'
        project_info['hourly_rate'] = 0
        url = '/project/' + str(project.id) + '/update'
        res = self.client.post(url, project_info, follow=True)
        self.assertIn(project_info['name'].encode(), res.content)
        self.assertIn(project_info['physical_address'].encode(), res.content)
        self.assertIn(project_info['site_contact'].encode(), res.content)
        self.assertIn(project_info['contact_phone'].encode(), res.content)
        self.assertIn(project_info['contact_email'].encode(), res.content)
        self.assertIn(str(project_info['hourly_rate']).encode(), res.content)

    def test_project_delete_get(self):
        project = Project.objects.create(**get_project_info())
        url = '/project/' + str(project.id) + '/delete'
        res = self.client.get(url, follow=True)
        self.assertIn(project.name.encode(), res.content)

    def test_project_delete_post(self):
        project = Project.objects.create(**get_project_info())
        url = '/account/' + str(project.account.id)
        res = self.client.get(url, follow=True)
        self.assertIn(project.name.encode(), res.content)
        self.client.post('/project/' + str(project.id) + '/delete')
        res = self.client.get('/', follow=True)
        self.assertNotIn(project.name.encode(), res.content)
