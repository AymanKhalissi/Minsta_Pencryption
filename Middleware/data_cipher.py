from cryptography.fernet import Fernet

class DataCipher:
    def __init__(self, key):
        self.cipher_suite = Fernet(key)

    def encrypt(self, data):
        return self.cipher_suite.encrypt(data.encode()).decode()

    def decrypt(self, data):
        return self.cipher_suite.decrypt(data.encode()).decode()