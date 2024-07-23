## 🟡 Guess random number

<br>

### 🟦 For this exercise i will be using `random.randint`

- In Python, **random.randint(a, b) is a function** provided **by** the **random module**, which is part of Python's standard library.

-  This function generates a random integer
𝑁 such that `𝑎 ≤ 𝑁 ≤ 𝑏`  `a≤N≤b`.


- In JavaScript (and many other programming languages), `≤ ≤` is represented as `<=`.

<br>
<br>

## 🟠 Generate a random integer

### To generate a random integer within a specified range, you use `random.randint(a, b)`, where:

<br>

🔶 **a** is the **lower** bound (inclusive) of the range.

🔵 **𝑁 (N):** This symbol is used to **represent** the **random integer** that the function generates. It can be any integer within the range specified by `𝑎 (a) and 𝑏 (b)`.

🔶 **b** is the **upper** bound (inclusive) of the range.


```python
#(a, b) , the the n will be the random number that will be generated
𝑁  such that 𝑎 ≤ 𝑁 ≤ 𝑏
#
```

- which means **𝑁** is **within/between** the range from 𝑎 a to 𝑏 b, ` 🟦 🟣 🟦` inclusive.

<br>


- When **we combine** these **two2** statements `𝑎 ≤ 𝑁 ≤ 𝑏` with `≤ ≤`, it indicates that **𝑁** can be any number that is between **𝑎** and **𝑏**, including 𝑎 a and 𝑏 b themselves.

<br>

### 🟣 Question: this has to always be: 𝑁 , or can be anything else?

#### ✅ chatgpt:

- In **mathematics and computer science**, ✋**𝑁** is commonly used as a variable to represent a number or an integer. It's a **convention often used** to denote an arbitrary number that fits a certain condition or specification within a formula or function.

#### 🟣 So It doesn't matter which variable I use, but in most mathematical functions, 'N' is commonly used to denote the number between 'a' and 'b'. However, i can use any variable, but using 'N' is cleaner.

<br>

#### ✅ chatgpt:

Yes, you're absolutely right. In mathematics and programming, the choice of variable names is flexible, but using conventions can help with clarity and understanding, especially when communicating mathematical ideas or writing code that others may read.

<br>


### 🟧 Here are some key points:

**Flexibility in Variable Names:** You can use any variable name to represent a number or integer in a mathematical function or formula. Common choices include `'𝑁', 'x', 'y', 'z', 'm', 'n', etc`.

<br>
<br>

## 🟢 Let's continue


```python
import random
#
import random

# Define a function called guess that takes a parameter 'x'.
# Here, 'x' represents the upper limit (B) for the random number generation.
def guess(x):
    # Generate a random number between 1 and 'x'.
    random_number = random.randint(1, x)

    # Initialize 'guess' to 0. Typically, this variable would be used
    # to store the user's guess in a number guessing game scenario.
    guess = 0

# Call the guess function with x = 10.
# limit is 10, can be 100 , 300 etc
guess(10)
```

<br>

## 🔴 If you miss a line here, you will have an endless LOOP

### i purposely removed the line:

The reason for this is because if you notice, there's **no input** prompt **to capture** a **user's guess**, <u>essential</u>  for the logic to function correctly within the range of `1 to 10`.

```python
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    # LOOP
    # you need a loop for the guessing
    while guess != random_number:
        #

        # the guess variable is initialized to 0, and because
        # there's NO user INPUT statement within the loop to update guess,
        # 🔴 the while loop will not exit, regardless of how
        # many iterations it performs

        #
      if guess < random_number:
        print("Sorry, guess again. Too LOW 👎")
      elif guess > random_number:
        print("Sorry, guess again. Too high")

    print("Yay, congrats. You have guessed the number {random_number}")

#  Call the guess function with x = 10.
# limit is 10, can be 100 , 300 etc
guess(10)
```

<br>



<br>


### 🌈 The missing line

- The missing line `guess = int(input(f"Guess a number between 1 and {x}: "))` is crucial because it prompts the user to enter their guess for the randomly generated number. Without this input, the program lacks the mechanism to interactively receive and compare guesses, leading to an infinite loop.

```python
     guess = int(input(f"Guess a number between 1 and {x}: "))
```

<br>
<br>

##  🔴  Intentionally Causing a BUG

#### This is only for testing purposes because the break in this guessing game is unnecessary. here is why:

<br>

- **If** your **loop naturally exits** when a **condition is met** (like in a typical **guessing game** where the loop exits **when the guess matches the target**), ✋ using break might be **redundant** and could **potentially complicate** the **logic**.

>


<br>

### 🟣 QUESTION: Does Python support a 'break' statement within a while loop?

#### ✅ chatgpt:

- Yes, in Python, you can use the **break** statement **to exit a while loop** prematurely.

>The break statement is typically used when a certain condition is met and you want to stop the loop immediately, regardless of whether the loop condition itself would normally allow for more iterations.


```python
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    # LOOP
    # you need a loop for the guessing
    while guess != random_number:
      guess = int(input(f"Guess a number between 1 and {x}: "))
        #---
      if guess < random_number:
        print("Sorry, guess again. Too LOW ")
      elif guess > random_number:
        print("Sorry, guess again. Too high")
        # ✋
        break
 # ✋ issue
    print("Yay, congrats. You have guessed the number {random_number}")


guess(10)
```
<br>


### output:

```bash
# here i guessed a number between 1 and 10, but instead of following the rule, i wanted to see what would happen if i typed 500
Guess a number between 1 and 10: 500
Sorry, guess again. Too high
# 🔴
Yay, congrats. You have guessed the number {random_number}
```

<br>
<br>

