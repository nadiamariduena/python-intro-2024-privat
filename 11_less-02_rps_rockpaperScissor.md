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

#
#
# TO THIS:
# print(playerChoice)
if player < 1  | player > 3:
     # TO EXIT the program
    sys.exit("You must enter 1, 2 , or 3")

```
