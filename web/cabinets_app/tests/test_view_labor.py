from django.test import TestCase, Client
from ..models import Labor
from .test_data import get_labor_info, UserFactory


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