### 🟣 QUESTION: Why does adding the 'break' statement ignore the condition? As a result, it seems to encounter an error but then displays 'congrats'.

#### ✅ chatgpt:

- The issue you're encountering is due to how you're handling the printing of the random number at the end of your function.



<br>
<br>

### 🌈 solution

- I really dont need this but its just a way to solve the issue (you can also remove the **break**)

```python
 if guess == random_number:
        print(f"Yay, congrats. You have guessed the number {random_number}")

```

### like so:

```python
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too LOW ")
        elif guess > random_number:
            print("Sorry, guess again. Too high")
            break  # Exit the loop if the guess is too high


            # ✋
    if guess == random_number:
        print(f"Yay, congrats. You have guessed the number {random_number}")

guess(10)
```
<br>

#### output

```python
Guess a number between 1 and 10: 598
Sorry, guess again. Too high
```


<br>
<br>

## 🟦 BREAK

### (Real-World Application:)

- 🟧 let's consider a simple game scenario where a player moves on a grid using directional **inputs:** `(up, down, left, right)`.

<br>

### 🟠 We'll use a loop to continuously process the player's INPUTS

 - - We'll use a loop to **continuously process** the **player's** **inputs** and **update** their **position on the grid**.

 <br>

#### Here's a conceptual example where using break can make sense:

- **break** ensures the game loop respects the player's decision to quit, providing a clear and immediate termination point for the game session.

```python
def move_player():
    #x, y = 0, 0: The player starts at position (0, 0) on a grid where x represents horizontal position and y represents vertical position.

    x, y = 0, 0  # Starting position of the player at coordinates (0, 0)

    while True:  # while True:: Start a loop that continues indefinitely until we decide to stop it.

        direction = input("Enter direction (up, down, left, right) or 'quit' to exit: ")  # Ask the player which direction they want to move

        if direction == 'up':  # If the player chooses 'up'
            y += 1  # Move the player up by increasing the y-coordinate by 1
        elif direction == 'down':  # If the player chooses 'down'
            y -= 1  # Move the player down by decreasing the y-coordinate by 1
        elif direction == 'left':  # If the player chooses 'left'
            x -= 1  # Move the player left by decreasing the x-coordinate by 1
        elif direction == 'right':  # If the player chooses 'right'
            x += 1  # Move the player right by increasing the x-coordinate by 1
        elif direction == 'quit':  # If the player chooses 'quit'
            print("Quitting game...")  # Display a message that we are quitting the game
            break  # Exit the loop and end the game if the player chooses to quit
        else:  # If the player enters any other input that is not recognized
            print("Invalid input. Please enter up, down, left, right, or quit.")  # Ask the player to enter a valid direction or 'quit'

        print(f"Player position: ({x}, {y})")  # After each move, show the player's current position on the grid

move_player()  # Call the function to start playing the game

```

<br>
<br>

## 🟡  BREAK (example 2)

<br>

#### 🟣 QUESTION: Can you provide a real-world scenario where the break statement is used in a loop within a banking system implemented in Python, and **explain how tokens** are managed to automatically log out a user after 3 minutes of inactivity?

<br>

#### ✅ chatgpt:

- In a Python-based banking application, the break statement is crucial for managing iterative processes efficiently.


<br>


### Token-based authentication and timeout functionality

<br

- let's integrate the concept of issuing and **Verifying tokens** along with the existing **PIN-based authentication**. **Tokens will expire** if the **user** is **inactive for 3 minutes** after logging in.

```python

import time
import random
import string

# Mock banking system

# Assume the correct PIN is 1234
correct_pin = '1234'

# Dictionary to store active tokens with their expiry times
active_tokens = {}

def generate_token():
    """Generate a random 6-character alphanumeric token."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

while True:
    start_time = time.time()  # Track start time of each login attempt
    pin = input("Please enter your 4-digit PIN (or 'q' to quit): ")

    if pin == 'q':
        print("Exiting the banking system.")
        break  # Exit the loop and therefore the program

    if pin == correct_pin:
        print("PIN accepted. Welcome to your account.")

        # Generate a new token and store it with its expiry time (3 minutes)
        token = generate_token()
        token_expiry = time.time() + 180  # 180 seconds = 3 minutes
        active_tokens[token] = token_expiry

        print(f"Your token is: {token}")
        print("Token will expire in 3 minutes if inactive.")

        while True:
            # Check if current time exceeds token's expiry time
            if time.time() > active_tokens[token]:
                print("Token expired due to inactivity.")
                del active_tokens[token]
                break  # Exit the inner loop to log out the user

            action = input("Enter your action (or 'q' to logout): ")

            if action == 'q':
                print("Logging out.")
                del active_tokens[token]
                break  # Logout and exit the inner loop

            # Perform banking operations here
            print(f"Performing action: {action}")

            # Reset the token's expiry time for each action
            active_tokens[token] = time.time() + 180  # Reset expiry to 3 minutes from now

        break  # Exit the outer loop since the user has successfully logged in

    else:
        print("Incorrect PIN. Please try again.")

# Additional code for banking operations could follow after the loop
# For example, displaying account balance, making transactions, etc.


```

<br>
<br>

<br>

#### 🟣 QUESTION: is there JWT for python?

<br>

#### ✅ chatgpt: Yes, there is a widely used library for working with JWT (JSON Web Tokens) in Python. The most popular library for handling JWTs in Python is PyJWT

<br>

🟠 **PyJWT Library**

#### [PyJWT Tutorial: Managing Authorization using JWT in Python](https://www.youtube.com/watch?v=ZWEIeLiysp0)

<br>

- - PyJWT is a Python library that allows you to encode and decode JWTs easily. It provides functions to create tokens, verify them, and decode them back to their original form. Here’s how you can use PyJWT: