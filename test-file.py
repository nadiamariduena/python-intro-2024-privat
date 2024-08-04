from abc import ABC, abstractmethod

class Base(ABC):
    #🤚
    @abstractmethod
    def abstract_method(self):
        pass


    @classmethod
    def class_method(cls):
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
