import sqlite3
#connection of database 
class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

#creation of tables
    def create_tables(self):
        # Create tables if they don't exist
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS suppliers (
                id INTEGER PRIMARY KEY,
                name TEXT,
                contact TEXT
            )
        """)
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
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT
            )
        """)
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY,
                product_id INTEGER,
                client_id INTEGER,
                quantity INTEGER,
                sale_date TEXT,
                FOREIGN KEY (product_id) REFERENCES products(id),
                FOREIGN KEY (client_id) REFERENCES clients(id)
            )
        """)
        #Commits the transaction to save the changes made by executing the SQL statements. 
        self.conn.commit()
        
        #closing of connection
    def close_connection(self):
        self.conn.close()
