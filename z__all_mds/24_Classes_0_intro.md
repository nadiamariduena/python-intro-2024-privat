## [Python Classes, Objects, Inheritance & Polymorphism for Beginners](https://youtu.be/RpBBzci_cBk?feature=shared)

## What are Classes?

##### chapgpt

Classes are like blueprints that **define how objects should be structured and behave in a program.**

> Think of them as a way to organize and describe the characteristics and actions of things you want to represent in your code.

[code academy | classes](https://www.codecademy.com/resources/docs/python/classes)

In Python, **classes** are defined using the class keyword. The **first letter** of the name of the class is always **capitalized.**

```python
class Pizza:
  # Class body starts here
```

### class definitions cannot be empty

- In Python, a class definition cannot be empty. It must contain at least one statement. However, there are scenarios where you may want to define a class without immediately implementing its methods or properties. In such cases, you can use the pass statement as a placeholder to avoid syntax errors.

#### Pass

- The pass statement in Python is a null operation that does nothing. It's used as a placeholder where syntactically a statement is required, but no action needs to be taken. It's commonly used in situations like:

```python
class Pizza:
    pass  # Placeholder statement to avoid syntax error

```

- This ensures that the class definition is valid syntactically, and you can later come back and implement the methods and properties as needed.

<br>
<br>

#### Basic exercises

```python

# 1 example
#
class Vehicle:

    #In Python, __init__ is an instance method that initializes a newly created object. It takes the object as its first argument followed by additional arguments.
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("MOves along...")
        # or  print(f"MOves along...{self.model}") , print(f"John drives a {self.make} '{self.model}'")


my_car = Vehicle("Tesla", "Model 3")

#
print(my_car.make)
print(my_car.model)

#
my_car.moves()

# OUTPUT
# Tesla
# Model 3
# MOves along...


```

<br>

### updated example

```python

# 1) example
# https://youtu.be/RpBBzci_cBk?feature=shared
#
#
# -----  CLASSES  -----
# - here below i will create the first class.
# - More at the bottom you will find objects , inheritance
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
```

<br>
<br>

---

<br>
<br>

# 🟠CLASSES: objects

- based on the above code, I will be creating the **object**

```python
# ----- OBJECTS  -----
#

# with the below we will be creating another Object based on the same VEHICLE class
#
your_car = Vehicle("Cadillac", "Escalada", "Paris")
your_car.get_make_model()
your_car.moves()


```

<br>

### updated code

```python

# 1) example
# https://youtu.be/RpBBzci_cBk?feature=shared
#
#
# -----  CLASSES  -----
# - here below i will create the first class.
# - More at the bottom you will find objects , inheritance
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
#
# ----- OBJECTS  -----
#

# with the below we will be creating another Object based on the same VEHICLE class
#
your_car = Vehicle("Cadillac", "Escalada", "Paris")
your_car.get_make_model()
your_car.moves()


#
# ----- INHERITANCE  -----
# Now I will create classes that depends on the ABOVE class ( the VEHICLE)

#
#
#
## ... CONTINUE below
```

<br>
<br>

# 🟠CLASSES: [Inheritance](https://www.w3schools.com/python/python_inheritance.asp)

### Inheritance allows us to define a class that inherits all the methods and properties from another class.

**Parent class** 🧑‍🦲 is the class being inherited from, also called base class.

**Child class** 👶 is the class that inherits from another class, also called derived class.

<br>

#### question:

so inheritance classes in python, works like the 🍰 **gremlins** react when pured water?

##### chatgpt:

Haha, that's an interesting comparison!

- In Python, inheritance allows a class to inherit attributes and methods from another class, which can be a bit like multiplying the functionality, much like the gremlins multiplying when they come in contact with water 🌧️.

But unlike the **gremlins...** inheritance in Python is usually a good thing!

- It helps in creating hierarchical relationships between classes, promoting code reusability, and making your code more organized and easier to maintain. Plus, you won't have to worry about your code causing chaos if it encounters water!

#### example 1

```python
class ParentClass:
    def __init__(self):
        self.parent_property = "I am a property from the parent class"

    def parent_method(self):
        print("This is a method from the parent class")


class childClass(ParentClass):
    def __init__(self):
        super().__init__() # CALL the __init__ method of the parent class
        self.child_property = "I am a property from the CHILD class"

    def child_method(self):
        print("This is a method from the  CHILD class")




# example usage
child_obj = childClass()
child_obj.parent_method() # ACCESSING method from parent class
print(child_obj.parent_property) # Accessing property from parent class
#
#
child_obj.child_method() # Accessing method from child class
print("child_obj.child_property")

# RESULT

# This is a method from the parent class
# I am a property from the parent class
# This is a method from the  CHILD class
# child_obj.child_property
```

<br>
<br>

## Example 2

```python
 # ** 0
class IceCreamStore:


    # ** 1 INIT ---------------
    #
    def __init__(self):
        """Initialize the
        IceCreamSTore with an empty list of toppings and a default
        extra topping COST
        """
        # ** 2
        self.toppings = []
        self.extra_topping_cost = 0.80 # The cost for extra toppings, because who doesn't love some extra toppings?
    # -------------------------
    #
    #
    #
    #
    # ** 3 ---- ADD TOPPING
    #
    def add_topping(self, topping, extra=False):

        """

        Add a topping to the ICE cream

        Args:

        - topping (str): the topping to be added.

        - extra (bool, optional): Whether the topping is extra. Defaults to FALSE

        """
        # ** 4 ---- EXTRA
        # conditional for extra topping
        #
        if extra:
            self.toppings.append((topping, self.extra_topping_cost))  # If extra, append with extra cost
        else:

            self.toppings.append((topping, 0)) # Otherwise, no extra cost
        #
        #
        # ---------


    # ** 5 ---- LIST of Toppings
    #
    def list_toppings(self):
        """
       🗒️ List all available toppings, indicating if they are extra or not."""

        print("Available toppings:")

        #
        # iterate on topping
        #
        for topping, cost in self.toppings:
            if cost == 0:
                print("- " + topping)
            else:
                print("- " + topping + " (Extra $" + str(cost) +  ")")


#
#

# ** --------- inherited class ------------
# STEP 6: Define the Special Ice Store class, inheriting from
class IceCreamStoreInherited(IceCreamStore):
    def __init__(self):
          """🍦Initialize the IceCreamStoreInherited, calling the parent class's __init__ method. 🍦"""
          #
          #🤚
          super().__init__() # Call the __init__ method of the parent class
          self.special_topping = "Magic Sprinkles" # The special topping that adds a touch of magic
          #
          # ** - super() is a built-in function used to access methods and properties from a parent class.
          # - It returns a proxy object that allows you to call methods of the superclass (parent class) in a subclass (child class).

#
#
# -----------
# ADD special TOPPING 🎊
# -----------

    def add_special_topping(self):
        """ADD the special topping 🌶️ to the ice cream"""
        #
        #So, in summary, this line is adding the special topping "Magic Sprinkles" to an ice cream instance (self) using the add_topping method, and it's explicitly specifying that this topping is extra.
        self.add_topping(self.special_topping, extra=True)
        #
        # the .add() method is primarily associated with set objects. Sets are unordered collections of unique elements. The .add() method is used to add a single element to a set. If the element is already present in the set, the set remains unchanged. ( check the example on the md) 🖐️ BUT IN THIS CASE, we are not making use of the add() method but to another function in STEP 3

# ---------------------------
# Test the parent class
# ---------------------------

regular_store = IceCreamStore()
regular_store.add_topping(" chocolate 🍫")
regular_store.add_topping("Nuts 🌰", extra=True)
regular_store.list_toppings()

print("-----/------")

# ** result
# this first result will show you the outcome of the PARENT class
# Available toppings:
# -  chocolate 🍫
# - Nuts 🌰 (Extra $0.8)
# -----/------


# ---------------------------
# Test the child class
# ---------------------------

special_store =  IceCreamStoreInherited()
special_store.add_topping("banana 🍌")
special_store.add_special_topping()
special_store.list_toppings()

# result
# this second result will show you the outcome of the CHILD class
#
# Available toppings:
# - banana 🍌
# - Magic Sprinkles (Extra $0.8)



```
