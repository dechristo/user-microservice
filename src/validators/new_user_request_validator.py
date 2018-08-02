from src.custom_exceptions.invalid_request_body import InvalidRequestBody

class NewUserRequestValidator:

    @staticmethod
    def validate(request_data):
        if not request_data or not isinstance(request_data, dict):
            raise InvalidRequestBody('Body for new user request is empty!', [])
        if not 'first_name' in request_data:
            raise InvalidRequestBody('Body for new user request is invalid: [first_name] is missing',[])
        if not 'last_name' in request_data:
            raise InvalidRequestBody('Body for new user request is invalid: [last_name] is missing',[])
        if not 'username' in request_data:
            raise InvalidRequestBody('Body for new user request is invalid: [username] is missing',[])
        if not 'password' in request_data:
            raise InvalidRequestBody('Body for new user request is invalid: [password] is missing',[])
        if not 'access_level' in request_data:
            raise InvalidRequestBody('Body for new user request is invalid: [access_level] is missing', [])
        if not 'email' in request_data:
            raise InvalidRequestBody('Body for new user request is invalid: [email] is missing',[])

        return True

