class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative")

        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}"


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        for existing_product in self.products:
            if existing_product.name.lower() == product.name.lower():
                existing_product.quantity += product.quantity
                print("Product quantity updated.")
                return

        self.products.append(product)
        print("Product added to cart.")

    def view_cart(self):
        if not self.products:
            print("Cart is empty.")
            return

        print("\nShopping Cart:")
        for product in self.products:
            print(product)

    def remove_product(self, product_name: str):
        for product in self.products:
            if product.name.lower() == product_name.lower():
                self.products.remove(product)
                print("Product removed successfully.")
                return

        print("Product not found.")

    def calculate_total(self):
        if not self.products:
            print("Cart is empty.")
            return 0

        total_price = sum(p.price * p.quantity for p in self.products)
        print(f"Total price: {total_price}")
        return total_price


# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()

    p1 = Product("Apple", 10, 2)
    p2 = Product("Banana", 5, 3)
    p3 = Product("Apple", 10, 1)  # duplicate to test quantity merge

    cart.add_product(p1)
    cart.add_product(p2)
    cart.add_product(p3)

    cart.view_cart()
    cart.calculate_total()

    cart.remove_product("Banana")
    cart.view_cart()