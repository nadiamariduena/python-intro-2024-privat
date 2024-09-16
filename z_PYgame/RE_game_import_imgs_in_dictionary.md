
# 🟡 Loading images in a Dictionary


<br>
<br>



- Image import with dictionary [a_pygame_convert_&_convertalpha_](../a_pygame_convert_&_convertalpha_.md)

<br>
<br>
<br>



## 🟢 Why Managing Images in a Dictionary is Beneficial in Game Development

When creating games, managing images through a dictionary offers several advantages that streamline development and improve code maintainability:


#### 🟤 Organization:

 A dictionary provides a central place to manage all image paths or surfaces.

- - 🟨 This organization **simplifies the process of updating or replacing images**, as you **only need to modify the paths in one location**.

<br>

#### 🟤 Scalability:

**As your game grows and more assets are added**, a dictionary keeps things tidy and manageable.

- -  🟨 You avoid scattering image loading code across different parts of your program.


<br>
<br>
<br>

## 🔴 Import images

<br>

### 🫐🟡 Applying a Single ALPHA_CONVERT to All Images

- - 🟦 **First**, we'll look at how we're currently handling the alpha conversion for the images.

<br>

- - 🟢 **Then**, we'll explore a more efficient approach using a loop, allowing us to apply a single alpha conversion to all the images.

<br>

### 🟠 Before diving in, let me explain my current setup:

- In 🔴 Lesson 6, I’m using a different method for handling images compared to what’s shown in the video tutorial.

<br>

- - **Right now, I’m working with images individually and importing** them into a dictionary  named  **`image_paths = {}`** **like here below:**

<br>

```python
# img's path
image_paths = {
    'player': os.path.join(script_dir, '..', 'images', 'player.png'),
    'star': os.path.join(script_dir, '..', 'images', 'star.png'),
    'meteor': os.path.join(script_dir, '..', 'images', 'meteor.png'),
    'laser': os.path.join(script_dir, '..', 'images', 'laser.png')

}

```

##  🟦  convert_alpha

```python

player_surf = pygame.image.load(image_paths['player']).convert_alpha()
meteor_surf = pygame.image.load(image_paths['meteor']).convert_alpha()
laser_surf = pygame.image.load(image_paths['laser']).convert_alpha()
```





### 🟡 The code

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

# 🧶  Modifying the CODE



## 🟡 <u>LOOP alpha </u>/ But We can always make the code better 🌈

<br>

### ⚫ We can improve it by using a loop to handle the `convert_alpha()` operation.



### 🌞 WHY?

>  #### 🌈 Instead of calling `convert_alpha()` multiple times for each image, `we handle it in a single loop` when loading the images.

<br>

- - This **avoids repeating the conversion for each image** individually, which can be inefficient.





### 🟦 This approach not only `makes the code cleaner but also enhances performance` by minimizing redundant operations.

### 🟡 Explanation


#### 🟩 Single Conversion Step:

- - By using a loop to apply `convert_alpha()` to each image as it’s loaded, we ensure that the alpha conversion happens only once per image.

> #### This reduces the amount of redundant computation and improves efficiency.

<br>


#### 🟩 Improved Performance:

- - While `convert_alpha()` itself is not highly computationally expensive, handling it in a loop avoids unnecessary repeated calls and keeps the code streamlined.

> #### This becomes particularly beneficial as the number of images increases.

<br>
<br>
<br>
<br>

## 🟠 1. STEP: Images Dictionary:

<br>

- - 🌈  The images **dictionary is initialized as** `images = {}` **and is populated in a loop with images loaded from file paths.**

> - - #### This loop also applies the convert_alpha() method to each image to handle transparency.

<br>

```python

#🟨 1 imgs -----
script_dir = os.path.dirname(__file__)
#🟨 2 img's path
image_paths = {
    'player': os.path.join(script_dir, '..', 'images', 'player.png'),
    'star': os.path.join(script_dir, '..', 'images', 'star.png'),
    'meteor': os.path.join(script_dir, '..', 'images', 'meteor.png'),
    'laser': os.path.join(script_dir, '..', 'images', 'laser.png')

}

#🟨 3 INIT the images dictionary
images = {}


# ---------
#🟨 4 LOOP alpha convert
# Load images and handle errors
# 🟢 Notice how we grab the dictionary "image_paths"

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

>   #### 🟢 Notice how we grab the dictionary "image_paths" in step 4

<br>

### 🟩 💥 If you plan to use the dictionary, be aware of the following:


<br>

### 🔴 Potential Issues:


#### 💥 File Paths:

 🟤 **Ensure that** `script_dir` is correctly set to the directory where your script is located.

 <br>

- - -  🔺**Using** `os.path.abspath` [os.path.html](https://docs.python.org/3/library/os.path.html) or `os.path.dirname(__file__)` **helps to determine the script's directory**.


<br>

## 🟠 2. STEP: Next, we’ll integrate the loop information into the class

- - Focus on the `images` **variable**, which carries the alpha data from the loop described earlier.

> #### 🔴 Remember, `images` is declared as `images = {}` and is subsequently used in the for loop to handle the alpha conversion.

```python


#--------------- CLASS
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        try:
            self.image = images['player']
        except KeyError:
            print("Player image not found in images dictionary.")



            self.image = pygame.Surface((50, 50))
            self.image.fill((0, 56, 175 ))  # BLUE Klein

        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))



# Create PLAYER class instance
player = Player()
#--------------- CLASS
```



<br>
<br>

## 🟠 3. STEP: Adding Additional Images


### 🟤 In this final step, we'll load and prepare other game images using the same loop.

> #### Although these images are not directly used in the Player class, they are essential for other parts of the game.

```python
# Create PLAYER class instance
player = Player()
#--------------- CLASS

# Define other surfaces
meteor_surf = images['meteor']
laser_surf = images['laser']
star_surf = images['star']
```

<br>
<br>

# The code

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




# imgs -----
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


#--------------- CLASS
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        try:

            self.image = images['player']
        except KeyError:
            print("Player image not found in images dictionary.")


            # Handle the failure (e.g., set a default image or exit)
            #  ---- 🔴 create a red square as a fallback/ shape red in case the img doesnt load --
            self.image = pygame.Surface((50, 50))  # Example fallback surface
            self.image.fill((0, 56, 175 ))  # BLUE Klein

        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))



# Create PLAYER class instance
player = Player()
#--------------- CLASS

# Define other surfaces
meteor_surf = images['meteor']
laser_surf = images['laser']
star_surf = images['star']


#----
# (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
# Will pos the plane or whatever at the center of the screen/window
# -----

meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 10))


star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]





#CLOCK:  FPS (frame per second)
clock = pygame.time.Clock()

#while loop related
running = True


while running:
    # DELTA time
    # frame rate / division
    dt = clock.tick() / 1000
    # print(dt)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # -----------------
    # -----------------
    display_surface.fill("lavenderblush2")

    for pos in star_positions:
        display_surface.blit(star_surf, pos)

    # display_surface.blit(player_surf, player_rect)
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)

    pygame.display.update()



pygame.quit()

```