class User():

    def __init__(self, user):
        if not isinstance(user, dict):
            raise ValueError("Invalid user information!")

        self.id = user.get("id")
        self.first_name = user.get("first_name")
        self.last_name = user.get("last_name")
        self.username = user.get("username")
        self.password = user.get("password")
        self.access_level = user.get("access_level")
        self.email = user.get("email")