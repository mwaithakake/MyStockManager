import sqlite3

class Product:
    def __init__(self, name, price, quantity, supplier_id=None, id=None):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier_id = supplier_id

#Saves or updates the current product instance in the database.
    def save(self):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("INSERT INTO products (name, price, quantity, supplier_id) VALUES (?, ?, ?, ?)",
                           (self.name, self.price, self.quantity, self.supplier_id))
        else:
            cursor.execute("UPDATE products SET name = ?, price = ?, quantity = ?, supplier_id = ? WHERE id = ?",
                           (self.name, self.price, self.quantity, self.supplier_id, self.id))
        conn.commit()
        conn.close()

#Retrieves all products from the database.
    @staticmethod
    def get_all():
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        conn.close()
        return rows

#Deletes a product from the database based on its id.
    @staticmethod
    def delete(id):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id = ?", (id,))
        conn.commit()
        conn.close()

#Searches for products in the database based on a partial or complete name match.
    @staticmethod
    def search(name):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + name + '%',))
        rows = cursor.fetchall()
        conn.close()
        return rows
