from unittest import TestCase
from unittest.mock import patch
from src.controllers.user_controller import UserController
from tests.mocks.mocks import Mocks


class UserControllerTest(TestCase):

    def setUp(self):
        self.user_controller = UserController()

    @patch('src.services.db.mysql_service.MySQLService.insert_user')
    def test_save_user_returns_info_msg_for_successfully_saved_user(self, insert_stub):
        insert_stub.return_value = {}
        result = self.user_controller.save_user(Mocks().USER_MOCK)
        self.assertEqual(result, {"info":"user successfully created."})

    @patch('src.services.db.mysql_service.MySQLService.find_user_by_id')
    def test_find_user_by_id_returns_array_with_user_info_for_existing_id(self, find_stub):
        find_stub.return_value = [4,
            'Unit Test',
            'User',
            'unittest.user',
            9,
            'user@unittest.com'
        ]
        result = self.user_controller.find_by_id(4)
        self.assertEqual(result, {
            'id': 4,
            'first_name': 'Unit Test',
            'last_name': 'User',
            'username': 'unittest.user',
            'access_level': 9,
            'email': 'user@unittest.com'
        })
