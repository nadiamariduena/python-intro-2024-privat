# intro
#
#
#
# Define the Pizza class
class Pizza:
    # Constructor method to initialize the pizza with toppings and size
    #
    #
    def __init__(self, toppings, size):
    # - The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
    # - It does not have to be named self , you can call it whatever you like (rainbow, potato but keep it clear), but it has to be the first parameter of any function in the class:

      self.toppings = toppings # properties: toppings
      self.size = size # properties: size


# 🧑‍🍳 Method to bake the pizza
def bake(self):
    print(f"Baking a {self.size}-inch pizza with {', '.join(self.toppings)} toppings!")






