# 🟡 Tic Tac Toe

#### 🫐 Course developed by Kylie Ying.

[min: 35:55 | 12 Beginner Python Projects - Coding Course](https://youtu.be/8ext9G7xspg?si=U_U7YuBMpWRwDksc&t=2155)




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

```python
self.board = [0, 1, 2, 3, 4, 5, 6, 7, 8]

```

#### This list represents the tic-tac-toe board like this:

```bash
   0 | 1 | 2
  ---|---|---
   3 | 4 | 5
  ---|---|---
   6 | 7 | 8

```


<br>
<br>

### `for row in`:

- - `for` row `in` ...: This part **tells** the **computer** to **go through each** <u>row</u>  **one by one**.

- - ##### It’s like saying, “For each row in the list we’re making, do something with it.”


<br>
<br>


### `[self.board[i*3:(i+1)*3] for i in range(3)]`:

- - This part creates a list of rows from the **board.**

- - **self.board:** This **is** the **list** with **all** the **spaces** on the **board**.


<br>
<br>

## 🟨 What Does `i*3:(i+1)*3` Do?

<br>

🟦 `i*3`: This tells us where to **start** in the list for each row.

🟦 `(i+1)*3`: This tells us where to **stop** in the list for each row.


<br>

#### Understanding i*3

- In this Tic-Tac-Toe game, the list of numbers is divided into three rows.

<br>
<br>

 ![https://youtu.be/LgR6UNeQxXE?feature=shared](https://github.com/user-attachments/assets/f8fbc564-6920-42a4-b72a-66b0f6fc024c)

<br>

### 🌈 short explanation:

### Imagine you’re at a funfair with a carousel that has 3 sections. Each section has different animals to ride on. You get to choose one animal from each section as the carousel spins.

- 🎠 Carousel Machine = Loop: Just like the carousel machine spins through different animal seats, the loop goes through different rows.

- 🎠 Each Turn = Each Iteration: Each turn of the carousel machine moves you to a new set of animal seats, just like each iteration of the loop moves to the next row. 🎠


```bash
   0 | 1 | 2
  ---|---|---
   3 | 4 | 5
  ---|---|---
   6 | 7 | 8

```

## or

[ 🐴 | 🦄 | 🐪 ]

[ 🦓 | 🦒 | 🦁 ]

[ 🐯 | 🐵 | 🦔 ]

#### Each section represents a different part of the carousel 🎠 . Think of these sections like the rows in our Tic-Tac-Toe game

- - Imagine you’re at a **funfair** 🎪 with a carousel 🎠 that has 3 sections.

- - Each section has different animals to ride on. You get to choose one animal 🦓 from each section as the carousel spins .

<br>


<br>

### 🍭 When i is 0:

- -  `i*3` is `0*3`, which equals `0`.

- - This means **we start at position `0`** in the **list**.

<br>

### 🎠 How it works, imagine a iteration, like a carousel SPIN, each turn is similar to a loop iteration

<br>


#### First Round (First Turn):

```bash
Round 1:
[ 🐴 | 🦄 | 🐪 ]


# - You start at the first section.
# - Pick an animal from this section.
# - Example: You choose the 🐴 from the first section.
```
#### Second Round (Second Turn):

```bash
Round 2:
[ 🦓 | 🦒 | 🦁 ]
# - Carousel turns to the second section.
# - Pick an animal from this new section.
# - Example: You choose the 🦓 from the second section.
```
#### Third Round (Third Turn):

```bash
Round 3:
[ 🐯 | 🐵 | 🦔 ]

# - Carousel turns to the third section.
# - Pick an animal from this last section.
# - Example: You choose the 🐯 from the third section.
```

<br>
<br>

```python
Tic-Tac-Toe Grid:

🍭
1. **First Iteration (i = 0)**
   - Start at index: 0
   - End at index: 3
   - Extract: [0, 1, 2]

   [0 | 1 | 2]  <- First Row (0 to 2)

🍰
2. **Second Iteration (i = 1)**
   - Start at index: 3
   - End at index: 6
   - Extract: [3, 4, 5]

   [3 | 4 | 5]  <- Second Row (3 to 5)

🍓
3. **Third Iteration (i = 2)**
   - Start at index: 6
   - End at index: 9
   - Extract: [6, 7, 8]

   [6 | 7 | 8]  <- Third Row (6 to 8)

```
<br>

#### and opla.. jump to the next row

![tumblr_f7a8d8b69cdcc60f31cb097c3a334d5f_82b2b893_500](https://github.com/user-attachments/assets/a1a09d4d-7946-4d44-8765-8b700a3a5280)


<br>

### Visual Explanation

```bash
| 0 | 1 | 2 |  <- First Row (0 to 2)
| 3 | 4 | 5 |  <- Second Row (3 to 5)
| 6 | 7 | 8 |  <- Third Row (6 to 8)
```



<br>

## `for row in [self.board[i*3:(i+1)*3] for i in range(3)]:`


## 🟠 What i+1 Does 🟡

`i+1` helps us figure out the end position of the slice.


```bash
i represents the current row index.

i + 1 gives you the next row’s index, which helps determine the end of the current row.
```
<br>

#### 🟣 in other words: `i + 1` gives you the next row’s index, which helps determine the end of the current row.

```bash
For i = 0: (0+1)*3 = 3 which gives us the end index 3.
For i = 1: (1+1)*3 = 6 which gives us the end index 6.
For i = 2: (2+1)*3 = 9 which gives us the end index 9.
```



### 🟣 In other words: when the first round (or spin) of the carousel ends, it slices at position 3, which marks the end of the first row and the beginning of the second row.

```python
# (i+1) or (0+1)
For i = 0: (0+1)*3 = 3 which gives us the end index 3.
```
<br>

### As the carousel continues to spin, the visible rows are updated, but this movement is not shown in the slice. The slicing expression [self.board[i*3:(i+1)*3]] dynamically adjusts to extract each row based on the current iteration.

```python
For i = 1: (1+1)*3 = 6 which gives us the end index 6.
# AND so on
```
<br>
<br>

### Expanding to a Grid with 4 Values Per Row


- - If you change the slicing formula to `[self.board[i*4:(i+1)*4]]`, this will create a grid where each row contains 4 values:

```bash
| 🐴 | 🦄 | 🐪 | 🦓 |  <- First Row (positions 0 to 3)
| 🦒 | 🦁 | 🐯 | 🐵 |  <- Second Row (positions 4 to 7)
| 🦔 | 🦋 | 🦜 | 🦨 |  <- Third Row (positions 8 to 11)
```
