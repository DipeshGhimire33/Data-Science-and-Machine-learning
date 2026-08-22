class Product:
    def __init__(self, product_name: str, product_price: float):
        self.product_name = product_name
        self.product_price = product_price

    def __str__(self):
        return f"{self.product_name}: {self.product_price}"


class User:
    def __init__(self, user_name: str, is_admin=False):
        self.user_name = user_name
        self.is_admin = is_admin
        self.membership = "normal"
        self.cart = ShoppingCart(self)

    def get_membership(self):
        return self.membership


class Admin(User):
    def __init__(self, user_name):
        super().__init__(user_name, is_admin=True)

    def create_admin(self, user, new_admin_name):
        if not self.is_admin:
            print("Only admins can create other admins.")
            return

        new_admin = Admin(new_admin_name)
        print(f"Admin '{new_admin_name}' created.")
        return new_admin

    def set_premium(self, user):
        if not self.is_admin:
            print("Only admins can set premium membership.")
            return

        user.membership = "premium"
        print(f"{user.user_name} is now a premium member.")


class ShoppingCart:
    def __init__(self, user):
        self.user = user
        self.item_list = []

    def add_item(self, product):
        self.item_list.append(product)

    def remove_item(self, product_name):
        for product in self.item_list:
            if product.product_name == product_name:
                self.item_list.remove(product)
                return

        print(f"{product_name} is not in the cart.")

    def calculate_total_cost(self):
        total = sum(
            product.product_price
            for product in self.item_list
        )

        if self.user.membership == "premium":
            total *= 0.90

        return total

    def invoice(self):
        print(f"\n{self.user.user_name} Shopping Invoice")
        print("-" * 30)

        for product in self.item_list:
            print(
                f"{product.product_name}: "
                f"{product.product_price}"
            )

        print("-" * 30)
        print(f"Total: {self.calculate_total_cost():.2f}")