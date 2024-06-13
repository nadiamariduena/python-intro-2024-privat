 # ** 0
class IceCreamStore:


    # ** 1 INIT ---------------
    #
    def __init__(self):
        """Initialize the
        IceCreamSTore with an empty list of toppings and a default
        extra topping COST
        """
        # ** 2
        self.toppings = []
        self.extra_topping_cost = 0.80 # The cost for extra toppings, because who doesn't love some extra toppings?
    # -------------------------
    #
    #
    #
    #
    # ** 3 ---- ADD TOPPING
    #
    def add_topping(self, topping, extra=False):

        """

        Add a topping to the ICE cream

        Args:

        - topping (str): the topping to be added.

        - extra (bool, optional): Whether the topping is extra. Defaults to FALSE

        """
        # ** 4 ---- EXTRA
        # conditional for extra topping
        #
        if extra:
            self.toppings.append((topping, self.extra_topping_cost))  # If extra, append with extra cost
        else:

            self.toppings.append((topping, 0)) # Otherwise, no extra cost
        #
        #
        # ---------


    # ** 5 ---- LIST of Toppings
    #
    def list_toppings(self):
        """
       🗒️ List all available toppings, indicating if they are extra or not."""

        print("Available toppings:")

        #
        # iterate on topping
        #
        for topping, cost in self.toppings:
            if cost == 0:
                print("- " + topping)
            else:
                print("- " + topping + " (Extra $" + str(cost) +  ")")


#
#

# ** --------- inherited class ------------
# STEP 2: Define the Special Ice Store class, inheriting from

class IceCreamStoreInherited(IceCreamStore):
    def __init__(self):
          """🍦Initialize the IceCreamStoreInherited, calling the parent class's __init__ method. 🍦"""
          #
          #🤚
          super().__init__() # Call the __init__ method of the parent class
          self.special_topping = "Magic Sprinkles" # The special topping that adds a touch of magic
          #
          # ** - super() is a built-in function used to access methods and properties from a parent class.
          # - It returns a proxy object that allows you to call methods of the superclass (parent class) in a subclass (child class).

#
#
# -----------
# ADD special TOPPING
# -----------

    def add_special_topping(self):
        """ADD the special topping 🌶️ to the ice cream"""
        self.add_topping(self.special_topping, extra=True)