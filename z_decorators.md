## 🧶 Python decorators


### - staticmethod [Go to section](#staticmethod)

 - -  examples: [Go to examples](#staticmethod_examples)

<br>




<br>
<br>

### 🌟 Remember:

- **self:** Refers to the instance of the class in instance methods. It allows access to instance attributes and other instance methods.



```python
class MyClass:
    def instance_method(self):
        print("This is an instance method")

```
<br>

- **cls:** Refers to the class itself in class methods. It allows access to class attributes and other class methods.

```python

class MyClass:
    class_attr = 42

    @classmethod
    def class_method(cls):
        print(f"This is a class method. Class attribute value: {cls.class_attr}")
#
# Here, cls is used to refer to MyClass, allowing access to class_attr and any other class-level data or methods. This is useful when you need to perform actions that affect the class as a whole rather than individual instances.
```

<br>

<br>

<br>


### Python decorators are a powerful feature that allows you to modify or enhance the behavior of functions or methods.

- 🍊 Decorators are often used to **add functionality** to functions or methods.

#### 🟧 Here's a list of common decorators and the most used ones in Python 🟧

### 🟦 Built-in Decorators


<br>
<br>

<a name="staticmethod"></a>


## 👾 `@staticmethod` 👾

<br>

- - 🍍 Defines a method that does not operate on an instance or class. It behaves like a regular function but is associated with the class.

<br>

- - 🤌 I used it in this project [tic_tac_toe_0](./LESSON_19_PPROJECTS/tic-tac-toe/tic_tac_toe_0/README.md)



<br>
<br>


### 🫐 What is `@staticmethod`

####  A staticmethod in Python is a 🔸 <u>method decorator</u> .

<br>
<br>

🍊 It is **used** to **define a method** in a **class** that **does not require access** to the **instance** (`self`) or the class (`cls`) to which it belongs.

#### In other words, a `staticmethod` is a method that can be called on the class itself, rather than on an instance of the class.

<br>

 In Python, a `staticmethod` is a method that <u>belongs to a class rather than an instance of the class </u> .


<br>
<br>

 🔴 This means **it doesn't have access to the instance (self)** or **class (cls) attributes** or **methods.**


  🔴 Instead, it is used to define a function within a class's namespace that doesn't need access to the instance or class.


<br>

## Purpose of `@staticmethod`

<br>

### 🟦 Encapsulation:

**It allows you to group functions** that are **related to a class** <u>together</u>, **even** if **those functions don't need** to **interact** with **class** or **instance data**. This helps in organizing code better.

<br>

### 🟦 Utility Functions:

`@staticmethod` is useful for **utility functions** that **might** be **relevant** to the **class but don't need** to **modify or access** the **class's state**.

<br>

### Code Organization:

It makes it clear that the method doesn't depend on the class's state or instance, and hence, it’s more about logical grouping rather than functionality.

<br>
<br>


<a name="staticmethod_examples"></a>


### 🟠 When to Use staticmethod

### 👾 1. Example:

 - - You have a utility function that logically belongs to a class but doesn’t need to interact with the class or instance data.

```python
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

# Usage
result = MathUtils.add(5, 3)
print(result)  # Output: 8

```

#### Explanation:

- - The add method is a utility function that performs an addition operation. It doesn't need to access or modify any class or instance attributes. It’s logically related to the MathUtils class, but it doesn’t rely on any class-specific data.

<br>
<br>


### 🟠 When Not to Use staticmethod

### 👾 2. Example:

- - You have a **method that needs to access or modify class or instance attributes**, or interact with other methods of the class.

Code Example 1: Accessing Instance Attributes

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

# Usage
p = Person("Alice")
p.greet()  # Output: Hello, my name is Alice

```



#### Explanation:

- - The `greet` method **needs to access** the **instance attribute** `self.name`.

- - This **method must be an instance** method, 🛑 **not** a static method, because it operates on the instance state.

<br>




### 🟣  QUESTION:

🔶 when you say:

**staticmethod** is a method, but it does not operate on the instance or the class directly. It does not take `self` or `cls` as its first parameter. Instead, it behaves like a regular function but lives in the namespace of the class.

Is it only the `staticmethod` or all decorators arent allowed to..(what you said above)

### ✅ Chatgpt:

-  When discussing decorators like staticmethod, the observation about not taking `self` or `cls` as parameters **specifically applies** to `staticmethod`. **However**, this concept can extend to other decorators based on their purpose and behavior.

#### Let’s break it down:

Behavior: A staticmethod is a method that does not operate on an instance (self) or the class (cls). It is essentially a regular function that is bound to the class's namespace.

Parameters: A staticmethod does not take self or cls as its first parameter. It behaves just like a normal function in terms of its parameters and return values.


<br>

## 🌠 More examples

####  1: Basic Static Method

```python
class IceCreamStore:
    @staticmethod
    def greet_customer(name):
        # 🛠️ This is a static method. It does not take 'self' or 'cls' as parameters.
        return f"Hello, {name}! Welcome to Ice Cream Store!"

# 🌟 Using the static method
greeting = IceCreamStore.greet_customer('Alice')
print(greeting)  # Output: Hello, Alice! Welcome to Ice Cream Store!

# 🔍 Notice: 'greet_customer' does not use 'self' or 'cls'
# ✋ Behavior: greet_customer is a static method because it doesn't operate on an instance (self) or the class (cls). It's like a regular function

# ✋ Parameters: It only takes name as its parameter and doesn’t need self or cls.
```
<br>

### 2: Static Method with Multiple Parameters

```python
class IceCreamStore:
    @staticmethod
    def recommend_flavor(age, preference):
        # 🛠️ This is a static method. It only takes parameters you provide and does not involve 'self' or 'cls' cls stands for class.
        if age < 12:
            return 'Vanilla' if preference == 'sweet' else 'Chocolate'
        else:
            return 'Mint Chocolate Chip' if preference == 'minty' else 'Coffee'

# 🌟 Using the static method
recommendation = IceCreamStore.recommend_flavor(10, 'sweet')
print(f"We recommend: {recommendation}")  # Output: We recommend: Vanilla

# 🔍 Notice: 'recommend_flavor' uses only provided parameters, not 'self' or 'cls'

```

<br>

### 3: Static Method Without Any Parameters

```python
class IceCreamStore:
    @staticmethod
    def store_hours():
        # 🛠️ This is a static method with no parameters. It still does not use 'self' or 'cls'.
        return "We are open from 10 AM to 10 PM daily."

# 🌟 Using the static method
hours = IceCreamStore.store_hours()
print(hours)  # Output: We are open from 10 AM to 10 PM daily.

# 🔍 Notice: 'store_hours' has no parameters and does not use 'self' or 'cls'

```

<br>
<br>

---


<br>
<br>

## 👾 `@classmethod:`


- -  Defines a method that **operates** on the  ✋ **class itself**, rather than on instances. It receives the class as its first argument (cls).

<br>

#### `@property:`

- -  Turns a method into a property, allowing you to access it like an attribute without calling it as a method.

<br>

#### `@abstractmethod`:


- - Used in abstract base classes to define abstract methods that must be implemented by any subclass.


<br>

<br>

---

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

---


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

---

<br>

<br>

## 🟤 `@retry`:


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







<br>
<br>

### Protected Example with Idempotency and Retry Management


1. Protected Code with Idempotency and Retry Management:

```python
import uuid # Notes: check the social media project, i used it there just to test it
import time
import requests
from functools import wraps
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from pymongo import MongoClient, errors

# Retry Decorator with Exponential Backoff 🔄
def retry_request(max_retries=3, backoff_factor=0.3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            session = requests.Session()
            retry = Retry(total=max_retries,
                          backoff_factor=backoff_factor,
                          status_forcelist=[500, 502, 503, 504])
            adapter = HTTPAdapter(max_retries=retry)
            session.mount('http://', adapter)
            session.mount('https://', adapter)
            return func(session, *args, **kwargs)
        return wrapper
    return decorator

# Function to Place Order with Idempotency 🛒
@retry_request(max_retries=5, backoff_factor=1)
def place_order(session, order_details):
    order_id = str(uuid.uuid4())  # Unique identifier for idempotency 🆔
    try:
        response = session.post('https://api.icecreamstore.com/order', json={**order_details, 'order_id': order_id})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Order placement failed: {e}")
        raise

# Connect to MongoDB 🗄️
client = MongoClient('mongodb://localhost:27017/')
db = client['icecream_store']
orders_collection = db['orders']

# Function to Store Order in MongoDB with Idempotency 📦
def store_order(order_id, order_details):
    try:
        orders_collection.update_one(
            {'order_id': order_id},  # Unique key for idempotency 🆔
            {'$set': order_details},
            upsert=True  # Insert the document if it does not exist
        )
    except errors.PyMongoError as e:
        print(f"Failed to store order in MongoDB: {e}")
        raise

# Usage Example 🚀
order_details = {'flavor': 'vanilla', 'quantity': 2}
try:
    order_response = place_order(requests.Session(), order_details)
    order_id = order_response['order_id']
    store_order(order_id, order_details)
    print("Order placed and stored successfully:", order_response)
except Exception as e:
    print(f"Failed to place or store order: {e}")

```

<br>

<br>


### 🛑 Risky Example without Protections
2. Risky Code without Idempotency or Retry Management:

```python
import time
import requests
from pymongo import MongoClient, errors

# Function to Place Order Without Retry or Idempotency 🚫
def place_order(order_details):
    try:
        response = requests.post('https://api.icecreamstore.com/order', json=order_details)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Order placement failed: {e}")
        # No retry mechanism, so we simply raise the exception 🚨
        raise

# Connect to MongoDB 🗄️
client = MongoClient('mongodb://localhost:27017/')
db = client['icecream_store']
orders_collection = db['orders']

# Function to Store Order in MongoDB Without Idempotency 📦
def store_order(order_id, order_details):
    try:
        orders_collection.insert_one({**order_details, 'order_id': order_id})
    except errors.PyMongoError as e:
        print(f"Failed to store order in MongoDB: {e}")
        raise

# Usage Example 🚀
order_details = {'flavor': 'vanilla', 'quantity': 2}
try:
    order_response = place_order(order_details)
    order_id = order_response['order_id']
    store_order(order_id, order_details)
    print("Order placed and stored successfully:", order_response)
except Exception as e:
    print(f"Failed to place or store order: {e}")

```



```bash
# Summary
🔄: Retry mechanism with exponential backoff.
🛒: Function to place orders with idempotency.
🆔: Unique identifier for idempotency.
🗄️: Connecting to MongoDB.
📦: Storing orders in MongoDB with idempotency.
🚀: Usage example.
🚫: No retry or idempotency protections.
🚨: Risk of failure without retries.
```

<br>
<br>

---

<br>
<br>

# 🌈 Summary


### Built-in decorators:

- - @staticmethod,
- - @classmethod,
- - @property,
- - @abstractmethod.

<br>

### Standard library decorators:

- - functools.lru_cache,
- - functools.wraps,
- - functools.total_ordering,
- - functools.singledispatch.

<br>

###  Custom/third-party decorators:

- - @login_required,
- - @csrf_exempt, @timer,
- - @retry.

<br>
<br>

---

<br>
<br>
