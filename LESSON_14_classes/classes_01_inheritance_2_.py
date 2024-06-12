class IceCreamStore:


    def __init__(self):
        """Initialize the
        IceCreamSTore with an empty list of toppings and a default
        extra topping COST
        """

    def add_topping(self, topping, extra=False):

        """

        Add a topping to the ICE cream

        Args:

        - topping (str): the topping to be added.

        - extra (bool, optional): Whether the topping is extra. Defaults to FALSE

        """

        if extra:
            self.append((topping, self.extra_topping_cost))  # If extra, append with extra cost

