# FUNCTIONS

```python


def hello():
   print('Hello World 🍰')
#
#
# just like in js, you call the function like here below: name + parentheses
hello()
## you can only use underscores but not minuses, capital or  uppercase, only lowercase
# hello_world()
```

<br>

### 🍭Parameters

- just like in javascript, you add your parameter within the parenthesis

```python
# num1 and num2 are the paremeters
def sum(num1, num2):
    print(num1 + num2)
#
#
#4. 5 are the arguments
sum(4, 5)
sum(1,7)
sum(100,3)
#
# 9
# 8
# 103

```

<br>
<br>

### another way

```python
##  -------
# Another way
# ----------
#
#
def sumFunction(num3, num4):
    return num3 + num4
total = sumFunction(2, 3)
print(total)
# result: 5
```

<br>
<br>

## 🍭 NONE (nor true or false)

#### Check the type of the data

```python
##  -------
# NONE (nor true or false)
# ----------
#
#
def suma(numm1, numm2):
#the first return from below is called an earlier return. it will ignore the second return
    if (type(numm1) is not int or type(numm2) is not int):
        return
# this if is checking if each of the parameters (numm1 and numm2) are integers, but as you can see i purposely added a letter to get an error
    return numm1 + numm2

total2 = suma("e", 4)
print(total2)
# result: None (because i have a letter which is not an integer but a string)
```

#### if you didnt add anything within here `total = sum() instead of total = sum(4. 5)` you will get this error

```python
in <module>
    total2 = suma( )
             ^^^^^^^
TypeError: suma() missing 2 required positional arguments: 'numm1' and 'numm2'
```

<br>

## 🍭A way to prevent this error, is by adding some **default values**

<br>

```python
# before
def suma(numm1, numm2):
#
#
# after
def suma(numm1, numm2 = 3):
```

<br>
<br>

```python
##  -------
# Another way to pass the arguments on the parameter
# ----------
#
def sumas(param1, param2 = 3):
    if (type(param1) is not int or type(param2) is not int):
        return
    return param1 + param2

totalParam = sumas(1)
print(totalParam)
#result: 4
```

<br>
<br>

## 🍭 `*args` in Python

