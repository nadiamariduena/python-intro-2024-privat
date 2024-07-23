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

### 🌈 This line prompts the user to "input" `(input(` their guess and converts that input into an integer `int(input(`.

<br>
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


 ### Continuing reading about the `break` here: [break-loop_token_JWT.md](../../z_break-loop_token_JWT.md)


 <br>
 <br>

 ### 🟧 Lets continue


 <br>

 ```python
import random  # Step 1: Importing the 'random' module for generating random numbers

def guess(x):
    #random_number: This variable holds the randomly generated integer, which remains constant throughout the program execution until the user correctly guesses it.
    random_number = random.randint(1, x)  # Step 2: Generating a random number between 1 and 'x'
    #    # random.randint(1, x): This function call from the random module generates a random integer. The parameters 1 and x specify the range within which the random number can fall. Here, 1 ensures the random number starts from the lowest possible value (which is 1), and x is the upper limit.

    #
    guess = 0  # Step 3: Initializing the 'guess' variable to 0

    # Step 4: Loop for guessing the number
    while guess != random_number:
        #This line prompts the user to "input" their guess and converts that input into an integer.
        guess = int(input(f"Guess a number between 1 and {x}: "))  # Step 5: Taking user input for a guess


        # Step 6: Checking if the guess is too low, too high, or correct
        if guess < random_number:
            print("Sorry, guess again. Too LOW 👎")  # Step 7a: Providing feedback for a guess that is too low
        elif guess > random_number:
            print("Sorry, guess again. Too high")  # Step 7b: Providing feedback for a guess that is too high

# Step 8: Calling the function with 'x' = 10, allowing guesses between 1 and 10
guess(10)

 ```