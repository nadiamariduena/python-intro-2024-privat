# 🟡 Tic Tac Toe


<br>
<br>

## I will be creating a simple setup for a game involving players.

  🔶 Imagine we’re talking about a game like **Tic-Tac-Toe** where players can be either people or computer characters.

```bash
   X | O | 3
  ---|---|---
   4 | X | 6
  ---|---|---
   7 | 8 | O

```
<br>
<br>

<br>

<br>

## 🟣 QUESTION: create a diagram to visualize the O and X on the game


#### ✅ CHATGPT:

- -  **a diagram** is a great idea. Here’s a simple textual representation of the game board where you can see how **Xs** and **Os** are placed:


<br>

### 🟦 To visualize the game of Tic-Tac-Toe with Xs and Os,


#### 🔶 Example 1: Initial Board


```bash
   1 | 2 | 3
  ---|---|---
   4 | 5 | 6
  ---|---|---
   7 | 8 | 9

```

<br>

- -   **1-9** are placeholders for where you can put **Xs and Os**.

- - You can **update the board** as **players** make their **moves**.

<br>


#### 🔶 Example 2: X and O Placed

```bash
   X | O | 3
  ---|---|---
   4 | X | 6
  ---|---|---
   7 | 8 | O

```

### How to Read the Board

https://www.vedantu.com/maths/rows-in-maths


**Rows:** The board is divided into three rows.

**Columns:** Each row has three columns.

**Cells:** The intersections of rows and columns are where you place Xs or Os


<br>
<br>

<br>
<br>

# 🟡 Let's Start

<br>
<br>





<br>

## 🟦 Within the `player.py`


- Start by importing the below




```python
import math
import random
```

<br>
<br>

## 🟦 Creating a `Player`:

<br>

- -  Create a **class:** `class Player:`


 - - #### Think of this as a blueprint for a player in the game.

 - - Each player has a special mark, like **X or O**.


<br>
<br>

```python
class Player:
    def __init__()
```

<br>
<br>

## 🟦 initialize it: `def __init__()`


- -  `__init__(self, letter)`: This is like setting up the player with their mark when they start the game.

- **For example**, if you choose X, then the player will be X.


<br>

- - ### `self.letter = letter`: (letter is X or O)

```bash
   X | O | 3
  ---|---|---
   4 | X | 6
  ---|---|---
   7 | 8 | O

```

<br>


- - ### 🟤 get_move(self, game)


- - `get_move(self, game)`: This is like a placeholder for where the **player will decide what move to make in the game**.

- -  Right **now**, it's **empty**, so the player doesn’t actually make a move yet.

<br>
<br>

```python
class Player:
    def __init__(self, letter):
        # letter is X or O
        self.letter = letter

    def get_move(self, game):
        pass


```


<br>
<br>

# 🟡 Child Classes and super()

- **When** you **create** a **child class**, you **often want** to **use the setup from the parent class**. This is where `super()` **comes in**.

<br>

### 🔶 What `super().`__init__(letter)` Does

- - **super():** This function is used to call methods from the parent class (Player in this case).


- - **super().__init__(letter)**: This calls the __init__ method of the Player class, passing the letter parameter to it.


<br>
<br>
<br>




### 🟠 `class RandomComputerPlayer` & `HumanPlayer`

#### When you use `super().__init__(letter)`, you are saying, “I want to use the setup that the Player class provides to initialize this new player, including setting up their mark (X or O).”


- It ensures that the **child classes** `(RandomComputerPlayer and HumanPlayer)` properly inherit and set up the letter attribute from the Player class.


<br>

```python
# child class
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass



# ✋ Same here
#
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)


    def get_move(self, game):
        pass
```


<br>

- - `class RandomComputerPlayer`: This is a special type of player who is a computer that makes random moves.


- - `super().__init__(letter)`: This line is like saying, “Hey, use the setup from the Player blueprint because I am still a player.”


- - `get_move(self, game)`: This is also a placeholder for where the computer would decide on a random move. For now, it’s empty.


<br>
<br>

## Summary


**Parent Class (Player):** Defines the basic setup, including the letter attribute.

**Child Classes (RandomComputerPlayer and HumanPlayer):** Use super() to inherit and utilize the setup from the Player class.


`super().__init__(letter):` Ensures that the child classes correctly set up the letter attribute by calling the parent class’s __init__ method.

<br>
<br>
<br>

## 🟡 Create the `game.py`

```python
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]

        self.current_winner = None # Keep track of winner
```

<br>

### 🟧 `self.board = [' ' for _ in range(9)]`


- -   This **creates a list** (like a **row of boxes**) with **9 empty spaces**. Each space will be where we put **X or O.**

- - ####  🔸 Think of it as a 3x3 grid but stored in a single line.

```python
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
#Each ' ' represents an empty spot on the board.

```
<br>

## 🟧  `self.current_winner = None`

<br>

**self.current_winner:** This keeps track of who is winning the game.

**None:** This means we don’t know yet if anyone has won because the game hasn’t been played.

<br>
<br>

---

<br>
<br>

## 🌴 Create a another function, call it:  `print_board`

- pass the param from the parent function: **self**

```python
def print_board(self):
    #This part creates a list of rows from the board. Let’s break this down:
    #- - self.board: This is the list with all the spaces on the board.
    for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
```

<br>
<br>

## 🟩  Let’s break this down:



### 🟠 `for row in [self.board[i*3:(i+1)*3] for i in range(3)]`:

<br>

- 🌈 **Imagine** we have a tic-tac-toe board represented as a list with 9 positions, like this:
