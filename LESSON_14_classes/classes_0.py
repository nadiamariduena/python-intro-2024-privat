
# 1 example
#
class Vehicle:

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