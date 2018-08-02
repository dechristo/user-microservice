from src.custom_exceptions.existing_user import ExistingUser
from src.utils.crypto import Crypto
from settings import Settings
import MySQLdb


class MySQLService():

    def __init__(self):
        self.connection = MySQLdb.connect(
            Settings.DB_SETTINGS["hostname"],
            user=Settings.DB_SETTINGS["username"],
            passwd=Settings.DB_SETTINGS["password"],
            db=Settings.DB_SETTINGS["db"])
        self.connection.autocommit(True)
        self.crypto = Crypto(Settings.KEY)

    def insert_user(self, user):
        cursor = self.connection.cursor()
        existing_user = self.find_user_by_email(user.email)
        if existing_user:
            raise ExistingUser('An user with this email already exists.', {})
        query = """INSERT INTO user (first_name, last_name, username, password, access_level, email)
            values(%s, %s, %s, %s, %s, %s);"""
        result = cursor.execute(query,(
                user.first_name,
                user.last_name,
                user.username,
                self.crypto.encrypt(user.password).decode('utf-8'),
                user.access_level,
                user.email))
        return result

    def update_user_by_id(self, id, user):
        cursor = self.connection.cursor()
        query = """UPDATE user SET first_name=%s, last_name=%s, username=%s, access_level=%s, email=%s
              WHERE id=%s;"""
        result = cursor.execute(query, (
            user.first_name,
            user.last_name,
            user.username,
            user.access_level,
            user.email,
            id))
        return result

    def get_all_users(self):
        cursor = self.connection.cursor()
        query = """SELECT id, first_name, last_name, username, access_level, email FROM user ;"""
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def find_user_by_name(self, name):
        cursor = self.connection.cursor()
        query = """SELECT id, first_name, last_name, username, access_level, email FROM user
                 WHERE concat(lower(first_name), ' ', lower(last_name)) LIKE %s;"""
        cursor.execute(query, ('%'+name+'%',))
        result = cursor.fetchall()
        return result

    def find_user_by_email(self, email):
        cursor = self.connection.cursor()
        query = """SELECT email FROM user
                       WHERE email = %s;"""
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        return result

    def find_user_by_id(self, id):
        cursor = self.connection.cursor()
        query = """SELECT id, first_name, last_name, username, access_level, email FROM user WHERE
                   id = %s;"""
        cursor.execute(query, (int(id),))
        result = cursor.fetchone()
        return result

    def find_user_by_email_and_password(self, email, password):
        cursor = self.connection.cursor()
        query = """SELECT id, first_name, last_name, username, access_level, email, password FROM user WHERE
                   email = %s;"""
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        decrypted_password = self.crypto.decrypt(result[6])
        if decrypted_password == password:
            return result
        return None

    def delete_user_by_id(self, id):
        cursor = self.connection.cursor()
        query = """DELETE FROM user WHERE id = %s;"""
        result = cursor.execute(query, (int(id),))
        return result
