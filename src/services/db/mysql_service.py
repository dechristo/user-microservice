import _mysql


class MySQLService():

    def __init__(self):
        self.connection = _mysql.connect("localhost", "root", "verysecure", "userms")