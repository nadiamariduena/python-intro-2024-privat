# Decorators

### Are decorators in python still used?

<br>

#### chapgpt

- Yes, decorators are still widely used in Python.

- They provide a powerful way to modify or extend the behavior of functions or methods without changing their actual implementation.

- **Decorators are commonly used for tasks such as logging, authentication, memoization, and more.**

- They help in keeping the code clean, modular, and readable by separating concerns. So, if you're working in Python, decorators are definitely a tool worth knowing and using when appropriate.

<br>
<br>

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

### the code

```python
#🔴 1
# OUT (on global scope)
def hello_deco(func):

    print("before inner1 function 🫐")
    # INSIDE (local sc) of the hello_deco()
    def inner1():
        print("Hello, this is before inner1 execution 🍓")

        # calling the actual function now, inside the wrapper function.
        func()
        #🌈 here the step 2 will show the print of the 'function_to_be_called', then it will show the final print 'after', check the result at the bottom

        print("This is AFTER 🔓 function execution")

    return inner1


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

<br>
<br>

---

<br>

### 🍭 in what kind of scenarios can ou use a similar logic?

#### chatgpt

- This pattern of using decorators to wrap functions with additional behavior can be useful in various scenarios:

**Logging:** You can use a decorator to log information before and after a function is called. This can help in debugging or tracking the flow of execution in your code.

**Authentication/Authorization:** Similar to the example you provided, you can use decorators to ensure that a user is authenticated before allowing them to access certain functions or endpoints.

**Caching/Memoization:** Decorators can be used to cache the results of expensive function calls, so that if the same inputs are provided again, the function can return the cached result instead of recalculating it.

**Timing:** You can use decorators to measure the execution time of functions, helping you identify performance bottlenecks in your code.

**Retry Logic:** Decorators can be used to automatically retry a function if it fails due to certain exceptions, with customizable retry strategies (e.g., exponential backoff).

**Rate Limiting:** Decorators can enforce rate limits on function calls, ensuring that they are not called too frequently within a certain time period.

<br>
<br>

### Logging

- consider a scenario where we have a list of user objects with both usernames and passwords, and we want to log each authentication attempt. We'll simulate this scenario by using a list of dictionaries as a mock user database:

```python
# Mock user database
# We have a mock user database (users) containing dictionaries with usernames and passwords.

#
users = [
    {"username": "alice", "password": "password123"},
    {"username": "bob", "password": "securepassword"},
    {"username": "charlie", "password": "strongpassword"},
]

def log_authentication(func):
    def wrapper(username, password):
        print(f"Authenticating user: {username}")
        # Simulate authentication by checking the username and password against the mock user database
        authenticated = False
        for user in users:
            if user["username"] == username and user["password"] == password:
                authenticated = True
                break
        if authenticated:
            print(f"User '{username}' authenticated successfully")
        else:
            print(f"Authentication failed for user '{username}'")
        return func(username, password)
    return wrapper

# Applying the decorator to a function
@log_authentication
def authenticate_user(username, password):
    # This function could contain more complex authentication logic, but for simplicity, we'll just return True or False
    authenticated = False
    for user in users:
        if user["username"] == username and user["password"] == password:
            authenticated = True
            break
    return authenticated

# Simulate authentication attempts
authentication_attempts = [
    {"username": "alice", "password": "password123"},
    {"username": "bob", "password": "wrongpassword"},
    {"username": "charlie", "password": "strongpassword"},
]

# Authenticate each user
for attempt in authentication_attempts:
    username = attempt["username"]
    password = attempt["password"]
    result = authenticate_user(username, password)
    print(f"Authentication result for '{username}': {result}")

```

<br>
<br>

---

<br>

# 🍭 are decorators similar to callback?

##### ChatGPT

- Decorators and callbacks serve somewhat different purposes, but they share some similarities, especially in terms of their usage patterns.

**Purpose:**

<u>Decorators</u> are primarily used to add additional functionality to functions or methods without modifying their original code. They wrap the original function with another function, enabling you to execute code before and/or after the original function call.

<u>Callbacks</u>, on the other hand, are functions that are passed as arguments to other functions. They are meant to be called by the receiving function at certain predetermined points or in response to certain events.

### ✋ MY question to the below text

:checkered_flag: when you said:

> Callbacks, on the other hand, are functions that are passed as arguments to other functions. They are meant to be called by the receiving function at certain predetermined points or in response to certain events.

#### ✋ if you remember the `hello_decorator` was also passed here

```python
#passing function_to_be_used inside the decorator to control its behavior
function_to_be_used = hello_deco(function_to_be_used)
```

#### chatgpt

✅ You're absolutely correct. In the example with `hello_decorator`, the function_to_be_used is indeed being passed as an argument to `hello_decorator`. So, in that sense, it does resemble a form of callback.

#### In the context of the hello_decorator example:

`function_to_be_used` is a callback function.

`hello_decorator` is the higher-order function that takes the callback function as an argument.

`inner1` is the function within `hello_decorator` that wraps around the callback function and is responsible for invoking it.

So, `function_to_be_used` serves as a callback in this scenario because it's being passed to another function `(hello_decorator)` to be executed at a certain point within that function's execution.

<br>
<br>

**Usage:**

<u>Decorators</u> are typically used to apply cross-cutting concerns such as logging, authentication, caching, etc., to multiple functions or methods.

<u>Callbacks</u> are often used in event-driven programming or asynchronous programming to handle responses to events or asynchronous operations.

**Execution Control:**

<u>With decorators</u>, you have control over the execution flow before and after the wrapped function is called.

<u>Callbacks</u>, on the other hand, give control to the called function to decide when and how to invoke the callback function(s) it receives as arguments.

Despite these differences, there can be scenarios where decorators and callbacks are used together. For instance, you might have a decorator that applies some pre-processing to a function and then invokes a callback function as part of its execution flow. In this way, they can complement each other in certain design patterns.
