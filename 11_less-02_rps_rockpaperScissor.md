## 🍊 Rock paper scissor

https://youtu.be/N94vSNBF-EI?feature=shared&t=31

<br>
<br>

### 1 Begin with the game

```python
print("")

playerChoice = input("Enter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

print(playerChoice)
#https://www.codecademy.com/forum_questions/52f31477282ae3c473002317
#
#
#  \n – newline
#
# result
Enter...
1 for Rock,
2 for Paper, or
3 for Scissors:

```

<br>

## 2

```python
print("")
#\n – newline
playerChoice = input("Enter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")


#
#
if playerChoice < 1  | playerChoice > 3:
    # the problem with the below code is that its going to continue to execute, so we have to find a way to EXIT the program
    print("You ust enter 1, 2, or 3")

```

## YOu remember that on the previous tutorial, I imported the math, so to use it on several examples:

```python
# ----
# 1 you can import the match method like here below
import math
#
# 2 and use it on the examples below
# ----- MATH
print(math.pi)
#result: 3.141592653589793
#
```

### So following that example we can import something else, we will import the sys to EXIT the program

```python
import sys
 #
 # TO EXIT the program
    sys.exit("You must enter 1, 2 , or 3")
```

### LIKE SO:

```python
import sys
#  without the sys you cannot EXIT the program on line 15
#
print("")

playerChoice = input("Enter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

#\n – newline
#
# print(playerChoice)
if playerChoice < 1  | playerChoice > 3:
    # print("You ust enter 1, 2, or 3")
    # sys.exit("You must enter 1, 2 , or 3")
    # 🍧 TO EXIT the program
    sys.exit("You must enter 1, 2 , or 3")
```

<br>
<br>

### 🟡 SYS

`sys.exit()` is a function **provided by the sys module** in Python that is used to exit the Python interpreter. It's typically called with an optional integer argument representing an exit status. If no argument is provided, it exits with a status code of zero, indicating successful termination.

### Here are some common functionalities provided by the sys module:

<br>

**Access to Command-Line Arguments:** sys.argv allows you to access the list of command-line arguments passed to a Python script.

**System-Specific Parameters and Functions:** sys.platform provides information about the platform where Python is running (e.g., 'linux', 'win32', 'darwin' for Linux, Windows, and macOS, respectively).

**Access to Python Interpreter Settings:** sys.version gives information about the version of Python being used. sys.path provides a list of directories where Python searches for modules.

**Interaction with the Python Interpreter:** sys.stdin, sys.stdout, and sys.stderr are file-like objects representing standard input, standard output, and standard error, respectively.

**Memory Management:** `sys.getsizeof()` can be used to determine the size of an object in memory.

**Exiting the Interpreter:** `sys.exit()` can be used to exit the Python interpreter with a specified exit status.

<br>
<br>

## BACK to the code

- 🔴 here we have another problem we didnt address, the **input** is a string and we have to convert it to an **INT** otherwise it will trigger an **error**

```python
playerChoice = input("Enter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

```

### converting it

```python

#  you need to convert the input from STRING to Int
player = int(playerChoice)

```

<br>

### now replace this

- use the new assigned variable "player"

```python
# from this
# print(playerChoice)
if playerChoice < 1  | playerChoice > 3:
     # TO EXIT the program
    sys.exit("You must enter 1, 2 , or 3")

#------------ **
#
# TO THIS:
# print(playerChoice)
if player < 1  | player > 3:
     # TO EXIT the program
    sys.exit("You must enter 1, 2 , or 3")

```

<br>
<br>

# 🟨 RANDOM

> The random module has a set of methods:

https://www.w3schools.com/python/module_random.asp

<br>

#### Now we need to compare between the options on the game

- I will import another Module, this module is called **random** and we will add also add it at the top of the component

```python
  # sys.exit() is a function provided by the sys module in Python that is used to exit the Python interpreter. It's typically called with an optional integer argument representing an exit status. If no argument is provided, it exits with a status code of zero, indicating successful termination.
# "
import sys
#  without the sys you cannot EXIT the program on line 15
#
# the RANDOM module
import random
 #

print("")

playerchoice = input("Enter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")
#\n – newline
#  you need to convert the input from STRING to Int
player = int(playerchoice)
#
# print(playerChoice)
if player < 1  | player > 3:
     # TO EXIT the program
    sys.exit("You must enter 1, 2 , or 3.")

# 🗯️ its going to randomly choose one of the characters from this string using random dot choice
computerchoice = random.choice("123")
# so after that we'll cast that to an integer
computer = int(computerchoice)

#
#
print("")
print("You choose " + playerchoice + ".")
print("Python chose " + computerchoice + ".")
print("")
```

