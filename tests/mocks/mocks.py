class Mocks:

    def __init__(self):
        self.USER_MOCK =  {
            'id': 89,
            'first_name': 'Unit Test',
            'last_name': 'User',
            'username': 'unittest.user',
            'password': 'chapisco100!',
            'access_level': 9,
            'email': 'user@unittest.com'
        }

        self.MYSQL_ALL_USERS_MOCK = ((
            1232,
            'Unit Test',
            'User',
            'unittest.user',
            9,
            'user@unittest.com'
            ),(
            8768,
            "Luke",
            "Skywalker",
            "luke",
            99,
            "lskywalker@sw.com"
            ), (
            24,
            "Mano",
            "Brow",
            "mbrow",
            0,
            "mbrow@warmbluw.com"
        ))

        self.MYSQL_FIND_USER_RESULT_SINGLE = [
            4,
            'Unit Test',
            'User',
            'unittest.user',
            9,
            'user@unittest.com'
        ]