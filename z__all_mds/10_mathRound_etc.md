# 🟨Built-in numeric functions

<br>

### ROUND

- similar to js Math.round() (but🔴 they may have slight differences in behavior due to language-specific implementations), check the differences after the code below

```python
#
# ----
gpa = 3.28
#
#  COMPLEX number
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

<br>
<br>

## IMport

- add the **import** at the top

```python
# ----
# you can import the match method like so, and use it on the examples below
import math
#
#
gpa = 3.28
#
#
#
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
#

# ----- MATH
print(math.pi)
#result: 3.141592653589793
#
# ----- math.SQUARE
print(math.sqrt(64))
# result: 8.0
# ----- math.CEIL
print(math.ceil(gpa))
# result: 4
# ----- math.floor
print(math.floor(gpa))
# result: 3

#
```

<br>
<br>

# 🔴 Error if you attempt to cast incorrect data

```python
#  check on the terminal what happens when you try to add the below code , its a different type and you will get an error:
zip_value = int("New York")
# -----
#
#

# result
 zip_value = int("New York")
                ^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'New York'
```
