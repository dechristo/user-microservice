from src.utils.new_user_request_validator import NewUserRequestValidator
from src.utils.existing_user_request_validator import ExistingUserRequestValidator
from src.custom_exceptions.invalid_request_body import InvalidRequestBody
from src.services.db.mysql_service import MySQLService
from src.models.user import User
from src.responses.user_json_response import UserJsonResponse

class UserController:

    def __init__(self):
        self.db_service = MySQLService()

    def save_user(self, request_data):
        try:
            self.__parse_new_user_request_data(request_data)
            new_user = User(request_data)
            result = self.db_service.insert_user(new_user)
            if not result:
                return self.__send_response('error', 'user could not be created.')
            return self.__send_response('info', 'user successfully created.')
        except InvalidRequestBody as err :
            print(err)
            return self.__send_response('error', err.args[0])

    def update_user(self, id, request_data):
        try:
            self.__parse_update_user_request_data(request_data)
            new_user_data = User(request_data)
            result = self.db_service.update_user_by_id(id, new_user_data)
            if not result:
                return self.__send_response('error', 'Could not update user information.')
            return self.__send_response('info', 'user information successfully updated.')
        except InvalidRequestBody as err:
            print(err)
            return self.__send_response('error', err.args[0])

    def get_all(self):
        try:
            users = self.db_service.get_all_users()
            users_response = UserJsonResponse.build_from_array(users)
            return users_response
        except Exception as err:
            print(err)
            return self.__send_response('error', err)

    def find_by_id(self, id):
        try:
            user = self.db_service.find_user_by_id(id)
            user_response = UserJsonResponse.build(user)
            return user_response
        except Exception as err:
            print(err)
            return self.__send_response('error', err)

    def delete_by_id(self, id):
        try:
            result =  self.db_service.delete_user_by_id(id)
            if not result:
                return self.__send_response('error', 'user could not be deleted because wasn`t found.')
            return self.__send_response('info', 'user successfully deleted.')

        except Exception as err:
            print(err)
            return self.__send_response('error', err)

    @staticmethod
    def __send_response(type, msg):
        return { type: msg }

    @staticmethod
    def __parse_new_user_request_data(request_data):
        is_valid = NewUserRequestValidator.validate(request_data)
        return is_valid

    @staticmethod
    def __parse_update_user_request_data(request_data):
        is_valid = ExistingUserRequestValidator.validate(request_data)
        return is_valid