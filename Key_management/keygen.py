from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os
import base64
import getpass

# Function to generate a new AES key for encryption
def generate_aes_key(passphrase):
    # Generate a random salt
    salt = os.urandom(16)
    # Use PBKDF2HMAC to generate a key derivation function
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    # Generate the key using the provided passphrase and the KDF
    key = base64.urlsafe_b64encode(kdf.derive(passphrase.encode()))
    return key

def save_key_to_file(key, filename):
    # Specify the directory where the key file will be saved
    directory = r'C:\Users\akhal\OneDrive\Desktop\Projects\minsta\Key_management\Keys'
    # Append .key extension if not already there
    if not filename.endswith('.key'):
        filename += '.key'
    # Create the full path for the file
    filepath = os.path.join(directory, filename)
    with open(filepath, 'wb') as file:
        file.write(key)

def main():
    # Ask the user for a passphrase
    passphrase = getpass.getpass("Enter a passphrase for key generation: ")
    # Ask the user for a filename
    filename = input("Enter a filename for the key file (default is 'encryption.key'): ")
    if not filename:
        filename = 'encryption.key'
    # Generate a new AES key
    aes_key = generate_aes_key(passphrase)
    # Save the key to a file
    save_key_to_file(aes_key, filename)
    print(f"AES key generated and saved to file '{filename}' in the directory 'C:\\Users\\akhal\\OneDrive\\Desktop\\Projects\\minsta\\Key_management\\Keys'.")

if __name__ == "__main__":
    main()
