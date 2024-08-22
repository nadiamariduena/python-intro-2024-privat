# 🟡 Phase 3

## 🟠 Rects & Frects


- -  Read more [a__about_rects](../a__about_rects.md)

<br>

### What is the Difference between Rects & Frects

-  In Pygame, `Rect and frect (or FRect)` are **both used to represent rectangular areas**, but **they differ** mainly in the type of **precision** they **use for their coordinates and dimensions:**

<br>

## `rect` & `frect`

### ⚫  Differences

🔴 **Precision:** `Rect uses integer` values(20), while `FRect uses floating-point` values(20.5).



```python
# ✋ rect
import pygame
rect = pygame.Rect(10, 20, 30, 40)

#
# ✋ FRECT (great precision: 30.5)
import pygame.freetype
frect = pygame.freetype.FRect(10.5, 20.5, 30.5, 40.5)
```

<br>

> - - 🔴
it doesn't make sense to keep Rect with integers, it will be deprecated once FRect is released in 2.1.4. [Frect OR RECT](https://github.com/pygame/pygame/issues/3643)



<br>
<br>


## 🟠 About  Rect's

In Pygame, Rect objects represent rectangles with defined size and position.

- - They include a variety of **points** ⚫, such as **tuples with X and Y coordinates**.

- - - Additionally, Rect objects have properties for width, height, and overall size.

<br>

**Read More:** exercises and ways you can use the rect (collision example) [a__about_rects](../a__about_rects.md) , check the exercise below also there:

https://github.com/user-attachments/assets/3397c1ba-e011-49a0-a8c9-f9f915067076

<br>
<br>
<br>

### 🟤 In Pygame, Rect objects include several <u>key ⚫ points</u>  that help define their position and dimensions:


[<img src="../rect__dots.png"/>](https://www.youtube.com/watch?v=8OMghdHP-zs&t=821s)


<br>

**Top-left corner:** The `(x, y)` position of the rectangle's top-left corner.

```python
rect = pygame.Rect(30, 40, 100, 80)

# This creates a rectangle with:
# ✋
# Top-left corner at (30, 40)
# Width of 100 pixels
# Height of 80 pixels
```

<br>

**Top-right corner:** The `(x + width, y)` position of the rectangle's top-right corner.

<br>

**Bottom-left corner:** The `(x, y + height)` position of the rectangle's bottom-left corner.

**Bottom-right corner:** The `(x + width, y + height)` position of the rectangle's bottom-right corner.

<br>
<br>



<br>
<br>
<br>
<br>

## 🟠 POS & Dimensions:

<br>


- **WIDTH & HEIGHT:** Create a rectangle that is 20 pixels wide and 30 pixels tall

- **POSITION on the screen:** and place it at the position (100, 50) on the screen

```python
myRect = pygame.Rect(100, 50, 20, 30)
```

[<img src="../pygame-coords.png"/>](https://sigon.gitlab.io/post/2018-10-10-pygame-rect/)

<br>
<br>
<br>

## 🟠 `surface.get_rect()` / `pygame.Rect`

<br>

### 🟪 QUESTION: Which of the following options is more commonly used in Pygame development?


<br>

#### ✅ chatgpt:

- -  `pygame.Rect` is the most widely used and  [canonical](https://canonical.com/) way to handle rectangles in Pygame.

- - `surface.get_rect()` is a standard and commonly used method in Pygame to **obtain the bounding rectangle of a surface**.

<br>

```python
# OPT 1
pygame.Rect(pos, size)
pygame.Frect(pos, size)


# OPT 2
surface.get_rect(point = pos)
surface.get_frect(point = pos)
```

**Therefore**, `Option 1` is the **more standard and widely used approach in Pygame.**

- - If you are working with traditional Pygame development and need rectangles, you’ll typically use pygame.Rect and surface.get_rect().


<br>
<br>

<br>
<br>

## 🟦 Back to the Tutorial


- Before continuing, this is what i have until now, in the next step i will remove the animation, and i will replace a couple of things, so to use the `get_frect()`


```python
#0
import pygame
#14
# from os.path import join
import os

# after you add the images within the loop, import the star and randomize it
from random import randint




# 1
pygame.init()


# 15 Get the directory of the current script
script_dir = os.path.dirname(__file__)


#2 --- window
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
#3
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#------
# 9 change the window caption:
pygame.display.set_caption("Space shooter")
# change icon
# add an img to the project folder and insert it below
# pygame.display.set_icon('')


# 4 LOOP var
running = True


#10 create a surface
# w:100 px & h: 200px
# size of the shape
surf = pygame.Surface((100,200))
# # Add color to the shape/Surface
# surf.fill('orange')
# 11 anima
x = 100



#13 IMporting img
# player_surf = pygame.image.load(join('../images', 'player.png'))
# 16
# Build the path to the image file
# image_path = os.path.join(script_dir, '..', 'images', 'player.png')
# -----
# 19 import several images, so to not repeat the above line
# Dictionary of image paths
image_paths = {
    'player': os.path.join(script_dir, '..', 'images', 'player.png'),
    'star': os.path.join(script_dir, '..', 'images', 'star.png')
}

# 17 Load the image
# player_surf = pygame.image.load(image_path)
# 18 - convert
# player_surf = pygame.image.load(image_path).convert_alpha()
# 21
player_surf = pygame.image.load(image_paths['player']).convert_alpha()
star_surf = pygame.image.load(image_paths['star']).convert_alpha()

# 22
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]


# 5 the Loop
while running:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            running = False


 # FILL the window with a red color
 # player = pygame.Rect((300, 250, 50, 50))
 # https://pyga.me/docs/ref/pygame.html

 # 7 --- DRAW the game ----
 # list of colors: https://pyga.me/docs/ref/color_list.html
    display_surface.fill("lavenderblush2")

    for pos in star_positions:
        display_surface.blit(star_surf, pos)

    # 12 anima
    # CAREFUL with the identation, otherwise it wont work
    # means **you are increasing** the **value of x by 0.1 each time the loop runs.**
    x += 0.1
    # pos of the shape
    #  Position: Top-left corner at (100, 150) on the display surface
    # 20 Anim images ---
    display_surface.blit(player_surf, (x,150))

    # Anim images ---
    #`Blit()` is a fancy way of saying **You want to put ONE surface on ANOTHER surface**
    pygame.display.update()




# 6 EXIT
# - if you dont add the below, its not going to cause a problem but it will behave
pygame.quit()
```

<br>
<br>

### You have  a couple of options here, like for example:

```python
#1
player_rect = player_surf.get_frect(topleft = (0, 0))
#2
player_rect = player_surf.get_frect(center = (0, 0))
```

<br>

### 🟠 this position: `(0, 0)`,  would be the position on the display surface from here:


```python
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
```

