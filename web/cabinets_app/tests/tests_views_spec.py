from django.test import TestCase, Client
from ..models import (
    Material, Hardware, Labor, Account,
    Project, Cabinet, Drawer, Specification, Room
)
from .tests_data import (
    get_material_info, get_hardware_info, get_labor_info,
    get_account_info, get_project_info, get_spec_info, get_room_info,
    get_cabinet_info, get_drawer_info, UserFactory
)


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
