
## 🟡 ANIMATION 2.


- Up & down animation

- delta

- vectors

- - Vector Multiplication

- - 🔴 (very important) Why do we need vectors if we have lists?




<br>
<br>

<br>

### 🟦 Vectors & Delta

- using vectors to store a direction, including **DELTA** to make the movement frame rate independent


<br>

### 🟠 At the moment I'm using the below code to move the player left & right, but i no longer want to do that, so lets remove the below



```python
    # Continuously check if the player's rectangle has moved past the window's boundaries.
    if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:
    # If the rectangle's right edge exceeds the window width or its left edge is less than 0,
    # it means the player has reached one of the screen edges.

     player_direction *= -1
    # Reverse the movement direction by multiplying `player_direction` by -1 to make the plane move in the opposite direction.
```

### 🟠 Modify this line



```python

    # if player x direction positive +=, then it will be increased +, hence will move to the right.
    player_rect.x += player_direction * 100
    # if player x direction negative -=, then it will be decreased -, hence will move to the left


    # - * 0.4 or *100: calculates the amount to move the player horizontally
```

### 🟠   for the below, as i only want to move the player in one direction

```python
    # it will be multiplied by 100px every single frame
    player_rect.x += 100
    #  if player x direction positive +=, then it will be increased +, hence will move to the right.
    # -------------
```

<br>
<br>

### 🌈 Before animating the player this is what i have

- i changed the fps again and the animation

```python

import pygame
import os
from random import randint


pygame.init()
script_dir = os.path.dirname(__file__)



WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space shooter")


#while loop related
running = True
#✋ CLOCK:  FPS (frame per second)
clock = pygame.time.Clock()




# img's path
image_paths = {
    'player': os.path.join(script_dir, '..', 'images', 'player.png'),
    'star': os.path.join(script_dir, '..', 'images', 'star.png'),
    'meteor': os.path.join(script_dir, '..', 'images', 'meteor.png'),
    'laser': os.path.join(script_dir, '..', 'images', 'laser.png')

}



player_surf = pygame.image.load(image_paths['player']).convert_alpha()

# 1. -----  move right to left loop  ---
player_direction = 1
# -----  move right to left loop  ---


meteor_surf = pygame.image.load(image_paths['meteor']).convert_alpha()
laser_surf = pygame.image.load(image_paths['laser']).convert_alpha()

# (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
# Will pos the plane at the center of the screen/window
player_rect = player_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 10))

# start
star_surf = pygame.image.load(image_paths['star']).convert_alpha()
# star pos
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]



while running:


    clock.tick(10) #✋


    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            running = False

    display_surface.fill("lavenderblush2")


    for pos in star_positions:
        display_surface.blit(star_surf, pos)


    # player
    display_surface.blit(player_surf, player_rect)
    # meteor
    display_surface.blit(meteor_surf, meteor_rect)
    # laser
    display_surface.blit(laser_surf, laser_rect)


    # it will be multiplied by 100px every single frame
    player_rect.x += 20 #✋
    #  if player x direction positive +=, then it will be increased +, hence will move to the right.
    # -------------





    pygame.display.update()



pygame.quit()
```

<br>
<br>




<br>

### 🧶 Up & down animation

- BASIC: for the basic **up animation** we will need 2 lines:

```python
player_rect.x += 20
# Moves the rectangle to the right by 20 pixels
# Increases the x-coordinate, moving the rectangle to the right.


player_rect.y += 10
# Moves the rectangle down by 10 pixels
# Increases the y-coordinate, moving the rectangle down.
```
> #### 🟠 In this part of the game development, we are dealing with updating the position of our player’s rectangle.

<br>

[<img src="../fps_up_anim_1.gif"/>]( )


<br>
<br>



### 🟧 1. We want to update, both the `x` and `y` coordinates:



```python
player_rect.x += 20
player_rect.y += 10

```






### 🟠 2. Now We want to update both the x and y coordinates simultaneously using a single operation:


- Here below we are grabbing one of the tuple() points inside of the rectangle

```python
player_rect.center += (20, -10)
```




<br>

### Explanation:

#### `player_rect.center`:

-  - Represents the center point of the rectangle.


#### `(20, -10)`:

-  - Moves the rectangle’s center by 20 pixels to the right and 10 pixels up.

<br>
<br>

### 🟦 If we tried to execute this, it will raise an error:

```python
player_rect.center += (20, -10)
```

## 🔴  error:

- We have an invalid **rect** assignment 🤔

>An its because we cannot add a tuple() or a list[] to a tuple position inside of the rectangle

```python
 File "main_0_fps.py", line 92, in <module>
    player_rect.center += (20, -10)
TypeError: invalid rect assignment 🔴
```

<br>

## 🧶 Why Does player_rect.center += (20, -10) Result in an Error?

#### Immutable Assignment:

- - In Pygame, the center attribute of a Rect object is a property that represents the center point of the rectangle.

<br>

- - This property is not directly mutable via operations like addition or subtraction with a tuple.

> - - #### ✋ It’s a special attribute that Pygame manages internally, and you can’t use operators like `+=` to modify it directly.

<br>

### 🔴 Why This Error Occurs


#### 🟫 Tuple Operations Not Allowed:

`player_rect.center`

- -  **returns a tuple** representing the `center position (x, y)` **of the rectangle**

<br>

- - 🔴 **In Python, tuples are immutable**, meaning their values cannot be changed once they are created.

<br>

- - 🔴  The operation `player_rect.center += (20, -10)` **attempts to modify** this **tuple directly**, which is **not allowed because tuples do not support** in-place modification.


<br>

### Direct Assignment Issue:

**Pygame's Rect** `object` **does not allow direct assignment** or modification of its attributes through mathematical operations on their values.

#### 🔴 You need to use explicit assignments to update the position.


<br>
<br>

## 🌈 Solutions

### 1. ✅ chatgpt approach:

- -  Instead of trying to add to `player_rect.center` directly, `you should calculate the new center position` and `then assign it back to the center` attribute.

  Here’s how you can do it:

```python
# Moves the rectangle to the right by 20 pixels
# Increases the x-coordinate, moving the rectangle to the right.

# Calculate the new center position
new_center_x = player_rect.centerx + 20

new_center_y = player_rect.centery - 10
# Moves the rectangle down by 10 pixels
# Increases the y-coordinate, moving the rectangle down.

# Update the center attribute with the new position
player_rect.center = (new_center_x, new_center_y)

```

<br>

### 2. 🟣 tutorial approach: VECTORS

- -  ✋ Using a vector can be a good solution to handle position updates more flexibly and avoid the issues you encountered with directly modifying **the** `center` attribute of a `Rect` **object**.



<br>
<br>

### 🟧 Using a Vector for Position Updates

 Here’s a detailed explanation of how and why using a vector helps:

 <br>

## 🟢 Why Use a Vector?


### 🔴 Mutable and Flexible:



- - #### Read More here: [z_VECTOR2_in_pygame](../z_VECTOR2_in_pygame.md)


<br>
