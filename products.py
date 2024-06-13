import sqlite3

class Product:
    def __init__(self, name, price, quantity, supplier_id=None, id=None):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier_id = supplier_id

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

    @staticmethod
    def get_all():
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def delete(id):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    @staticmethod
    def search(name):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + name + '%',))
        rows = cursor.fetchall()
        conn.close()
        return rows
