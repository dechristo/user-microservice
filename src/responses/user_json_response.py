class UserJsonResponse:

    @staticmethod
    def build(data):
        if not data or len(data) < 6:
            raise ValueError('Invalid data parameter for building user response.')
        return {
            "id": data[0],
            "first_name": data[1],
            "last_name": data[2],
            "username": data[3],
            "access_level": data[4],
            "email": data[5]
        }

    @staticmethod
    def build_from_array(data):
        if not isinstance(data, tuple):
            raise ValueError('Invalid array data parameter for building user response.')
        result = {
            'data':[UserJsonResponse.build(user) for user in data]
        }
        return result