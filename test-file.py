from abc import ABC, abstractmethod

class Base_class(ABC):
    def __init__(self, value):
        self._value = value

    @abstractmethod
    def transform(self):
        pass


    #-----
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
    # ---------

class Derived_class(Base_class):
    def transform(self):
        self._value += 10

