# 0
class Pizza:
        #
        # 1 ---------------
    def __init__(self, toppings):
        self.toppings = toppings
        #
        #
        self.slices = 8
        self.slices_eaten = 0 # default, you havent eat anything
        #-----------------
        #
        #
        # 2
    def eat_slice(self):
        if self.slices_eaten < self.slices:
            self.slices_eaten += 1
            self.slices == 1
            print("Once slice down")
        else:
            print("Sorry, the pizza is all gone!")


    #
    #
    # 3 ---------
    @property
    #
    # 4
    def remaining_slices(self):
        return self.slices # look at the STEP 1: self.slices = 8
    # 5
    def add_toppings(self, topping):
        self.toppings.append(topping) # self.toppings = toppings
        print(f"Added {topping} to the toppings!!")
    # 6
    def display_toppings(self):
        print("Toppings on the pizza:")
        #
        # loop on the toppings
        for topping in self.toppings:
            print("-", topping)
    # ---------

# 7 CREATE A PIZZA with some initial toppings
my_pizza = Pizza(["cheese", "pepperoni"])


# 8 Time to eat some slices
# use the step #2 here below
my_pizza.eat_slice()
my_pizza.eat_slice()

# 9 🟡 Forgot how many slices are left? No problem, underscore to the rescue!
#  use the step #4 here below
_ = my_pizza.remaining_slices
print("Remaining slices:", _) # the underscore _ ,  will remembers the last result

# 10 Add some extra toppings
my_pizza.add_toppings("mushrrom")
my_pizza.add_toppings("olives")

# 11 Display toppings
my_pizza.display_toppings()