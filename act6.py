class Product:
    def __init__(self, product_id, name, details, cost):
        if cost < 0:
            raise ValueError("Cost must be a non-negative value.")
        self.product_id = product_id
        self.name = name
        self.details = details
        self.cost = cost

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Details: {self.details}, Cost: {self.cost}"


class InventoryManager:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, details, cost):
        if product_id in self.products:
            print("Error: This product ID already exists.")
            return
        try:
            self.products[product_id] = Product(product_id, name, details, cost)
            print("Product added successfully!")
        except ValueError as error:
            print(f"Error: {error}")

    def display_products(self):
        if not self.products:
            print("No products available.")
        else:
            for product in self.products.values():
                print(product)

    def modify_product(self, product_id, name=None, details=None, cost=None):
        if product_id not in self.products:
            print("Error: Product not found.")
            return
        try:
            if cost is not None and cost < 0:
                raise ValueError("Cost must be a positive number.")
            if name:
                self.products[product_id].name = name
            if details:
                self.products[product_id].details = details
            if cost is not None:
                self.products[product_id].cost = cost
            print("Product updated successfully!")
        except ValueError as error:
            print(f"Error: {error}")

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print("Product removed successfully!")
        else:
            print("Error: Product not found.")


def main():
    inventory = InventoryManager()
    
    while True:
        print("\nInventory Management System")
        print("[A] Add Product")
        print("[V] View Products")
        print("[M] Modify Product")
        print("[R] Remove Product")
        print("[X] Exit")

        selection = input("Enter your choice: ").upper()

        if selection == 'X':
            print("Closing the program. See you next time!")
            break

        if selection == 'A':
            try:
                product_id = input("Enter Product ID: ")
                name = input("Enter Product Name: ")
                details = input("Enter Product Description: ")
                cost = float(input("Enter Product Cost: "))
                inventory.add_product(product_id, name, details, cost)
            except ValueError:
                print("Error: Invalid cost. Please enter a valid number.")

        elif selection == 'V':
            inventory.display_products()

        elif selection == 'M':
            product_id = input("Enter Product ID to modify: ")
            name = input("Enter new name (leave blank to keep current): ") or None
            details = input("Enter new description (leave blank to keep current): ") or None
            try:
                new_cost = input("Enter new cost (leave blank to keep current): ")
                cost = float(new_cost) if new_cost else None
                inventory.modify_product(product_id, name, details, cost)
            except ValueError:
                print("Error: Invalid cost. Please enter a valid number.")

        elif selection == 'R':
            product_id = input("Enter Product ID to remove: ")
            inventory.remove_product(product_id)

        else:
            print("Invalid option. Please choose a valid one.")


if __name__ == "__main__":
    main()
