from database import Database
from products import Product
from supplier import Supplier
from client import Client
from sale import Sale
import datetime

#displays the main menu options
def main_menu():
    print("\n=== MyStockManager ===")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Add Supplier")
    print("6. View Suppliers")
    print("7. Update Supplier")
    print("8. Delete Supplier")
    print("9. Search Products")
    print("10. Add Client")
    print("11. View Clients")
    print("12. Update Client")
    print("13. Delete Client")
    print("14. Record Sale")
    print("15. View Sales")
    print("16. Exit")

#Prompts the user to enter details of a new product
def add_product():
    print("\n=== Add Product ===")
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    supplier_id = input("Enter supplier ID (or leave blank): ")
    supplier_id = int(supplier_id) if supplier_id else None
    product = Product(name, price, quantity, supplier_id)
    product.save()
    print("Product added successfully!")

#Prompts the user to view details of a product 
def view_products():
    print("\n=== Products ===")
    products = Product.get_all()
    if products:
        for product in products:
            print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Quantity: {product[3]}, Supplier ID: {product[4]}")
    else:
        print("No products found.")

#Prompts the user to make changes to an existing product
def update_product():
    print("\n=== Update Product ===")
    id = int(input("Enter product ID to update: "))
    name = input("Enter new product name: ")
    price = float(input("Enter new product price: "))
    quantity = int(input("Enter new product quantity: "))
    supplier_id = input("Enter new supplier ID (or leave blank): ")
    supplier_id = int(supplier_id) if supplier_id else None
    product = Product(name, price, quantity, supplier_id, id)
    product.save()
    print("Product updated successfully!")

#Prompts the user to delete a product based on the id of the product
def delete_product():
    print("\n=== Delete Product ===")
    id = int(input("Enter product ID to delete: "))
    Product.delete(id)
    print("Product deleted successfully!")

#Prompts the user to enter details of a new supplier
def add_supplier():
    print("\n=== Add Supplier ===")
    name = input("Enter supplier name: ")
    contact = input("Enter supplier contact: ")
    supplier = Supplier(name, contact)
    supplier.save()
    print("Supplier added successfully!")

#Prompts the user to view details of a supplier
def view_suppliers():
    print("\n=== Suppliers ===")
    suppliers = Supplier.get_all()
    if suppliers:
        for supplier in suppliers:
            print(f"ID: {supplier[0]}, Name: {supplier[1]}, Contact: {supplier[2]}")
    else:
        print("No suppliers found.")

#Prompts the user to make changes to an existing supplier
def update_supplier():
    print("\n=== Update Supplier ===")
    id = int(input("Enter supplier ID to update: "))
    name = input("Enter new supplier name: ")
    contact = input("Enter new supplier contact: ")
    supplier = Supplier(name, contact, id)
    supplier.save()
    print("Supplier updated successfully!")


#Prompts the user to delete a supplier based on the id of the supplier
def delete_supplier():
    print("\n=== Delete Supplier ===")
    id = int(input("Enter supplier ID to delete: "))
    Supplier.delete(id)
    print("Supplier deleted successfully!")

#Prompts the user to search for products in the database based on a partial or complete name match.
def search_products():
    print("\n=== Search Products ===")
    search_term = input("Enter product name or part of the name to search: ")
    products = Product.search(search_term)
    if products:
        for product in products:
            print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Quantity: {product[3]}, Supplier ID: {product[4]}")
    else:
        print("No products found.")

#Prompts the user to enter details of a new client
def add_client():
    print("\n=== Add Client ===")
    name = input("Enter client name: ")
    email = input("Enter client email: ")
    client = Client(name, email)
    client.save()
    print("Client added successfully!")

#Prompts the user to view a client
def view_clients():
    print("\n=== Clients ===")
    clients = Client.get_all()
    if clients:
        for client in clients:
            print(f"ID: {client[0]}, Name: {client[1]}, Email: {client[2]}")
    else:
        print("No clients found.")

#Prompts the user to make changes to an existing client
def update_client():
    print("\n=== Update Client ===")
    id = int(input("Enter client ID to update: "))
    name = input("Enter new client name: ")
    email = input("Enter new client email: ")
    client = Client(name, email, id)
    client.save()
    print("Client updated successfully!")

#Prompts the user to delete a client based on the id of the client
def delete_client():
    print("\n=== Delete Client ===")
    id = int(input("Enter client ID to delete: "))
    Client.delete(id)
    print("Client deleted successfully!")

#Prompts the user to add new sales into the database
def record_sale():
    print("\n=== Record Sale ===")
    product_id = int(input("Enter product ID: "))
    client_id = int(input("Enter client ID: "))
    quantity = int(input("Enter quantity sold: "))
    sale_date = datetime.date.today().strftime('%Y-%m-%d')
    sale = Sale(product_id, client_id, quantity, sale_date)
    sale.save()
    print("Sale recorded successfully!")

#Prompts the user to view the sales recorded in the database
def view_sales():
    print("\n=== Sales ===")
    sales = Sale.get_all()
    if sales:
        for sale in sales:
            print(f"Sale ID: {sale[0]}, Product: {sale[1]}, Client: {sale[2]}, Quantity: {sale[3]}, Sale Date: {sale[4]}")
    else:
        print("No sales found.")

def main():
    db = Database('inventory.db')
    db.create_tables()

    while True:
        main_menu()
        choice = input("Enter the number of the choices given: ")

        if choice == '1':
            add_product()
        elif choice == '2':
            view_products()
        elif choice == '3':
            update_product()
        elif choice == '4':
            delete_product()
        elif choice == '5':
            add_supplier()
        elif choice == '6':
            view_suppliers()
        elif choice == '7':
            update_supplier()
        elif choice == '8':
            delete_supplier()
        elif choice == '9':
            search_products()
        elif choice == '10':
            add_client()
        elif choice == '11':
            view_clients()
        elif choice == '12':
            update_client()
        elif choice == '13':
            delete_client()
        elif choice == '14':
            record_sale()
        elif choice == '15':
            view_sales()
        elif choice == '16':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    db.close_connection()

if __name__ == "__main__":
    main()
