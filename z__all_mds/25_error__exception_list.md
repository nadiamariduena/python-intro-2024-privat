# \*\* Built-in Exceptions

## Beginner-friendly examples of handling Python exceptions based on common exceptions from the list provided by W3Schools: https://www.w3schools.com/python/python_ref_exceptions.asp

<br>
<br>

## 1) example

### ----- Value ERROR -----

```python
#
#

try:
    num = int(input("Enter a number: "))
    if num < 0:
        # read under this code, about the uses of "raise"
        raise ValueError("Number must be positive")
    print("Number entered:", num)

except ValueError as e:
    print("Invalid input", e)

# ✋ OUTPUT
# if you type: -20 or using the minus, its going to be negative, and it will give you this:
# Enter a number: -10
# Invalid input Number must be positive
#
# BUT if you type a positibe number like: 20 , it will give you this:
# Enter a number: 20
# Number entered: 20
```

<br>
<br>

### QUESTION: what is "raise" and what is it's purpose, is it necessary?

##### chatgpt:

- In Python, raise is a keyword **used to explicitly raise an exception**.

- It **allows you to create custom exceptions or raise built-in exceptions** when certain conditions occur in your code.

- The raise statement is **used to interrupt the normal flow** of the program and transfer control to an exception-handling block.

<br>
<br>
