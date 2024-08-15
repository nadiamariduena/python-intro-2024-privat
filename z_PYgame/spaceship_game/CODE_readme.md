
## 🧶 Sections

<br>
<br>

### 🟡 Scene

- `update()` : [Go to section](#update_)

-  `flip()`: [Go to section](#flip_)


-  `surface()`: [Go to section](#surface_)

- -  `surface.fill(())`

-   `display()`: [Go to section](#display_)

<br>

### 🟡 Blit | Animation | load img's

<br>

- Animation:  [Go to section](#anim1_)

- Create a Surface shape: [Go to section](#anotherSurface_)


- - `Blit()`: [Go to section](#blit_)

> - - - Blit() is a fancy way of saying <u>You want to put ONE surface on ANOTHER surface</u>



- Load Image: [Go to section](#load_img_)



<br>

---


<br>
<br>


## 🟦 Phase 1


## 🟠 Import and Init

```python

import pygame  # Import the Pygame library, which provides functionalities for game development and multimedia applications.

# ---- general setup ----

# Initialize Pygame modules and settings
pygame.init()  # Initialize all imported Pygame modules. This must be called before using other Pygame functions.
```
<br>
<br>

### 🟦 The following should be added at the top and bottom of the file

```python
# init/start
pygame.init()

# end
pygame.quit()
# the pygame,quit() should always be placed after the loop
```

<br>
<br>
<br>

## 🟠 Create the window

- Its a bit similar to threejs [3d-waving-flag-threejs](https://github.com/nadiamariduena/3d-waving-flag-threejs)


```python
# Define the dimensions for the window
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720  # Set the width and height of the window. These values define the resolution of the display surface.

# Create a display surface with the specified dimensions
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # Create a window or screen for display with the specified width and height. This surface is where you'll draw your game graphics and handle user interactions.
```

<br>
<br>

## 🟠 Implement the Loop

- -  Compare the below codes (both):

- - - The code below is from a previous project

[https://github.com/nadiamariduena/python-intro-2024-privat/blob/master/LESSON_5_loops/loop_rain/intro_pygame.py](https://github.com/nadiamariduena/python-intro-2024-privat/blob/master/LESSON_5_loops/loop_rain/intro_pygame.py)


```python
import pygame

pygame.init()

# Define the dimensions for the window
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# ✋
running = True

# ✋
while running:
#------------- GAME LOOP
# 6 WHILE 'run' is TRUE ':' execute all the code below
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False

```

<br>
<br>


## 🟠 DRAW <u>the game</u>

#### `pygame.display.update()` and `pygame.display.flip()

 The teacher on the tutorial says that **they are the same**, `but` **they are not**. [read more: update_and_flip_diff](../update_and_flip_diff_.md)

- - In Pygame, both `pygame.display.update()` and `pygame.display.flip()` are **used** to **update** the contents of the display, **but** they have **different use cases and behaviors**.

<br>
<br>


## 🟦 Draw: `Fill`



### Read the documentation

- - https://pyga.me/docs/ref/draw.html

- - https://pyga.me/docs/ref/display.html

<br>

🔶 I will be using the **display** & the `surface`

<br>
<br>

#### 🟣 QUESTION:  to draw something using pygame, do you need first the `display` and then the `surface`, why?

<br>

#### ✅ chatgpt:

-  When using Pygame to draw graphics, the process involves working with both the display and surfaces. Here's a breakdown of why both are necessary: