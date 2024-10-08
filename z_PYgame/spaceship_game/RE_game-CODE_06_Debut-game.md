
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



## 🟧 Different Structure

> ####  If you're using a code structure <u>where all images are managed via a dictionary</u>  `image_paths['player']` (as in My code), follow the approach below:

```python
class Player(pygame.sprite.Sprite):


    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(image_paths['player']).convert_alpha()
        self.rect
```


### 🟠 But if you are following the  [tutorial | 1:57:26](https://youtu.be/8OMghdHP-zs?si=PmVQXMiJDKqBUPIE&t=7046) structure, then use the below

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
<br>
<br>

---



<a name="for_loop_for_some_situations_"></a>

 ## 🟠 For vs map

 ###  Performance issues

> #### 🟣 Question: I've read that <u>using for loops can be less efficient for certain situations and that map might be a better alternative</u> . Does this apply to `Pygame` as well?

> #### ✅ chatgpt: You’ve heard correctly in many modern  React and JavaScript contexts.

<br>

 **React and JavaScript**

  **Using `map` over `for` loops for rendering lists of components in React is generally recommended for several reasons**:

- - -  **Immutability:** map does not mutate the original array but returns a new array, aligning with functional programming principles and making your code easier to reason about.

- - - **Inline Rendering:** With map, you can directly embed the logic for rendering lists of components within the JSX, which keeps your component logic more compact and expressive.

- - - **Avoid Side Effects:** map avoids the potential for side effects that could arise from modifying external variables or arrays, which is something to be cautious about when using for loops.


<br>



#### 1.  QUESTION: `for` loop also cause issues with certain animations in threejs, is that right?

#### 2.  QUESTION: "I’m not entirely sure, ✋ but I seem to recall that using map in this code might lead to animation issues. Could you explain why using map instead of a for loop could have potential consequences?

#### 🟫 Read More: [a_FOR_vs_MAP__loop](../a_FOR_vs_MAP__loop.md)


<br>
<br>



🟠 **PYTHON: pygame**

 **In Pygame**, using `for` **loops** is generally **acceptable and often necessary** for tasks like iterating over game objects or handling events.

 <br>

 - - - 🔴 **While map can be useful for applying functions to sequences, it doesn't always fit** well with Pygame's need for explicit iteration and real-time processing.



 <br>

> #### 🍦 Performance differences are usually minimal for small to medium-scale tasks.

For complex operations, optimizing code through profiling and targeted improvements is more effective than relying solely on map or for loops.

---

<br>
<br>
<br>
<br>
<br>

## 🟦 Moving Forward:



<a name="dictionary_to_manage_img_imports_"></a>

## <u>Dictionary</u>

### 🟧 In my project, my code differs from the tutorial due to my use of a dictionary to manage image imports.

- - Although **the tutorial does not cover this approach**, my experience with **Three.js** ✋ taught me that organizing assets in this way can be beneficial.

 #### Why?

> - - By grouping image assets in a dictionary (arrays in Javascript), I can efficiently handle multiple model parts and animations, or any other use cases.

<br>

### 🟠 If you plan to use the dictionary as I do, be aware of the following:

###  Potential Issues:

- - - Consider adding **error handling** around image loading to catch issues like missing files.

### 🟠 Why Managing Images in a Dictionary is Beneficial in Game Development

- - - ####   Read More: [RE_game_import_imgs_in_dictionary](../RE_game_import_imgs_in_dictionary.md)


<br>
<br>
<br>
<br>

<a name="LOOP_ALPHA_"></a>

##  🟠 <u>LOOP  alpha </u>


 ###  Instead of calling `convert_alpha()` multiple times for each image, `we handle it in a single loop` when loading the images.

```python
for key, path_imgs in image_paths.items():
    try:
        #LOAD and CONVERT the image in one step
        images[key] = pygame.image.load(path_imgs).convert_alpha()

    except pygame.error as img_item:

        print(f"Failed to load image '{path_imgs}': {img_item}")
        # Fall img IF LOAD fails
        images[key] = pygame.Surface((50,50)) # square
        images[key].fill((249, 255, 51 )) # yellow acid
```


<br>
<br>
<br>
<br>
<br>

---




## 🟦 Moving Forward:

## 🟧 In this section, we will focus on the following tasks:

**Add the Image to the Surface:** We will integrate an image into the Player class by assigning it to the sprite’s surface, enabling visual representation in the game.

