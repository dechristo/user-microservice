from unittest import TestCase
from unittest.mock import patch
from src.controllers.user_controller import UserController
from tests.mocks.mocks import Mocks
from tests.mocks.mysql_mock import MysqlMock


class UserControllerTest(TestCase):

    @patch('MySQLdb.connect')
    @patch('src.services.db.mysql_service.MySQLService.insert_user')
    def test_save_user_returns_info_msg_for_successfully_saved_user(self, insert_stub, db_mock):
        db_mock.return_value = MysqlMock()
        insert_stub.return_value = {'info':'user successfully created.'}
        self.user_controller = UserController()
        result = self.user_controller.save_user(Mocks().USER_MOCK)
        self.assertEqual(result, {'info':'user successfully created.'})

    @patch('MySQLdb.connect')
    @patch('src.services.db.mysql_service.MySQLService.insert_user')
    def test_save_user_returns_error_msg_for_failed_saving_operation(self, insert_stub, db_mock):
        db_mock.return_value = MysqlMock()
        insert_stub.return_value = {}
        self.user_controller = UserController()
        result = self.user_controller.save_user(Mocks().USER_MOCK)
        self.assertEqual(result, {'error': 'user could not be created.'})

    @patch('MySQLdb.connect')
    @patch('src.services.db.mysql_service.MySQLService.find_user_by_id')
    def test_find_user_by_id_returns_array_with_user_info_for_existing_id(self, find_stub, db_mock):
        db_mock.return_value = MysqlMock()
        find_stub.return_value = [4,
            'Unit Test',
            'User',
            'unittest.user',
            9,
            'user@unittest.com'
        ]
        self.user_controller = UserController()
        result = self.user_controller.find_by_id(4)
        self.assertEqual(result, {
            'id': 4,
            'first_name': 'Unit Test',
            'last_name': 'User',
            'username': 'unittest.user',
            'access_level': 9,
            'email': 'user@unittest.com'
        })

    @patch('MySQLdb.connect')
    @patch('src.services.db.mysql_service.MySQLService.delete_user_by_id')
    def test_delete_user_returns_info_msg_for_successfully_deleted_user(self, delete_stub, db_mock):
        db_mock.return_value = MysqlMock()
        delete_stub.return_value = {'info': 'user successfully deleted.'}
        self.user_controller = UserController()
        result = self.user_controller.delete_by_id(Mocks().USER_MOCK['id'])
        self.assertEqual(result, {'info': 'user successfully deleted.'})

    @patch('MySQLdb.connect')
    @patch('src.services.db.mysql_service.MySQLService.delete_user_by_id')
    def test_delete_user_returns_error_msg_for_non_existent_user(self, delete_stub, db_mock):
        db_mock.return_value = MysqlMock()
        delete_stub.return_value = {}
        self.user_controller = UserController()
        result = self.user_controller.delete_by_id(11129)
        self.assertEqual(result, {'error': 'user could not be deleted because wasn`t found.'})

    @patch('MySQLdb.connect')
    @patch('src.services.db.mysql_service.MySQLService.get_all_users')
    def test_get_all_users_returns_array_of_users(self, get_all_stub, db_mock):
        db_mock.return_value = MysqlMock()
        get_all_stub.return_value = Mocks().MYSQL_ALL_USERS_MOCK
        self.user_controller = UserController()
        result = self.user_controller.get_all()
        self.assertIn('data', result)
        self.assertEqual(len(result.get('data')), 3)

    @patch('MySQLdb.connect')
    @patch('src.services.db.mysql_service.MySQLService.find_user_by_name')
    def test_find_user_by_name_returns_array_with_user_info_for_existing_users(self, find_stub, db_mock):
        db_mock.return_value = MysqlMock()
        find_stub.return_value = tuple(filter((lambda user: user[1] == 'Luke'), Mocks().MYSQL_ALL_USERS_MOCK))
        self.user_controller = UserController()
        result = self.user_controller.find_by_name('Luke')
        self.assertIn('data', result)
        self.assertEqual(len(result.get('data')),1)