
## 🟡 Useful beginner info or tips

<br>

- __name__ == "__main__" [Go to section](#__main____)




- **__init__** [Go to section](#__init__)



- **__new__** [Go to section](#__new__)

<!-- - <a name="isinstance"></a> -->

-  **SUPER( )** [Go to section](#about__super())



- **isinstance** [Go to section](#isinstance)


<br>
<br>

- **PPRINT:**  TO "prettify" your code result (**indentated** results too) [Go to section](#pretiffy_indentation)


<br>




<br>
<br>


---

<br>
<br>
<br>


## 🟠 Indentation

<br>

#### 🟣 What is it?

- to move a piece of code use the **tab key** to indent the code

 - - 🔸 to reverse the indentation use **Shift+Tab**

https://www.computerhope.com/jargon/s/shift-tab.htm#:~:text=Shift%2BTab%20is%20a%20keyboard,line%20in%20most%20text%20editors.


<br>

<a name="pretiffy_indentation"></a>

## 🌈 TO prettify your code result (indentated results too)


<br>

- use **PPRINT** [READ more |  identation-issues.md](./z_identation-issues.md)

<br>

### other

https://defkey.com/what-means/shift-tab

<br>
<br>

---


<br>
<br>
<br>
<br>

## 🟡 If you have many of this `print("")` on your code, you can remove all of them depending on the situation

- If you remove them add this `\n`

```python
#  print("")
   print("\nYou choose " + str(RPS(player)).
```

<br>

<br>
<br>

---


<br>
<br>

## 🟡 DEF

- to start with a function you will use the **def** that stands for **defining**

```python
def hello():
   print('Hello World')
#
#
# just like in js, you call the function like here below: name + parentheses
hello()
```

<br>
<br>

---


<br>



<a name="__init__"></a>

<br>

## 🟡 `__init__`

- a constructor is a special method within a class that is automatically called when a new instance of the class is created. The constructor method is named `__init__()` and is used to initialize the object's attributes.

<br>

Here's a breakdown of its purpose and usage:

**Initialization:** The primary purpose of a constructor is to initialize the newly created object with any necessary initial values. This typically involves setting the initial state of instance variables (also known as attributes) within the object.

**Automatic Invocation:** When you create a new instance of a class using the class name followed by parentheses (e.g., `obj = MyClass())`, Python automatically invokes the constructor method `__init__().`

**Customization:** You can define the constructor to accept parameters, allowing you to customize the initialization process based on specific values passed during object creation. These parameters are passed as arguments to the `__init__()` method.

<br>

Here's a basic example to illustrate the concept:

<br>

```python
class Person:

   def __init__(self, name, age):
      self.name = name
      self.age = age

# Creating an instance of the Person class
person1 = Person("Alice", 30)

# Accessing attributes of the object

print(person1.name) # output: Alice
print(person1.age) # output: 30

```

<br>
<br>

---


<br>
<br>

## 🟡 NONE

- IN python **none** is neither true or false

<br>
<br>

---


<br>


<a name="__main____"></a>

<br>

## 🟡   `__name__ == "__main__"`

<br>

- `__name__ == "__main__` is like asking, "Am I the main character in this story?" It helps a program know if it's the main program being run or just a helper in another program. This way, it can act differently depending on how it's being used.



<br>

### 🔴 in this scenario (it seems the opposite but...)

- In this scenario, the "main character" or the main script that gets executed when you run the code directly is calculator.py. Let me break down how it works:

#### helper code (no main character)



```python
# calculator.py
# File: statistics.py

# Importing functions from calculator.py
import calculator

# Using the functions from calculator.py
result = calculator.subtract(10, 4)
print("Result of subtraction:", result)

```


 ### main character

```python
# ✋ I will be using the code here
# File: calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# This block will only run if this script is the main program
if __name__ == "__main__":
    # Example usage when run directly
    result = add(5, 3)
    print("Result of addition:", result)
# So, if __name__ == "__main__": is like a signal that tells Python: "Hey, I'm the main box! Do what's inside me when someone wants to play with me directly."
```

#### chatgpt

- The if `__name__ == "__main__"`: block at the end of a Python script is a common idiom used to control whether the script should be executed when it's run directly or when it's imported as a module into another script.

#### 🔴 Here's what it does:

`__name__` is a special variable in Python that holds the name of the current module. If the script is being run directly (i.e., it's the main program), Python sets `__name__` to "`__main__`".
When the script is imported as a module into another script, `__name__` is set to the name of the script.

<br>

In the example you provided, the randomfunfact3() function is defined, and then the script checks if it's being run directly (**name** == "**main**"). If so, it calls the randomfunfact3() function, printing a random fun fact about Kansas. If the script were imported into another Python script, the randomfunfact3() function would still be available for use, but the code inside the if **name** == "**main**": block would not be executed unless explicitly called.

<br>
<br>

---

<br>
<br>

<a name="isinstance"></a>

<br>

## 🟡 isinstance()

##### ChatGPT:

- In Python, `isinstance()` is a built-in function used to check if an object is an instance of a particular class or if it belongs to a subclass of that class. Here's how it works and some key points to understand:

```python

class A:
    pass

obj = A()
print(isinstance(obj, A))  # True, obj is an instance of class A

```

<br>

#### subclasses

```python
class A:
    pass

class B(A):
    pass

obj = B()
print(isinstance(obj, A))  # True, obj is also considered an instance of A

```

<br>

#### another example

```python
def process_data(data):
    if isinstance(data, str):
        return data.upper()
    elif isinstance(data, (list, tuple)):
        return [str(item) for item in data]
    else:
        return str(data)

```

<br>
<br>

---

<br>

## 🟡 `%` is the modulo operator

`%` is the modulo operator, not a percentage calculation.

- The % operator returns the remainder of the division operation. So, x % 2 returns 0 if x is even (because it's divisible by 2 with no remainder), and it returns a non-zero value if x is odd.

#### For example:

```javascript
4 % 2 equals 0 because 4 is evenly divisible by 2.
5 % 2 equals 1 because 5 divided by 2 leaves a remainder of 1.
So, x % 2 == 0 checks if x is divisible by 2 with no remainder, which is true for even numbers.
```

<br>
<br>

---

<br>



<a name="__new__"></a>

<br>

## 🟡  `__new__` Method

source [https://builtin.com/data-science/new-python](https://builtin.com/data-science/new-python#:~:text=In%20Python%2C%20__init__,to%20be%20passed%20to%20it.)

<br>

- `__new__` Method in Python Defined
  In Python, **new** is a static method that’s responsible for creating and returning a new instance of the class. It takes the class as its first argument followed by additional arguments.

<br>

##### example:

```python

class IceCream:
    def __new__(ice_cream_class, flavor):
        # __new__ method creates a new instance of the class
        print(f"Creating a new {flavor} ice cream!")
        #     # In Python, super() is a build-in function used to access methods and properties from a parent class.
        instance = super().__new__(ice_cream_class)
        return instance

    def __init__(self, flavor):
        # __init__ method initializes the instance
        self.flavor = flavor
        print(f"A {self.flavor} ice cream is ready!")

# Creating instances of IceCream using __new__ and __init__
chocolate_ice_cream = IceCream("chocolate")
vanilla_ice_cream = IceCream("vanilla")




```

 <br>

 ##### output

 ```python
Creating a new chocolate ice cream!
A chocolate ice cream is ready!
Creating a new vanilla ice cream!
A vanilla ice cream is ready!

 ```


<br>
<br>

---

<br>

<br>

<a name="about__super()"></a>

<br>

## 🟡 ` super().`

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


## 🔴 More examples [z\_\_all_mds/24_Classes_2%20inheritance](./z__all_mds/24_Classes_2%20inheritance.md)

<br>
<br>

---

<br>


## `f` strings

-  **f-strings** in Python are indeed similar to template literals in other programming languages, such as JavaScript.

```python
name = "Alice"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)

```