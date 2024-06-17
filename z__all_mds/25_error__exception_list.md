# Built-in Exceptions

#### Beginner-friendly examples of handling Python exceptions based on common exceptions from the list provided by W3Schools: https://www.w3schools.com/python/python_ref_exceptions.asp

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

### 🍊 Purpose of raise:

<br>

**Custom Exceptions:** You can define and raise your own exceptions to handle specific error conditions that may not be covered by built-in Python exceptions.

**Error Propagation:** If a function encounters an error that it cannot handle itself, it can raise an exception to signal to its caller that something unexpected has occurred.

**Control Flow:** raise allows you to control the flow of your program by terminating execution in case of errors or exceptional conditions.

<br>
<br>

### 🍊 Is raise Necessary?

While raise is not always necessary (especially when handling built-in exceptions like ValueError, TypeError, etc., that naturally occur), it is essential for:

**Custom Exceptions:** When you need to define and raise exceptions specific to your application logic or error handling requirements.

**Specific Error Messages:** When you want to provide detailed error messages or additional context to explain why an exception occurred.

<br>
<br>

### 🍊 When Not to Use raise:

**Handling Built-in Exceptions:** Python provides many built-in exceptions `(ValueError, TypeError, ZeroDivisionError, etc.)` that handle common error conditions. You typically don't need to raise these yourself unless you're adding additional context or custom error messages.

**Unnecessary Complexity:** Don't introduce raise unnecessarily if your code does not have specific error conditions that need to be explicitly handled. Overuse of custom exceptions can complicate code without providing significant benefit.
