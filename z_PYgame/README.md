
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
        player.move_ip() # ip: stands for MOVE IN-PLACE
        #  between the parentheses/brackets I pass in the movement in the X direction and the Y direction, if i am moving LEFT then I am subtracting from the X coordinate and I am not affecting the Y coordinate
```

<br>
<br>

## 🟠 Duplicate the KEY logic


```python
if key[pygame.K_a] == True:
    # X , Y
        player.move_ip(-1, 0)
```

#### Instead of using **if** all the time, we'll use `elif` for the next key.

- - This way, if the first key isn’t being pressed, it will check the next key, and so on (depending on how many keys you have).

>**elif** means "else if" and it helps to check more keys in order if the first one isn’t pressed.




```python
  # 🤚 X coordinates
    if key[pygame.K_a] == True:
        # LEFT : -1 , the 0 is Y, here we dont do anything with the Y:0
        player.move_ip(-1, 0)

    elif key[pygame.K_d] == True:
        # RIGHT:
        player.move_ip(1, 0)



        # 🤚 Y coordinates
    elif key[pygame.K_w] == True:
        # TOP
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        # Bottom
        player.move_ip(0, 1)
```

<br>
<br>

### Working Correctly

- 🔴 Its working, but its leaving a trail

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



    #14 First thing i need to know, is which key on the keyboard is being pressed
    key = pygame.key.get_pressed()

    # W.A.S.P
    # 15 if the KEY being pressed is A so its true, then i want to ...
     # 🤚 X coordinates
    if key[pygame.K_a] == True:
        #16
        # ...move the rectangle to the left, the rectangle is assigned to the variable player
        player.move_ip(-1, 0) # ip: stands for MOVE IN-PLACE
        #  between the parentheses/brackets I pass in the movement in the X  direction and the Y direction, if i am moving LEFT (X) then I am subtracting from the X coordinate and I am not affecting the Y coordinate
    elif key[pygame.K_d] == True:
        # move it to RIGHT
        player.move_ip(1, 0)
        # 🤚 Y coordinates
    elif key[pygame.K_w] == True:
        # move it to RIGHT
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        # move it to RIGHT
        player.move_ip(0, 1)

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

## 🟦 The trail

- The reason for the trail is that the screen is not being refreshed, its keeping a history of everything that has been drawn

<br>

- 🔴 a short term solution is to **add a black screen**

```python
screen.fill((0,0,0))
```

<br>
<br>

#### 🟣 QUESTION: The teacher's solution to the trail issue in the code involved adding a dark fill. However, I’m not sure this is the best approach, as it seems to overlap with the data of the trail.

 In React, we can use `useEffect()` to manage and **clean up processes** specially for 3d apps running in the background.

#### What would be the equivalent solution in Python for clearing the trail?

<br>

#### ✅ chatgpt:

- **Yes**, your concern is valid.

- - **Adding a dark fill might not be the best solution** if it affects the visibility or clarity of the trail data.

- - Overlapping or obscuring important data with a fill could create more problems than it solves.

In programming, especially when dealing with graphical elements or animations, it's important to ensure that each component is properly managed and cleaned up to avoid visual artifacts or performance issues.

In Python, especially if you're working with graphical libraries like Pygame or Tkinter, you might handle cleanup differently than in React. You would typically need to:

#### Clear the Canvas:

Ensure that the drawing area or canvas is cleared or reset appropriately between frames or updates.

#### Manage State:

Keep track of the state of your trails and clear or update them as needed.

#### Use Event Loops:

Properly manage event loops to ensure that resources are released and not left running in the background.


<br>

### 🌈 SOLUTION

#### Update Player Position and Screen Update:

- - The player’s position should be updated before drawing it to the screen.


#### Handle the `pygame.display.update()` Correctly:

- - `pygame.display.update()` should be called after you have drawn everything for the current frame.


```python
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT ))

player = pygame.Rect((300, 250, 50, 50))

run = True

