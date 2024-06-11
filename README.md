MY STOCK MANAGER
Project Description
MY STOCK MANAGER is a simple Python-based application that allows users to manage products and suppliers in a database. The application supports basic CRUD (Create, Read, Update, Delete) operations and establishes relationships between products and suppliers using SQLite as the database.

FEATURES
Product Management: Add, view, update, delete, and search for products.
Supplier Management: Add, view, update, and delete suppliers.
Database: Uses SQLite to store and manage data.
Relationships: Each product can be associated with a supplier.

PROJECT STRUCTURE
main.py: The main entry point of the application. Contains the user interface and main menu.
database.py: Defines the Database class for creating tables and managing database connections.
product.py: Defines the Product class for managing product-related operations.
supplier.py: Defines the Supplier class for managing supplier-related operations.

GETTING STARTED
Prerequisites
Python 3.8.12
SQLite 

INSTALLATION
Clone the repository:
Copy code
git clone https://github.com/mwaithakake/MyStockManager
cd inventory-management-system
Run the application:
python3 database_initializer.py
sqlite3 database.py

Add Product
View Products
Update Product
Delete Product
Add Supplier
View Suppliers
Update Supplier
Delete Supplier
Search Products
Exit
Follow the prompts to manage products and suppliers.

Database Schema
products table:

id (INTEGER PRIMARY KEY)
name (TEXT)
price (REAL)
quantity (INTEGER)
supplier_id (INTEGER, FOREIGN KEY references suppliers(id))
suppliers table:

id (INTEGER PRIMARY KEY)
name (TEXT)
contact (TEXT)
Examples
Adding a Product
Select "Add Product" from the main menu.
Enter the product name, price, quantity, and supplier ID.
Viewing Products
Select "View Products" from the main menu.
A list of products with their details will be displayed.
Updating a Product
Select "Update Product" from the main menu.
Enter the product ID, and the new product details (name, price, quantity, supplier ID).
Deleting a Product
Select "Delete Product" from the main menu.
Enter the product ID to delete.
Searching for Products
Select "Search Products" from the main menu.
Enter the product name or part of the name to search.
Adding a Supplier
Select "Add Supplier" from the main menu.
Enter the supplier name and contact information.
Viewing Suppliers
Select "View Suppliers" from the main menu.
A list of suppliers with their details will be displayed.
Updating a Supplier
Select "Update Supplier" from the main menu.
Enter the supplier ID, and the new supplier details (name, contact).
Deleting a Supplier
Select "Delete Supplier" from the main menu.
Enter the supplier ID to delete.
License
This project is licensed under the MIT License. See the LICENSE file for more information.

Acknowledgements
Inspired by common inventory management systems.
Built using Python and SQLite.
