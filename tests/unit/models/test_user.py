from unittest import TestCase
from src.models.user import User

class UserTest(TestCase):

    def setUp(self):
        self.user_mock = {
            'first_name': 'Unit Test',
            'last_name': 'User',
            'username': 'unittest.user',
            'password': 'oooops',
            'access_level': 9,
            'email': 'user@unittest.com'
        }

    def test_raise_exception_with_constructor_parameter_is_invalid(self):
        invalid_param='name;last_name;1234'
        self.assertRaises(ValueError, User, invalid_param)

    def test_constructor_returns_instance_with_correct_values(self):
        user = User(self.user_mock)
        self.assertEqual(user.first_name, 'Unit Test')
        self.assertEqual(user.last_name, 'User')
        self.assertEqual(user.username, 'unittest.user')
        self.assertEqual(user.password, 'oooops')
        self.assertEqual(user.access_level, 9)
        self.assertEqual(user.email, 'user@unittest.com')

