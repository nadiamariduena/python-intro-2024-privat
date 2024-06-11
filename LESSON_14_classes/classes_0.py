
# 1) example
# https://youtu.be/RpBBzci_cBk?feature=shared
#
class Vehicle:

    #In Python, __init__ is an instance method that initializes a newly created object. It takes the object as its first argument followed by additional arguments.
    def __init__(self, make, model, place):
        self.make = make
        self.model = model
        self.place = place

    def moves(self):
         print("MOves along...")

    def get_make_model(self):
        # print("MOves along...")
        print(f"John drives a {self.make} '{self.model}' that goes to {self.place} ") # output: John drives a Tesla 'Model 3'
        #or  print(f"MOves along...{self.model}")

    def get_car_to_place(self):
        # print("MOves along...")
        print(f"on direction to {self.place}")




my_car = Vehicle("Tesla", "Model 3", "Oregon")

#
print(my_car.make)
print(my_car.model)
print(my_car.place)

#
my_car.moves()

# OUTPUT
# Tesla
# Model 3
# MOves along...


# 2) example
# lets create more cars from the same class from above

my_car.get_make_model()
my_car.moves()
my_car.get_car_to_place()
###
#
print("---------")
# OBJECTS
# with the below we will be creating another Object based on the same VEHICLE class
#
your_car = Vehicle("Cadillac", "Escalada", "Paris")
your_car.get_make_model()
your_car.moves()
