# Pencryption.py

def decrypt_column(conn, table_name, column_name, cipher, limit=None):
    query = f"SELECT {column_name} FROM {table_name}"
    if limit is not None:
        query += f" LIMIT {limit}"
    with conn.cursor() as cur:
        cur.execute(query)
        encrypted_data = cur.fetchall()
    return [(cipher.decrypt(data[0]),) for data in encrypted_data]

