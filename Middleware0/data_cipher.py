from cryptography.fernet import Fernet

class DataCipher:
    def __init__(self, key):
        self.fernet = Fernet(key)

    def encrypt(self, data):
        return self.fernet.encrypt(data.encode()).decode()

    def decrypt(self, data):
        return self.fernet.decrypt(data.encode()).decode()
    
