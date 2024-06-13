import sqlite3

class Supplier:
    def __init__(self, name, contact, id=None):
        self.id = id
        self.name = name
        self.contact = contact

    def save(self):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("INSERT INTO suppliers (name, contact) VALUES (?, ?)", (self.name, self.contact))
        else:
            cursor.execute("UPDATE suppliers SET name = ?, contact = ? WHERE id = ?", (self.name, self.contact, self.id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM suppliers")
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def delete(id):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM suppliers WHERE id = ?", (id,))
        conn.commit()
        conn.close()
