from abc import ABC

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
    @property
    def value(self):
        return self._value
