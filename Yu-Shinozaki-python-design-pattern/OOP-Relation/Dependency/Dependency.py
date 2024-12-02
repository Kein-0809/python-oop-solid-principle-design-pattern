# 依存 (Dependency)

# クラス: ShoppingCart (依存先)
class ShoppingCart:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def get_items(self):
        return self._items


# クラス: Customer (依存元)
class Customer:
    def __init__(self, name):
        self._name = name

    def checkout(self, cart):
        print(f"{self._name} is checking out with the following items:")
        for item in cart.get_items():
            print(f"- {item}")


# 使用例
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Laptop")
    cart.add_item("Mouse")

    customer = Customer("Alice")
    customer.checkout(cart)  # Customer が一時的に ShoppingCart を利用
