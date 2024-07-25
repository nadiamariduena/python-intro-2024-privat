## 🟡 SET

<br>
<br>

🟦 `set` **function** in Python is used to create a set, which is a built-in data type representing an unordered collection of unique elements.


<br>

### 🟠 Here's a brief explanation and a list of methods or functions similar to set, including their purposes:

<br>

#### Similar Methods or Functions


🟧 **list(iterable):**

<br>

- - **Purpose:** Creates a **list object** from an iterable. Unlike sets, lists can contain duplicate elements and maintain the order of elements.
tuple(iterable):

-  - **Purpose:** Creates a **tuple object** from an iterable. Tuples are similar to lists but are immutable, meaning their contents cannot be changed once created.
frozenset(iterable):

- - **Purpose:** Creates an **immutable version** of a set. Frozensets are hashable and can be used as dictionary keys or elements of other sets, but you cannot modify their contents after creation.
dict(iterable):

-  - **Purpose:** Creates a dictionary object from an iterable of key-value pairs.

-  - Dictionaries store data in key-value pairs and do not allow duplicate keys.

<br>


### collections.Counter(iterable):

<br>

- - **Purpose:** ✋ Creates a Counter object, which is a specialized dictionary subclass for counting **hashable objects**.


- -  It counts the frequency of elements in an iterable and can be used for various counting and frequency operations.



### collections.defaultdict(default_factory):

-  - **Purpose:** Creates a dictionary with a default value for non-existent keys. This allows for automatic handling of missing keys with a specified default factory function.
setdefault(key, default) (method of dictionaries):

- -  **Purpose:** Retrieves the value for the given key if it exists in the dictionary; otherwise, it sets the key with a default value and returns that default value.
Each of these functions and methods has its specific use cases, but they all deal with creating or manipulating collections of data in various ways.



<br>
<br>


<br>


## 🟡 Mongo