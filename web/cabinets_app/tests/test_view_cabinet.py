from django.test import TestCase, Client
from ..models import Project, Specification, Room, Cabinet, Drawer
from .test_data import (
    get_project_info, get_room_info, get_spec_info,
    get_cabinet_info, get_drawer_form_info, get_drawer_info, UserFactory
)


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

    def test_cabinet_detail(self):
        cabinet = Cabinet.objects.create(**get_cabinet_info())
        url = '/project/' + str(cabinet.project.id) + '/cabinet/' + str(cabinet.id)
        res = self.client.get(url, follow=True)
        self.assertIn(str(cabinet.cabinet_number).encode(), res.content)
        self.assertIn(str(cabinet.width).encode(), res.content)
        self.assertIn(str(cabinet.height).encode(), res.content)
        self.assertIn(str(cabinet.depth).encode(), res.content)
        self.assertIn(str(cabinet.number_of_doors).encode(), res.content)
        self.assertIn(str(cabinet.number_of_shelves).encode(), res.content)

    def test_cabinet_create_get(self):
        room = Room.objects.create(**get_room_info())
        url = '/project/' + str(room.project.id) + '/room/' + str(room.id) + '/cabinet'
        res = self.client.get(url, follow=True)
        self.assertIn(b'<title>Cabinet Create</title>', res.content)

    def test_cabinet_create_post(self):
        spec = Specification.objects.create(**get_spec_info())
        room = Room.objects.create(**get_room_info(project=spec.project))
        cabinet_info = get_cabinet_info(project=room.project, room=room)
        cabinet_info['specification'] = cabinet_info['specification'].id
        drawer_info = get_drawer_form_info()
        cabinet_info.update(drawer_info)

        url = '/project/' + str(room.project.id) + '/room/' + str(room.id) + '/cabinet'
        res = self.client.post(url, cabinet_info, follow=True)
        self.assertIn(str(cabinet_info['cabinet_number']).encode(), res.content)
        self.assertIn(spec.name.encode(), res.content)
        self.assertIn(str(cabinet_info['width']).encode(), res.content)
        self.assertIn(str(cabinet_info['height']).encode(), res.content)
        self.assertIn(str(cabinet_info['depth']).encode(), res.content)
        self.assertIn(str(cabinet_info['number_of_doors']).encode(), res.content)
        self.assertIn(str(cabinet_info['number_of_shelves']).encode(), res.content)
        self.assertIn(str(drawer_info['form-0-height']).encode(), res.content)
        self.assertTrue(Cabinet.objects.get(cabinet_number=cabinet_info['cabinet_number']))

    def test_cabinet_update_get(self):
        cabinet = Cabinet.objects.create(**get_cabinet_info())
        url = '/project/' + str(cabinet.project.id) + '/cabinet/' + str(cabinet.id) + '/update'
        res = self.client.get(url, follow=True)
        self.assertIn(str(cabinet.cabinet_number).encode(), res.content)
        self.assertIn(str(cabinet.width).encode(), res.content)
        self.assertIn(str(cabinet.height).encode(), res.content)
        self.assertIn(str(cabinet.depth).encode(), res.content)
        self.assertIn(str(cabinet.number_of_doors).encode(), res.content)
        self.assertIn(str(cabinet.number_of_shelves).encode(), res.content)

    def test_cabinet_update_post(self):
        spec = Specification.objects.create(**get_spec_info())
        room = Room.objects.create(**get_room_info(project=spec.project))
        cabinet_info = get_cabinet_info(project=room.project, room=room, spec=spec)
        cabinet = Cabinet.objects.create(**cabinet_info)

        cabinet_info['specification'] = cabinet_info['specification'].id
        cabinet_info['width'] = 17.5
        cabinet_info['height'] = 33.25
        cabinet_info['depth'] = 27.75

        drawer = Drawer.objects.create(**get_drawer_info(cabinet=cabinet))
        drawer_form_info = get_drawer_form_info(cabinet=cabinet)
        drawer_form_info['form-0-id'] = drawer.id
        drawer_form_info['form-TOTAL_FORMS'] = 2
        drawer_form_info['form-INITIAL_FORMS'] = 1
        drawer_form_info['form-1-height'] = 10
        drawer_form_info['form-1-material'] = drawer.material.id
        drawer_form_info['form-1-id'] = ''

        cabinet_info.update(drawer_form_info)
        url = '/project/' + str(cabinet.project.id) + '/cabinet/' + str(cabinet.id) + '/update'
        res = self.client.post(url, cabinet_info, follow=True)
        self.assertIn(str(cabinet_info['cabinet_number']).encode(), res.content)
        self.assertIn(cabinet.specification.name.encode(), res.content)
        self.assertIn(str(cabinet_info['width']).encode(), res.content)
        self.assertIn(str(cabinet_info['height']).encode(), res.content)
        self.assertIn(str(cabinet_info['depth']).encode(), res.content)
        self.assertIn(str(cabinet_info['number_of_doors']).encode(), res.content)
        self.assertIn(str(cabinet_info['number_of_shelves']).encode(), res.content)
        self.assertIn(str(drawer_form_info['form-0-height']).encode(), res.content)
        self.assertIn(str(drawer_form_info['form-1-height']).encode(), res.content)
        drawer_count = 'Drawers (' + str(len(cabinet.drawers.all())) + ')'
        self.assertIn(drawer_count.encode(), res.content)

    def test_cabinet_delete_get(self):
        cabinet = Cabinet.objects.create(**get_cabinet_info())
        url = '/project/' + str(cabinet.project.id) + '/cabinet/' + str(cabinet.id) + '/delete'
        res = self.client.get(url, follow=True)
        self.assertIn(str(cabinet.cabinet_number).encode(), res.content)

    def test_cabinet_delete_post(self):
        project = Project.objects.create(**get_project_info())
        spec = Specification.objects.create(**get_spec_info(project=project))
        room = Room.objects.create(**get_room_info(project=project))
        cabinet = Cabinet.objects.create(
            **get_cabinet_info(project=project, room=room, spec=spec))
        drawer = Drawer.objects.create(**get_drawer_info(cabinet=cabinet))

        res = self.client.get('/project/' + str(cabinet.project.id), follow=True)
        self.assertEqual(project, cabinet.project)
        self.assertIn(str(cabinet.cabinet_number).encode(), res.content)
        self.assertIn(str(cabinet.width).encode(), res.content)
        self.assertIn(str(cabinet.height).encode(), res.content)
        self.assertIn(str(cabinet.depth).encode(), res.content)

        url = '/project/' + str(cabinet.project.id) + '/cabinet/' + str(cabinet.id) + '/delete'
        self.client.post(url, follow=True)

        res = self.client.get('/project/' + str(cabinet.project.id), follow=True)
        self.assertNotIn(str(cabinet.width).encode(), res.content)
        self.assertNotIn(str(cabinet.height).encode(), res.content)
        self.assertNotIn(str(cabinet.depth).encode(), res.content)