[source/ geeksforgeeks.org/](https://www.geeksforgeeks.org/args-kwargs-python/)

In this article, we will cover what `**` (double star/asterisk) and **(star/asterisk)** do for parameters in Python, Here, we will also cover args and **kwargs** examples in Python.

- We can pass a variable number of arguments to a function using special symbols.

<br>

### Special Symbols Used for passing arguments in Python:

`*args` (Non-Keyword Arguments)
`**kwargs` (Keyword Arguments)

<br>

### There are two special symbols:

<br>

- The `*args` parameter allows you to write a function that can accept a varying number of individual positional arguments in each call

<br>

#### example 1:

```python
##  -------
# ** ARGS
# ----------
# args will work like in javascript
# ** The *args parameter allows you to write a function that can accept a varying number of individual positional arguments in each call

def multiple_items(*args):
    # as you can see i am not adding names like in the num1 & num2, instead i grab the various values within the multiple_items("Dave"...
        print(args)
        print(type(args))

multiple_items("Dave", "John", "Noaln")
# -----------------  REMEMBER: -----------
#  TUPLES -----
# #tuples can't be changed after they're created, but lists can be modified
# Typically use parentheses (), but can also be created without them by simply separating items with commas.
#my_tuple = (1, 2, 3)  # Using parentheses
#my_tuple = 1, 2, 3    # Without parentheses (still a tuple)
#  LISTS -------
# Use square brackets [].
#my_list = [1, 2, 3]  # Using square brackets
```

<br>

### Example 2:

- Python program to illustrate \*args with a first extra argument

```python
# EXAMPLE 2

def myFun(arg1, *argv):
    print('First argument :', arg1)
    for arg in argv:
        print('Next argument through *argv :', arg)

myFun('Hello', 'Welcome', 'to', 'Paradisse')
# RESULT:
# First argument : Hello
# Next argument through *argv : Welcome
# Next argument through *argv : to
# Next argument through *argv : Paradisse


```

<br>
<br>

## `**kwargs` in Python

<br>

- Using `**kwargs` in Python **allows you to pass a variable number of keyword arguments to a function**. Here's a breakdown of how it works along with additional examples to help you understand its usage better.

```python
def myFunny(**kwargs):
    for key, value in kwargs.items():
        print('%s == %s' % (key,value))
        #The syntax "%s == %s" % (key, value) in Python uses the old-style string formatting (also known as printf-style string formatting). Here, the % operator is used to format a string. Let's break down the components:

myFunny(first='Geeks', mid='for', last='Geeks')

```

### Output

```python
first == Geeks
mid == for
last == Geeks

```

<br>

# 🔴 the old way

### 👾The syntax `"%s == %s"` %

The syntax "%s == %s" % (key, value) in Python uses the old-style string formatting (also known as printf-style string formatting). Here, the % operator is used to format a string. Let's break down the components:

<br>

# Explanation

### Format Specifiers:

`%s`: This is a placeholder for a string. When the string is formatted, %s will be replaced by the corresponding value.

#### example 1

```python
name = "Alice"
age = 30

# Using %s as a placeholder for strings
# alice will be raplaced by the %s which is at the end alice, because alice is within the string and that is the purpose of the %s, to replace the string
print("Name: %s, Age: %s" % (name, age))
#
#Here, the %s in "Name: %s, Age: %s" is replaced by the
# values of name and age.

# OUTPUT:
Name: Alice, Age: 30

```

<br>
<br>

## 2. String with Placeholders

#### example 2

- A string with placeholders (%s) can be designed to include multiple placeholders which will be replaced by corresponding values provided later.

```python
# ✋ as you can see below, Bon IS REPLACED BY THE string which is the %s
template = "Hello, %s! You have %s new messages."

# Placeholder string with two %s placeholders
name = "Bob"
messages = 5

print(template % (name, messages))
# OUTPUT:
Hello, Bob! You have 5 new messages.

```

<br>

In this example, the template "Hello, `%s!` You have %s new messages." contains two `%s` placeholders. When formatted, the first %s is replaced by name and the second `%s` is replaced by messages.

<br>
<br>

## 3. % Operator

The `%` operator is used to provide the actual values that replace the placeholders in the format string. The % operator takes a tuple of values, and each value corresponds to a `%s` in the format string.

<br>

```python
def myFunny(**kwargs):
    for key, value in kwargs.items():
    # Using % operator to replace placeholders with actual values
    print("%s == %s" % (key, value))

#
myFun(first="Geeks", mid="for", last="Geeks")
```

#### output

```python
first == Geeks
mid == for
last == Geeks
```

Here, for each key-value pair in the kwargs dictionary, the string "%s == %s" contains two %s placeholders. The % operator then takes a tuple (key, value) and replaces the placeholders with the actual values of key and value.

<br>
<br>

## COMBINED

```python
def myFune(**kwargs):
    #String with placeholders and format specifiers
    format_string = "%s == %s"
    #Using % operator to provide values that replace the placeholders
    print(format_string % (key, value))
#The % operator takes a tuple (key, value) and substitutes each %s with the respective elements of the tuple.




myFune(first="Geeks", mid="for", last="Geeks")

#first == Geeks
# mid == for
# last == Geeks
```

<br>
<br>

## 🌈 THE new way

- This approach using %s and the % operator is a classic way of string formatting in Python. However, for modern Python code, you might prefer using str.format or f-strings for better readability and flexibility:

#### Using str.format

```python
name = "Alice"
age = 30
# ✋ as you can see the string goes before the .format
formatted_string = "Name: {}, Age: {}".format(name, age)
print(formatted_string)

```
