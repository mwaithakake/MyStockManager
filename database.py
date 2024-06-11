import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def create_tables(self):
        # Create suppliers table
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS suppliers (
                id INTEGER PRIMARY KEY,
                name TEXT,
                contact TEXT
            )
        """)

        # Create products table with foreign key to suppliers
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price REAL,
                quantity INTEGER,
                supplier_id INTEGER,
                FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
            )
        """)

        self.conn.commit()

    def close_connection(self):
        self.conn.close()
