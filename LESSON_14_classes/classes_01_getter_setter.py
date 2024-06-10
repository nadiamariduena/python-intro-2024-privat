## GETTER & SETTER
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