class Mocks:

    def __init__(self):
        self.USER_MOCK =  {
            'first_name': 'Unit Test',
            'last_name': 'User',
            'username': 'unittest.user',
            'password': 'oooops',
            'access_level': 9,
            'email': 'user@unittest.com'
        }
        self.MYSQL_FIND_USER_RESULT_SINGLE = [
            4,
            'Unit Test',
            'User',
            'unittest.user',
            9,
            'user@unittest.com'
        ]