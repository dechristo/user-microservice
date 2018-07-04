import MySQLdb


class MySQLService():

    def __init__(self):
        self.connection = MySQLdb.connect("localhost", user="root", passwd="verysecure", db="userms")
        self.connection.autocommit(True)

    def insert_user(self, user):
        cursor = self.connection.cursor()
        query = """INSERT INTO user (first_name, last_name, username, password, access_level, email)
            values(%s, %s, %s, %s, %s, %s);"""
        result = cursor.execute(query,(
                user.first_name,
                user.last_name,
                user.username,
                user.password,
                user.access_level,
                user.email))
        return result

    def find_user_by_id(self, id):
        cursor = self.connection.cursor()
        query = """SELECT id, first_name, last_name, username, access_level, email FROM user WHERE
                   id = %s;"""
        cursor.execute(query, (int(id),))
        result = cursor.fetchone()
        return result

    def delete_user_by_id(self, id):
        cursor = self.connection.cursor()
        query = """DELETE FROM user WHERE id = %s;"""
        result = cursor.execute(query, (int(id),))
        return result
