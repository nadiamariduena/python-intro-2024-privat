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
