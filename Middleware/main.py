import os
import glob
import time
from data_cipher import DataCipher
from database_connection import DatabaseConnection
from user_data_operations import extract_users, insert_users, count_users
from metrics import calculate_metrics, log_and_save_metrics
from utils import get_key_from_file


# Get the most recently modified file in the directory
files = glob.glob('C:/Users/akhal/OneDrive/Desktop/Projects/minsta/Key_management/Keys/*.*')
latest_file = max(files, key=os.path.getmtime)
key = get_key_from_file(latest_file)

print(f"Key used: {key}, from file: {latest_file}")

cipher = DataCipher(key)

source_dsn = "dbname=ig_clone user=postgres password=easypass host=localhost"
destination_dsn = "dbname=Minsta user=postgres password=easypass host=localhost"

start_time = time.time()

# Extract data from source database
with DatabaseConnection(source_dsn) as source_conn:
    user_data = extract_users(source_conn)
    original_table_size = count_users(source_conn)

# Encrypt the data
encryption_start_time = time.time()
encrypted_user_data = [
    (cipher.encrypt(username), created_at)
    for username, created_at in user_data
]
encryption_end_time = time.time()

# Insert encrypted data into destination database
with DatabaseConnection(destination_dsn) as destination_conn:
    insert_users(destination_conn, encrypted_user_data)
    encrypted_table_size = count_users(destination_conn)

end_time = time.time()

overhead, encryption_speed = calculate_metrics(start_time, end_time, user_data, encryption_start_time, encryption_end_time)

log_and_save_metrics(overhead, original_table_size, encrypted_table_size, encryption_speed, 'C:\\Users\\akhal\\OneDrive\\Desktop\\Projects\\minsta\\Middleware0\\Analysis\\metrics.csv')