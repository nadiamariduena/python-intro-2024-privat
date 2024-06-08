# Decorators

### Are decorators in python still used?

<br>

#### chapgpt

- Yes, decorators are still widely used in Python.

- They provide a powerful way to modify or extend the behavior of functions or methods without changing their actual implementation.

- **Decorators are commonly used for tasks such as logging, authentication, memoization, and more.**

- They help in keeping the code clean, modular, and readable by separating concerns. So, if you're working in Python, decorators are definitely a tool worth knowing and using when appropriate.

### 1) step

```python
def hello_deco(func):

    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now, inside the wrapper function.
        func()

        print("This is AFTER function execution")

    return inner1
```

### 2) step

```python
#🔴 2
# OUT (on global scope)
# DEFINING a function, to be called inside WRAPPER
def function_to_be_used():
    print("This is INSIDE 🍀 the`function_to_be_used()` ")

# INSIDE (local sc) of the function_to_be_used
#
#passing function_to_be_used inside the decorator to control its behavior
function_to_be_used = hello_deco(function_to_be_used)

# INSIDE (local sc) of the function_to_be_used
#
# calling the function
function_to_be_used()

#result
# before inner1 function 🫐
# Hello, this is before inner1 execution 🍓
# This is INSIDE 🍀 the`function_to_be_used()`
# This is AFTER 🔓 function execution
```

### in what kind of scenarios you can use a similar logic?
