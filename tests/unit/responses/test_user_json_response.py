from unittest import TestCase
from src.responses.user_json_response import UserJsonResponse
from tests.mocks.mocks import Mocks


class UserJsonResponseTest(TestCase):

    def setUp(self):
        self.user_mock = Mocks().MYSQL_FIND_USER_RESULT_SINGLE

    def test_raise_exception_if_build_parameter_is_none(self):
        self.assertRaises(ValueError, UserJsonResponse.build, {})

    def test_raise_exception_if_build_parameter_length_is_less_than_6(self):
            self.user_mock.pop(0)
            self.assertRaises(ValueError, UserJsonResponse.build, self.user_mock)

    def test_build_returns_correct_response_object(self):
       result = UserJsonResponse.build(self.user_mock)
       self.assertEqual(result, {
               "id": self.user_mock[0],
               "first_name": self.user_mock[1],
               "last_name": self.user_mock[2],
               "username": self.user_mock[3],
               "access_level": self.user_mock[4],
               "email": self.user_mock[5]
       })

