# Closures

https://www.geeksforgeeks.org/python-closures/

<br>
<br>

### 🍭 What is a Closure?

by chatgpt

- A closure is a function object that has access to variables in its enclosing lexical scope, even when the function is called outside that scope. This means that the inner function remembers the environment in which it was created.

<br>
<br>

the below text source [geeksforgeeks.org/python-closures](https://www.geeksforgeeks.org/python-closures/)

- Before seeing what a closure is, we have to first **understand** what **nested functions and non-local variables are**.

#### Nested functions in Python

- A function that is defined inside another function is known as a nested function. Nested functions are able to access variables of the enclosing scope.

```python
# Python program to illustrate
# nested functions
def outerFunction(text):

	def innerFunction():
		print(text)

	innerFunction()


if __name__ == '__main__':
	outerFunction('Hey!')
```

<br>
<br>

## Closure example:

```python
def outer_function(x):
    # This is the outer function

    def inner_function(y):
        # This is the inner function
        # It accesses the variable 'x' from the outer function
        return x + y

    # The outer function returns the inner function
    return inner_function

# Create a closure
closure = outer_function(10)

# Call the closure with an argument
result = closure(5)
print(result)  # Output: 15

```

<br>
<br>

## 🪙 Small game

<br>

- first i will try with only tommy, in the sencon example you will see what happens when tommy is called twice

```python
# Closure is a function having accesss to the scope of its parent.
#
# Function after the parent function has returned

##  ----
# COINS example
# -------

#
# 0
def parent_function(person):
    #1 by default the user has 3 coins
    coins = 3
    #2
    def play_game():
        # 3 🟥 --- important!
        # we need the nonlocal key to tell python we will be reassigning a value
        nonlocal coins
        #The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.Use the keyword nonlocal to declare that the variable is not local.
        #-------------
        #
        # 4 defining how many coins the user has now, he has
        coins -= 1

        # 5 conditional
        # if the user has more than 1 show the first image, then if the user has equal to 1 show that he has 1 coin left, at last the user is OUT of coins
        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins")

    # 6 🟥 --- important!  here below we are not calling() the function, WE ARE ONLY "returning" it
    return play_game

#7 here TOMMY = is a new function, this tommy function  is going to handle the "parent_function" , within it i will add the value as "Tommy"
tommy = parent_function("Tommy")

# 8 calling tommy function which is holdinf the data of the parent_function and all the nested functions etc
tommy()
#
# 🌟 RESULT
# #Tommy has 2 coins left.

```

<br>
<br>

## 🍭 Duplicate the names

### here i call tommy a sencond time, and because of it tommy will have 1 coin lef

```python
# Closure is a function having accesss to the scope of its parent.
#
# Function after the parent function has returned

##  ----
# COINS example
# -------

#
# 0
def parent_function(person):
    #1 by default the user has 3 coins
    coins = 3
    #2
    def play_game():
        # 3 🟥 --- important!
        # we need the nonlocal key to tell python we will be reassigning a value
        nonlocal coins
        #The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.Use the keyword nonlocal to declare that the variable is not local.
        #-------------
        #
        # 4 defining how many coins the user has now, he has
        coins -= 1

        # 5 conditional
        # if the user has more than 1 show the first image, then if the user has equal to 1 show that he has 1 coin left, at last the user is OUT of coins
        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins")

    # 6 🟥 --- important!  here below we are not calling() the function, WE ARE ONLY "returning" it
    return play_game

#7 here TOMMY = is a new function, this tommy function  is going to handle the "parent_function" , within it i will add the value as "Tommy"
tommy = parent_function("Tommy")
jenny = parent_function("Jenny")

# 8 calling tommy function which is holdinf the data of the parent_function and all the nested functions etc
tommy()
#🟥 here i call tommy a sencond time, and because of it tommy will have 1 coin left
tommy()
jenny()
#
# RESULT
# Tommy has 2 coins left.
# Tommy has 1 coin left.
# Jenny has 2 coins left.

```

<br>

---

<br>

## 🍭 Spotify example

chatgpt

- **Imagine each user can have multiple playlists**, and we want to create a system where users can **add** songs to their playlists, **remove** songs, and view their playlists. We can use closures to manage each playlist's data and operations.

<br>

```python
def create_playlist(user_id):
    # This dictionary stores the user's playlist
    playlists = {}


    # ✋
    def add_song(playlist_name, song):
        # Inner function to add a song to a playlist
        if playlist_name not in playlists:
            # Create the playlist if it doesn't exist:
            playlists[playlist_name] = []
            # add/append the song to the list
        playlists[playlist_name].append(song)
        print(f"Added song '{song}' to {user_id}'s playlist '{playlist_name}'.")
  # ✋
    def remove_song(playlist_name, song):
        # Inner function to remove a song from a playlist
        if playlist_name in playlists and song in playlists[playlist_name]:
            playlists[playlist_name].remove(song)
            print(f"Removed song '{song}' from {user_id}'s playlist '{playlist_name}'.")
        else:
            print(f"Song '{song}' not found in {user_id}'s playlist '{playlist_name}'.")
      # ✋
    def view_playlist(playlist_name):
        # Inner function to view a playlist
        if playlist_name in playlists:
            print(f"{user_id}'s playlist '{playlist_name}': {playlists[playlist_name]}")
        else:
            print(f"Playlist '{playlist_name}' does not exist for user {user_id}.")

    # Return the inner functions as a dictionary of operations
    return {
          # ✋
        'add_song': add_song,
          # ✋
        'remove_song': remove_song,
          # ✋
        'view_playlist': view_playlist
    }

# Create playlist managers for different users
user1_playlists = create_playlist("user1")
user2_playlists = create_playlist("user2")

# User 1 operations
user1_playlists['add_song']("Rock Classics", "Bohemian Rhapsody")
user1_playlists['add_song']("Rock Classics", "Stairway to Heaven")
user1_playlists['view_playlist']("Rock Classics")
user1_playlists['remove_song']("Rock Classics", "Stairway to Heaven")
user1_playlists['view_playlist']("Rock Classics")

# User 2 operations
user2_playlists['add_song']("Jazz Vibes", "So What")
user2_playlists['view_playlist']("Jazz Vibes")
user2_playlists['add_song']("Jazz Vibes", "Take Five")
user2_playlists['view_playlist']("Jazz Vibes")

```

<br>
<br>

## Python vs. JavaScript: Lists within Objects

```python
 playlists = {}

            playlists[playlist_name] = []
```

<br>

### In both Python and JavaScript, you can store arrays (lists) within objects (dictionaries) to manage collections of data. Here's a comparison:

## Python

In Python, you often use dictionaries to store related data. A list within a dictionary is a common way to manage collections of items associated with keys.

Example:

```python

```
