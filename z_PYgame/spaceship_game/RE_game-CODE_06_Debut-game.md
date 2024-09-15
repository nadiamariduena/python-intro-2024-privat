
# 🟡 SPRITES

<br>





-  - **for loops can be less efficient** for certain situations [Go to section](#for_loop_for_some_situations_)



<br>
<br>
<br>

[1:54:37](https://youtu.be/8OMghdHP-zs?si=_tFF1DTbYRBdkw9e&t=6877)

## 🫐 🟡 What is a SPRITE?


#### 🟦 In gaming, a "sprite" refers to a two-dimensional image or animation that is integrated into a larger scene, typically representing objects or characters.

>  -  ✋ The term originated from early computer graphics where sprites were small, movable graphics elements, like a character or an item, which could be manipulated independently of the background.


<br>

- - Sprites are usually used in 2D games, where they are drawn over a static or dynamically changing background.

<br>

> - - #### In more modern contexts, the term can also apply to certain 3D games where elements are rendered in a 2D manner, such as icons, HUD elements, or particle effects.


<br>
<br>

## 🟦 Key features of sprites include:


<br>

**Layering:**

 #### Sprites can be layered over or under other sprites and backgrounds to create complex scenes.


- - - **Sprites are a fundamental concept in game development**, especially for classic and indie games, due to their simplicity and versatility.

<br>

**Transparency:**

- - Sprites often have transparent backgrounds so they can blend seamlessly with the game environment.




**Animation:**

- -  Sprites can be animated by displaying a sequence of images (frames) in rapid succession to create the illusion of movement.


<br>
<br>
<br>

---



## 🟡 Moving Forward: Building Your Space Shooter with Classes and Sprites


Now we're ready to move into the exciting phase of building our game.

<br>

<br>

## 🟢🫐  What We’ll Be Doing

###  💥 Creating Game Classes:

We’ll define classes for different elements of our game.

> #### For example:

- -  a Player class for the player character, an Enemy class for enemies, and so on. Each class will manage its own behavior and properties.




### 🧸 Using Sprites:

We’ll use `pygame.sprite.Sprite` to create these classes.

> #### This class helps us by automatically providing the Surface and Rect attributes and making it easier to manage updates and interactions.

<br>

### 🍯 Building the Game Loop:

> #### 🐝 We’ll integrate our sprite classes into the main game loop, updating and drawing each sprite, handling collisions, and managing game states.



<br>
<br>


<br>
<br>

------



### 0) Before any modification to the code, this is what we have:

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

# 1. -----  move right to left loop  ---

#
##20 X, - 10Y axis
#🤚 VECTOR
player_direction = pygame.math.Vector2(0) # This vector represents the direction and speed at which the player is moving:
# player speed
#🟡 actual movement
player_speed = 300
# -----  move right to left loop  ---

while running:
    #🤚 DELTA time
    # frame rate / division
    dt = clock.tick() / 1000
    # print(dt)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
        #     print(1)


    # print(pygame.mouse.get_pos())
   # ---------KEY  ---------
    keys = pygame.key.get_pressed()

    player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    # `int()` is the function doing the conversion. int converts this boolean value into an integer. In Python, True is equivalent to 1 and False is equivalent to 0. Therefore, int(keys[pygame.K_RIGHT]) gives 1 if the key is pressed and 0 if it is not
    player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

    # to normalize the vector, after the issue when pressing top and left at the same time
    player_direction = player_direction.normalize() if player_direction else player_direction


    player_rect.center += player_direction * player_speed * dt

    #MAGNITUDE
    print((player_direction * player_speed).magnitude())
    # -----------------
    # -----------------
    display_surface.fill("lavenderblush2")

    for pos in star_positions:
        display_surface.blit(star_surf, pos)

    display_surface.blit(player_surf, player_rect)
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)

    pygame.display.update()



pygame.quit()
```


<br>
<br>
<br>
<br>

---

## 🟡 Why Use Classes:

### 🟤 Organization:

 As our game grows, our code can become messy.

- - - #### Classes help keep things tidy by grouping related data and functions together.

> #### This makes it easier to manage and understand.

<br>

### 🟤 Structure:

We’ll create specific classes for different game elements like the player, enemies, and other objects.

- - #### 🟦 Each class will handle its own behavior and properties, making the code modular and easier to maintain.

<br>
<br>


<br>

### 🟢 Why Use the `pygame.sprite.Sprite` Class:

<br>

### 🟠 Built-In Features:



The `pygame.sprite.Sprite` class provides **built-in methods and properties** that simplify working with game objects.

> #### Each sprite has a Surface (the image) and a Rect (the rectangle defining its position and size).

<br>

#### 🟠 Ease of Use:

By inheriting from `pygame.sprite.Sprite`, our game objects automatically gain these features.

- - This makes it easier to handle drawing, updating, and collision detection.

<br>
<br>
<br>
<br>

---




## 1) 🟡 create the first class

```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

```

  <br>

 🟤 **Purpose:** This line `class Player(pygame.sprite.Sprite)` defines a new class called **Player**.

 <br>


- - 💥 It inherits from `pygame.sprite.Sprite`, which is a built-in Pygame class designed to make working with game objects easier.

<br>

