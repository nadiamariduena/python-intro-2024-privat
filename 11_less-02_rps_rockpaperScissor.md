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
