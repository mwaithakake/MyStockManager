from database import Database
import sqlite3

class Supplier:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def save(self):
        db = Database('inventory.db')
        db.cur.execute("INSERT INTO suppliers (name, contact) VALUES (?, ?)", (self.name, self.contact))
        db.conn.commit()
        db.close_connection()

    @staticmethod
    def get_all():
        db = Database('inventory.db')
        db.cur.execute("SELECT * FROM suppliers")
        rows = db.cur.fetchall()
        db.close_connection()
        return rows
    

    def update(self):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()

        cursor.execute("UPDATE suppliers SET name = ?, contact = ? WHERE id = ?",
                       (self.name, self.contact, self.id))

        conn.commit()
        conn.close()

    def delete(self):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()

        cursor.execute("DELETE FROM suppliers WHERE id = ?", (self.id,))

        conn.commit()
        conn.close()

    @staticmethod
    def search_by_name(name):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM suppliers WHERE name LIKE ?", ('%' + name + '%',))
        rows = cursor.fetchall()

        conn.close()
        return rows

