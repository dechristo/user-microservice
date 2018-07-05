from unittest import TestCase
from src.responses.user_json_response import UserJsonResponse
from tests.mocks.mocks import Mocks


class UserJsonResponseTest(TestCase):

    def setUp(self):
        self.user_mock = Mocks().MYSQL_FIND_USER_RESULT_SINGLE
        self.users_mock =  Mocks().MYSQL_ALL_USERS_MOCK
    def test_raise_exception_if_build_parameter_is_none(self):
        self.assertRaises(ValueError, UserJsonResponse.build, {})

    def test_raise_exception_if_build_parameter_length_is_less_than_6(self):
            self.user_mock.pop(0)
            self.assertRaises(ValueError, UserJsonResponse.build, self.user_mock)

    def test_build_returns_correct_json_response_object(self):
       result = UserJsonResponse.build(self.user_mock)
       self.assertEqual(result, {
               "id": self.user_mock[0],
               "first_name": self.user_mock[1],
               "last_name": self.user_mock[2],
               "username": self.user_mock[3],
               "access_level": self.user_mock[4],
               "email": self.user_mock[5]
       })

    def test_build_from_array_returs_correct_json_response_object(self):
        result = UserJsonResponse.build_from_array(self.users_mock)
        self.assertEqual(result, {'data':[{
            'first_name': 'Unit Test',
            'last_name': 'User',
            'username': 'unittest.user',
            'password': 'oooops',
            'access_level': 9,
            'email': 'user@unittest.com'
            },
            {
            "username": "Luke",
            "first_name": "Luke",
            "last_name": "Skywalker",
            "password": "theforce",
            "access_level": 99,
            "email": "lskywalker@sw.com"
            },
            {
            "username": "mbrow",
            "first_name": "Mano",
            "last_name": "Brow",
            "password": "chapisco1000!",
            "access_level": 0,
            "email": "mbrow@warmbluw.com"
            }]}
        )
