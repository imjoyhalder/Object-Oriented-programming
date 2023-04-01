products = {}

# Define functions for CRUD operations
def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter product stock: "))
    products[name] = {"price": price, "stock": stock}
    print("Product added successfully")

def update_product():
    name = input("Enter product name: ")
    if name not in products:
        print("Product not found")
        return
    price = float(input("Enter new price: "))
    stock = int(input("Enter new stock: "))
    products[name]["price"] = price
    products[name]["stock"] = stock
    print("Product updated successfully")

def view_products():
    for name, data in products.items():
        print(name, data["price"], data["stock"])

# Define the menu
while True:
    print("1. Add product")
    print("2. Update product")
    print("3. View products")
    choice = input("Enter choice: ")
    if choice == "1":
        add_product()
    elif choice == "2":
        update_product()
    elif choice == "3":
        view_products()
    else:
        print("Invalid choice")