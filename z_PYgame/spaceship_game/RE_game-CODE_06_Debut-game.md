
### 🟠 Intro:

- - What We’ve **Accomplished**: [Go to section](#What_We_ve_Accomplished)

- - What **We’ll Be Doing** [Go to section](#What_We_will_Be_Doing_)



<br>
<br>

### 🟠 What is a SPRITE?

- - **What is a SPRITE?** [Go to section](#What_is_a_SPRITE?_)

- - **Classes and Sprites** [Go to section](#Classes_and_Sprites_)

- - - **Classes / Why Use Classes?** [Go to section](#Classes_)

- - - 🟫 **Class VS `pygame.sprite.Sprite` Class** [Go to section](#Classes_vs_pygameClasses_)

<br>

- -  `INIT`: Creating the Initial class [Go to section](#Creating_the_Initial_class)

- -  `Img & Rect`:  Adding Image and Rectangle to the Sprite [Go to section](#Img_and_Rect_)

<br>

- - Dictionary **to manage image imports**  [Go to section](#dictionary_to_manage_img_imports_)



  - - -   **LOOP  alpha** Instead of calling `convert_alpha()` multiple times for each image, `we handle it in a single loop` when loading the images. [Go to section](#LOOP_ALPHA_)




<br>
<br>



### ⚫ `For` Loops

-  - **for loops can be less efficient** for certain situations [Go to section](#for_loop_for_some_situations_)

<br>
<br>


<br>
<br>

### 🟠 Blitting Sprites

**Directly Blitting Sprites:** Why It’s Not Ideal  [Go to section](#DirectlyBlittingSprites_)

> - - -  Direct blitting requires manual management of each sprite's position and updates, which can become cumbersome and error-prone.

<br>

  **The Benefits of Using Sprite Groups**  [Go to section](#BenefitsofUsingSpriteGroups_)


> - - -  Sprite groups simplify sprite management by handling updates and drawing in bulk, improving code organization and performance.

<br>

  **Getting Started with Sprite Groups** [Go to section](#GettingStartedwithSpriteGroups_)

>- - -  Learn how to create and use sprite groups to streamline your game development and efficiently manage multiple sprites.

<br>
<br>

### 🟠 Adding Sprites to the Group

- -  [Go to section](#AddingSpritestotheGroup_)

- - - ### 🟤 Init: Asterisk `*`

- -  - - Adding **groups** when initializing the Class: `super().__init__(*groups)`: [ ⤵️ Go to section](#ASTERISK_)

> - - - - the asterisk (*) means "unpack the elements" and is essential for properly passing the groups to the parent class's __init__ method.






<br>
<br>
<br>
<br>
<br>
<br>

---

<br>


<a name="What_We_ve_Accomplished"></a>


# 🟡 Before Starting:


### 🟩  <u>What We’ve Accomplished: </u>



#### 🟠 Handling Inputs:

We’ve successfully set up code to manage **keyboard and mouse inputs**, allowing us to control the player and interact with the game world effectively.

#### 🟠 Player Movement:

We’ve **implemented smooth movement mechanics for the player**, ensuring consistent **speed and responsiveness**, even with **diagonal movements**.

<br>
<br>
<br>


<a name="What_We_will_Be_Doing_"></a>

## 🫐🟡 <u>What We’ll Be Doing </u>

####  💥 Creating Game Classes:

  We’ll define classes for different elements of our game.

> #### For example, a Player class for the player character, an Enemy class for enemies, and so on. Each class will manage its own behavior and properties.

####  💥 Using Sprites:

We’ll use `pygame.sprite.Sprite` to create these classes.

> #### This class helps us by automatically providing the Surface and Rect attributes and making it easier to manage updates and interactions.



####  💥 Building the Game Loop:

> ####  We’ll integrate our sprite classes into the main game loop, updating and drawing each sprite, handling collisions, and managing game states.



### 🟦 Here's the current state of the code before any modifications:

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
---

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>


<a name="What_is_a_SPRITE?_"></a>



#  🟠  <u>What is a SPRITE?</u>

[1:54:37](https://youtu.be/8OMghdHP-zs?si=_tFF1DTbYRBdkw9e&t=6877)

#### In gaming, a "sprite" refers to a two-dimensional image or animation that is integrated into a larger scene, typically representing objects or characters.




---




<br>
<br>
<br>
<br>
<br>




## 🟦 Moving Forward:


<a name="Classes_and_Sprites_"></a>


## 🫐 🟡 <u>Classes and Sprites</u>

<br>

#### 🟢 Building Your Space Shooter with `Classes and Sprites`



<br>

<a name="Classes_"></a>

## 💥  <u>Classes</u>

<br>

### 🟢  Why Use Classes:



#### 🟤 Organization:

 As our game grows, our code can become messy.

>  - #### Classes help keep things tidy by grouping related data and functions together.

> #### This makes it easier to manage and understand.


#### 🟤 Structure:

We’ll create specific classes for different game elements like the player, enemies, and other objects.

- - #### Each class will handle its own behavior and properties, making the code modular and easier to maintain.



<br>
<br>


## 🟦 Moving Forward:

<br>

<a name="Classes_vs_pygameClasses_"></a>

## 💥 <u>Class vs `pygame.sprite.Sprite` Class</u>

### The primary difference is that a general Class is a fundamental building block in Python, defining objects with attributes and methods.

> - - #### In contrast, `pygame.sprite.Sprite` is a specialized class from the Pygame library designed for managing and rendering game objects.

> - - #### 🟤  `pygame.sprite.Sprite` comes with **built-in functionality for** position, image handling, and collision detection, <u>whereas a generic Class requires custom implementation for these features. Essentially, pygame.sprite</u> .



> - - #### Sprite simplifies game development by providing predefined methods and attributes tailored for game development.



<br>

## 🟠  Built-In Features:

 ⚫ recap:

The `pygame.sprite.Sprite` **class provides built-in methods and properties** that simplify working with game objects.

> #### Each sprite has a Surface (the image) and a Rect (the rectangle defining its position and size).


###  Ease of Use:

By inheriting from `pygame.sprite.Sprite`, our game objects automatically gain these features.

> - - #### 🟤 This makes it easier to handle drawing, updating, and collision detection.



---

<br>
<br>
<br>



<br>
<br>
<br>

## 🟦 Moving Forward:

 <a name="Creating_the_Initial_class"></a>



## Init:

### 🟠 The teacher will start by creating the initial class and incorporating the `pygame.sprite.Sprite class.`



#### 🟤 1)  <u>Create the Initial Class</u>

```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

```


### Purpose:

> - - #### This line `class Player(pygame.sprite.Sprite)` defines a new class called **Player**.

> - - ####  It inherits from `pygame.sprite.Sprite`, which is a built-in Pygame class designed to make working with game objects easier.

<br>

## 🟧 Why `pygame.sprite.Sprite`:

**By inheriting from** `pygame.sprite.Sprite`, ✋ our **`Player` class automatically gets some useful features**, like handling its own image and position (using Surface and Rect).


<br>

## 🟧 Detailed Breakdown of Each Component:


> ### In this section, we will provide a comprehensive explanation of each part of the Player class.

<br>


- - This **includes** the **purpose and functionality of the** `__init__` **"constructor" method**, **as well as how it interacts** with the `pygame.sprite.Sprite` **class to initialize the Player** object.


<br>

### `def __init__(self)`:

 **Purpose:**

 - - This is the constructor method for the `Player` **class**.

- - It’s called when a new instance of Player is created.

#### 🟤 It initializes the object and sets up its attributes.

```python
    def __init__(self):
        super().__init__()

```


<br>

#### `super().__init__()`:

**Purpose:**

- - This line calls the `__init__` **method of the parent class** `(pygame.sprite.Sprite)`.


**Why:**

- - It ensures that the Player class inherits and sets up any initial functionality provided by pygame.sprite.Sprite.

<br>

---



> #### 🟣 Question: `Super()` is like mitosis (not technically)?

> #### ✅ chatgpt: Yes, that’s a good way to think about it in a broad sense! While `super()` and [mitosis](https://youtu.be/skPOXcVvS5c?si=69yX-O8AKtoqkPe-)  are not technically the same, the analogy of a "division of a parent" works for understanding the concept of inheritance and initialization in object-oriented programming.

---

<br>
<br>
<br>
<br>

<br>
<br>
<br>

## 🟦 Moving Forward:

<a name="Img_and_Rect_"></a>

### 🟠  <u>`Img & Rect`</u> :

### Adding Image and Rectangle to the Sprite

```python
        self.image
        self.rect
```


<br>

> ### 🟤 In this section, we will enhance the Player class by incorporating an image and a rectangle to define its visual appearance and boundary.

<br>

### This involves the following steps:

- - **Integrate the image into** the `Player` **class** to represent the sprite visually.

- - Define a rectangle around the sprite to manage its position and handle collisions.



<br>
<br>

### 🟧 Add the following to the `class`:

```python
        self.image
        self.rect
```

### Like so:

```python
class Player(pygame.sprite.Sprite):


    def __init__(self):
        super().__init__()
        self.image # (we will be adding the img here)
        self.rect
```
> if you are following the  [tutorial | 1:57:26](https://youtu.be/8OMghdHP-zs?si=PmVQXMiJDKqBUPIE&t=7046) structure, then use the above.



<br>

### 🟤 `self.image`

**Purpose:** This **attribute will hold the image (or surface)** that represents the player on the screen.

**Why:** We need this to visually display the player. It’s a placeholder here and will be assigned a value later.

### 🟤 `self.rect`

**Purpose:** This **attribute will be used to store the rectangle** (or bounding box) around the player’s image.

**Why:** `self.rect` helps with positioning the player on the screen and handling collisions. It’s also a placeholder here and will be set up later.
