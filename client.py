import sqlite3

class Client:
    def __init__(self, name, email, id=None):
        self.id = id
        self.name = name
        self.email = email

    def save(self):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("INSERT INTO clients (name, email) VALUES (?, ?)", (self.name, self.email))
        else:
            cursor.execute("UPDATE clients SET name = ?, email = ? WHERE id = ?", (self.name, self.email, self.id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clients")
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def delete(id):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clients WHERE id = ?", (id,))
        conn.commit()
        conn.close()
