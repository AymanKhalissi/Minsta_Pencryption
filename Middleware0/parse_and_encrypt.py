import re
from data_cipher import DataCipher

class StatementParserAndEncryptor:
    def __init__(self, cipher):
        self.cipher = cipher

    def parse_and_encrypt_insert_statement(self, sql):
        # This pattern is designed to capture tuples in the VALUES clause, being more lenient with spaces and quotes
        values_pattern = r"VALUES\s*\((.*?)\),?"
        # Using re.DOTALL to ensure that newline characters inside the VALUES clause are matched as well
        tuples = re.findall(values_pattern, sql, re.IGNORECASE | re.DOTALL)

        if not tuples:
            raise ValueError("SQL statement does not match the expected format or no values found.")

        encrypted_values = []

        for tuple_str in tuples:
            parts = [part.strip().strip("'\"") for part in tuple_str.split(",")]
            if len(parts) != 2:
                print(f"Problematic tuple: {tuple_str}")  # Add this line
                raise ValueError(f"Unexpected format for values tuple: {tuple_str}")

            username, created_at = parts

            # Encrypt the username
            encrypted_username = self.cipher.encrypt(username)
            # Adding encrypted username and plaintext created_at to the list
            encrypted_values.append((encrypted_username, created_at))

        return encrypted_values
