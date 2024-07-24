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

### 🌈 So, the line goes through `each friend (user) in the users` list. It checks if the number (`id`) of <u>that friend </u> is *not* the same as your number (`current_user_id`). 🔸  If it's not the same, that friend is added to the other_users list.

<br>

- **users** is the original list that has information about all your friends (`step 1.` ).

- **current_user_id** is your own number that identifies you among your friends (`step 2.` ).

- **other_users** is the new list that this line of code creates.(`step 3.` )

<br>



<br>
<br>

## step 4.

### 🟠 Randomly select a user from the remaining list

- `random.choice` to select a random user from other_users, which are all users except the current one.

```python
suggested_user = random.choice(other_users)
```

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


#suggest_random_user(current_user_id): This function takes current_user_id as a parameter and suggests a random user from users excluding the current user. It uses random.choice to select a random user from other_users, which are all users except the current one.
def suggest_random_user(current_user_id):
    #
    # Exclude the current user from suggestions
    other_users = [user for user in users if user["id"] != current_user_id]



    # Randomly select a user from the remaining list
    suggested_user = random.choice(other_users)
    # random.choice to select a random user from other_users, which are all users except the current one.

    return suggested_user
```

<br>

---

<br>
<br>

# 🐝 main.py

<br>
<br>


## 🟠 step 1.

#### 🟦 Import

<br>

- -  **Import** the **function** `suggest_random_user` and the array/list with the `users = []`.

<br>

- - Within the function that you are importing, **also** import the `suggested_user`.


<br>

```python
from helper import suggest_random_user, users
```


<br>
<br>

### 🟦 Now, in main.py, we simulate suggesting friends for Mario (user ID 2):


<br>

 ## 🟠 step 2.

 ```python
from helper import suggest_random_user, users
```


<br>
<br>

 ## 🟠 step 3.

 - - **Simulating** a `current user` (in real application, this <u>could come from session or login</u> )

 <br>


```python
def main():

    # ✋ this current_user_id is coming from the helper TOO
    current_user_id = 4 # Assuming current user is Alice with user ID 1, ✋ you can change this to choose another user from the list/array
```
### 🟢 In your terminal you will see something like this:



```python
Suggested friends for Anatole:
```

<br>
<br>

 ## 🟠 step 4.

 #### Suggesting 3 random users that the current user may know

 <br>

 - - If `current_user_id`  is **1**, then `users[current_user_id - 1]` means we're looking at the first user in the list (because computers start counting from 0, not 1).

 -  📌 If the **current user's ID** is 2 (Mario), we want to ensure that Mario is excluded from the list of suggested friends.

<br>

 ```python
#  In programming, we typically start counting from 0 for the first element in a list, so users[current_user_id - 1] refers to the user at index current_user_id - 1 in the users list.
  print(f"Suggested friends for {users[current_user_id - 1]['name']}:")
 ```

 <br>

 ## `["name"]`

 - 🌈 This syntax (`["name"]`) is used because `users[current_user_id - 1]` returns a dictionary (a type of collection in Python), and dictionaries use keys to access their values.

 <br>
 <br>


 ## 🟠 step 5.

 ### Loop:

<br>

 - - 🌈 `for i in range(3):`: **This** line **tells** the **computer** to **do**  <u>something</u> **three times** in a row.


 <br>


 - - 🌈 The **range(3)** part **means** it will **count from 0 to 2** (because in programming, it starts counting from 0). So, it will repeat the next lines of code three times.

 ```python
   for i in range(3): # suggest 3 users
        #
        suggested_user = suggest_random_user(current_user_id)
        print(f"- {suggested_user['name']}")
 ```

 <br>

 - - 🌈 `suggested_user = suggest_random_user(current_user_id)`: Inside the loop, this **line asks** the **computer** to **find** a **random friend** for you.

 - - It **uses** a **function** called `suggest_random_user` (comes from the helper.py) and **gives** it **your number** (`current_user_id`).