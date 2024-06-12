class IceCreamStore:


    # 1
    def __init__(self):
        """Initialize the
        IceCreamSTore with an empty list of toppings and a default
        extra topping COST
        """
        # ** 2
        self.toppings = []
        self.extra_topping_cost = 0.80 # The cost for extra toppings, because who doesn't love some extra toppings?
    # 3
    def add_topping(self, topping, extra=False):

        """

        Add a topping to the ICE cream

        Args:

        - topping (str): the topping to be added.

        - extra (bool, optional): Whether the topping is extra. Defaults to FALSE

        """
        # 4
        if extra:
            self.toppings.append((topping, self.extra_topping_cost))  # If extra, append with extra cost
        else:

            self.toppings.append((topping, 0)) # Otherwise, no extra cost

