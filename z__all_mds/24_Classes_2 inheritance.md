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

<br>
<br>

#### Parent class

- under this parent class i will be adding the **child or inherited class**

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
```

#### child class

```python

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

<br>

# ` super().`

## what is the `super()` method in python?

- In Python, **super()** is a build-in function used to access methods and properties from a parent class.

- 🟢 It return a proxy object that **allows you** to **call methods of** the **superclass** (parent CLASS) in a subclass (child CLASS).

- 🟢 This is **particularly useful in inheritance when you want to extend the functionality of a parent class in a subclass(child)** while still retaining the behavior of the parent class.

<br>

##### Here's how super() is typically used:

```python
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

```

<br>

#### Another example

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

# Creating objects of Dog and Cat classes
my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")

# Calling methods defined in superclass Animal
print(f"{my_dog.name} says {my_dog.sound()}")  # Output: Buddy says Woof!
print(f"{my_cat.name} says {my_cat.sound()}")  # Output: Whiskers says Meow!

```