**Comment and Reorganize the Code:** We will review and update the code, adding comments for clarity and reorganizing it to improve structure and readability.

<br>

## 🟠 Adding the Image to the Surface

### Image Assignment in the Code
In this part, we'll assign an image to the Player class using the **self.image attribute**.

```python
 self.image = images['player']
```




##  Why?

- - **To ensure the sprite is correctly positioned on the screen**, `self.rect` defines the sprite's rectangular area.


<br>

### 🟤 Assigning the `ìmage`

```python
  self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)) , explain it in 5 lines
```
#### This step is crucial because it aligns the image on the surface, allowing accurate positioning and rendering of the sprite in the game.

<br>

### 🟤 Centering

- -  #### 🟤 By using `self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))`, we create a rectangle that centers the sprite in the window.


<br>

```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        try:
            # self.image = pygame.image.load(image_paths['player']).convert_alpha()
            self.image = images['player']
        except KeyError:
            print("Player image not found in images dictionary.")
            # Handle the failure (e.g., set a default image or exit)
            #  ----  create a red square as a fallback/ shape red in case the img doesnt load --
            self.image = pygame.Surface((50, 50))  # Example fallback surface
            self.image.fill((0, 56, 175 ))  # BLUE Klein


        # 🔴
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
```



<br>
<br>


## 🟠  Integrating the Player Class into Your Game


###  Adding the Player to the Display Surface

```python
# PLAYER class instance
# with this you can go to the while loop and DRAW the player
# remember: this player is carrying the img etc
player = Player()
```

<br>

### 🟤 Within the game loop:

- - Within the game loop, add the following code to draw the player sprite on the screen:


```python
display_surface.blit(player.image, player.rect)
```
<br>

## BLIT

> #### This line uses `blit` to draw the player's image at the location specified by player.rect, ensuring the player appears in the correct spot on the screen.

<br>

