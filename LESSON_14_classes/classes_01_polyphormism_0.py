# The 👾 BIG BOSS pizza class that all the other pizzas look up to
#🔴
class PizzaBoss:
    def __init__(self, toppings):
        # constructor of the pizza BOSS
        self.toppings = toppings
        # REMEMBER: a constructor is a special method within a class that is automatically called when a new instance of the class is created. The constructor method is named __init__() and is used to initialize the object's attributes.


    # S SPECIAL method to represent the pizza when printed
    def __str__(self):
        return f"A pizza with {', '.join(self.toppings)} toppings 🌶️"
#----------
#
#
#
#


# 🟠 Pepperoni Pizza: A cool pizza with pepperoni toppings
class PepperoniPizza(PizzaBoss):

    def __init__(self, toppings):
        #
        #Calls the constructor of the pizza boss
        super().__init__(toppings)
        #In Python, **super()** is a build-in function used to access methods and properties from a parent class.


        # A special method only for veggie pizza
    def cook(self):
        return "Cooking Pepperoni Pizza"
#----------
#
#
#
#
# 🟠 Veggie Pizza: A groovy pizza loaded with veggies
class VeggiePizza(PizzaBoss):
    def __init__(self, toppings):
        # Calls the constructor of the pizza boss
        super().__init__(toppings)

    # A special method only for Veggie Pizza
    def cook(self):
        return "Cooking veggie pizza"

#
#
#
#

#----------
# 🟠 BBQ Chickent Pizza: A sizzling pizza topped with BBQ chicken
class BBQChickenPizza(PizzaBoss):
    def __init__(self, toppings):
        # Calls the constructor of the pizza boss
        super().__init__(toppings)

        # A special method only for BBQ Chicken Pizza
    def cook(self):
         return "Cooking BBQ chicken pizza"
#----------
#
#
#
#
pizzas  = [
    PepperoniPizza(["cheese", "pepperoni"]),
    VeggiePizza([""])
]