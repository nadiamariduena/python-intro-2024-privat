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

## Global 🐖

#### what if i wanted to modify the content of a variable inside of a function, that was initially defined on the global scope (outside)

- in this example you will notice that the **1** is going to be modified in the new count = **2**

# EXAMPLE

```python


#-------------
name_b = 'Sully'
# step a: we cannot re assign this
count = 1

def another_b():
    color_b = 'orande'
 # step b: If we do this below (count = 2), it will ignore the count variable containing the 1 that is in step a, that is why that as a result we obtain 2, but that IS NOT THE POINT, we want to reassign a value to the already existent count that is in step a
      count = 2
    print(count)


    def greeting_b(name_b):
        print(color_b)
        print(name_b)

    greeting_b('Darius')

another_b()

#
# output
# 2 ✋ we obtain 2 but its not because we assigned it to the one in step a, so lets find the solution in the next code here below
# orande
# Darius
```

### 🍰 SOLUTION

- 🟠 to REASSIGN it we need to add the **global** key to tell python what we want to do

```python
name_b = 'Sully'
# step a: we cannot re assign this
count = 1

def another_b():
    color_b = 'orande'
# ✋ step b: to reassign it, i will need a global key
    global count
# step c: now i need to add the += with 1 , so step a + step b will give me the 2
    count += 1
# count += 1 increments the global variable count by 1.
    print(count)

    # NESTED
    def greeting_b(name_b):
        print(color_b)
        print(name_b)

    greeting_b('Darius')

another_b()

#
# output
# 2
# orande
# Darius
```

### Lets review the steps

- 1 The `global count` statement inside another_b()

```python
def another_b():
    color_b = 'orande'
# step b: to reassign it, i will need a global key
    global count
```

indicates that **count** refers to the global variable declared outside the function.

<br>

- 2 `count += 1` increments the global variable count by 1.

#### 3 Nested Function and Scope:

`def greeting_b(name_b)`: defines a **nested** function within `another_b()`.

<br>

#### 🌈 Output of the Function:

Calling `another_b()` will print the incremented value of count, which is **2**.
