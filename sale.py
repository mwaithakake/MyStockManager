import sqlite3

class Sale:
    def __init__(self, product_id, client_id, quantity, sale_date, id=None):
        self.id = id
        self.product_id = product_id
        self.client_id = client_id
        self.quantity = quantity
        self.sale_date = sale_date

#Saves or updates the current product instance in the database.
    def save(self):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("INSERT INTO sales (product_id, client_id, quantity, sale_date) VALUES (?, ?, ?, ?)",
                           (self.product_id, self.client_id, self.quantity, self.sale_date))
        else:
            cursor.execute("UPDATE sales SET product_id = ?, client_id = ?, quantity = ?, sale_date = ? WHERE id = ?",
                           (self.product_id, self.client_id, self.quantity, self.sale_date, self.id))
        conn.commit()
        conn.close()


    @staticmethod
    def get_all():
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT sales.id, products.name, clients.name, sales.quantity, sales.sale_date
            FROM sales
            JOIN products ON sales.product_id = products.id
            JOIN clients ON sales.client_id = clients.id
        """)
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def delete(id):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM sales WHERE id = ?", (id,))
        conn.commit()
        conn.close()
