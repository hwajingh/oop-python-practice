"""Corrected companion for oop-python-practice/shoppingcartOOP.ipynb.

The notebook itself was LEFT UNCHANGED (see SUMMARY.md): its single code
cell has broken indentation, a missing colon on clear(), an undefined
global `thisdict`, and a constructor call that does not match its
signature (__init__(self, price, item) called with 3 arguments).
This file is the runnable version of the same idea: a cart that owns
its own dict, instead of referencing a global.

Use it as: python shoppingcartOOP_fixed.py
Or import ShoppingCart and call show()/add()/delete()/clear().
"""


class ShoppingCart:
    """A cart holding item -> price, owned by the instance."""

    def __init__(self):
        self.items = {}

    def show(self):
        print("The shopping list has:")
        for item, price in self.items.items():
            print(f"  {item}: {price}")

    def add(self, item, price):
        self.items[item] = price

    def delete(self, item):
        # discard-style: deleting a missing item is a no-op, not KeyError.
        self.items.pop(item, None)

    def clear(self):
        self.items.clear()

    def total(self):
        return sum(self.items.values())


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add("oranges", 5.99)
    cart.add("apples", 3.00)
    cart.show()
    print(f"Total: {cart.total()}")
    cart.delete("apples")
    cart.show()
