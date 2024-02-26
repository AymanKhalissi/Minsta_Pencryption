import psycopg2
from user_data_operations import insert_users
import time

key = 'q4Zj1rj9w1piWQ41SEE9u7UIFldRxySayKU-_qU4lK0='  
cipher = DataCipher(key)

# Define the connection parameters for the source and destination databases
source_dsn = "dbname=ig_clone user=postgres password=easypass host=localhost"
destination_dsn = "dbname=Minsta user=postgres password=easypass host=localhost"

# Connect to the source database and fetch the data
with psycopg2.connect(source_dsn) as source_conn:
    with source_conn.cursor() as source_cur:
        source_cur.execute("SELECT username, created_at FROM users")
        user_data = source_cur.fetchall()

# Encrypt the data
encrypted_user_data = [
    (cipher.encrypt(username), cipher.encrypt(created_at))
    for username, created_at in user_data
]

# Connect to the destination database and insert the encrypted data
with psycopg2.connect(destination_dsn) as destination_conn:
    start_time = time.time()
    insert_users(destination_conn, cipher, encrypted_user_data)
    end_time = time.time()
    print(f"Inserted all users in {end_time - start_time} seconds")