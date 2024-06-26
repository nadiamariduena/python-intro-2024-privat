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
# STEP 6: Define the Special Ice Store class, inheriting from
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
# ADD special TOPPING 🎊
# -----------

    def add_special_topping(self):
        """ADD the special topping 🌶️ to the ice cream"""
        #
        #So, in summary, this line is adding the special topping "Magic Sprinkles" to an ice cream instance (self) using the add_topping method, and it's explicitly specifying that this topping is extra.
        self.add_topping(self.special_topping, extra=True)
        #
        # the .add() method is primarily associated with set objects. Sets are unordered collections of unique elements. The .add() method is used to add a single element to a set. If the element is already present in the set, the set remains unchanged. ( check the example on the md) 🖐️ BUT IN THIS CASE, we are not making use of the add() method but to another function in STEP 3

# ---------------------------
# Test the parent class
# ---------------------------

regular_store = IceCreamStore()
regular_store.add_topping(" chocolate 🍫")
regular_store.add_topping("Nuts 🌰", extra=True)
regular_store.list_toppings()

print("-----/------")

# ** result
# this first result will show you the outcome of the PARENT class
# Available toppings:
# -  chocolate 🍫
# - Nuts 🌰 (Extra $0.8)
# -----/------


# ---------------------------
# Test the child class
# ---------------------------

special_store =  IceCreamStoreInherited()
special_store.add_topping("banana 🍌")
special_store.add_special_topping()
special_store.list_toppings()

# result
# this second result will show you the outcome of the CHILD class
#
# Available toppings:
# - banana 🍌
# - Magic Sprinkles (Extra $0.8)



#
#
# ---------

class ParentClass:
    def __init__(self):
        self.parent_property = "I am a property from the parent class"

    def parent_method(self):
        print("This is a method from the parent class")


class childClass(ParentClass):
    def __init__(self):
        super().__init__() # CALL the __init__ method of the parent class
        self.child_property = "I am a property from the CHILD class"

    def child_method(self):
        print("This is a method from the  CHILD class")




# example usage
child_obj = childClass()
child_obj.parent_method() # ACCESSING method from parent class
print(child_obj.parent_property) # Accessing property from parent class
#
#
child_obj.child_method() # Accessing method from child class
print("child_obj.child_property")

# RESULT

# This is a method from the parent class
# I am a property from the parent class
# This is a method from the  CHILD class
# child_obj.child_property