import psycopg2

class DatabaseConnection:
    def __init__(self, dsn):
        self.dsn = dsn
        self.conn = None

    def __enter__(self):
        self.conn = psycopg2.connect(self.dsn)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
