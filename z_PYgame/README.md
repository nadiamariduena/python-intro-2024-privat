
# 🟡 PyGame

**Pygame** is a popular library **used for** creating **games** and multimedia applications **in Python**.

- - It provides a set of Python modules designed to handle common game development tasks, such as handling graphics, sound, and user input.

<br>

- - >Pygame is a great tool for learning game development and building simple games, prototypes, or multimedia projects.


<br>

#### 🟤 [Get Started in Pygame in 10 minutes!](https://www.youtube.com/watch?v=y9VG3Pztok8)


#### 🟤 [Master Python by making 5 games [the new ultimate introduction to pygame]](https://youtu.be/8OMghdHP-zs?si=EctW5eUYfkCyUZ7s)

<br>
<br>

# 🟡 INTRO

### Drawing on screen

- Simple exercise to get started with **Pygame**, based on this tutorial:  [Get Started in Pygame in 10 minutes!](https://www.youtube.com/watch?v=y9VG3Pztok8)


<br>

```python
# 1
import pygame
# 2
pygame.init()
# 3
# Window dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# 4 create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT ))
```

- - - Python is going to scann one by one the below steps, then when it reaches the step 4, it will EXIT the window automatically (because there is nothing yet)

<br>
<br>
<br>

## 🍍   WHILE Loop

<br>

#### In order to Keep the the window open, I need to CREATE a second element from those 3 steps (from step 2 to 4), one way to do that is by using LOOPS.

<br>

- For this game I will be using the While loop (i think you can also use the SWITCH loop)

- - **WHILE loop:** As long as a condition is true the while loop continue running

- - To do that, lets create a variable with some boolean: `run = True`
