# based on the example below:
#
# 1 the a is the argument i will be using
# 2  i assign the a to the __a
#
#
# 3 then  on the GETTER, I will get the __a  and its value, and prepare it to be changed(ONLY prepare it)
# 4 then on the SETTER, I take the __a, and actually change the value
# **  so similar to the const [ state, setState] = useState() , read the example on the MD



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
