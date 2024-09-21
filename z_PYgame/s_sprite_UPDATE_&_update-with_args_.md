## 🟡 Update and Update with arguments


 <br>
 <br>
 <br>


### 1. 👾 🟠 Now that we’ve created the Player class and added the group argument to its constructor, like this:

```python
class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        try:
            # self.image = pygame.image.load(image_paths['player']).convert_alpha()
            self.image = images['player']
        except KeyError:
```
<br>

### 2. 🌴 🟧 We can move on to incorporating the `update()` method for the sprite group within the main game loop.

#### Adding `update()` to the `While` Loop

- - **Next, we need to add `all_sprites.update()` to our while loop** to ensure that all sprites in the group are updated each frame.

#### Example Loop Integration:

```python
while True:
    all_sprites.update()
    # Update all sprites in the group

    display_surface.fill("lavenderblush2")
    # Clear the screen with a color

    all_sprites.draw(display_surface)
    # Draw all sprites on the display surface

    pygame.display.update()
    # Refresh the screen

```

<br>
<br>

## 🫐 🟡 In-Depth:

### 🧶 Understanding update()



> #### This line below, calls the `update()` method `on every sprite`  <u>in the all_sprites group.</u>

#### `all_sprites.update():`



**Purpose:** Typically used to handle game logic like movement, animations, or state changes for each sprite.

  > #### Each sprite’s update() method is responsible for updating its own state.

<br>

```python
    # 🟨 UPDATE sprite group
    all_sprites.update()


    display_surface.fill("lavenderblush2")

    for pos in star_positions:
        display_surface.blit(star_surf, pos)
```

<br>

## 🟠 Options for update() in Sprite Groups



### 🟦 Basic Update Without Arguments:

```python
group.update()  # Calls update() on every sprite in the group
```

- - **This will call the `update()` method on each** sprite in the group without passing any additional arguments.

- - **Each sprite’s `update()` method should be defined** to handle whatever updates are needed (e.g., movement, animation).

<br>

### 🟦  Update with Arguments:


 **`group.update(arg1, arg2)`:**

- - -  #### Calls update() on every sprite with additional arguments

```python
group.update(arg1, arg2)
# Calls update() on every sprite with additional arguments
```

> #### ✋ You can pass arguments to the update() method of the group. These arguments are then passed to each sprite’s update() method.


<br>
<br>

### The updated() code

```bash

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