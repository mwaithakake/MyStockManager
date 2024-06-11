from sqlalchemy.orm import sessionmaker
from database import engine, create_tables, Session
from models import Product, Supplier

create_tables()

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
    session = Session()
    print("\n=== Add Product ===")
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    supplier_id = int(input("Enter supplier ID: "))
    new_product = Product(name=name, price=price, quantity=quantity, supplier_id=supplier_id)
    session.add(new_product)
    session.commit()
    print("Product added successfully!")
    session.close()

def view_products():
    session = Session()
    print("\n=== Products ===")
    products = session.query(Product).all()
    if products:
        for product in products:
            print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}, Supplier ID: {product.supplier_id}")
    else:
        print("No products found.")
    session.close()

def update_product():
    session = Session()
    print("\n=== Update Product ===")
    id = int(input("Enter product ID to update: "))
    product = session.query(Product).get(id)
    if product:
        product.name = input("Enter new product name: ")
        product.price = float(input("Enter new product price: "))
        product.quantity = int(input("Enter new product quantity: "))
        product.supplier_id = int(input("Enter new supplier ID: "))
        session.commit()
        print("Product updated successfully!")
    else:
        print("Product not found.")
    session.close()

def delete_product():
    session = Session()
    print("\n=== Delete Product ===")
    id = int(input("Enter product ID to delete: "))
    product = session.query(Product).get(id)
    if product:
        session.delete(product)
        session.commit()
        print("Product deleted successfully!")
    else:
        print("Product not found.")
    session.close()

def add_supplier():
    session = Session()
    print("\n=== Add Supplier ===")
    name = input("Enter supplier name: ")
    contact = input("Enter supplier contact: ")
    new_supplier = Supplier(name=name, contact=contact)
    session.add(new_supplier)
    session.commit()
    print("Supplier added successfully!")
    session.close()

def view_suppliers():
    session = Session()
    print("\n=== Suppliers ===")
    suppliers = session.query(Supplier).all()
    if suppliers:
        for supplier in suppliers:
            print(f"ID: {supplier.id}, Name: {supplier.name}, Contact: {supplier.contact}")
    else:
        print("No suppliers found.")
    session.close()

def update_supplier():
    session = Session()
    print("\n=== Update Supplier ===")
    id = int(input("Enter supplier ID to update: "))
    supplier = session.query(Supplier).get(id)
    if supplier:
        supplier.name = input("Enter new supplier name: ")
        supplier.contact = input("Enter new supplier contact: ")
        session.commit()
        print("Supplier updated successfully!")
    else:
        print("Supplier not found.")
    session.close()

def delete_supplier():
    session = Session()
    print("\n=== Delete Supplier ===")
    id = int(input("Enter supplier ID to delete: "))
    supplier = session.query(Supplier).get(id)
    if supplier:
        session.delete(supplier)
        session.commit()
        print("Supplier deleted successfully!")
    else:
        print("Supplier not found.")
    session.close()

def search_products():
    session = Session()
    print("\n=== Search Products ===")
    search_term = input("Enter product name or part of the name to search: ")
    products = session.query(Product).filter(Product.name.like(f'%{search_term}%')).all()
    if products:
        for product in products:
            print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}, Supplier ID: {product.supplier_id}")
    else:
        print("No products found.")
    session.close()

def main():
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

if __name__ == "__main__":
    main()