[1:58:53](https://youtu.be/8OMghdHP-zs?si=mQbabPYogwnMD3q9&t=7133):


<br>

### 🟤 Example in Context::

```bash
   display_surface.blit(player.image, player.rect)
    pygame.display.update()
pygame.quit()
```
<br>


<br>
<br>



<a name="DirectlyBlittingSprites_"></a>



## 🟠  Why This Direct Approach Isn't Ideal for Sprites

####  <u>Directly blitting</u>  the sprite’s image and rectangle to the surface is functional, but it's not the recommended approach when working with sprites.

<br>

```python
display_surface.blit(player.image, player.rect)
```
> #### 🟤 🔺 This method does not take advantage of Pygame's built-in sprite management and can make your code harder to maintain and extend.




<br>
<br>

## 🟠 To Display the Sprite, you could use:

```python
surface.blit(sprite.image, sprite.rect)
```

## 👎 Alternative, But Still Not Ideal:

While this alternative is similar, **it also bypasses Pygame's sprite groups and other features designed to manage multiple sprites efficiently**.

- 🟥 **A Better Approach:** Using Pygame Sprite Groups




<a name="BenefitsofUsingSpriteGroups_"></a>

##  <u>Benefits of Using Sprite Groups</u>

- - **Using sprite groups allows for more** advanced features like batch drawing and collision detection, making your game code cleaner and more scalable.

<br>
<br>
<br>


## 🟠 Why Use Sprite Groups?

<br>

🟤 **Efficiency:**  Games often have many sprites.

> #### Pygame sprite groups are designed to handle large numbers of sprites efficiently.

<br>

🟤 **Organization:** Sprite groups help **organize and manage multiple sprites**, making your code cleaner and more manageable.

 <br>
 <br>

### 🟧 Key Benefits of Sprite Groups:

🟫 **Drawing:**  You can draw all sprites in a group onto a surface with a single command.

```python
group.draw(surface)  # Draws all sprites in the group on the specified surface

```


🟫 **Updating:** You can update all sprites in a group at once.

```python
group.update(args)  # Calls the update method on every sprite in the group with the given arguments

```



🟫 **Flexibility:**  You can loop over sprites and use them in other methods, which makes it easy to sort and manage them logically.


<br>
<br>
<br>


## 🟦 Moving Forward:

<a name="GettingStartedwithSpriteGroups_"></a>

### 🟠 Sprite Group

- Getting Started with SpriteGroups

<br>
<br>

###  Setting Up a `Sprite Group`

### 🟤 1. Create the Sprite Group

This line initializes a new sprite group called all_sprites.

```python
all_sprites = pygame.sprite.Group()
```
### 🟤 2. Add Sprites to the Group

- -  In your game loop (WHILE), you'll use the group’s **draw** and **update** `methods`:

```python
all_sprites.draw(display_surface) # Renders all sprites, which is your game window.
all_sprites.update() # Refreshes the display to show the updated frame

```

> ####  This draws and updates all sprites in the all_sprites group on the display_surface.

<br>
<br>

### 3. 🟤 Draw sprites on the display surface

**`all_sprites.draw(display_surface)`:**

- -  Renders all sprites onto the `display_surface`, which is your game window.

- - ###  In your main loop, add the following lines to draw your sprites:



```python
    # all_sprites.update() # OPTION
   all_sprites.draw(display_surface)
   # Draw sprites on the display surface

    pygame.display.update()
pygame.quit()
```


<br>

### 🟤 4. Test

 **If you test it now, you won’t see anything** 👎

- -  Because the **sprites are not being added to the `all_sprites` group**.

- Make sure to attach sprites to the group in their class initialization to ensure they are managed and drawn correctly.

<br>
<br>


## 🟦 Moving Forward:


<a name="AddingSpritestotheGroup_"></a>

## 🟡 Adding Sprites to the Group


- -  To ensure that sprites appear on the screen when using `all_sprites.draw(display_surface)`, **you need to add each sprite to the `all_sprites` group** during the sprite's initialization.

- - - #####  ⬛ Forgot about: Constructor? `__init__` [a_CONSTRUCTOR](../../b_CONSTRUCTOR.md)

- - - This is done by passing all_sprites to `super().__init__(all_sprites)` in the sprite class constructor.



<br>

>#### "If you create a `player` sprite and want it to be part of the `all_sprites` group, you need to add it to the group"

<br>

## 🟫 Option 1:

###  Adding After Creation

- After creating the `player` **instance**:

```python
player = Player()

# adding the CLASS to the all_sprites
all_sprites.add(player)
```
>  Here, we add the player to the `all_sprites` group manually.


## 🟫 Option 2:

teachers choice

###  Adding During Sprite Initialization

- - #### A more common practice is to add sprites to groups directly when initializing them:

```python
class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

```



<br>

## 🟧 Explanation:

### 🧸   When creating a sprite in Pygame, you need to specify <u>which groups the sprite should belong to</u> .

<br>

- - 🔴 This is done by **passing these groups as an argument to the `__init__` constructor method** of your sprite class.

> - -  #### 🦄 Then, you can forward these groups to the parent class using `super()`.



- - #### 🟤 By modifying the `__init__` method to accept and pass groups to the parent class via `super()`, you ensure that your sprite is properly added to those groups upon creation.


<br>

### 🟧  Here's how you can do it:

###  Before

- In the below version, the sprite isn’t assigned to any groups because the __init__ method doesn’t take any arguments for groups.

```python

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

```
###  After:

```python
class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(*groups)
        # 🔴 NOTICE the asterisk
        # we will talk about it after this
```

<br>

---


### 🌈  In this updated version, you pass the groups argument to the `__init__` method of your sprite.

<br>

- - 👾 **The `super().__init__(*groups)` call forwards these groups to the** `pygame.sprite.Sprite` **initializer**, ensuring that your sprite is added to the specified groups right from the start.

<br>

> #### By making this change, you can easily manage which groups your sprite is part of when creating it, improving the organization of your game objects.

<br>
<br>
<br>

---



<a name="ASTERISK_"></a>


## 🟠 asterisk (*)

- Chatgpt added the arterisk to the group but the teacher hasn done it yet

```python
super().__init__(*groups)
# the asterisk (*) means "unpack the elements" and is essential for properly passing the groups to the parent class's __init__ method.
```


### 🟧 The asterisk (`*`) in this context is not symbolic; it has a specific meaning.

- - #### It is used to unpack arguments in Python.

-  - When you use `*groups` in the `super().__init__(*groups)` call, it unpacks the list or tuple of groups so that each element is passed as a separate argument.

> - - - #### 🔴 This is necessary because the `pygame.sprite.Sprite` initializer <u>expects multiple arguments, each representing a different group</u> .

### Here's a breakdown of how it works:

<br>

**Without `*`:**

- - 👎 If you just passed groups like this: `super().__init__(groups)`, it would pass the entire list or tuple as a single argument. This is not what the pygame.sprite.Sprite constructor expects.

<br>

 👍  **With `*`:**

 - - When you use *groups, it unpacks the list or tuple so that each element is passed individually. For example, if groups is ['group1', 'group2'], *groups effectively passes group1 and group2 as separate arguments to the super().__init__ method.

<br>

### 🌈 So, the asterisk (*) means "unpack the elements" and is essential for properly passing the groups to the parent class's __init__ method.

<br>

### In summary:

#### Use `super().__init__(groups)` if groups is a single argument or if you're testing with just one group.

#### Use `super().__init__(*groups)` if groups is a list or tuple of multiple groups and you want each group to be passed as a separate argument to the parent class constructor.

 <br>

### 🟤 If you’re just testing

> #### If you’re just testing with a single group, you might get away with super().__init__(groups) if groups is already a single object or just a single group.

### 🔴However, for handling multiple groups, the asterisk is essential.


---

<br>
<br>
<br>
<br>

## 🟦 Moving Forward:


### 🟠 Now that <u>we’ve updated the code by adding the group to the Player class and passing it to</u> `super()`, 🔺 the sprite is properly attached to the group and can be managed as an instance, as shown below:

```python
class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        try:
```



### 🟠 We can proceed to modify the code as follows:

<br>

#### 🟠 Remove the line:  `all_sprites.add(player)`

<br>


```python
all_sprites = pygame.sprite.Group()
# Create PLAYER class instance
player = Player()
all_sprites.add(player)

```
### 🟠 Replace it with:

```python
all_sprites = pygame.sprite.Group()
player = Player(all_sprites)
```

<br>

## Why?



###  🟧 Removing all_sprites.add(player):

- -  In the original code, after creating a Player instance, you explicitly add it to the `all_sprites` **group** using `all_sprites.add(player)`.

> - -  ####  🔴 This approach requires separate management of adding sprites to the group, which can be less organized.

```python
# before
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
# --------
# after
all_sprites = pygame.sprite.Group()
player = Player(all_sprites)
```

---


<br>
<br>
<br>
<br>

## 🟦 Moving Forward:


## 🟠 Update()

> ####  You can pass arguments to the update() method of the group.

- - These arguments are then **passed to each sprite’s `update()` method**.

<br>

###  Options for update() in Sprite Groups


- -  🟤 Basic Update Without Arguments **&** 🟦  Update with Arguments.

<br>

### 🟥  Read More: [s_sprite UPDATE & update with args](..//s_sprite_UPDATE_&_update-with_args_.md)



---


<br>
<br>
<br>
<br>



## 🟦 Moving Forward:

### 🟠 After the teacher added the `update()` call within the while loop (as discussed above), 🔴 `you will need to create the update method in the Player class that is linked to that call`.

<br>

```python
    def update(self):
        print("shipt is being updated")
```

### Like so:

```python
class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        try:

            self.image = images['player']
        except KeyError:
            print("Player image not found in images dictionary.")

            self.image = pygame.Surface((50, 50))  # Example fallback surface
            self.image.fill((0, 56, 175 ))  # BLUE Klein

        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

    # ---- 🟡 UPDATE METHOD
    def update(self):
        print("shipt is being updated")
```

<br>

 ### 🌈 The update in the while loop isn’t a method by itself;

 > - - #### 💥 it's actually calling the update method I created in the Player class.


 > - - #### That method gets executed for each `sprite` in the `all_sprites` group during each frame of the game.

 #### So, every time the game updates, it’s using the update function from the player class!

<br>
<br>


<br>



## Key points:

## 1. `all_sprites.update()`:

```javascript
    // ✋
    all_sprites.draw(display_surface)


    pygame.display.update()
pygame.quit()
```

<br>

## 2. `Player.update(self)`:

```python

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        try:

            self.image = images['player']
        except KeyError:
            print("Player image not found in images dictionary.")

            self.image = pygame.Surface((50, 50))
            self.image.fill((0, 56, 175 ))

        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

    # ✋
    def update(self):
        print("shipt is being updated")



all_sprites = pygame.sprite.Group()
# Create PLAYER class instance
player = Player(all_sprites)
# all_sprites.add(player)
```


<br>
<br>
<br>

---


## 🟠 Current Code:

### 🌈 Before we proceed, let’s take a look at the current state of the code.  This will help us understand where we are and what changes we need to make as we recreate the player movements.

#### Here’s the latest version of the code:


```python

import pygame
import os
from random import randint

#------------- INIT
pygame.init()
# -------------


# SCREEN
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# TEXT screen
pygame.display.set_caption("Space shooter")




#🟨 imgs -----
script_dir = os.path.dirname(__file__)
# img's path
image_paths = {
    'player': os.path.join(script_dir, '..', 'images', 'player.png'),
    'star': os.path.join(script_dir, '..', 'images', 'star.png'),
    'meteor': os.path.join(script_dir, '..', 'images', 'meteor.png'),
    'laser': os.path.join(script_dir, '..', 'images', 'laser.png')

}

# INIT the images dictionary
images = {}

#Load images and handle errors
# Notice how we grab the dictionary "image_paths"
for key, path_imgs in image_paths.items():
    try:
        #LOAD and CONVERT the image in one step
        images[key] = pygame.image.load(path_imgs).convert_alpha()

    except pygame.error as img_item:

        print(f"Failed to load image '{path_imgs}': {img_item}")
        # Fall img IF LOAD fails
        images[key] = pygame.Surface((50,50)) # square
        images[key].fill((249, 255, 51 )) # yellow acid



class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        try:
            # self.image = pygame.image.load(image_paths['player']).convert_alpha()
            self.image = images['player']
        except KeyError:
            print("Player image not found in images dictionary.")
            # Handle the failure (e.g., set a default image or exit)
            #  ---- 🔴 create a red square as a fallback/ shape red in case the img doesnt load --
            self.image = pygame.Surface((50, 50))  # Example fallback surface
            self.image.fill((0, 56, 175 ))  # BLUE Klein

        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

    def update(self):
        print("shipt is being updated")


all_sprites = pygame.sprite.Group()
# Create PLAYER class instance
player = Player(all_sprites)
# all_sprites.add(player)




# IMAGES out of the class

# meteor_surf = pygame.image.load(image_paths['meteor']).convert_alpha()
# laser_surf = pygame.image.load(image_paths['laser']).convert_alpha()

# Define other surfaces
meteor_surf = images['meteor']
laser_surf = images['laser']
star_surf = images['star']



# (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
# Will pos the plane at the center of the screen/window
# player_rect = player_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 10))

# start
# star_surf = pygame.image.load(image_paths['star']).convert_alpha()
# star pos
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

# 1. -----  move right to left loop  ---

#
##20 X, - 10Y axis
#🤚 VECTOR
# player_direction = pygame.math.Vector2() # This vector represents the direction and speed at which the player is moving:
# player speed
#🟡 actual movement
# player_speed = 300
# -----  move right to left loop  ---




#✋ CLOCK:  FPS (frame per second)
clock = pygame.time.Clock()

#while loop related
running = True


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
    # keys = pygame.key.get_pressed()

    # player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    # # `int()` is the function doing the conversion. int converts this boolean value into an integer. In Python, True is equivalent to 1 and False is equivalent to 0. Therefore, int(keys[pygame.K_RIGHT]) gives 1 if the key is pressed and 0 if it is not
    # player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

    # # to normalize the vector, after the issue when pressing top and left at the same time
    # player_direction = player_direction.normalize() if player_direction else player_direction


    # player_rect.center += player_direction * player_speed * dt

    # #MAGNITUDE
    # print((player_direction * player_speed).magnitude())
    # -----------------
    # -----------------

    # 🟨 UPDATE sprite group
    all_sprites.update()


    display_surface.fill("lavenderblush2")

    for pos in star_positions:
        display_surface.blit(star_surf, pos)

    # display_surface.blit(player_surf, player_rect)
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)

    # display_surface.blit(player.image, player.rect)
    # surface.blit(sprite.image, sprite.rect)
    # all_sprites.update()
    all_sprites.draw(display_surface)

    pygame.display.update()



pygame.quit()
```


<br>
<br>

---

## 🟦   Moving Forward:

### 🟤 Let’s Recreate Our Previous Movements!

🟥 In the upcoming steps, we will reintroduce the movement logic that allows the player to navigate smoothly.

<br>

<!-- ###  [ NEXT ➡️ ]() -->