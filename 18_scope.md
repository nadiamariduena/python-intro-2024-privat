# 📙 Scope

<br>
<br>

### Different type of scopes in Python

- local Scope

- Enclosing Scope (Nonlocal)

- Global Scope

- Built in Scope

<br>
<br>

### Similarities with ReactJS

ReactJS is a JavaScript handles variable scope differently. **However**, some conceptual **similarities** exist (I will add the similarities at the bottom )

<br>
<br>

## LOcal SCOPE

```python

def my_function():
    x = 10  # x is local to my_function
    print(x)

my_function()  #  Outputs: 10
print(x)  # ✋Error: x is not defined outside the function

```

<br>

---

<br>

# nested functions

## Enclosing Scope (Nonlocal):

**Definition:** Variables in the local scope of enclosing functions. Useful in nested functions.

```python
def outer_function():
    x = 5
    def inner_function():
#nonlocal  tells Python that inner_function intends to modify the x variable defined in outer_function's scope. Without nonlocal, inner_function would create a new local variable x within its own scope
        nonlocal x
        x = 10
        print(x)
    inner_function()  # Outputs: 10
    print(x)  # Outputs: 10 (modified by inner_function)✋

outer_function()
#
#
#
#-------- another example ---------
#
#
z_name = 'Sopgia'


z_greeting('john')


# parent
def another():
    # local scope
    z_color:'pink'

    # child function, belongs to the parent local scope
    def z_greeting(z_name):
        print(z_color)
        print(z_name)

    z_greeting('David')

```

- 🔴 🔴 **nonlocal** `nonlocal x` tells Python that inner_function intends to modify the x variable defined in outer_function's scope. Without nonlocal, inner_function would create a new local variable x within its own scope.

<br>

---

<br>

## Global Scope:

**Definition:** Variables defined at the top level of a script or module, outside of any function or class. They can be accessed throughout the module.

```python
x = 20  # Global variable

def my_function():
    global x
    x = 30
    print(x)  # Outputs: 30

my_function()
print(x)  # Outputs: 30 (modified by my_function)
#
#
#
# ------- another example
#
#
name = "Dave"

def greeting(name):
    color = "blue"
    print(color)
    print(name)

greeting("John")

# output
# blue
# John
#
# ------- another example
#
# create another function that will contain the greeting function within this new scope
name = 'Davee'

def greeting(name):
    color = "blue"
    print(color)
    print(name)

greeting("John")
## creating the new scope
print('----')

def anotherscope():
    greeting('Dave')

anotherscope()

# output:

# blue
# John
# ----
# blue
# Dave

```

<br>

---

<br>

## Built-in Scope:

**Definition:** Names that are preassigned in Python. These include functions like **len()**, **range()**, etc.

```python
print(len([1, 2, 3]))  # Outputs: 3 (len is a built-in function)

```

<br>
<br>
