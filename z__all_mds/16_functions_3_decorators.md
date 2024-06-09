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

#
# The log_authentication decorator takes a function func as input and returns a wrapper function wrapper.
#
def log_authentication(func):
    #
    # Inside the wrapper function wrapper, it logs a message indicating the username being authenticated before performing the authentication check against the mock user database.
    #
    def wrapper(username, password):
        print(f"Authenticating user: {username}")
        # Simulate authentication by checking the username and password against the mock user database
        authenticated = False
        for user in users:
            if user["username"] == username and user["password"] == password:
                authenticated = True
                break
            #
            # After the authentication check, it logs a message indicating whether the authentication was successful or failed.
            #
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
    #
    # The authenticate_user function takes a username and password as input and returns True if the authentication is successful, and False otherwise.
    #
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
#
# We simulate authentication attempts by "iterating" over a list of dictionaries containing usernames and passwords, calling the authenticate_user function for each attempt, and logging the authentication result.
#
for attempt in authentication_attempts:
    username = attempt["username"]
    password = attempt["password"]
    result = authenticate_user(username, password)
    print(f"Authentication result for '{username}': {result}")

```

<br>
<br>

## Caching/Memoization:

```python

# Importing functools module to use lru_cache decorator
from functools import lru_cache

# Define a decorator for caching/memoization
def memoize(func):
    # Applying lru_cache decorator to the function to cache its results
    @lru_cache(maxsize=None)  # Using lru_cache with unlimited cache size
    def wrapper(*args, **kwargs):
        # Print a message indicating the function call
        print(f"Calling function '{func.__name__}' with args: {args}, kwargs: {kwargs}")
        # Call the original function and return its result
        return func(*args, **kwargs)
    # Return the wrapper function
    return wrapper

# Applying the memoize decorator to a function
@memoize
def fibonacci(n):
    # Base cases for Fibonacci sequence
    if n <= 1:
        return n
    # Recursive calculation of Fibonacci sequence
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Calling the Fibonacci function multiple times to observe caching behavior
print("Fibonacci result (5):", fibonacci(5))  # Function call, result not cached
print("Fibonacci result (4):", fibonacci(4))  # Function call, result not cached
print("Fibonacci result (5):", fibonacci(5))  # Result retrieved from cache, no function call

```

<br>

### memoize Decorator Function:

- The memoize function defines a decorator for caching/memoization.

- It takes a function func as input and returns a wrapper function wrapper.
  Inside the wrapper function, it applies the lru_cache decorator with an unlimited cache size `(maxsize=None)`.
- This decorator caches the results of function calls based on their arguments.

- The wrapper function prints a message indicating the function call, then calls the original function func with the provided arguments `(*args and **kwargs)`, and returns its result.

<br>

### fibonacci Function:

- The fibonacci function calculates the nth Fibonacci number recursively.

- It is decorated with @memoize, which means that its results will be cached, preventing unnecessary recalculation of Fibonacci numbers for the same inputs.
  Function Calls:

- We call the fibonacci function multiple times with different inputs to observe the caching behavior.

- The first two calls `(fibonacci(5)` and `fibonacci(4))` result in function calls, as their results are not cached yet.

- The third call `fibonacci(5)` retrieves the result from the cache, as it has been computed and cached during the first call, so no function call is made, demonstrating **caching/memoization** in action.

<br>

### 🏁 Questions

```css
what you mean? @lru_cache(maxsize=None) # Using lru_cache with unlimited cache
size what is the user going to be allowed to do with it?
```

#### chatgpt

In the line `@lru_cache(maxsize=None)`, **lru_cache** is a decorator provided by Python's func tools module.

```python

# Importing functools module to use lru_cache decorator
from functools import lru_cache
```

- It's used for **caching/memoization**, meaning it stores the results of expensive function calls so that if the same inputs are provided again, the function can return the cached result instead of recalculating it.

#### The `maxsize=None` argument specifies that the cache can grow indefinitely, meaning there is no limit to the number of results that can be cached. This is suitable when you want to cache all function results without imposing a limit on the cache size.

<br>

## What the user can do with this caching decorator:

**Improve Performance:** By using caching, the user can significantly improve the performance of functions that are called frequently with the same inputs. Instead of recalculating the result every time, the function can return the cached result, which can be much faster.

**Reduce Resource Usage:** Caching helps reduce resource usage by avoiding redundant calculations. This can be particularly useful for functions with expensive computations or I/O operations.

**Transparent Integration:** The user can easily integrate caching into their functions by simply applying the @lru_cache decorator. The decorator takes care of caching the results transparently, without requiring changes to the function's logic.

**Customize Cache Size:** Although maxsize=None specifies an unlimited cache size, the user can customize the cache size by providing a specific value. For example, maxsize=100 would limit the cache to store the most recent 100 results.

Overall, the @lru_cache decorator with an unlimited cache size (maxsize=None) provides a convenient and efficient way for users to implement caching in their Python functions, improving performance and reducing resource usage.

### 🏁 Questions

so its not for threejs type of scenario where the model can be expensive, but more like in a social network such as facebook , where millions of people use the app?

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
