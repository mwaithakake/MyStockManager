import sqlite3

class Client:
    def __init__(self, name, email, id=None):
        self.id = id
        self.name = name
        self.email = email

#Saves or updates the current client instance in the database.
    def save(self):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("INSERT INTO clients (name, email) VALUES (?, ?)", (self.name, self.email))
        else:
            cursor.execute("UPDATE clients SET name = ?, email = ? WHERE id = ?", (self.name, self.email, self.id))
        conn.commit()
        conn.close()

#Retrieves all clients from the database.
    @staticmethod
    def get_all():
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clients")
        rows = cursor.fetchall()
        conn.close()
        return rows

#Deletes a client from the database based on its id.
    @staticmethod
    def delete(id):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clients WHERE id = ?", (id,))
        conn.commit()
        conn.close()
