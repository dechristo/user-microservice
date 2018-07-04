import MySQLdb


class MySQLService():

    def __init__(self):
        self.connection = MySQLdb.connect("localhost", user="root", passwd="verysecure", db="userms")
        self.connection.autocommit(True)

    def insert_user(self, user):
        cursor = self.connection.cursor()
        query = """INSERT INTO user (first_name, last_name, username, password, access_level, email)
            values(%s, %s, %s, %s, %s, %s);"""
        cursor.execute(query,(
                user.first_name,
                user.last_name,
                user.username,
                user.password,
                user.access_level,
                user.email))

    def find_user_by_id(self, id):
        cursor = self.connection.cursor()
        query = """SELECT id, first_name, last_name, username, access_level, email FROM user WHERE
                   id = %s;"""
        user_id = int(id)
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        return result