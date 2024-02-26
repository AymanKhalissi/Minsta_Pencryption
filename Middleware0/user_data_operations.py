
def insert_user(conn, cipher, username, created_at):
    encrypted_username = cipher.encrypt(username)
    encrypted_created_at = cipher.encrypt(created_at)
    with conn.cursor() as cur:
        cur.execute("INSERT INTO users (username, created_at) VALUES (%s, %s) RETURNING id;",
                    (encrypted_username, encrypted_created_at))
        user_id = cur.fetchone()[0]
        conn.commit()
    return user_id


# def insert_users(conn, cipher, user_data):
#     with conn.cursor() as cur:
#         for username, created_at in user_data:
#             # Encrypt the username
#             encrypted_username = cipher.encrypt(username)
#             # Insert the encrypted username and plaintext created_at
#             cur.execute(
#                 "INSERT INTO users (username, created_at) VALUES (%s, %s) RETURNING id;",
#                 (encrypted_username, created_at)
#             )
#             user_id = cur.fetchone()[0]
#             print(f"User ID {user_id} inserted")
#         # Commit the transaction after all inserts
#         conn.commit()

def insert_users(conn, cipher, encrypted_username, encrypted_created_at):
    with conn.cursor() as cur:
        # Decrypt the created_at value
        created_at = cipher.decrypt(encrypted_created_at)
        cur.execute(
            "INSERT INTO users (username, created_at) VALUES (%s, %s) RETURNING id;",
            (encrypted_username, created_at)
        )
        user_id = cur.fetchone()[0]
        print(f"User ID {user_id} inserted")
    conn.commit()



def get_user(conn, cipher, user_id):
    with conn.cursor() as cur:
        cur.execute("SELECT username FROM users WHERE id = %s;", (user_id,))
        encrypted_username = cur.fetchone()[0]
        username = cipher.decrypt(encrypted_username)
    return username
