from unittest import TestCase
from src.utils.crypto import Crypto
from settings import Settings

class CryptoTest(TestCase):
    def setUp(self):
        self.crypto = Crypto(Settings.KEY)

    def test_encrypt_returns_encrypted_bytes(self):
        encrypted = self.crypto.encrypt("1234")
        self.assertIsInstance(encrypted, str)
        self.assertNotEqual(encrypted, b"1234")

    def test_encrypt_returns_encrypted_bytes_long_text(self):
        encrypted = self.crypto.encrypt("Thinking about a good password")
        self.assertIsInstance(encrypted, str)
        self.assertNotEqual(encrypted, b"Thinking about a good password")

    def test_decrypt_returns_original_string(self):
        encrypted = self.crypto.encrypt("1234")
        decrypted = self.crypto.decrypt(encrypted)
        self.assertIsInstance(encrypted, str)
        self.assertEqual(decrypted, "1234")

    def test_decrypt_returns_original_string_long_text(self):
        encrypted = self.crypto.encrypt("Look how beautiful is the blue sea under the blue sky")
        decrypted = self.crypto.decrypt(encrypted)
        self.assertIsInstance(encrypted, str)
        self.assertEqual(decrypted, "Look how beautiful is the blue sea under the blue sky")