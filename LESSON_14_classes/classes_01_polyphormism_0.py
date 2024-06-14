# The 👾 BIG BOSS pizza class that all the other pizzas look up to

class PizzaBoss:
    def __init__(self, toppings):
        # constructor of the pizza BOSS
        self.toppings = toppings


    # S SPECIAL method to represent the pizza when printed
    def __str__(self):
        return f"A pizza with {', '.join(self.toppings)} toppings 🌶️"

#  Pepperoni Pizza: A cool pizza with pepperoni toppings
class PepperoniPizza(PizzaBoss):

    def __init__(self, toppings):
        #
        #Calls the constructor of the pizza boss
        super().__init__(toppings)
