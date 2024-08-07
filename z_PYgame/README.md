
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

<br>

```python
# 5 create a variable that is going to be used for the condition on the WHILE LOOP
run = True
# 6 WHILE 'run' is  (equal to true) ':' execute all the code below
while run == True:
```

<br>

#### You can also use this way:

```python
while run
# its the same as this:
while run == True:
```

<br>

### 🟦 WHILE loop & EVENT handler


```python

#------------- GAME LOOP
# 6 WHILE 'run' is  (equal to true) ':' execute all the code below
while run:
    # Note: The while loop contains a nested for loop, so make sure to keep an eye on the indentation.



    #------------- EVENT handler
    for event in pygame.event.get():
        # 7 This for loop goes through all the events that Pygame has collected.

        # We can examine each event individually to find specific ones.

        # For simplicity, we are only interested in the event that allows us to close the game window,

        # which is triggered by clicking the X in the top-right corner of the screen.


        # 8 We can detect this event with an if statement.
        if event.type == pygame.QUIT:
            # 9 If the condition is true (i.e., the QUIT event is detected),
            # we set 'run' to False to exit the while loop, effectively closing the game.
            run = False
#-------------
# 10 at this point we can run the game (which is only a black window for now)
pygame.quit()
```

<br>
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
#
# the rect() function, similar to canvas i guess https://www.w3schools.com/jsref/canvas_rect.asp
# screen = pygame.Rect((300, 250, 50, 50))

# 5 create a variable that is going to be used for the condition on the WHILE LOOP
run = True

#------------- GAME LOOP
# 6 WHILE 'run' is  (equal to true) ':' execute all the code below
while run:
    # Note: The while loop contains a nested for loop, so make sure to keep an eye on the indentation.



    #------------- EVENT handler
    for event in pygame.event.get():
        # 7 This for loop goes through all the events that Pygame has collected.

        # We can examine each event individually to find specific ones.

        # For simplicity, we are only interested in the event that allows us to close the game window,

        # which is triggered by clicking the X in the top-right corner of the screen.


        # 8 We can detect this event with an if statement.
        if event.type == pygame.QUIT:
            # 9 If the condition is true (i.e., the QUIT event is detected),
            # we set 'run' to False to exit the while loop, effectively closing the game.
            run = False
#-------------
# 10 at this point we can run the game (which is only a black window for now)
pygame.quit()
```

<br>
<br>
<br>
<br>

## 🍍 THE TOOL/PEN

- Here I will be implementing the Position of the tool and the style of the tool

<br>

### 🟠 POSITION of the TOOL:

- -  Create a <u>tool/rectangle</u>  that can be moved across the screen with the keyboard


<br>

> - - 🔴 This has to be done **outside of the game loop**

> - - You have to position this rectangle before the while loop starts

<BR>
<br>



### 🟠 Coordinates

`player = pygame.Rect((300, 250, 50, 50))`

### The rectangle has 4 coordinates

**The first 2 coordinates**: are the `X and Y` coordinates on the screen which all passes 300 and 250

- - **300**: This tells us how far the box is from the left side of the screen. If your screen is very wide, 300 steps from the left might be somewhere in the middle, but not exactly in the center.

- - **250**: This tells us how far the box is from the top of the screen. If your screen is tall, 250 steps down from the top might place the box roughly in the middle of the screen’s height.

- - **50:** This is the width of the box, meaning how wide it is from left to right. If you measure the box, it will be 50 steps wide.

- - **50:** This is the height of the box, meaning how tall it is from top to bottom. If you measure the box, it will be 50 steps tall.


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

# 11 create the tool to draw (outside of the loop),
# the functioning tool logic, will be added within the WHILE loop after this.
# 🟥
player = pygame.Rect((300, 250, 50, 50))
#300, 250:  a bit towards the center of the screen
```

<br>
<br>

### 🟠 Style of the TOOL:

## `pygame.draw.rect(screen, (255, 0, 0), player)` has three main parts, each serving a specific purpose:

<br>

#### `screen`:

- - This is where you are drawing. It’s the surface or canvas that will display everything.

#### `(255, 0, 0)`:

- - This is the color of the rectangle. In this case, it specifies a bright red color using the RGB color model.

#### `player`:


- - This defines the position and size of the rectangle. It tells Pygame where to draw the box and how big it should be, based on the coordinates and dimensions you provided.

```python
while run:
    # 12 ✋ THE TOOL: contain 3 arguments, the screen , the rgb and the player who is going to draw
    pygame.draw.rect(screen, (255, 0, 0), player)
    #------------- EVENT handler
    for event in pygame.event.get():
```

<br>

## 🟦 Refresh the changes


- - Think of `pygame.display.update()` as a final step to show what you’ve drawn.

```python
# the purpose is to refresh or update the screen with any changes that have been made.
pygame.display.update()
```

<br>
<br>

### Before continuing

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
#
# the rect() function, similar to canvas i guess https://www.w3schools.com/jsref/canvas_rect.asp


# 11 create the tool to draw (outside of the loop), the functioning tool logic, will be added within the WHILE loop after this.
#
#
# we want to draw as a small box on the screen. To decide where this box will go, we use four numbers:  is like saying: “Put a small box that’s 50 steps wide and 50 steps tall, starting 300 steps from the left and 250 steps down from the top of the screen.
player = pygame.Rect((300, 250, 50, 50))
#300, 250:  a bit towards the center of the screen


# 5 create a variable that is going to be used for the condition on the WHILE LOOP
run = True

#------------- GAME LOOP
# 6 WHILE 'run' is  (equal to true) ':' execute all the code below
while run:
    # Note: The while loop contains a nested for loop, so make sure to keep an eye on the indentation.

    # 12 THE TOOL: contain 3 arguments, the screen , the rgb and the player who is going to draw
    pygame.draw.rect(screen, (255, 0, 0), player)


    #------------- EVENT handler
    for event in pygame.event.get():
        # 7 This for loop goes through all the events that Pygame has collected.

        # We can examine each event individually to find specific ones.

        # For simplicity, we are only interested in the event that allows us to close the game window,

        # which is triggered by clicking the X in the top-right corner of the screen.


        # 8 We can detect this event with an if statement.
        if event.type == pygame.QUIT:
            # 9 If the condition is true (i.e., the QUIT event is detected),
            # we set 'run' to False to exit the while loop, effectively closing the game.
            run = False

    # 13 Think of pygame.display.update() as a final step to show what you’ve drawn.
    pygame.display.update()
    # the purpose is to refresh or update the screen with any changes that have been made.

#-------------
# 10 at this point we can run the game (which is only a black window for now)
pygame.quit()
```

<br>
<br>
<br>
<br>


## 🍍 Add some controls

### 🟠 First thing i need to know, is which key on the keyboard is being pressed

```bash
key = pygame.key.get_pressed()
```

<br>

## 🟦 KEYS

### 🟠 Now i can look for specific key with an `if` statement

```python
# 15 if the KEY being pressed is A so its true, then i want to ...
 if key[pygame.K_a] == True:
```

<br>

### Move the tool with the KEY

```python
if key[pygame.K_a] == True:
#16
        # ...move the rectangle to the left, the rectangle is assigned to the variable player
        player.move_ip()
```