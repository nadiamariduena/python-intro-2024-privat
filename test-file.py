
#  ABC stands for Abstract Base Class. It's a class provided by the abc module in Python that helps you define abstract base classes.
from abc import ABC, abstractmethod

class Base(ABC):
    #🤚The purpose of the abstract base class (Base) and its derived class (Derived) in this simplified example is to illustrate how abstract methods and properties can be used to manage and interact with state.
    @abstractmethod
    def abstract_method(self):
        print("pass")
        pass


    @classmethod
    def class_method(clsThe purpose of the abstract base class (Base) and its derived class (Derived) in this simplified example is to illustrate how abstract methods and properties can be used to manage and interact with state.):
        print("This is class METHOD")

    @staticmethod
    def static_method():
        print("This is a static method")

    # ---------- interesting
    # 🔓 the @property here below, works as a lock on a box, when you use the lock to look inside the box, it shows you what is inside. the getter method works on the same way, it lets you see the value of something
    #
    @property
    def value(self):
        return self._value

    @value.setter

    # :🔑 the @value.setter, this @value from this setter here, is the key from the @property above, so when you say @value.setter, you are seeing: @property_name.setter

    def value(self, new_value):

        # and here we can now change the old value from @property, to the new_value
        self._value = new_value


# Pass the first class within the parenthesis here below
class Derived(Base):
    def __init__(self, value):
        self._value = value

# then use the abstract function from the class 1 here
    def abstract_method(self):
        print("Implemented abstract method in the 'Derived' function")



d = Derived(10)
d.abstract_method()

print(d.value)
d.value = 20
print(d.value)