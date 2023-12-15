class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name}, price: {self.price}"


class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        string = f"User: {self.user}\nItems:\n"
        for item, cnt in self.products.items():
            string = string + f"{item.name}: {cnt} pcs.\n"
        return string

    def get_total(self):
        self.total = 0
        for items, cnt in self.products.items():
            self.total = self.total + (cnt * items.price)
        return self.total


plane = Item('Airbus A380', 445000000, 'help from the Speedwagon fund', 'large')
print(plane)
stake = Item("wooden stake", 500, "in legends can kill vampyre", "small")
print(stake)
jojo = User('Joseph', "Jostar", "0934474358")
print(jojo)
shopping = Purchase(jojo)
shopping.add_item(plane, 1)
shopping.add_item(stake, 3)
print(shopping.get_total())


lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40
