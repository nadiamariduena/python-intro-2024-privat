
# 🟡 SPRITES 2.

<br>
<br>


### 🟠 Intro:



- - What **We’ll Be Doing** [Go to section](#What_We_will_Be_Doing_)



<br>
<br>

### 🧶 Global Accessibility of Delta Time (dt)

- -  Global Accessibility of Delta Time (dt):  [Go to section](#Global_Accessibility_of_DT)

- -  - **Global Scope** to access Delta Time:  ( 🔺 **not a good practice in some scenarios**) [Go to section](#Global_Accessibility_of_DT_not_good_inthis_situation)

- - - - - **`Global Scope` issue**  <u>check the solution here </u>  [Go to section](#Global_Accessibility_solution) )


<br>
<br>

<!-- ### 🟦 Final Touches Before Creating the `Star Class`

- - - The **Issue with `get_just_pressed()`** [Go to section](#get_just_pressed_)



> -  - - - 🔺  In the upcoming part of the lesson, the teacher will demonstrate the use of `get_just_pressed()`, but be aware that this might lead to an error: -->


<br>
<br>
<br>
<br>
<br>
<br>

---

<br>

<a name="What_We_will_Be_Doing_"></a>

## 🫐🟡 <u>What We’ll Be Doing </u>




 <br>



<!-- ## 🟦   Moving Forward: -->

### 🟠 Let’s Recreate Our Previous Movements!

### 🔸 Remember What We Had Before?

> #### In the upcoming steps, we will reintroduce the movement logic that allows the player to navigate smoothly.

<br>

- - **First**, we’ll copy the key direction input code into the update() method of the Player class.

- - - **Next**, we’ll ensure that we **`normalize`** the direction vector to maintain consistent speed.

- - - **We’ll also define the `speed` variable** to control how fast the player moves.

> - - #### Finally, we’ll incorporate delta time to ensure movement remains fluid across different frame rates.



<br>

### Here’s the movement logic we were using:

 ```python

#   print(pygame.mouse.get_pos())
   # ---------KEY  ---------
   keys = pygame.key.get_pressed()

    player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    # # `int()` is the function doing the conversion. int converts this boolean value into an integer. In Python, True is equivalent to 1 and False is equivalent to 0. Therefore, int(keys[pygame.K_RIGHT]) gives 1 if the key is pressed and 0 if it is not
     player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

    # # to normalize the vector, after the issue when pressing top and left at the same time
    player_direction = player_direction.normalize() if player_direction else player_direction


    # player_rect.center += player_direction * player_speed * dt

    # #MAGNITUDE
    # print((player_direction * player_speed).magnitude())
    # -----------------
    # -----------------
 ```
---

<br>
<br>
 <br>
 <br>

##  🟠 Transforming the Player Class for Smooth Movement!

<br>

### 🧶 Step 1:

### 💥 Move the Logic into the `Player` Class


- - -   **Instead of having movement** logic <u>in the main loop (WHILE loop)</u> , let’s **encapsulate it in the Player class!** This will make our code cleaner and more organized.

<br>

### 🧶 Step 2:

### 💥 `Update` the `Player` Class

> - - - ####   We’ll modify the Player class to include the movement logic directly in its `update()` method.

- - ####  This way, we can call it easily from our main game loop.

<br>
<br>
<br>
<br>

#### [2:04:10](https://youtu.be/8OMghdHP-zs?si=lDJzumH66g9rAMgc&t=7450)

## 🟠 Here’s How We’ll Do It:

### Add Movement Logic:

- - **Incorporate `key` presses to control the player’s** direction and **normalize** the **vector**.


### Update Position:

- - Adjust the player’s position based on the calculated direction and speed.

<br>
<br>

## 🟫 STEPS

<br>

## 🔶 1.  Move the Movement Logic

- - **Take the entire commented section** related to movement from the `WHILE` loop and paste it below the **`def update` method** in the `Player` class.

- like so:

```python
    def update(self):
        print("shipt is being updated")

      # ---------KEY  ---------
    # keys = pygame.key.get_pressed()

    # player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    # # `int()` is the function doing the conversion. int converts this boolean value into an integer. In Python, True is equivalent to 1 and False is equivalent to 0. Therefore, int(keys[pygame.K_RIGHT]) gives 1 if the key is pressed and 0 if it is not
    # player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

    # # to normalize the vector, after the issue when pressing top and left at the same time
    # player_direction = player_direction.normalize() if player_direction else player_direction


    # player_rect.center += player_direction * player_speed * dt
    # print(pygame.mouse.get_pos())

    # #MAGNITUDE
    # print((player_direction * player_speed).magnitude())


all_sprites = pygame.sprite.Group()
```

<br>
<br>


## 🔶 2. Insert the line `keys = pygame.key.get_pressed()` inside the `def update` method of the `Player` class.

>The **purpose of adding** `keys = pygame.key.get_pressed()` **inside** the **def update** method **is to continuously check the current state** of the **keyboard** during each frame.

```python
    def update(self):
        keys = pygame.key.get_pressed()
        # print("shipt is being updated")


```


> - - #### This allows the player to respond to key presses in real-time, enabling smooth movement. By placing it in the update method, we ensure that the player’s movement is updated every time the game loop runs.

<br>
<br>

## 🔶 3. Add the Direction Vector in the Player Class Initialization


- - **Before we do this**, remember that we previously grouped/**HIDE the direction vector with the speed** definition:


```python
##20 X, - 10Y axis
# VECTOR
# player_direction = pygame.math.Vector2() # This vector represents the direction and speed at which the player is moving:
# player speed
# actual movement
# player_speed = 300
# -----  move right to left loop  ---




#✋ CLOCK:  FPS (frame per second)
clock = pygame.time.Clock()
```
<br>
<br>

## 🟠 Now, Include the Direction Vector in the Player Class

- - In the `__init__` **method** of the `Player` **class**, add the following line: `self.direction = pygame.Vector2()`

<br>

```python
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        # ✋
        self.direction = pygame.Vector2()

    def update(self):
```
<br>

## 🟫 self.direction = pygame.Vector2()

**`self.direction = pygame.Vector2()` initializes a vector to manage the player's movement direction**.

> - - ####  This **allows for easy calculations of position based on user input, simplifying movement logic**.

> - - #### Using a vector enables smooth diagonal movement and ensures consistent speed.

```python
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        # ✋
        self.direction = pygame.Vector2()

    def update(self):
```
<br>

## 🟫 self.direction = pygame.Vector2()

**`self.direction = pygame.Vector2()` initializes a vector to manage the player's movement direction**.

> - - ####  This **allows for easy calculations of position based on user input, simplifying movement logic**.

> - - #### Using a vector enables smooth diagonal movement and ensures consistent speed.

> - - #### It also provides flexibility for future enhancements, like adding acceleration or new movement features.

- - Overall, it sets a solid foundation for effective movement handling in the game.


<br>
<br>

## 🔶 4. Update the Direction Lines (`x,y`) in the `update()` Method

- After completing the previous steps, **copy the x and y direction lines** and **paste** them **into the** `def update()` **method**:

<br>

```python
        player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
```
<br>
<br>

### Once you’ve pasted them, modify `player_direction` to `self.direction` for both lines:


```python
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
```

<br>

> #### 🟫 This ensures that the player’s movement direction is now stored in the self.direction vector, allowing for more organized and efficient handling of movement within the Player class.

<br>
<br>

## 🔶 5. Normalize the Direction Vector

### To ensure smooth movement, it’s important to normalize the direction vector:



```python
       player_direction = player_direction.normalize() if player_direction else player_direction
```

> 🔴 **Remember to add this line**; otherwise, we may encounter the same issue we faced earlier, where the values become erratic if both the up and left keys are pressed simultaneously.

 #### Normalizing the direction vector prevents faster diagonal movement by ensuring that the player’s speed remains consistent, regardless of the input direction. This helps maintain a smooth and predictable gameplay experience.


<br>

- Don't forget to replace the **player_direction** for **self**

```python
      self.direction = self.direction.normalize() if self.direction else self.direction
```

<br>

### 🔶 Make sure your update() method looks like this:

```python
    def update(self):
        keys = pygame.key.get_pressed()

        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])


        #NORMALIZE ✋
        self.direction = self.direction.normalize() if self.direction else self.direction
        #    print("shipt is being updated")
```

<br>
<br>

## 🔶 6. `DeltaTime:` Integrate Speed Calculations into Player Dynamics!

#### The line `player_rect.center += self.direction * player_speed * dt` dynamically updates the player’s position by combining the direction vector with the speed and the time elapsed since the last frame.

```python
# before
player_rect.center += player_direction * player_speed * dt
# after
self.rect.center += self.direction * self.speed * dt

```

> #### This ensures that movement is smooth and responsive, adapting to player input in real time.

> - - - #### 🔴 Without this calculation, your player would remain stationary, missing out on all the action happening around them. Curious about how this simple equation keeps the game alive? Let’s explore the magic of motion!

<br>
<br>
<br>

---


<a name="Global_Accessibility_of_DT"></a>

<br>

# 🟧  Global Accessibility of Delta Time (dt)

### 💥 DT  parameter

**To improve the way our player moves**, we’ll **incorporate the dt parameter**, which represents the time elapsed since the last frame.



> - - - #### The `delta time (dt)` variable is calculated in the main game loop, making it globally accessible throughout the entire program.

```python
while running:
    #🤚 DELTA time
    # frame rate / division
    dt = clock.tick() / 1000
```
<br>

> ### 🌐 This means you can use dt in any class, including the Player class, to ensure consistent movement speed.

<br>

- - By multiplying the player’s movement by dt, you account for variations in frame rates.

-  - This ensures that the player's speed remains the same, regardless of how fast or slow the game runs. Essentially, dt helps make your game smoother and more reliable across different hardware!

<br>
<br>
<br>
<br>
<br>
<br>

---

<a name="Global_Accessibility_of_DT_not_good_inthis_situation"></a>


# 🔴 1) Important: Delta Time Accessibility


<br>

### 🟫 <u>Another thing to keep in mind</u>  is that delta time (dt) is defined in the global scope, making it accessible within the Player class as well.

<br>

> ####  *Global Scope*  ( 🟥 accessible but its not a good practice,  <u>check the solution here </u>  [Go to section](#Global_Accessibility_solution) )

<br>

```python
    def update(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

        self.direction = self.direction.normalize() if self.direction else self.direction

        # SPEED ✋
        self.rect.center += self.direction * self.speed * dt

all_sprites = pygame.sprite.Group()
```


# 🔴 2) Important: The SPEED Variable Needs to Be Defined

- **Keep in mind that the speed variable doesn’t exist yet**, so we need to create it.

Recall that we previously had the speed defined, but we’ve moved away from that implementation:

```python
# We are no longer using the below, but it serves as a reminder of what we had before
# ----- move right to left loop ---

# VECTOR
# player_direction = pygame.math.Vector2()  # This vector represented the direction and speed of the player

# ✋ player speed
# player_speed = 300  # Speed of the player

```

<br>
<br>

<a name="Global_Accessibility_solution"></a>

# 🟡 Solution

### 🟫 Step 1: Pass the dt Parameter

- - **First, we will modify the while loop to include the `dt`** parameter when updating our sprite group.

> - - - By doing this, we ensure that each sprite has access to the time elapsed, which is crucial for calculating movement accurately. Here’s the updated line:

```python
# 🟨 UPDATE sprite group
all_sprites.update(dt)
```

<br>

### 🟫 Step 2: Capture dt in the Player Class

- - **Next**, we need to **capture the `dt parameter` in the `update()` method of the `Player class`**.

> - - - This is done by modifying the method signature to accept dt as an argument. Here’s how it changes:

```python
# Before
def update(self):
# After
def update(self, dt):

```

> #### 🟧 By doing this, we’re making the delta time accessible within the player’s update logic, which is essential for calculating movement speed effectively. This flexibility allows us to create a more responsive gaming experience.

<br>

### 🟫 Step 3: Utilize dt for Smooth Movement

- -  With `dt` now available in our `update()` **method**, we can use it to update the player’s position based on speed and direction.

> #### This line of code allows us to calculate how far the player should move in that frame:

```python
self.rect.center += self.direction * self.speed * dt
```

<br>

---

<br>
<br>
<br>
<br>
<br>

## 🟦 Moving Forward:

## 🔶 7. Define the Speed Variable:

- - To set the **speed**, add the following line in the `__init__` method of the `Player` class:



```python
self.speed = 300
```
<br>

### 🔴 Place it right after initializing the direction vector:


```python
        self.direction = pygame.Vector2()
        self.speed = 300

    def update(self):
```
> ### This ensures that your player has a defined speed for movement calculations!

<br>
<br>
<br>

# 🟠 Current Code

### Before we proceed, let’s take a look at the current state of the code.



> ### Here’s the latest version of the code:


<details>
<summary> <h4> 🟦 🟡Click to unfold the CODE with DT changes</h4> </summary>

<br>

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

        self.direction = pygame.Vector2()
        self.speed = 300

    def update(self, dt):
        keys = pygame.key.get_pressed()
        # INT:  `int()` is the function doing the conversion. int converts this boolean value into an integer. In Python, True is equivalent to 1 and False is equivalent to 0. Therefore, int(keys[pygame.K_RIGHT]) gives 1 if the key is pressed, and 0 if it is not
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])


        # to normalize the vector, after the issue when pressing top and left at the same time
        self.direction = self.direction.normalize() if self.direction else self.direction
        #    print("shipt is being updated")

        # Update the player position with speed and delta time
        self.rect.center += self.direction * self.speed * dt




        # print(pygame.mouse.get_pos())
        # #MAGNITUDE
        # print((player_direction * player_speed).magnitude())


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




    # -----------------
    # -----------------

    # 🟨 UPDATE sprite group
    all_sprites.update(dt)


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
</details>

<details>
<summary> <h4> 🟡 Click to unfold the CODE without DT changes</h4> </summary>



<br>



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

        self.direction = pygame.Vector2()
        self.speed = 300

    def update(self):
        keys = pygame.key.get_pressed()
        # INT:  `int()` is the function doing the conversion. int converts this boolean value into an integer. In Python, True is equivalent to 1 and False is equivalent to 0. Therefore, int(keys[pygame.K_RIGHT]) gives 1 if the key is pressed, and 0 if it is not
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])


        # to normalize the vector, after the issue when pressing top and left at the same time
        self.direction = self.direction.normalize() if self.direction else self.direction
        #    print("shipt is being updated")

        # Update the player position with speed and delta time
        self.rect.center += self.direction * self.speed * dt




        # print(pygame.mouse.get_pos())
        # #MAGNITUDE
        # print((player_direction * player_speed).magnitude())


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
</details>




<br>
<br>

<br>
<br>

## 🟦 Moving Forward:

## 🔶 Step 8: Final Touches Before Creating the `Star Class`

<br>

### 🔴  The Issue with `get_just_pressed()`

<a name="get_just_pressed_"></a>

- ####  In the upcoming part of the lesson, the teacher will demonstrate the use of `get_just_pressed()`, but be aware that this might lead to an error:

```python
      recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE]:
            print('fire laser')

```
>This function may not be supported in the latest versions of Pygame, so it's essential to understand why.

<br>

- 🟣 **QUESTION:**  Is `get_just_pressed()` from an Older Version?

- ✅ **chatgpt:** Yes, `pygame.key.get_just_pressed()` is a function that was part of older versions of Pygame, but it might not work as expected in more recent versions.

>Instead, the recommended approach is to use pygame.key.get_pressed() to check the current state of keys (whether they are pressed down) during the game loop.

<br>


<br>
<br>
<br>

## Clean the code


<details>
<summary> <h4> 🟦 🟡Click to unfold the CODE with DT changes</h4> </summary>

<br>

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

# Load images and handle errors
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

        self.direction = pygame.Vector2()
        self.speed = 300

    def update(self, dt):
        keys = pygame.key.get_pressed()
        # INT:  `int()` is the function doing the conversion. int converts this boolean value into an integer. In Python, True is equivalent to 1 and False is equivalent to 0. Therefore, int(keys[pygame.K_RIGHT]) gives 1 if the key is pressed, and 0 if it is not
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])


        # to normalize the vector, after the issue when pressing top and left at the same time
        self.direction = self.direction.normalize() if self.direction else self.direction
        #    print("shipt is being updated")

        # Update the player position with speed and delta time
        self.rect.center += self.direction * self.speed * dt

        recent_keys = pygame.key.get_pressed()
        if recent_keys[pygame.K_SPACE]:
            print('fire laser')


all_sprites = pygame.sprite.Group()
# Create PLAYER class instance
player = Player(all_sprites)
# all_sprites.add(player)


# IMAGES out of the class
# Define other surfaces
meteor_surf = images['meteor']
laser_surf = images['laser']
star_surf = images['star']




meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 10))
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]




# CLOCK:
#FPS (frame per second)
clock = pygame.time.Clock()


running = True
while running:
    # DELTA time
    # frame rate / division
    dt = clock.tick() / 1000
    # print(dt)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # ---- update ---------
    # check the update() function within the PLAYER Class
    # 🟨 UPDATE sprite group
    all_sprites.update(dt)


    display_surface.fill("lavenderblush2")

    for pos in star_positions:
        display_surface.blit(star_surf, pos)


    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)

    # ---- sprites ----
    all_sprites.draw(display_surface)



    pygame.display.update()

pygame.quit()
```
</details>

<br>
<br>
<br>

<!-- ### NEXT ➡️ [Debut-game_create_star_class](https://github.com/nadiamariduena/python-games-01/blob/master/0_SPACESHIP-game/RE_game-CODE_09_Debut-game_create_star_class.md) -->