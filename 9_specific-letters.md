## 🟡 REACH specific letter

## `print(first[1])`

```python
#--- reach specific letter from the vars below
first = 'Laure'
last = "Blaz"

# string index values
print(first[1])
#
# RESULT
a
```

<br>

## `print(first[-1])`

```python

#--- reach specific letter from the vars below
first = 'Laure'
last = "Blaz"

# string index values
print(first[1])
#
print(first[-1])
#result: e

#
# RESULT
# will grab the last letter
e

```

<br><br>

https://pynative.com/python-range-function/

```python
first2 = 'Lorraino'
last2 = "Patsy"
#
#will remove the first and the last one
print(first2[1:-1])
# result: orrain
#
#
print(first2[1:])
# result: orraino
```

<br>
<br>

# Starts with or Ends

## 🟡 BOOLEAN (find if a word contains a specific letter, if yes then TRUE )

```python
#
first2 = 'Lorraino'
last2 = "Patsy"
#
print(first.startswith("D"))
# result: False
# --- check if the variable ends with Z
print(first2.endswith("Z"))
```

<br>
<br>

## 🟡 Boolean type

```python
# BOOLEAN TPE

myvalue = True
x = bool(False)
# check the type
print(type(x))
print(isinstance(myvalue, bool))
```

<br>

---

<br>

# 🟡 NUMERIC types

```python
#
#
#


price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))
# it will check i its true its a number/integer
#result: <class 'int'>
#result: True
```

<br>
<br>

### Float types

https://www.w3resource.com/python-exercises/python-basic-exercise-48.php

```python
# check if it a float type

gpa = 3.28
y = float(1.14)
print(type(gpa))
```

### Write a Python program to parse a string to float or integer.

```python
#-----
# 1 Define a string "n" containing a numeric value
chiffre = "245.256"

# 2 convert the string "chifree" to floating-point number and print the result.
print(float(chiffre))
#result: 245.256

# 3 convert the floating-point to an integer, truncating any decimal part, and print the result.
print(int(float(chiffre)))
# result: 245
```

<br>
<br>

# Complex Number

```python
# Define a complex number and assign it to the variable comp_value
comp_value = 5 + 3j

# Print the data type of the variable comp_value
print(type(comp_value))

# Print the real part of the complex number stored in comp_value
print(comp_value.real)

# Print the imaginary part of the complex number stored in comp_value
print(comp_value.imag)
#
#
# RESULT
<class 'complex'>
5.0
3.0
```

In Python, abs() is a built-in function that returns the absolute value of a number. For real numbers, it's straightforward; it returns the distance of the number from zero on the number line, regardless of its sign.

However, when it comes to complex numbers, the absolute value is a bit different. For a complex number a + bj (where a and b are real numbers and j is the imaginary unit), the absolute value (or modulus) is calculated as the square root of the sum of the squares of the real and imaginary parts.

<br>
<br>

## Complex number

```python
#
#
#  COMPLEX number

comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)



```

<br>
<br>

# 🟨 ROUND

- similar to js Math.round() (but🔴 they may have slight differences in behavior due to language-specific implementations), check the differences after the code below

```python
# ----
gpa = 3.28
#
#
#  COMPLEX number

comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# result: <class 'complex'>
# result: 5.0
# result: 3.0
#
# ----
# abs for absolute
print(abs(gpa))
# result: 3.28

# 🟡  ROUND
# -round a floating-point number to the nearest integer.
#
# #rounding the value
# similar to js Math.round() (but they may have slight differences in behavior due to language-specific implementations), check the MD to see the differences

print(abs(gpa * -1))
# result: 3.28
#
print(round(gpa))
# result: 3
print(round(gpa, 1))
# result: 3.3

```

# (js) Math.round() vs round (python)

```javascript
// javascript
Math.round(4.5); // returns 5
Math.round(4.4); // returns 4
```

<br>

```python
round(4.5) # returns 4
round(4.4) # returns 4
```

- The key difference you might notice is how they handle halfway cases. JavaScript's Math.round() function follows the round half away from zero rule, while Python's round() function follows the round half to even rule, also known as banker's rounding. This means that in Python, if the number is exactly halfway between two integers, it rounds to the nearest even integer.