<br>

### result

```python
Enter...
1 for Rock,
2 for Paper, or
3 for Scissors:

2 # you have to type 2 here, then you will get the result below:

You choose 2.
Python chose 1.

```

<br>

### 🍊 its working as expect, but its not telling me who won

- here below i will add a conditional with a message depending of each result

```python
#
# Define who won
# if player choose 1 which is rock and computer choose 3 which is scissors
if player == 1 and computer == 3:
    print("You win!")
elif player == 2 and computer == 1:
    print("You win!")
elif player == 3 and computer == 2:
    print("You win!")
else:
    print("Python wins")
```

<br>

### 🍊 BUT WHAT IF the computer and the player choose the same

```python
# /else if: the choice of the player is equal to the choice the computer then it a "tie game"
elif player == computer:
    print("Tie game!")
```

<br>
<br>

### the game

```python
  # sys.exit() is a function provided by the sys module in Python that is used to exit the Python interpreter. It's typically called with an optional integer argument representing an exit status. If no argument is provided, it exits with a status code of zero, indicating successful termination.
# "
import sys
#  without the sys you cannot EXIT the program on line 15
#
# the RANDOM module
import random
 #

print("")

playerchoice = input("Enter... \n1 for Rock🪨,\n2 for Paper🧻, or \n3 for Scissors 🌂 :\n\n")
#\n – newline
#  you need to convert the input from STRING to Int
player = int(playerchoice)
#
# print(playerChoice)
if player < 1  | player > 3:
     # TO EXIT the program
    sys.exit("You must enter 1, 2 , or 3.")
    # result: if someone types 0 or 4 or more than 4, it will exit the program with this message: You must enter 1, 2 , or 3.

# 🗯️ its going to randomly choose one of the characters from this string using random dot choice
computerchoice = random.choice("123")
# so after that we'll cast that to an integer
computer = int(computerchoice)

#
#
print("")
print("You choose " + playerchoice + ".")
print("Python chose " + computerchoice + ".")
print("")

#
# Define who won
# if player choose 1 which is rock and computer choose 3 which is scissors
if player == 1 and computer == 3:
    print("🎉 You win!")
elif player == 2 and computer == 1:
    print("🎉You win!")
elif player == 3 and computer == 2:
    print("🎉You win!")
elif player == computer:
    print("🍿Tie game!")
else:
    print("👾Python wins")

#
# 👍
#result
Enter...
1 for Rock🪨,
2 for Paper🧻, or
3 for Scissors 🌂 :

2

You choose 2.
Python chose 2.

🍿Tie game!
```

<br>

---

<br>

### Another way

- add the following:

```python
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print(RPS(2))
print(RPS.ROCK)
print(RPS['ROCK'])
print(RPS.ROCK.value)
#exit the program
sys.exit()
#
# #
# #  --
# # result
RPS.PAPER #print(RPS(2)) check line 342 and 339
RPS.ROCK # print(RPS.ROCK)
RPS.ROCK # print(RPS['ROCK'])
1 # print(RPS.ROCK.value)
```

### Like so

- you will notice that from the moment we add the code with the above **class** , the line of the **playerchoice** and all after that will be ignored

```python
import sys
#  without the sys you cannot EXIT the program on line 15
#
# the RANDOM module
import random
#
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print(RPS(2))
print(RPS.ROCK)
print(RPS['ROCK'])
print(RPS.ROCK.value)
#exit the program
sys.exit()
#
#-------
print("")

playerchoice = input("Enter... \n1 for Rock🪨,
```

<br>
<br>

### 🔶 so now we are going to replace a couple of things for the setup with the enum

- start by hiding the RPS from here

```python
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# ✋ hide this, i will be using the RPS in another way
#
# print(RPS(2))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)
# #exit the program
# sys.exit()
#
```

<br>

### then replace this for the RPS

```python
# before
print("")
print("You choose " + playerchoice + ".")
print("Python chose " + computerchoice + ".")
print("")

#
#
# AFTER
print("")
print("You choose " + str(RPS(player)) + ".")
print("Python chose " + str(RPS(computer)) + ".")
print("")
#
#
# ✋ RESULT

Enter...
1 for Rock🪨,
2 for Paper🧻, or
3 for Scissors 🌂 :

3

You choose RPS.SCISSORS.
Python chose RPS.PAPER.

🎉You win!
```

<br>

### But why?

<br>
