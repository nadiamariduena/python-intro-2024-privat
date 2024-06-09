# intro
#
#
#
# Define the Pizza class
class Pizza:
    # Constructor method to initialize the pizza with toppings and size
    #
    # ** __new__ Method in Python Defined
    # In Python, __new__ is a static method that’s responsible for creating and returning a new instance of the class. It takes the class as its first argument followed by additional arguments.

    # 1
    def __init__(self, toppings, size):
    # - The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
    # - It does not have to be named self , you can call it whatever you like (rainbow, potato but keep it clear), but it has to be the first parameter of any function in the class:

      self.toppings = toppings # properties: toppings
      self.size = size # properties: size


    # 2 🧑‍🍳  Method to bake the pizza
    def bake(self):
        print(f"Baking a {self.size}-inch pizza with {', '.join(self.toppings)} toppings!")

    # 3 🔪 Method to cut the pizza
    def cut(self):
        print("Cutting the pizza into slices")

    # 4 🍽️ Method to serve the pizza
    def serve(self):
        print("Enjoy your delicious pizza")


# 5 Create instances of the Pizza class
# We create two instances of the Pizza class (hawaiian_pizza and pepperoni_pizza) with different toppings and sizes.
hawaiian_pizza = Pizza(["ham", "pineapple"], 12)
pepperoni_pizza = Pizza(["pepperoni", "cheese", "tomato sauce"], 16)

# 6 We then use the methods of each pizza object to bake, cut, and serve the pizzas.
# Make and serve the pizzas
hawaiian_pizza.bake()
hawaiian_pizza.cut()
hawaiian_pizza.serve()