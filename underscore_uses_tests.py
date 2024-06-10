class Pizza:
        #
        # ---------------
    def __init__(self, toppings):
        self.toppings = toppings
        #
        #
        self.slices = 8
        self.slices_eaten = 0
        #-----------------
    def eat_slice(self):
        #
        #
        if self.slices_eaten < self.slices:
            self.slices_eaten += 1
            self.slices == 1
            print("Once slice down")
        else:
            print("Sorry, the pizza is all gone!")


    #
    #
    # ---------
    @property
    def remaining_slices(self):
        return self.slices # look at the top: self.slices = 8

    def add_toppings(self, topping):
        self.toppings.append(topping) # self.toppings = toppings
        print(f"Added {topping} to the toppings!!")

    def display_toppings(self):
        print("Toppings on the pizza:")
        for topping in self.toppings:
            print("-", topping)
    # ---------
