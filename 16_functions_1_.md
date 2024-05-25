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

## 🍭 ARGS

- The \*args parameter allows you to write a function that can accept a varying number of individual positional arguments in each call

<br>

```python
##  -------
# ARGS
# ----------
# args will work like in javascript
# **

def multiple_items(*args):
        print(args)
        print(type(args))

# tuble list
multiple_items("Dave", "John", "Noaln")
# tuples can't be changed after they're created, but lists can be modified
```