while run:

    # fill BG
    # screen.fill((0,0,0))
    # pygame.draw.rect(screen, (255, 0, 0), player)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    key = pygame.key.get_pressed()

    # W.A.S.P
     # 🤚 X coordinates
    if key[pygame.K_a] == True:
        # move it to LEFT
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        # move it to RIGHT
        player.move_ip(1, 0)
        # 🤚 Y coordinates
    elif key[pygame.K_w] == True:
        # move it to TOP
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        # move it to BOTTOM
        player.move_ip(0, 1)

    #------------- EVENT handler
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         run = False

    # Fill the background
    screen.fill((0, 0, 0))

    # Draw the player
    pygame.draw.rect(screen, (255, 0, 0), player)

    # Update the display
    pygame.display.update()

    pygame.display.update()

pygame.quit()
```

<br>

### 🔴 Before the changes

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



    #14 First thing i need to know, is which key on the keyboard is being pressed
    key = pygame.key.get_pressed()

    # W.A.S.P
    # 15 if the KEY being pressed is A so its true, then i want to ...
     # 🤚 X coordinates
    if key[pygame.K_a] == True:
        #16
        # ...move the rectangle to the left, the rectangle is assigned to the variable player
        player.move_ip(-1, 0) # ip: stands for MOVE IN-PLACE
        #  between the parentheses/brackets I pass in the movement in the X  direction and the Y direction, if i am moving LEFT (X) then I am subtracting from the X coordinate and I am not affecting the Y coordinate
    elif key[pygame.K_d] == True:
        # move it to RIGHT
        player.move_ip(1, 0)
        # 🤚 Y coordinates
    elif key[pygame.K_w] == True:
        # move it to RIGHT
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        # move it to RIGHT
        player.move_ip(0, 1)

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

# 🟡 FPS

<br>

### 🟣 QUESTION: Could you provide me with the code to check the FPS of this project in Python?

<br>

#### ✅ chatgpt: You can modify your Pygame code to include FPS tracking and display the FPS on the screen.

- Here’s an updated version of your code with FPS tracking:

```python
import pygame
import sys ✋

pygame.init()

# Set up display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set up player
player = pygame.Rect((300, 250, 50, 50))

# Set up FPS clock
clock = pygame.time.Clock()
FPS = 60  # Set the desired FPS 🤚

run = True

while run:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Get pressed keys
    key = pygame.key.get_pressed()

    # Move the player based on key presses
    if key[pygame.K_a]:
        player.move_ip(-1, 0)
    elif key[pygame.K_d]:
        player.move_ip(1, 0)
    elif key[pygame.K_w]:
        player.move_ip(0, -1)
    elif key[pygame.K_s]:
        player.move_ip(0, 1)

    # Fill the background
    screen.fill((0, 0, 0))

    # Draw the player
    pygame.draw.rect(screen, (255, 0, 0), player)

    # Display FPS🤚
    font = pygame.font.Font(None, 36)
    fps_text = font.render(f'FPS: {int(clock.get_fps())}', True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Control the frame rate 🤚
    clock.tick(FPS)

pygame.quit()
sys.exit()

```

<br>
<br>

### 🟦 Understanding FPS (frames per second) helps you gauge how smoothly your game or application is running.

#### Here's how to interpret FPS values:

### 🟠 FPS Interpretation:

**High FPS (e.g., 60 FPS or more):**

 - -  This indicates smooth performance. The game or application is updating quickly, and you should experience fluid motion and responsiveness. This is typically considered ideal for most interactive applications.

**Low FPS (e.g., 30 FPS or less):**

- -  This suggests slower performance. The game or application is updating less frequently, which may result in choppy or stuttery visuals and reduced responsiveness. Lower FPS can affect the user experience negatively.

<br>
<br>

### 🟦 What is "Okay" FPS?

<br>

🌈**60 FPS:** Often considered the target for smooth gameplay or applications, providing a very fluid experience.

🟤**30 FPS:** Generally acceptable for many games and applications, though it may feel less smooth compared to 60 FPS.

🔴 **Below 30 FPS:** Can be problematic and might indicate performance issues. It could lead to noticeable lag and poor user experience.

<br>

### Understanding FPS Limitations:

Monitor Capabilities: The refresh rate of your monitor can limit your FPS. For example, a 60Hz monitor can display up to 60 FPS.

- - 🔴 Hardware Constraints: 🔴 The performance of your CPU, GPU, and other components can affect your achievable FPS.