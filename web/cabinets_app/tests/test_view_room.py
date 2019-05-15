from django.test import TestCase, Client
from ..models import Project, Room
from .test_data import get_project_info, get_room_info, UserFactory


class TestRooms(TestCase):

    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('12345')
        self.user.save()
        self.client = Client()
        self.client.login(
            username=self.user.username,
            password='12345'
        )

    def test_room_detail(self):
        room = Room.objects.create(**get_room_info())
        url = '/project/' + str(room.project.id) + '/detail'
        res = self.client.get(url, follow=True)
        self.assertIn(room.name.encode(), res.content)

    def test_room_create_get(self):
        project = Project.objects.create(**get_project_info())
        url = '/project/' + str(project.id) + '/room'
        res = self.client.get(url, follow=True)
        self.assertIn(b'<title>Create Room</title>', res.content)

    def test_room_create_post(self):
        room_info = get_room_info()
        url = '/project/' + str(room_info['project'].id) + '/room/'
        res = self.client.post(url, room_info, follow=True)
        self.assertIn(room_info['name'].encode(), res.content)
        self.assertIn(room_info['project'].name.encode(), res.content)
        self.assertTrue(Room.objects.get(name=room_info['name']))

    def test_room_update_get(self):
        room = Room.objects.create(**get_room_info())
        url = '/project/' + str(room.project.id) + '/room/' + str(room.id) + '/update'
        res = self.client.get(url, follow=True)
        self.assertIn(room.name.encode(), res.content)

    def test_room_update_post(self):
        room_info = get_room_info()
        room = Room.objects.create(**room_info)
        room_info['name'] = 'New Name'
        url = '/project/' + str(room.project.id) + '/room/' + str(room.id) + '/update'
        res = self.client.post(url, room_info, follow=True)
        self.assertIn(room_info['name'].encode(), res.content)

    def test_room_delete_get(self):
        room = Room.objects.create(**get_room_info())
        url = '/project/' + str(room.project.id) + '/room/' + str(room.id) + '/delete'
        res = self.client.get(url, follow=True)
        self.assertIn(room.name.encode(), res.content)

    def test_room_delete_post(self):
        room = Room.objects.create(**get_room_info())
        project_detail = '/project/' + str(room.project.id) + '/detail'
        res = self.client.get(project_detail, follow=True)
        self.assertIn(room.name.encode(), res.content)
        url = '/project/' + str(room.project.id) + '/room/' + str(room.id) + '/delete'
        self.client.post(url, follow=True)
        res = self.client.get(project_detail, follow=True)
        self.assertNotIn(room.name.encode(), res.content)
