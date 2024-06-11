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
<br>

---

<br>
<br>

# CLASSES: objects

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
<br>

# CLASSES: INheritance
