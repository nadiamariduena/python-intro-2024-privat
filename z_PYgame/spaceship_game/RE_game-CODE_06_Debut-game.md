
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


#### 🟤 Why `pygame.sprite.Sprite`:

**By inheriting from** `pygame.sprite.Sprite`, ✋ our **Player class automatically gets some useful features**, like handling its own image and position (using Surface and Rect).

<br>
<br>


### 🍯 `def __init__(self)`:

🟤 **Purpose:** This is the constructor method for the `Player` **class**.

- - It’s called when a new instance of Player is created.

#### 🟤 It initializes the object and sets up its attributes.

<br>

```python
    def __init__(self):
        super().__init__()

```

### 🍯 `super().__init__()`:

**Purpose:** This line calls the `__init__` **method of the parent class** `(pygame.sprite.Sprite)`.

**Why:** It ensures that the Player class inherits and sets up any initial functionality provided by pygame.sprite.Sprite.



<br>

---

#### 🟣 Question: `Super()` is like mitosis (not technically)?

#### ✅ chatgpt: Yes, that’s a good way to think about it in a broad sense! While `super()` and [mitosis](https://youtu.be/skPOXcVvS5c?si=69yX-O8AKtoqkPe-) 🧸 are not technically the same, the analogy of a "division of a parent" works for understanding the concept of inheritance and initialization in object-oriented programming.

---


<br>
<br>

## 🟨 🫐 Img & Rect

- **Add** the following **to the `class`**

```python
        self.image
        self.rect
```

<br>

#### 🟤 `self.image`

**Purpose:** This **attribute will hold the image (or surface)** that represents the player on the screen.

**Why:** We need this to visually display the player.

>#### It’s a placeholder here and will be assigned a value later.

<br>

#### 🟤 `self.rect`


**Purpose:** This **attribute will be used to store the rectangle** (or bounding box) around the player’s image.

**Why:** `self.rect` helps with positioning the player on the screen and handling collisions. It’s also a placeholder here and will be set up later.


<br>
<br>


### 🟦 Before

```python
class Player(pygame.sprite.Sprite):


    def __init__(self):
        super().__init__()
        self.image # (we will be adding the img here)
        self.rect
```

<br>

## 🟦 After

#### 🔴 If you're using a code structure where all images are managed via a dictionary `image_paths['player']` (as in My code), follow the approach below:

```python
class Player(pygame.sprite.Sprite):


    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(image_paths['player']).convert_alpha()
        self.rect
```

<br>
<br>

### 🟡 But if you are following the  [tutorial | 1:57:26](https://youtu.be/8OMghdHP-zs?si=PmVQXMiJDKqBUPIE&t=7046) structure, then use the below

```python
class Player(pygame.sprite.Sprite):


    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(join('images', 'player.png',)).convert_alpha()
        self.rect
```

<br>
<br>
<br>

---


### 🌈 🧸 In my project, my code differs from the tutorial due to my use of a dictionary to manage image imports.

- - 🔴 Although **the tutorial does not cover this approach**, my experience with **Three.js** ✋ taught me that organizing assets in this way can be beneficial.

 ####  🟤(threejs)

> - - By grouping image assets in a dictionary (arrays in Javascript), I can efficiently handle multiple model parts and animations, or any other use cases.


<br>
<br>

---

 # 🟡 For vs map

 ### Performance issues

 <br>

<a name="for_loop_for_some_situations_"></a>

 ### 🟣 Question: I've read that <u>using for loops can be less efficient for certain situations and that map might be a better alternative</u> . Does this apply to `Pygame` as well?

 #### ✅ chatgpt:


You’ve heard correctly in many modern  React and JavaScript contexts.

🟫 **React and JavaScript**

  **Using `map` over `for` loops for rendering lists of components in React is generally recommended for several reasons**:

- - - 🟡 **Immutability:** map does not mutate the original array but returns a new array, aligning with functional programming principles and making your code easier to reason about.

- - - **Inline Rendering:** With map, you can directly embed the logic for rendering lists of components within the JSX, which keeps your component logic more compact and expressive.

- - - **Avoid Side Effects:** map avoids the potential for side effects that could arise from modifying external variables or arrays, which is something to be cautious about when using for loops.


<br>

---

#### 1. 🟣 QUESTION: `for` loop also cause issues with certain animations in threejs, is that right?

#### 2. 🟣 QUESTION: "I’m not entirely sure, ✋ but I seem to recall that using map in this code might lead to animation issues. Could you explain why using map instead of a for loop could have potential consequences?

#### 🌈 Read More here: [a_FOR_vs_MAP__loop](../a_FOR_vs_MAP__loop.md)