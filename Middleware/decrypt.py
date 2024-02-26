import random
import glob
import os
from data_cipher import DataCipher
from database_connection import DatabaseConnection
from utils import get_key_from_file

# Get the most recently modified key file in the directory
files = glob.glob('C:/Users/akhal/OneDrive/Desktop/Projects/minsta/Key_management/Keys/*.*')
latest_file = max(files, key=os.path.getmtime)
key = get_key_from_file(latest_file)

cipher = DataCipher(key)

destination_dsn = "dbname=Minsta user=postgres password=easypass host=localhost"

# Fetch data from destination database
with DatabaseConnection(destination_dsn) as destination_conn:
    cursor = destination_conn.cursor()
    cursor.execute("SELECT * FROM users;")
    user_data = cursor.fetchall()

# Select a random row
random_row = random.choice(user_data)

# Decrypt the username
decrypted_username = cipher.decrypt(random_row[1])  # assuming the username is in the second column

print(f"Decrypted username: {decrypted_username}")