from unittest import TestCase
from tests.mocks.mocks import Mocks
from src.utils.new_user_request_validator import NewUserRequestValidator
from src.custom_exceptions.invalid_request_body import InvalidRequestBody


class NewUserRequestValidatorTest(TestCase):

    def setUp(self):
        self.new_user_request_body = Mocks().USER_MOCK

    def test_empty_request_data_raises_invalid_request_body_exception(self):
        self.assertRaises(InvalidRequestBody, NewUserRequestValidator.validate, {})

    def test_array_request_data_raises_invalid_request_body_exception(self):
        self.assertRaises(InvalidRequestBody, NewUserRequestValidator.validate, [])

    def test_missing_first_name_raises_invalid_request_body_exception(self):
        self.new_user_request_body.pop('first_name')
        self.assertRaises(InvalidRequestBody, NewUserRequestValidator.validate, self.new_user_request_body)

    def test_missing_last_name_raises_invalid_request_body_exception(self):
        self.new_user_request_body.pop('last_name')
        self.assertRaises(InvalidRequestBody, NewUserRequestValidator.validate, self.new_user_request_body)

    def test_missing_username_raises_invalid_request_body_exception(self):
        self.new_user_request_body.pop('username')
        self.assertRaises(InvalidRequestBody, NewUserRequestValidator.validate, self.new_user_request_body)

    def test_missing_password_raises_invalid_request_body_exception(self):
        self.new_user_request_body.pop('password')
        self.assertRaises(InvalidRequestBody, NewUserRequestValidator.validate, self.new_user_request_body)

    def test_missing_access_level_raises_invalid_request_body_exception(self):
        self.new_user_request_body.pop('access_level')
        self.assertRaises(InvalidRequestBody, NewUserRequestValidator.validate, self.new_user_request_body)

    def test_missing_email_raises_invalid_request_body_exception(self):
        self.new_user_request_body.pop('email')
        self.assertRaises(InvalidRequestBody, NewUserRequestValidator.validate, self.new_user_request_body)

    def test_valid_request_body_returns_true(self):
        result = NewUserRequestValidator().validate(self.new_user_request_body)
        self.assertTrue(result)
