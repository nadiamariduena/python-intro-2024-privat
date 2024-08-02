## 🧶 Python decorators

#### Python decorators are a powerful feature that allows you to modify or enhance the behavior of functions or methods.

- 🍊 Decorators are often used to **add functionality** to functions or methods.


<br>
<br>

### 🟧 Here's a list of common decorators and the most used ones in Python:

<br>

## 🟦 Built-in Decorators


#### `@staticmethod`:

- - Defines a method that does not operate on an instance or class. It behaves like a regular function but is associated with the class.

<br>

- - 🍍 I used it in this project [tic_tac_toe_0](./LESSON_19_PPROJECTS/tic-tac-toe/tic_tac_toe_0/README.md)

<br>
<br>

#### `@classmethod:`


- -  Defines a method that operates on the class itself, rather than on instances. It receives the class as its first argument (cls).

<br>

#### `@property:`

- -  Turns a method into a property, allowing you to access it like an attribute without calling it as a method.

<br>

#### `@abstractmethod`:


- - Used in abstract base classes to define abstract methods that must be implemented by any subclass.


<br>
<br>
<br>

## 🟦 Standard Library Decorators

<br>

#### `functools.lru_cache`:

- - Caches the results of expensive function calls to speed up subsequent calls with the same arguments. Useful for memoization.

<br>

####  `functools.total_ordering`:

- - Automatically generates missing comparison methods (<, <=, >, >=) based on the defined ones (==, !=).


<br>

#### `functools.singledispatch`:

- - Allows a function to behave differently based on the type of its first argument. It’s a form of generic function dispatch.


<br>



#### `functools.wraps`:


- - A helper decorator used to preserve the metadata of the original function when decorating functions. This is especially useful when creating custom decorators.

#### 🟣 QUESTION: In the `@functools.wraps` **decorator** shown below, why does it appear in grey and look like a comment, even though it is an important part of the code?

```python
def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

```

#### ✅ chatgpt:

- The `@functools.wraps` decorator might appear in grey and look like a comment in some code editors or IDEs due to syntax highlighting settings or themes that treat decorators differently. Despite its appearance, @functools.wraps is indeed an important part of the code.

>It is used to update the wrapper function to look more like the original function being decorated.

>This means it copies metadata such as the function name, docstring, and other attributes from the original function to the wrapper function.


>This is crucial for preserving the original function's identity and documentation, especially when debugging or inspecting the function.

<br>

 ### 🟧 Another example:



 ```python
import functools

def log_decorator(func):
    #
    #
    @functools.wraps(func)  # Preserves the metadata of 'func'
    #
    #
    def wrapper(*args, **kwargs):
        #
        print(f"Calling {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        #
        result = func(*args, **kwargs)
        #
        print(f"{func.__name__} returned {result}")
        return result
        #
    return wrapper

@log_decorator
def add(a, b):
    """Add two numbers."""
    return a + b

print(add.__name__)      # Output: add
print(add.__doc__)       # Output: Add two numbers.


 ```


 <br>

### In this example:

- - `@functools.wraps(func)` ensures that wrapper retains the __name__ and __doc__ attributes of add.


🔴 **Without** `functools.wraps`, **add.__name__** would be **'wrapper'** and **add.__doc__** would be **None**, which would be **misleading**.


<br>
<br>
<br>
<br>


## 🟦  Custom and Third-Party Decorators


#### `@login_required`:

- - Common in web frameworks like Django, it ensures that a user is authenticated before accessing a view.

#### `@csrf_exempt`:

- - Used in web frameworks to exempt a view from CSRF (Cross-Site Request Forgery) protection.

#### `@timer`:

- - Custom decorator for measuring the execution time of a function. Not built-in but commonly used in practice.


<br>
<br>
<br>

### 🟤 `@retry`:


- - Custom decorator that allows you to automatically retry a function if it fails. Useful for handling transient errors in network operations or **API calls**.

<br>

