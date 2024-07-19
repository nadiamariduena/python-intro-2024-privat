# 🟠 underscore(`_`) in python.

- Most of the below info, has been taken from the link below (not with the intention to steal it, but to save it in case they take down their page)

<br>

[SOURCE: www.datacamp.com](https://www.datacamp.com/tutorial/role-underscore-python)

<br>

### Many of the Python Developers don't know about the functionalities of underscore(`_`) in Python. It helps users to write Python code productively.

### Underscore(`_`) is a unique character in Python.

<br>

- If you're a Python programmer, you probably familiar with the following syntax:

`for _ in range(100)`

**init**(self)

`_ = 2` It has some special meaning in different conditions. Let's see all of those.

<br>

- You will find max six different uses of `underscore(_)`. If you want you can use it for different purposes after you have an idea about `underscore(_)`.

#### 1. Use in Interpreter

> Python automatically stores the value of the last expression in the interpreter to a particular variable called `_.` You can also assign these value to another variable if you want.

You can use it as a normal variable. See the **example:**

```python
>>> 5 + 4
9
>>> _     # 🪄 Magic! It remembers the last result
9
>>> _ + 6  # 🌠 Adding more magic, because why not?
15
>>> _     # 🔥  Still on fire with the last result
15
>>> a = _  # 🦸‍♂️ Let's give the hero a cape and a new name
>>> a
15


```

<br>
<br>

### 🟠 Use the `_` in a Pizza management example

```python

# 0
class Pizza:
        #
        # 1 ---------------
    def __init__(self, toppings):
        self.toppings = toppings
        #
        #
        self.slices = 8
        self.slices_eaten = 0 # default, you havent eat anything
        #-----------------
        #
        #
        # 2
    def eat_slice(self):
        if self.slices_eaten < self.slices:
            self.slices_eaten += 1
            # self.slices -= 1
            self.slices == 1
            print("Once slice down")
        else:
            print("Sorry, the pizza is all gone!")


    #
    #
    # 3 ---------
    @property
    #
    # 4
    def remaining_slices(self):
        return self.slices # look at the STEP 1: self.slices = 8
    # 5
    def add_toppings(self, topping):
        self.toppings.append(topping) # self.toppings = toppings
        print(f"Added {topping} to the toppings!!")
    # 6
    def display_toppings(self):
        print("Toppings on the pizza:")
        #
        # loop on the toppings
        for topping in self.toppings:
            print("-", topping)
    # ---------

# 7 CREATE A PIZZA with some initial toppings
my_pizza = Pizza(["cheese", "pepperoni"])

# Define a loop to eat slices until the pizza is all gone
# while my_pizza.remaining_slices > 0:
#     my_pizza.eat_slice()
# Define a loop to eat slices until 8 slices are eaten
for _ in range(8):
    my_pizza.eat_slice()

    # Check if the pizza is all gone
    if my_pizza.remaining_slices == 0:
        print("All slices eaten!")
        break


    #
    #
    #
    #
# 8 Time to eat some slices
# use the step #2 here below
my_pizza.eat_slice()
my_pizza.eat_slice()

# 9 🟡 Forgot how many slices are left? No problem, underscore to the rescue!
#  use the step #4 here below
_ = my_pizza.remaining_slices
print("Remaining slices:", _) # the underscore _ ,  will remembers the last result

# 10 Add some extra toppings
my_pizza.add_toppings("mushrrom")
my_pizza.add_toppings("olives")

# 11 Display toppings
my_pizza.display_toppings()


# result
# Once slice down
# Once slice down
# Remaining slices: 8
# Added mushrrom to the toppings!!
# Added olives to the toppings!!
# Toppings on the pizza:
# - cheese
# - pepperoni
# - mushrrom
# - olives
```

<br>

## Ignoring Values

```python
#
#
# --------------
## ignoring a value
a, _, b = (1, 2, 3) # a = 1, b = 3
print(a, b)

#----------
print("-----------")
#----------
#
## ignoring multiple values
## *(variable) used to assign multiple value to a variable as list while unpacking
## it's called "Extended Unpacking", only available in Python 3.x
a, *_, b = (7, 6, 5, 4, 3, 2, 1)
print(a, b)
# Here, (7, 6, 5, 4, 3, 2, 1) is a tuple. With the unpacking syntax, a will get the first value, b will get the last value, and *_ (denoted by the asterisk followed by an underscore) will hold any values in between. In this case, *_ collects all values except the first and last, which are 6, 5, 4, 3, 2.

# ✋ OUTPUT
# -----------
# 1 3
# -----------
# 7 1
```

<br>

Here, **(7, 6, 5, 4, 3, 2, 1)** is a tuple. With the unpacking syntax, a will get the first value, b will get the last value, and `*_` (denoted by the asterisk followed by an underscore) will hold any values in between.

- In this case, `*_` collects all values except the first and last, which are **6, 5, 4, 3, 2.**

#### another example

```python
pizza = ["crust", "tomato sauce", "cheese", "pepperoni", "mushrooms", "olives", "bell peppers"]

crust, *toppings, last_topping = pizza

print("Pizza with", crust, "and toppings:", toppings)
print("Last topping is:", last_topping)

# output
# Pizza with crust and toppings: ['tomato sauce', 'cheese', 'pepperoni', 'mushrooms', 'olives']
# Last topping is: bell peppers
```

<br>
<br>

## 🟠 Use in Looping

You can use `underscore(_)` as a variable in looping. See the examples below to get an idea.

```python
## lopping ten times using _
for _ in range(5):
    print(_)

## iterating over a list using _
## you can use _ same as a variable
languages = ["Python", "JS", "PHP", "Java"]
for _ in languages:
    print(_)

_ = 5
while _ < 10:
    print(_, end = ' ') # default value of 'end' id '\n' in python. we're changing it to space
    _ += 1

#
#
# ✋ output
# 0
# 1
# 2
# 3
# 4
# Python
# JS
# PHP
# Java
# 5 6 7 8 9

```

<br>
<br>

## 🟠 Separating Digits of Numbers

If you have a long digits number, you can separate the group of digits as you like for better understanding.

**Ex:-** `million = 1_000_000`

**Next**, you can also use `underscore(_)` to separate the binary, octal or hex parts of numbers.

**Ex:-** `binary = 0b_0010, octa = 0o_64, hexa = 0x_23_ab`

Execute all the above examples to see the results.

```python
# OUTPUT
## different number systems
## you can also check whether they are correct or not by coverting them into integer using "int" method
million = 1_000_000
binary = 0b_0010
octa = 0o_64
hexa = 0x_23_ab

print(million)
print(binary)
print(octa)
print(hexa)

```

<br>
<br>

## 🟠 Naming Using `Underscore(_)`

`Underscore(_)` can be used to name variables, functions and classes, etc..,

- Single **Pre** Underscore:- `_variable`

- Single **Post** Underscore:- `variable_`

- Double **Pre** Underscores:- `**variable`

- Double **Pre and Post** Underscores:- `**variable__`

<br>

### `_single_pre_underscore`

`_name`

Single Pre Underscore is used for internal use. Most of us don't use it because of that reason.

See the following example.

```python
class Test:

    def __init__(self):
        self.name = "datacamp"
        self._num = 7

obj = Test()
print(obj.name)
print(obj._num)

# output
datacamp
7


```

single pre underscore doesn't stop you from accessing the single pre underscore variable.

But, single pre underscore effects the names that are imported from the module.

Let's write the following code in the my_funtions file

```python
## filename:- my_functions.py

def func():
    return "datacamp"

def _private_func():
    return 7

```

### Now, if you import all the methods and names from my_functions.py, Python doesn't import the names which starts with a single pre underscore.

```python

>>> from my_functions import *
>>> func()
'datacamp'
>>> _private_func()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name '_private_func' is not defined

```

### You avoid the above error by importing the module normally.

```python
>>> import my_functions
>>> my_functions.func()
'datacamp'
>>> my_functions._private_func()
7

```

<br>
<br>

## single_postunderscore

`name_`

Sometimes if you want to use Python Keywords as a variable, function or class names, you can use this convention for that.

You can avoid conflicts with the Python Keywords by adding an underscore at the end of the name which you want to use.

Let's see the example.

```python
>>> def function(class):
  File "<stdin>", line 1
    def function(class):
                 ^
SyntaxError: invalid syntax
>>> def function(class_):
...     pass
...
>>>

```

## Single Post Underscore

- is used for naming your variables as Python Keywords and to avoid the clashes by adding an underscore at last of your variable name.

```python
>>> def function(class):
  File "<stdin>", line 1
    def function(class):
                 ^
SyntaxError: invalid syntax
>>> def function(class_):
...     pass
...
>>>

```

<br>
<br>

## Double Pre Underscore

`__name`

Double Pre Underscores are used for the name mangling.

Double Pre Underscores tells the Python interpreter to rewrite the attribute name of subclasses to avoid naming conflicts.

**Name Mangling:-** interpreter of the Python alters the variable name in a way that it is challenging to clash when the class is inherited.

```python
class Sample():

    def __init__(self):
        self.a = 1
        self._b = 2
        self.__c = 3
obj1 = Sample()
dir(obj1)

```

```python
['_Sample__c',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_b',
 'a']

```

<br>

The above code returns all the attributes of the class object. Let's see our variables in the attributes list.

self.a variable appears in the list without any change.

self.\_b Variable also appears in the list without any change. As we discussed above, it's just for the internal use.

Is there self.\_\_c variable in the list?

If you carefully look at the attributes list, you will find an attribute called \_Sample\_\_c. This is the name mangling. It is to avoid the overriding of the variable in subclasses.
Let's create another class by inheriting Sample class to see how overriding works.

```python
class SecondClass(Sample):

    def __init__(self):
        super().__init__()
        self.a = "overridden"
        self._b = "overridden"
        self.__c = "overridden"
obj2 = SecondClass()
print(obj2.a)
print(obj2._b)
print(obj2.__c)

```

```python
overridden
overridden



---------------------------------------------------------------------------

AttributeError                            Traceback (most recent call last)

<ipython-input-2-4bf6884fbd34> in <module>()
      9 print(obj2.a)
     10 print(obj2._b)
---> 11 print(obj2.__c)


AttributeError: 'SecondClass' object has no attribute '__c'

```
