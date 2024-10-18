
# 🟡 SPRITES 7.

- TEXT






<br>


[2:53:16](https://youtu.be/8OMghdHP-zs?si=rHAejITFrnbrO3Rk&t=10396)



<br>

## 🟦 Let's Get Started:

## 🟡   1. Enhancing the Game with Additional Elements






### 🟫  Adding Text to Your Game

#### In this section, we’ll be learning how to add text to our game.

<br>

> #### Based on the tutorial, the first thing we need is a font and a font size.



To do this in `Pygame`, we use the `pygame.font.Font()` **function**, which allows us to create a font object that we can later use to render text on the screen.

> #### Here’s how you start by creating the font object:

```python
font = pygame.font.Font()
```
 <br>

### 🟤 1. Creating a Font Object

### You need a font object to define the font style and size.

> - #### This is done using pygame.font.Font().

- - You can either provide a specific font file (like a **TTF** file) or use the default font.

```python
font = pygame.font.Font(None, 20)  # 'None' means using the default system font, size 20

```

- **The first argument** (`None`) is where you can specify the path to a custom font file (like "path/to/font.ttf").

- **The second argument** is the font size (in this case, 20).

<br>
<br>

### 🟤 2. Rendering the Text

#### Once you have the font object, you can render the text.

- - This is done using the render() method, which takes three arguments:

```python
text_surface = font.render('Your Text Here', True, (255, 0, 0))  # Example with red text

```
<br>

### 🟢 Explanation:

### Arguments for render():

**Text:** The actual string you want to display (e.g., 'Hello World!').

<br>

**Anti-Aliasing** (Boolean): This smooths the edges of the text, making it look nicer.

> - - Usually, you'll want this to be True, except when using pixel art fonts, as anti-aliasing can make pixel fonts look blurry.

<br>

**Color:** The color of the text.

> - - This is typically given as an RGB tuple (e.g., (255, 0, 0) for red).


<br>

### 🟫 So, putting it all together:

```python
font = pygame.font.Font(None, 20)  # Create a font object
text_surface = font.render('Hello, Pygame!', True, (255, 0, 0))  # Render the text in red with anti-aliasing

```

<br>

### 🟤 3. Displaying the Text

Now that you have the text rendered as a surface `(text_surface)`, you can display it on the screen by **blitting** it to the main game surface.

#### Go tot the Game loop:

```python
display_surface.blit(text_surface, (x, y))  # Blit the text at position (x, y)
```



```python
    # TEXT 🟡
    display_surface.blit(text_surf, (0, 0))  # Blit the text at position (x, y)


    pygame.display.update()

pygame.quit()
```
<br>

 #### Code

```python

import pygame
import os
from random import randint, uniform


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
# ---------

# IMAGES out of the class
# Define other surfaces
meteor_surf = images['meteor']
laser_surf = images['laser']
star_surf = images['star']
# ----------
# ----------
# FONT
font = pygame.font.Font('../../FONT/NeutralFace-Bold.otf', 20)
text_surf = font.render('text', True, 'red')
# ----------
# positioning of the imgaes with surfaces, we will no longer need the below, because we are adding it directly within the laser for each one of them, like laser, meteor etc
# center of the screen for the 2 items below
# meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
# laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 10))
# -----------






#🤵 PLAYER ---------
class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        try:

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

        # 🥶 cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400 #  Players must wait 2 (2000) seconds between shots, promoting strategic timing and balanced gameplay by preventing rapid fire.


    def laser_timer(self):
        if not self.can_shoot:

            current_time = pygame.time.get_ticks()
            # print(current_time)
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True

    def update(self, dt):
        keys = pygame.key.get_pressed()
        # INT:  `int()` is the function doing the conversion. int converts this boolean value into an integer. In Python, True is equivalent to 1 and False is equivalent to 0. Therefore, int(keys[pygame.K_RIGHT]) gives 1 if the key is pressed, and 0 if it is not.
        #  --- KEYS / ARROWS:  -----
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])


        # to normalize the vector, after the issue when pressing top and left at the same time
        self.direction = self.direction.normalize() if self.direction else self.direction
        #    print("shipt is being updated")

        # Update the player position with speed and delta time
        self.rect.center += self.direction * self.speed * dt

        #  --- KEYS /  space bar
        recent_keys = pygame.key.get_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            #print('fire laser')
            # 🟡 Laser SURF 🟡
            Laser(laser_surf, self.rect.midtop, (all_sprites, laser_sprites))
            # final phase: By adding `laser_sprites` as an argument in `Laser()`, each laser will be added to this group when created.

            # The player is unable to fire lasers continuously
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()

        # Call the Laser_timer function from line 74
        self.laser_timer()

#🌟 STAR ---------
class Star(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        try:

            self.image = images['star']
        except KeyError:
            print("Star image not found in images dictionary.")

            self.image = pygame.Surface((70, 50))
            self.image.fill((241, 183, 0 )) # yellow

        self.rect = self.image.get_frect(center = (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))

# 🔫 LASER ---------
class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)

        try:
            self.image = surf
        except KeyError:
            print("Laser image not found in images dictionary.")
            self.image = pygame.Surface((80, 50))
            self.image.fill((255, 238, 72))  # Acid yellow


        # Set the position of the laser
        self.rect = self.image.get_frect(midbottom = pos)

    # 🔫 moving LASER bullets
    def update(self, dt):
        # centery because we only want to move 1 point
        self.rect.centery -= 400 * dt


        # conditional: to see if the laser bullet is off the window (not visible anymore), we want to destroy the sprite
        if self.rect.bottom < 0:
            self.kill()

#🪨 METEOR
class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)

        try:
            self.image = surf
        except KeyError:
            print("Meteor image not found in images dictionary.")
            self.image = pygame.Surface((80, 50))
            self.image.fill((255, 238, 72))  # Acid yellow


        # Set the position of the laser
        self.rect = self.image.get_frect(center = pos)
        # meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 3000 # lower than 3000 the user will be able to see the rocks fading

        self.direction = pygame.Vector2(uniform(-0.5, 0.5), 1)
        self.speed = randint(400, 500)



    def update(self, dt):
        #self.rect.centery += 400 * dt
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()

# METEOR & LASER collitions LOGIC

def collitions():

    global running  # 🟡 This makes 'running' refer to the global variable


    # Check for collisions between the player sprite and meteor sprites.
    # (third argument is True) This will remove the meteors that collide with the player.
    collision_sprites =  pygame.sprite.spritecollide(player, meteor_sprites, True)

    # If there are any collisions (i.e., a meteor collided with the player), print the first meteor that collided.
    if collision_sprites:
        # print(collision_sprites[0])
        running = False


    # a For each laser in the laser_sprites group, the code checks for collisions between that laser and all meteors in the meteor_sprites group.
    for laser in laser_sprites:
        # b If a collision is detected, the meteor is removed from the group (True tells the function to remove the colliding sprite).
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprites,  True)
        # c This allows individual lasers to interact with meteors, removing both if they collide.
        if collided_sprites:
            laser.kill()
            #laser.kill() removes the laser sprite from the game, effectively destroying it.



# SPRITES  ------
all_sprites = pygame.sprite.Group()

# Second sprite 2:42:40
#https://youtu.be/8OMghdHP-zs?si=hrzM_sFtk8LEG8vq&t=9768
# Why create a second sprite when handling collision during the final phase of the game?: If all sprites are in one spot, collision detection isn’t as fast
meteor_sprites = pygame.sprite.Group()



# laser collision (final phase)
laser_sprites = pygame.sprite.Group()

# Create PLAYER class instance
# all stars, without this you will only see 1 star, if i add it here
for i in range(20):
    Star(all_sprites)
## the player line below, has to be positioned under the Star(all_sprites), otherwise the star will appear on top of the player and it doesnt look good
player = Player(all_sprites)

# -----------------
# CLOCK:
# -----------------
#FPS (frame per second)
clock = pygame.time.Clock()


# CUSTOM EVENTS /timer
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)


running = True
while running:
    # DELTA time
    # frame rate / division
    dt = clock.tick() / 1000
    # print(dt)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            # print('create meteor 🪨')
            # x, y = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)
            x, y = randint(0, WINDOW_WIDTH), randint(-200, -100)

            Meteor(meteor_surf, (x,y),(all_sprites, meteor_sprites))


    # ---- update ---------
    # check the update() function within the PLAYER Class
    # 🟨 UPDATE sprite group
    all_sprites.update(dt)

    # look for the function collisions in line 205
    collitions()



    # DRAW the game ------
    display_surface.fill("lavenderblush2")
    # sprites
    all_sprites.draw(display_surface)
    # DRAW the game ------

    # TEXT
    display_surface.blit(text_surf, (0, 0))  # Blit the text at position (x, y)


    pygame.display.update()

pygame.quit()
```





<br>
<br>

##  🟡 2. Importing a Font from a Folder in Our `Space Shooter `Project

### Currently, I’m importing the font like this.

```python
# ----------
# FONT
# ----------
font = pygame.font.Font('../../FONT/WhateverFace-Bold.otf', 20)
text_surf = font.render('text', True, 'red')
# ----------
```
<br>


- - 🔴 **Note** that the path includes **`../../`**, indicating the font folder is **located outside the "spaceshooter"** project, within the pygame folder.

> ####  I will fix this in the next step by reorganizing the folder structure.



<br>
<br>

```python
# ----------
# FONT
# ----------

font = pygame.font.Font('../../FONT/PotatoFace-Bold.otf', 20)
text_surf = font.render('text', True, 'red')
# ----------
```
<br>
<br>

## 🟢 The correct path

- First we have to be sure where the images folder is in our project

```python

PYTHON_GAMES-01/
├── audio/
├── images/
├── FONT/
└── your_script.py (main.py)

  ├── 0_SPACESHIP-game/
    ├── audio/
    ├── images/
    ├── fonts/ 🍨
    │   └── NeutralFace-Bold.otf
    ├── game/
    └── main.py) # 💥  I am working on this main.py

```




<br>

## `join()`

### Once the `fonts` folder is within the <u>space shooter</u> project, I will use `join` to import the images

- import **join** (Don't ignore this, or you will have errors), at the top of you main.py file

```python
from os.path import join
```

```python
# ----------
# FONT
# ----------
font = pygame.font.Font(join('../fonts', 'PotatoFace-Bold.otf'), 20)
text_surf = font.render('text', True, 'red')
# ----------
```

<br>
<br>

### 🟣 Question:  Will importing `join` cause any conflicts with my existing use of `os.path.join()` in the script?

For example, here below (within the images) i am using os.path.join already:

```python
import pygame
import os
from random import randint, uniform
```


```python
script_dir = os.path.dirname(__file__)
# Image paths
image_paths = {
    'player': os.path.join(script_dir, '..', 'images', 'player.png'),
    'star': os.path.join(script_dir, '..', 'images', 'star.png'),
    'meteor': os.path.join(script_dir, '..', 'images', 'meteor.png'),
    'laser': os.path.join(script_dir, '..', 'images', 'laser.png')
}
```
### ✅ chatgpt: No, importing join from os.path won't cause a clash with your local join in the image_paths dictionary.

<br>

### Why?

In Python, when you import a specific function or object like this:

```python
from os.path import join
```

<br>

It temporarily replaces the reference to `os.path.join` with **`join`** in your current namespace.

- **However**, this doesn't interfere with other uses of join in other scopes (like inside dictionaries or functions).

<br>

#### If you look at the code below:

```python
from os.path import join

script_dir = os.path.dirname(__file__)
image_paths = {
    'player': join(script_dir, '..', 'images', 'player.png'),
    'star': join(script_dir, '..', 'images', 'star.png'),
    'meteor': join(script_dir, '..', 'images', 'meteor.png'),
    'laser': join(script_dir, '..', 'images', 'laser.png')
}
```
### `join` refers to `os.path.join`, and it works exactly as it did before.

If you're worried about potential conflicts, you can be explicit and use `os.path.join` in both places, like this:

```python
import os

script_dir = os.path.dirname(__file__)
image_paths = {
    'player': os.path.join(script_dir, '..', 'images', 'player.png'),
    'star': os.path.join(script_dir, '..', 'images', 'star.png'),
    'meteor': os.path.join(script_dir, '..', 'images', 'meteor.png'),
    'laser': os.path.join(script_dir, '..', 'images', 'laser.png')
}
```

- This way, you won't have to worry about shadowing any variable or function names.

### Summary:

- - Using from **`os.path import` join** <u> will not cause</u> any **clash** in your `image_paths` dictionary because the local join used there is from the os.path module.




<br>
<br>

### Code

```python

import pygame
import os
from os.path import join
from random import randint, uniform


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
# ---------

# IMAGES out of the class
# Define other surfaces
meteor_surf = images['meteor']
laser_surf = images['laser']
star_surf = images['star']
# ----------
# FONT
font = pygame.font.Font(join('../fonts', 'NeutralFace-Bold.otf'), 20)
# font = pygame.font.Font('../../FONT/NeutralFace-Bold.otf', 20)
text_surf = font.render('text', True, 'red')
# ----------
# positioning of the imgaes with surfaces, we will no longer need the below, because we are adding it directly within the laser for each one of them, like laser, meteor etc
# center of the screen for the 2 items below
# meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
# laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 10))
# -----------






#🤵 PLAYER ---------
class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        try:

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

        # 🥶 cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400 #  Players must wait 2 (2000) seconds between shots, promoting strategic timing and balanced gameplay by preventing rapid fire.


    def laser_timer(self):
        if not self.can_shoot:

            current_time = pygame.time.get_ticks()
            # print(current_time)
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True

    def update(self, dt):
        keys = pygame.key.get_pressed()
        # INT:  `int()` is the function doing the conversion. int converts this boolean value into an integer. In Python, True is equivalent to 1 and False is equivalent to 0. Therefore, int(keys[pygame.K_RIGHT]) gives 1 if the key is pressed, and 0 if it is not.
        #  --- KEYS / ARROWS:  -----
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])


        # to normalize the vector, after the issue when pressing top and left at the same time
        self.direction = self.direction.normalize() if self.direction else self.direction
        #    print("shipt is being updated")

        # Update the player position with speed and delta time
        self.rect.center += self.direction * self.speed * dt

        #  --- KEYS /  space bar
        recent_keys = pygame.key.get_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            #print('fire laser')
            # 🟡 Laser SURF 🟡
            Laser(laser_surf, self.rect.midtop, (all_sprites, laser_sprites))
            # final phase: By adding `laser_sprites` as an argument in `Laser()`, each laser will be added to this group when created.

            # The player is unable to fire lasers continuously
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()

        # Call the Laser_timer function from line 74
        self.laser_timer()

#🌟 STAR ---------
class Star(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        try:

            self.image = images['star']
        except KeyError:
            print("Star image not found in images dictionary.")

            self.image = pygame.Surface((70, 50))
            self.image.fill((241, 183, 0 )) # yellow

        self.rect = self.image.get_frect(center = (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))

# 🔫 LASER ---------
class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)

        try:
            self.image = surf
        except KeyError:
            print("Laser image not found in images dictionary.")
            self.image = pygame.Surface((80, 50))
            self.image.fill((255, 238, 72))  # Acid yellow


        # Set the position of the laser
        self.rect = self.image.get_frect(midbottom = pos)

    # 🔫 moving LASER bullets
    def update(self, dt):
        # centery because we only want to move 1 point
        self.rect.centery -= 400 * dt


        # conditional: to see if the laser bullet is off the window (not visible anymore), we want to destroy the sprite
        if self.rect.bottom < 0:
            self.kill()

#🪨 METEOR
class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)

        try:
            self.image = surf
        except KeyError:
            print("Meteor image not found in images dictionary.")
            self.image = pygame.Surface((80, 50))
            self.image.fill((255, 238, 72))  # Acid yellow


        # Set the position of the laser
        self.rect = self.image.get_frect(center = pos)
        # meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 3000 # lower than 3000 the user will be able to see the rocks fading

        self.direction = pygame.Vector2(uniform(-0.5, 0.5), 1)
        self.speed = randint(400, 500)



    def update(self, dt):
        #self.rect.centery += 400 * dt
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()

# METEOR & LASER collitions LOGIC

def collitions():

    global running  # 🟡 This makes 'running' refer to the global variable


    # Check for collisions between the player sprite and meteor sprites.
    # (third argument is True) This will remove the meteors that collide with the player.
    collision_sprites =  pygame.sprite.spritecollide(player, meteor_sprites, True)

    # If there are any collisions (i.e., a meteor collided with the player), print the first meteor that collided.
    if collision_sprites:
        # print(collision_sprites[0])
        running = False


    # a For each laser in the laser_sprites group, the code checks for collisions between that laser and all meteors in the meteor_sprites group.
    for laser in laser_sprites:
        # b If a collision is detected, the meteor is removed from the group (True tells the function to remove the colliding sprite).
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprites,  True)
        # c This allows individual lasers to interact with meteors, removing both if they collide.
        if collided_sprites:
            laser.kill()
            #laser.kill() removes the laser sprite from the game, effectively destroying it.



# SPRITES  ------
all_sprites = pygame.sprite.Group()

# Second sprite 2:42:40
#https://youtu.be/8OMghdHP-zs?si=hrzM_sFtk8LEG8vq&t=9768
# Why create a second sprite when handling collision during the final phase of the game?: If all sprites are in one spot, collision detection isn’t as fast
meteor_sprites = pygame.sprite.Group()



# laser collision (final phase)
laser_sprites = pygame.sprite.Group()

# Create PLAYER class instance
# all stars, without this you will only see 1 star, if i add it here
for i in range(20):
    Star(all_sprites)
## the player line below, has to be positioned under the Star(all_sprites), otherwise the star will appear on top of the player and it doesnt look good
player = Player(all_sprites)

# -----------------







# CLOCK:
#FPS (frame per second)
clock = pygame.time.Clock()


# CUSTOM EVENTS /timer
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)


running = True
while running:
    # DELTA time
    # frame rate / division
    dt = clock.tick() / 1000
    # print(dt)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            # print('create meteor 🪨')
            # x, y = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)
            x, y = randint(0, WINDOW_WIDTH), randint(-200, -100)

            Meteor(meteor_surf, (x,y),(all_sprites, meteor_sprites))


    # ---- update ---------
    # check the update() function within the PLAYER Class
    # 🟨 UPDATE sprite group
    all_sprites.update(dt)

    # look for the function collisions in line 205
    collitions()



    # DRAW the game ------
    display_surface.fill("lavenderblush2")
    # sprites
    all_sprites.draw(display_surface)
    # DRAW the game ------

    # TEXT
    display_surface.blit(text_surf, (0, 0))  # Blit the text at position (x, y)


    pygame.display.update()

pygame.quit()
```

---

<br>
<br>
<br>

##  🟡 3.  load multiple fonts

> #### The teacher doesn't cover this in the tutorial, but I’m curious if there are other ways to load multiple fonts.

- I believe there might be different approaches for handling this.

<br>

### 🟧 You can definitely load multiple fonts in Pygame, but they are not stored in a list directly.

> - #### Each font you load with `pygame.font.Font()` is an independent font object.

- - You can store them in a list or a dictionary if you want to organize and manage them efficiently.

<br>

### 🟤 1. Loading Multiple Fonts:

You can load different fonts with different styles or sizes into a list or dictionary. For instance:

```python
# ----------- FONT & TEXT 🟡

fonts = {
    'default': pygame.font.Font(None, 20),  # Default system font at size 20
    'bold': pygame.font.Font('../../FONT/NeutralFace-Bold.otf', 20),  # Bold font
    'italic': pygame.font.Font('../../FONT/Syncopate-Regular.ttf', 24)  # Italic font
}

text_surf_default = fonts['default'].render('Default Font', True, (255, 0, 0))
text_surf_bold = fonts['bold'].render('Bold Font', True, (0, 255, 0))
text_surf_italic = fonts['italic'].render('Italic Font', True, (0, 0, 255))
# ----------- FONT & TEXT

```

### 🟤 2. Using the Fonts:
You can now use these fonts for rendering text, just by referencing the keys in the dictionary.

```python


text_surf_default = fonts['default'].render('Default Font', True, (255, 0, 0))
text_surf_bold = fonts['bold'].render('Bold Font', True, (0, 255, 0))
text_surf_italic = fonts['italic'].render('Italic Font', True, (0, 0, 255))
# ----------- FONT & TEXT

```


<br>


### 🟤 3. Update them within the loop:

```python
    # DRAW the game ------
    display_surface.fill("lavenderblush2")
    # sprites
    all_sprites.draw(display_surface)
    # DRAW the game ------

    # TEXT
    display_surface.blit(text_surf_default, (100, 100))
    display_surface.blit(text_surf_bold, (100, 150))
    display_surface.blit(text_surf_italic, (100, 200))

    pygame.display.update()

pygame.quit()
```

### 🟢 This approach allows you to switch between fonts seamlessly, and you can render text with different styles and sizes wherever needed in your game.

<br>

[<img src="../spaceshooter_text_endphase2__.gif"/>]( )


###  Code

- i did some changes (playing with the fonts and pos)

- to move the position of the text, go to the loop, there you can handle the position

```python

import pygame
import os
from random import randint, uniform


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
# ---------

# IMAGES out of the class
# Define other surfaces
meteor_surf = images['meteor']
laser_surf = images['laser']
star_surf = images['star']
# ----------
# FONT

fonts = {
    'wagon bold': pygame.font.Font('../../FONT/NeutralFace-Bold.otf' , 45),
    'default': pygame.font.Font('../../FONT/Syncopate-Regular.ttf', 32),  # Default system font at size 20
    'bold': pygame.font.Font('../../FONT/Rajdhani-Medium.ttf', 25),  # Bold font
    'italic': pygame.font.Font(None, 24)  # Italic font
 }


text_surf_wagonbold = fonts['wagon bold'].render('Testos', True, (198, 198, 198)) # grey CCC
text_surf_default = fonts['default'].render('Default Font', True, (61, 61, 61)) # grey 3D3D3D dark
text_surf_bold = fonts['bold'].render('Bold Font', True,    (125, 125, 125)) # grey 7D7D7D mid Dark
text_surf_italic = fonts['italic'].render('Italic Font', True, (125, 125, 125)) # grey 7D7D7D mid Dark



# font = pygame.font.Font('None' 20)
 #font = pygame.font.Font('../../FONT/NeutralFace-Bold.otf', 20)
# text_surf = font.render('text', True, 'red')
# ----------
# positioning of the imgaes with surfaces, we will no longer need the below, because we are adding it directly within the laser for each one of them, like laser, meteor etc
# center of the screen for the 2 items below
# meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
# laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 10))
# -----------






#🤵 PLAYER ---------
class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        try:

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

        # 🥶 cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400 #  Players must wait 2 (2000) seconds between shots, promoting strategic timing and balanced gameplay by preventing rapid fire.


    def laser_timer(self):
        if not self.can_shoot:

            current_time = pygame.time.get_ticks()
            # print(current_time)
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True

    def update(self, dt):
        keys = pygame.key.get_pressed()
        # INT:  `int()` is the function doing the conversion. int converts this boolean value into an integer. In Python, True is equivalent to 1 and False is equivalent to 0. Therefore, int(keys[pygame.K_RIGHT]) gives 1 if the key is pressed, and 0 if it is not.
        #  --- KEYS / ARROWS:  -----
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])


        # to normalize the vector, after the issue when pressing top and left at the same time
        self.direction = self.direction.normalize() if self.direction else self.direction
        #    print("shipt is being updated")

        # Update the player position with speed and delta time
        self.rect.center += self.direction * self.speed * dt

        #  --- KEYS /  space bar
        recent_keys = pygame.key.get_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            #print('fire laser')
            # 🟡 Laser SURF 🟡
            Laser(laser_surf, self.rect.midtop, (all_sprites, laser_sprites))
            # final phase: By adding `laser_sprites` as an argument in `Laser()`, each laser will be added to this group when created.

            # The player is unable to fire lasers continuously
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()

        # Call the Laser_timer function from line 74
        self.laser_timer()

#🌟 STAR ---------
class Star(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        try:

            self.image = images['star']
        except KeyError:
            print("Star image not found in images dictionary.")

            self.image = pygame.Surface((70, 50))
            self.image.fill((241, 183, 0 )) # yellow

        self.rect = self.image.get_frect(center = (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))

# 🔫 LASER ---------
class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)

        try:
            self.image = surf
        except KeyError:
            print("Laser image not found in images dictionary.")
            self.image = pygame.Surface((80, 50))
            self.image.fill((255, 238, 72))  # Acid yellow


        # Set the position of the laser
        self.rect = self.image.get_frect(midbottom = pos)

    # 🔫 moving LASER bullets
    def update(self, dt):
        # centery because we only want to move 1 point
        self.rect.centery -= 400 * dt


        # conditional: to see if the laser bullet is off the window (not visible anymore), we want to destroy the sprite
        if self.rect.bottom < 0:
            self.kill()

#🪨 METEOR
class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)

        try:
            self.image = surf
        except KeyError:
            print("Meteor image not found in images dictionary.")
            self.image = pygame.Surface((80, 50))
            self.image.fill((255, 238, 72))  # Acid yellow


        # Set the position of the laser
        self.rect = self.image.get_frect(center = pos)
        # meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 3000 # lower than 3000 the user will be able to see the rocks fading

        self.direction = pygame.Vector2(uniform(-0.5, 0.5), 1)
        self.speed = randint(400, 500)



    def update(self, dt):
        #self.rect.centery += 400 * dt
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()

# METEOR & LASER collitions LOGIC

def collitions():

    global running  # 🟡 This makes 'running' refer to the global variable


    # Check for collisions between the player sprite and meteor sprites.
    # (third argument is True) This will remove the meteors that collide with the player.
    collision_sprites =  pygame.sprite.spritecollide(player, meteor_sprites, True)

    # If there are any collisions (i.e., a meteor collided with the player), print the first meteor that collided.
    if collision_sprites:
        # print(collision_sprites[0])
        running = False


    # a For each laser in the laser_sprites group, the code checks for collisions between that laser and all meteors in the meteor_sprites group.
    for laser in laser_sprites:
        # b If a collision is detected, the meteor is removed from the group (True tells the function to remove the colliding sprite).
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprites,  True)
        # c This allows individual lasers to interact with meteors, removing both if they collide.
        if collided_sprites:
            laser.kill()
            #laser.kill() removes the laser sprite from the game, effectively destroying it.



# SPRITES  ------
all_sprites = pygame.sprite.Group()

# Second sprite 2:42:40
#https://youtu.be/8OMghdHP-zs?si=hrzM_sFtk8LEG8vq&t=9768
# Why create a second sprite when handling collision during the final phase of the game?: If all sprites are in one spot, collision detection isn’t as fast
meteor_sprites = pygame.sprite.Group()



# laser collision (final phase)
laser_sprites = pygame.sprite.Group()

# Create PLAYER class instance
# all stars, without this you will only see 1 star, if i add it here
for i in range(20):
    Star(all_sprites)
## the player line below, has to be positioned under the Star(all_sprites), otherwise the star will appear on top of the player and it doesnt look good
player = Player(all_sprites)

# -----------------







# CLOCK:
#FPS (frame per second)
clock = pygame.time.Clock()


# CUSTOM EVENTS /timer
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)


running = True
while running:
    # DELTA time
    # frame rate / division
    dt = clock.tick() / 1000
    # print(dt)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            # print('create meteor 🪨')
            # x, y = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)
            x, y = randint(0, WINDOW_WIDTH), randint(-200, -100)

            Meteor(meteor_surf, (x,y),(all_sprites, meteor_sprites))


    # ---- update ---------
    # check the update() function within the PLAYER Class
    # 🟨 UPDATE sprite group
    all_sprites.update(dt)

    # look for the function collisions in line 205
    collitions()



    # DRAW the game ------
    display_surface.fill("lavenderblush2")
    # sprites
    all_sprites.draw(display_surface)
    # DRAW the game ------

    # TEXT
    # display_surface.blit(text_surf, (0, 0))  # Blit the text at position (x, y)
    # Display them on the screen

    # display_surface.blit(text_surf_wagonbold,(100, 150))
    # display_surface.blit(text_surf_bold, (110, 180))

    display_surface.blit(text_surf_default, (40, 60))
    display_surface.blit(text_surf_italic, (40, 100))


    pygame.display.update()

pygame.quit()
```

<br>
<br>
<br>
<br>

---

## 🟠  An Alternative Approach

### Use a dictionary to store font paths and sizes, and load them dynamically with a loop

> #### Here’s how you could do it:

```python
# Define font paths and sizes in a dictionary
font_paths = {
    'small': os.path.join(script_dir, '..', 'fonts', 'font_small.ttf'),
    'medium': os.path.join(script_dir, '..', 'fonts', 'font_medium.ttf'),
    'large': os.path.join(script_dir, '..', 'fonts', 'font_large.ttf')
}

# Load fonts into a dictionary
fonts = {
    key: pygame.font.Font(path, 24 if key == 'small' else 32 if key == 'medium' else 48)
    for key, path in font_paths.items()
}

```

<br>

## 🍨 How it works:

- - **`font_paths`**:  This dictionary holds the paths to the font files.

- - **fonts:** This dictionary loads each font dynamically, specifying a different font size depending on the key (small, medium, large).

#### This way, you avoid repeating code and keep the loading process organized. You can then access the fonts like this:

```python
# Use the fonts
text_small = fonts['small'].render("Small Text", True, (255, 0, 0))
text_medium = fonts['medium'].render("Medium Text", True, (0, 255, 0))
text_large = fonts['large'].render("Large Text", True, (0, 0, 255))

```

#### This approach is much cleaner and makes it easy to manage multiple fonts just like you do with images.

---

<br>
<br>
<br>
<br>

