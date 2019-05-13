from django.test import TestCase, Client
from ..models import Hardware
from .tests_data import get_hardware_info, UserFactory


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
