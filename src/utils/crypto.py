from cryptography.fernet import Fernet


class Crypto():

    def __init__(self, key):
        if not key:
            raise('A key must be provided for encryption.')
        self.cipher = Fernet(key.encode('utf-8'))

    def encrypt(self, password):
        return self.cipher.encrypt(password.encode('utf-8')).decode('utf-8')

    def decrypt(self, password):
        plain = self.cipher.decrypt(password.encode('utf-8'))
        return bytes(plain).decode('utf-8')