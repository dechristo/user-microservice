from unittest import TestCase
from unittest.mock import patch
from src.controllers.user_controller import UserController
from tests.mocks.mocks import Mocks


class UserControllerTest(TestCase):

    @patch('src.services.db.mysql_service.MySQLService.insert')
    def test_save_user_returns_info_msg_for_successfully_saved_user(self, insert_stub):
        insert_stub.result = {}
        user_controller = UserController()
        result = user_controller.save_user(Mocks().USER_MOCK)
        self.assertEqual(result, {"info":"user successfully created."})

