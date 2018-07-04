from src.utils.new_user_request_validator import NewUserRequestValidator
from src.custom_exceptions.invalid_request_body import InvalidRequestBody
from src.services.db.mysql_service import MySQLService
from src.models.user import User
from src.responses.user_json_response import UserJsonResponse

class UserController:

    def __init__(self):
        self.db_service = MySQLService()

    def save_user(self, request_data):
        try:
            self.__parse_request_data(request_data)
            new_user = User(request_data)
            self.db_service.insert_user(new_user)
            return self.__send_response("info", "user successfully created.")
        except InvalidRequestBody as err :
            print(err)
            return self.__send_response("error", err.args[0])

    def find_by_id(self, id):
        try:
            user = self.db_service.find_user_by_id(id)
            user_response = UserJsonResponse.build(user)
            return user_response
        except Exception as err:
            print(err)
            return self.__send_response("error", err)

    @staticmethod
    def __send_response(type, msg):
        return { type: msg }

    @staticmethod
    def __parse_request_data(request_data):
        is_valid = NewUserRequestValidator.validate(request_data)
        return is_valid
