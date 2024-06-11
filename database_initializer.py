# database_initializer.py

from database import Database

def initialize_database():
    db = Database('inventory.db')
    db.create_tables()
    db.close_connection()

if __name__ == "__main__":
    initialize_database()
