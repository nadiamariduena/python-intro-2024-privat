# The 👾 BIG BOSS pizza class that all the other pizzas look up to

class PizzaBoss:
    def __init__(self, toppings):
        self.toppings = toppings


    # S SPECIAL method to represent the pizza when printed
    def __str__(self):
        return f"A pizza with {', '.join(self.toppings)} toppings"