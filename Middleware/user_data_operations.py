def extract_users(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT username, created_at FROM users")
        return cur.fetchall()

def insert_users(conn, user_data):
    with conn.cursor() as cur:
        cur.executemany(
            "INSERT INTO users (username, created_at) VALUES (%s, %s)",
            user_data
        )
        conn.commit()

def count_users(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT COUNT(*) FROM users")
        return cur.fetchone()[0]
    
def count_rows(conn, table_name):
    with conn.cursor() as cur:
        cur.execute(f"SELECT COUNT(*) FROM {table_name}")
        return cur.fetchone()[0]