from database import Database
from product import Product
from supplier import Supplier

def main_menu():
    print("\n=== Inventory Management System ===")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Add Supplier")
    print("6. View Suppliers")
    print("7. Update Supplier")
    print("8. Delete Supplier")
    print("9. Search Products")
    print("10. Exit")

def add_product():
    print("\n=== Add Product ===")
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    supplier_id = int(input("Enter supplier ID: "))  # New field
    product = Product(name, price, quantity, supplier_id)
    product.save()
    print("Product added successfully!")

def view_products():
    print("\n=== Products ===")
    products = Product.get_all()
    if products:
        for product in products:
            print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Quantity: {product[3]}, Supplier ID: {product[4]}")
    else:
        print("No products found.")

def update_product():
    print("\n=== Update Product ===")
    id = int(input("Enter product ID to update: "))
    name = input("Enter new product name: ")
    price = float(input("Enter new product price: "))
    quantity = int(input("Enter new product quantity: "))
    supplier_id = int(input("Enter new supplier ID: "))  # New field
    product = Product(name, price, quantity, supplier_id, id)
    product.save()
    print("Product updated successfully!")

def delete_product():
    print("\n=== Delete Product ===")
    id = int(input("Enter product ID to delete: "))
    Product.delete(id)
    print("Product deleted successfully!")

def add_supplier():
    print("\n=== Add Supplier ===")
    name = input("Enter supplier name: ")
    contact = input("Enter supplier contact: ")
    supplier = Supplier(name, contact)
    supplier.save()
    print("Supplier added successfully!")

def view_suppliers():
    print("\n=== Suppliers ===")
    suppliers = Supplier.get_all()
    if suppliers:
        for supplier in suppliers:
            print(f"ID: {supplier[0]}, Name: {supplier[1]}, Contact: {supplier[2]}")
    else:
        print("No suppliers found.")

def update_supplier():
    print("\n=== Update Supplier ===")
    id = int(input("Enter supplier ID to update: "))
    name = input("Enter new supplier name: ")
    contact = input("Enter new supplier contact: ")
    supplier = Supplier(name, contact, id)
    supplier.update()
    print("Supplier updated successfully!")

def delete_supplier():
    print("\n=== Delete Supplier ===")
    id = int(input("Enter supplier ID to delete: "))
    Supplier.delete(id)
    print("Supplier deleted successfully!")

def search_products():
    print("\n=== Search Products ===")
    search_term = input("Enter product name or part of the name to search: ")
    products = Product.search(search_term)
    if products:
        for product in products:
            print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Quantity: {product[3]}, Supplier ID: {product[4]}")
    else:
        print("No products found.")

def main():
    db = Database('inventory.db')
    db.create_tables()

    while True:
        main_menu()
        choice = input("Enter your choice: ")

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
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    db.close_connection()

if __name__ == "__main__":
    main()
