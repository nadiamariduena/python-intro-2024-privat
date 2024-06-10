## GETTER & SETTER (the first example will be boring asf, next one will be interesting)
class Circle:
    def __init__(self, radius):
        self.radius = radius # Private attribute

    # GETTER method for radius (property)
    # ** you need to declare both @property and @radius.setter decorators if you want to use both the getter and setter methods within a single property in Python.
    @property
    def radius(self):
        return self._radius

    # Setter method from radius property
    # ** you need to declare both @property and @radius.setter decorators if you want to use both the getter and setter methods within a single property in Python.
    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            print("Invalid radius, Please provide a positive value.")

# Create an instance of Circle
my_circle = Circle(5)


# Get the radius (via property)
print("Circle radius (via property):", my_circle.radius)

my_circle.radius = 10
print("Circle radius (after setting via property):", my_circle.radius)


#
#
#-----------
# CAR example
# -----------
#
#
class Car:

    def __init__(self, make, model,year): #3args
        self.make = make
        self.model = model
        self.year = year

   # Getter method for year attribute
    def get_year(self):
        return self._year

   # SETTER method for year attribute with validation
    def set_year(self, year):
        # if the inst is an integer
        if isinstance(year, int) and year > 0:
            self._year = year
        else:
            print("Invalid year value. Please provide a positive integer")


#Create an intance of the car class
my_car = Car("Toyota", "Camry", 2015)

# Accessing the year using the GETTER method



