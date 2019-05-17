from django.test import TestCase, Client
from ..models import Material
from .test_data import get_material_info, UserFactory


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
