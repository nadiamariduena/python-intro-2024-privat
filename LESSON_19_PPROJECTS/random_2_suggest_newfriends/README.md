## 🟡 Random: Suggest new friends

- create a scenario where we use Python to implement a simplified version of suggesting new friends or people you may know on a **social media** platform like **Facebook**.



#### We'll have two files: `helper.py` and `main.py`.

<br>
<br>
<br>

---

<br>
<br>

# 🟣 helper.py 🐻

- - In `helper.py`, we'll define a function that generates **random users** or profiles. This will simulate fetching potential friends or suggested connections.


<br>
<br>

## 🟦 This will simulate fetching friends or suggested connections


<br>

 ## 🟠 step 1.

 <br>

 ##   `users:`

 - - Represents a list of example user profiles. In a real application, this data would typically come from a database or `API`.


<br>



```python
import random

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Mario"},
    {"id": 3, "name": "Anastasia"},
    {"id": 4, "name": "Anatole"},
    {"id": 5, "name": "Filomena"}
]

```

<br>
<br>


## 🟠 step 2.

<br>

## `suggest_random_user()`

<br>


 `suggest_random_user(current_user_id)`: This  <u>function takes</u> **current_user_id** as a **parameter** ... 🟤(continue after the code)


<br>

```python
# the function
 def suggest_random_user(current_user_id):
```
<br>
<br>

## 🟠 step 3.

<br>

## `other_users`


🟤 and **suggests a random user** from **users** <u>excluding the current user</u> .

<br>

- - 🌈 Imagine you have a **list of all your friends**, and **each friend** has a **number** that **identifies them**.

- - 🌈 Now, let's say **you want to make a new list**, but **you don't want your own number in it**. This line of code does exactly that:

<br>

```python
other_users = [user for user in users if user["id"] != current_user_id]
```

<br>
