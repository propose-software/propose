from django.test import TestCase, Client
from ..models import Project, Specification
from .tests_data import get_project_info, get_spec_info, UserFactory


class TestSpecifications(TestCase):

    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('12345')
        self.user.save()
        self.client = Client()
        self.client.login(
            username=self.user.username,
            password='12345'
        )

    def test_spec_detail(self):
        spec = Specification.objects.create(**get_spec_info())
        url = '/project/' + str(spec.project.id) + '/spec/' + str(spec.id)
        res = self.client.get(url, follow=True)
        self.assertIn(spec.name.encode(), res.content)
        self.assertIn(spec.construction.encode(), res.content)
        self.assertIn(spec.catalog.encode(), res.content)
        self.assertIn(spec.finish_level.encode(), res.content)
        self.assertIn(spec.interior_material.name.encode(), res.content)
        self.assertIn(spec.exterior_material.name.encode(), res.content)

    def test_spec_create_get(self):
        project = Project.objects.create(**get_project_info())
        url = '/project/' + str(project.id) + '/spec'
        res = self.client.get(url, follow=True)
        self.assertIn(b'<title>Create Specification</title>', res.content)

    def test_spec_create_post(self):
        spec_info = get_spec_info()
        spec_info['interior_material'] = spec_info['interior_material'].id
        spec_info['exterior_material'] = spec_info['exterior_material'].id
        url = '/project/' + str(spec_info['project'].id) + '/spec/'
        res = self.client.post(url, spec_info, follow=True)
        self.assertIn(spec_info['name'].encode(), res.content)
        self.assertIn(spec_info['project'].name.encode(), res.content)
        self.assertIn(spec_info['catalog'].encode(), res.content)
        self.assertTrue(Specification.objects.get(name=spec_info['name']))

    def test_spec_update_get(self):
        spec = Specification.objects.create(**get_spec_info())
        url = '/project/' + str(spec.project.id) + '/spec/' + str(spec.id)
        res = self.client.get(url, follow=True)
        self.assertIn(spec.name.encode(), res.content)

    def test_spec_update_post(self):
        spec_info = get_spec_info()
        spec = Specification.objects.create(**spec_info)
        spec_info['name'] = 'New Name'
        spec_info['construction'] = 'Faceframe Overlay'
        spec_info['catalog'] = 'Wood Slab'
        url = '/project/' + str(spec.project.id) + '/spec/' + str(spec.id) + '/update'
        res = self.client.post(url, spec_info, follow=True)
        self.assertIn(spec_info['name'].encode(), res.content)
        self.assertIn(spec_info['project'].name.encode(), res.content)
        self.assertIn(spec_info['catalog'].encode(), res.content)

    def test_spec_delete_get(self):
        spec = Specification.objects.create(**get_spec_info())
        url = '/project/' + str(spec.project.id) + '/spec/' + str(spec.id) + '/delete'
        res = self.client.get(url, follow=True)
        self.assertIn(spec.name.encode(), res.content)

    def test_spec_delete_post(self):
        spec = Specification.objects.create(**get_spec_info())
        project_detail = '/project/' + str(spec.project.id) + '/detail'
        res = self.client.get(project_detail, follow=True)
        self.assertIn(spec.name.encode(), res.content)
        url = '/project/' + str(spec.project.id) + '/spec/' + str(spec.id) + '/delete'
        self.client.post(url, follow=True)
        res = self.client.get(project_detail, follow=True)
        self.assertNotIn(spec.name.encode(), res.content)
