class SampleClass:

    def __init__(self, a):
        ## private varibale or property in Python
        self.__a = a

    ## getter method to get the properties using an object
    def get_a(self):
        return self.__a

    ## setter method to change the value 'a' using an object
    def set_a(self, a):
        self.__a = a




## creating an object
# assign the 10 value to the obj (or whatever variable you want)
# obj = SampleClass(10)
sweetpotato = SampleClass(10)
#
#
## getting the value of 'a' using get_a() method
print(sweetpotato.get_a())

## setting a new value to the 'a' using set_a() method
sweetpotato.set_a(45)

print(sweetpotato.get_a())