#### 🟣 QUESTION:  In ReactJS, failing to use useEffect when making API calls can lead to issues such as memory leaks. Is there a similar risk when using the 🟤 <u>@retry decorator</u>  in Python for handling retries?

- If so, how can this risk be mitigated? For example, consider a scenario where we're managing **API calls** to an ice cream store's inventory system.

#### ✅ Chatgpt:

- - 🔴 **Yes**, there can be risks of resource leaks or unintended behavior when using a retry decorator in Python, similar to how you might face issues with useEffect in React if not properly managed.

- - In Python, this can often **manifest** as **unclosed resources**, **such** as **file handles or network connections**,

- -  ✋ especially if the retrying logic involves repeated resource usage.


<br>
<br>

### 🍨 Let’s illustrate this with an example from an ice cream store scenario.

##### Example Scenario

- Imagine you’re developing a Python function to place an order at an ice cream store via an API.

- - You want to **retry** the **request** if it fails due to transient errors. Here’s a simple implementation of such a function using a retry decorator:

```python
import time
import requests
from functools import wraps

def retry(max_retries=3, delay=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except requests.RequestException as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(delay)
            raise Exception("Max retries reached")
        return wrapper
    return decorator

@retry(max_retries=5, delay=1)
def place_order(order_details):
    response = requests.post('https://api.icecreamstore.com/order', json=order_details)
    response.raise_for_status()  # Raise an error for bad HTTP responses
    return response.json()

```

<br>

## 🔴 Potential Risks

### Resource Leaks:

If the function place_order involves opening resources (e.g., file handles, database connections) that are not properly closed or managed, retrying could exacerbate the issue.

<br>


### Performance Issues:
Excessive retries might result in unnecessary load or delay, affecting the performance and user experience.

<br>

#### 🟣 QUESTION:  When you mention state inconsistencies: does this mean that retrying `API calls` could result in multiple requests, which might lead to state inconsistencies if the operations aren't handled right? For example, if a shop is using MongoDB, could this potentially lead to higher costs due to the increased number of requests?

<br>

#### ✅ chatgpt: Yes, retrying API calls can indeed lead to multiple requests, which may cause state inconsistencies if those requests aren’t idempotent.

<br>

### Idempotent operations


- Idempotent operations are those where repeating the same request has the same effect as making it just once. If the operations aren’t idempotent, retrying can result in unintended side effects or duplicate actions.

**Multiple Charges**: If an order request is retried and each attempt results in a new charge or order entry, the customer might be billed multiple times.

**Duplicate Entries**: Non-idempotent operations might lead to duplicate records in the database, which can cause confusion and require additional cleanup.

### 💸 Increased Costs 💳
In MongoDB or any other database service, multiple requests can lead to:

**Higher Data Transfer Costs:**

- -  Each request involves data being sent over the network. Retry attempts increase the amount of data transferred, which might lead to higher costs, especially if the requests are large or frequent.

**Increased Read/Write Operations:**

- - Each request that creates or updates a document counts as a read or write operation. More operations can lead to higher costs, particularly if you're charged per operation.


**Service Charges:**

- -  Some database services charge based on the number of requests or the amount of data processed. More retries can result in higher bills.



<br>
<br>


## 🟧 How to Manage These Issues

### Use Idempotent API Endpoints:

#### Design your API to handle retries safely. This often involves:

#### Idempotent Operations:

- - Ensure that repeating an operation (like placing an order) does not change the outcome beyond the initial request.


#### Unique Request Identifiers:

- - Include unique identifiers (e.g., transaction_id) in requests so that the server can detect and ignore duplicate requests.


### Implement Retry Strategies Wisely:

#### 🔶 Limit Retries:

- - Set a reasonable limit on the number of retries to avoid excessive requests.

#### 🔶 Exponential Backoff:

- - Use exponential backoff strategies to space out retry attempts, reducing the load on the system.

###   Monitor and Optimize:

- - **Track API Usage:** Monitor the number of requests and failures to understand the impact of retries.


- - **Optimize Queries:** Ensure that your database queries are efficient to reduce the cost of operations.

