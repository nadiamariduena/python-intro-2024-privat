## 🧶 Array or List? 🤔

<br>

in Python, the term **"list"** is used **instead** of **"array"** for the data structure that holds a collection of items.

#### 🫐 However, the concept is similar. Here’s a bit more detail:

<br>

### 🟧 Python Lists

## 🌵 List:

- - In Python, **a list** is a **built-in data type**

<br>

- - **used to store an ordered collection of items**, which can be of different types. Lists are dynamic, meaning you can change their size and contents after creation. Lists are more flexible and commonly used in Python.

```python
my_list = [1, 2, 3, 4]
```

<br>
<br>

### 🟧 Arrays in Python

#### Array:

 - - **Python does have an array module** that provides a more constrained array type that only supports items of the same type.


  - - 🔴 **It’s less commonly used** than lists in everyday Python programming.

```python
import array
my_array = array.array('i', [1, 2, 3, 4])  # 'i' indicates an array of integers

  ```