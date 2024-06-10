
# 1) example
#
class Vehicle:

    #In Python, __init__ is an instance method that initializes a newly created object. It takes the object as its first argument followed by additional arguments.
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("MOves along...")
        #or  print(f"MOves along...{self.model}")


my_car = Vehicle("Tesla", "Model 3")

#
print(my_car.make)
print(my_car.model)

#
my_car.moves()

# OUTPUT
# Tesla
# Model 3
# MOves along...


# 2) example
# ADDING a getter
