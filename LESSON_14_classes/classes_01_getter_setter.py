## GETTER & SETTER
class Circle:
    def __init__(self, radius):
        self.radius = radius # Private attribute

    # GETTER method for radius (property)
    @property
    def radius(self):
        return self._radius

    # Setter method from radius property
    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value

