
# 🟡 SPRITES 10.

- Sounds

<br>
<br>

### INTRO:



<br>
<br>
<br>

---

### [3:40:06](https://youtu.be/8OMghdHP-zs?si=kVVA4Yh1DIOLcrYx&t=13206)



# 🟡 SOUNDS



<br>

## 🟡 1. Create a Sound Object

### To begin, we need to create a sound object.

> #### Use the following line to create a sound object:

```python
laser_sound = pygame.mixer.Sound('your_file_path_here')

```

#### What Can You Do with a Sound Object?

- Play the sound

- Stop the sound

- Rewind the sound

- Adjust the volume


#### For more details, check out the Pygame documentation on the mixer, which explains how sound and music work in Pygame:

[Documentation](https://www.pygame.org/docs/ref/mixer.html)

<br>
<br>


## 🟡 2. Import the Sound Files

**Next**, we need to import the sound files into our code. Make sure you have your audio files ready in the **audio folder**.

#### Here’s how to import a sound file:

```python
# AUDIO
laser_sound = pygame.mixer.Sound(join('../audio', 'laser.wav'))
```

> Make sure the file path matches where your audio files are stored.

<br>
<br>

## 🟡 3. Play the Sound

**Now** that we have the sound set up, it's time to **play it** when an **event happens**, like s**hooting a laser**.

#### Find the part of your code where the laser is created.

> - - This is typically in the player class. You want to add the sound to the function that handles shooting.

#### Here’s how to do it in your `update()` function:

```python
if recent_keys[pygame.K_SPACE] and self.can_shoot:
    # Create the laser instance
    Laser(laser_surf, self.rect.midtop, (all_sprites, laser_sprites))

    self.can_shoot = False
    self.laser_shoot_time = pygame.time.get_ticks()

    # PLAY SOUND
    laser_sound.play()
```


### As you can see in the video below, the gun sound is working perfectly, but its too Loud 🔊 🔫.

https://github.com/user-attachments/assets/519b0ade-e21c-4500-aec8-3631d9062349

<br>
<br>

## 🟡 4. Adjusting the Laser Volume

###  If the laser sound is too loud, you can easily adjust its volume to create a more balanced audio experience.

#### To control the volume, use the following line of code:

```python
laser_sound.set_volume()
```
### 🟢 This function requires a floating-point value between 0 and 1.

Here’s how it works:

- - `0` means the sound is completely muted.

- - `1` means the sound is at full volume.
For example, to set the volume to **50%**, you would write:

```python
laser_sound.set_volume(0.5)

```

> 🟤 This means that the sound will play at half of its maximum volume.

<br>



### 🟧 Make sure to position this code right after you load the sound file to ensure the volume setting takes effect:

```python
# AUDIO
laser_sound = pygame.mixer.Sound(join('../audio', 'laser.wav'))
laser_sound.set_volume(0.5)

```

<br>
<br>

## 🟡 5. lets import all the other sounds

```python
explosion_sound = pygame.mixer.Sound(join('../audio', 'explosion.wav'))
damage_sound = pygame.mixer.Sound(join('../audio', 'damage.ogg'))

game_music = pygame.mixer.Sound(join('../audio', 'game_music.wav'))
```

<br>

## 🟡 6.  Playing the Explosion Sound on Collision


> ### 🟧 To play the explosion sound when a laser hits a meteor, you have <u>two options</u> .

<br>

#### Let's go through the first one:

### 🟤  1.Modify the collision() Function:

 - ####  Within the existing loop that checks for collisions, add the line:

> - - 💥 `explosion_sound.play()` to play the explosion sound.


#### Here’s how you can do it:



```python
def collisions():
    global running  # Refers to the global variable 'running'

    # Check for collisions between the player sprite and meteor sprites.
    # The third argument is True, which removes colliding meteors.
    collision_sprites = pygame.sprite.spritecollide(player, meteor_sprites, True)

    # If any collisions occur, print the first meteor that collided.
    if collision_sprites:
        running = False

    # Check for collisions between lasers and meteors.
    for laser in laser_sprites:
        # If a collision is detected, the meteor is removed from the group.
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprites, True)

        # Handle the collision if it occurs.
        if collided_sprites:
            laser.kill()  # Remove the laser sprite from the game.
            AnimateExplosion(explosion_frames, laser.rect.midtop, all_sprites)

            # 💥 SOUND
            explosion_sound.play()  # Play the explosion sound.

```

<br>

## 🟡 7. You can also play the explosion sound by moving the line into the `AnimateExplosion` class.


```python
explosion_sound.play() # If a collision occurs, the laser is destroyed, an explosion animation is triggered, and the explosion sound plays.
```
### ✋This approach works as well.

 Here’s how to do it:

### 🟢 Reposition the Sound Line:

- - Place the `explosion_sound.play()` line inside the AnimateExplosion class.

#### Here’s the updated code:

```python
class AnimateExplosion(pygame.sprite.Sprite):
    def __init__(self, frames,pos, groups):
        super().__init__(groups)
        try:
            self.frames = frames
            self.frame_index = 0
            self.image = self.frames[self.frame_index]


        except KeyError:
            print("Star image not found in images dictionary.")


        self.rect = self.image.get_frect(center = pos)


        explosion_sound.play() # 💥🔉 If a collision occurs, the laser is destroyed, an explosion animation is triggered, and the explosion sound plays.
```

<br>
<br>

## 🟡 8. Setting Up Game Music



### The teacher has decided not to include a damage sound, as it not necessary.

> #### 🔴 However, if you’re interested in implementing a sound effect for when the player gets hit, go to <u>step 9</u>  ✋

<br>

### Add the game sound:

- The teacher added the following lines to handle the game's background music:

```python
# The music you will hear when you are playing
game_music = pygame.mixer.Sound(join('../audio', 'game_music.wav'))
game_music.set_volume(0.4)
game_music.play()

```

### output

https://github.com/user-attachments/assets/b7ce5e32-e5ed-40ec-ac23-477fdc92b269


<br>

### 🔴 Playing with Loops: This command starts playing the music and loops it 5 times.

```python
game_music.play(loops=5)

```

- - So, the music will play once, then repeat for an additional four times (a total of five times).

```python
game_music.play(loops=-1)  # indefinitely
```

<br>

>**Indefinite Looping:** Here, using loops=-1 means the music will play continuously without stopping. It will loop indefinitely until you stop it manually or the game ends.

<br>

### End of the tutorial

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
# -----------------------

#------------------------
# Load explosion images

# explosion_frames = [pygame.image.load(join('images', 'explosion', f'{i}.png')).convert_alpha() for i in range(21)]
# explosion_frames = [join('images', 'explosion', f'{i}.png') for i in range(1, 21)]

# Load explosion frames
explosion_frames = []
for i in range(21):
    path = os.path.join(script_dir, '..', 'images', 'explosion', f'{i}.png')
    try:
        explosion_frames.append(pygame.image.load(path).convert_alpha())
    except pygame.error as e:
        print(f"Failed to load explosion image '{path}': {e}")
        # Optionally add a fallback surface if needed
        explosion_frames.append(pygame.Surface((50, 50)).fill((255, 0, 0)))  # Red square as fallback

print(explosion_frames)


# ----------
# FONT
font = pygame.font.Font(join('../fonts', 'NeutralFace-Bold.otf'), 30)
# font = pygame.font.Font('../../FONT/NeutralFace-Bold.otf', 20)

# ----------
# positioning of the imgaes with surfaces, we will no longer need the below, because we are adding it directly within the laser for each one of them, like laser, meteor etc
# center of the screen for the 2 items below
# meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
# laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 10))
# -----------
# AUDIO
laser_sound = pygame.mixer.Sound(join('../audio', 'laser.wav'))
laser_sound.set_volume(0.5)

explosion_sound = pygame.mixer.Sound(join('../audio', 'explosion.wav'))

# The music you will hear when you are playing
game_music = pygame.mixer.Sound(join('../audio', 'game_music.wav'))
game_music.set_volume(0.4)
game_music.play(loops= 5)
# game_music.play(loops= -1) #indefinitely


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

        # self.image = pygame.transform.rotate(self.image, 90)
        # self.image = pygame.transform.scale2x(self.image)
        # rotation
        # self.rotation = 0



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

            # SOUND
            laser_sound.play()

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

            # 1 rotation
            self.original_surf = surf

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

        # 2 rotation
        self.rotation_speed = randint(40,100)
        #3
        self.rotation = 0


    def update(self, dt):
        #self.rect.centery += 400 * dt
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()

        # 4
        self.rotation += self.rotation_speed * dt

        # 5
        self.image = pygame.transform.rotozoom(self.original_surf, self.rotation, 1 )

        # 6
        self.rect = self.image.get_frect(center = self.rect.center)


#💥
class AnimateExplosion(pygame.sprite.Sprite):
    def __init__(self, frames,pos, groups):
        super().__init__(groups)
        try:
            self.frames = frames
            self.frame_index = 0
            self.image = self.frames[self.frame_index]


        except KeyError:
            print("Star image not found in images dictionary.")


        self.rect = self.image.get_frect(center = pos)


        explosion_sound.play() # 💥🔉 If a collision occurs, the laser is destroyed, an explosion animation is triggered, and the explosion sound plays.


    def update(self, dt):
        self.frame_index += 5 * dt
        # NO: self.image = self.frames[self.frame_index]
        # ALSO NO: self.image = self.frames[int(self.frame_index)]
        print(self.frame_index)

        if self.frame_index < len(self.frames):
            self.image = self.frames[int(self.frame_index)]
        else:
            self.kill()

        # self.image = self.frames[int(self.frame_index) % len(self.frames)]


# 💥 🪨 METEOR & LASER collitions LOGIC

def collitions():

    global running  # 🟡 This makes 'running' refer to the global variable


    # Check for collisions between the player sprite and meteor sprites.
    # (third argument is True) This will remove the meteors that collide with the player.
    collision_sprites =  pygame.sprite.spritecollide(player, meteor_sprites, True)

    # If there are any collisions (i.e., a meteor collided with the player), print the first meteor that collided.
    if collision_sprites:

        running = False  # End the game


    # a For each laser in the laser_sprites group, the code checks for collisions between that laser and all meteors in the meteor_sprites group.
    for laser in laser_sprites:
        # b If a collision is detected, the meteor is removed from the group (True tells the function to remove the colliding sprite).
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprites,  True)
        # c This allows individual lasers to interact with meteors, removing both if they collide.
        if collided_sprites:
            laser.kill()
            #laser.kill() removes the laser sprite from the game, effectively destroying it.
            AnimateExplosion(explosion_frames, laser.rect.midtop,all_sprites)

            #explosion_sound.play() # If a collision occurs, the laser is destroyed, an explosion animation is triggered, and the explosion sound plays.


# SCORE

def display_score():
    current_time = pygame.time.get_ticks() // 100
    text_surf = font.render(str(current_time), True, (255,255,255))
    # text_rect = text_surf.get_frect(midbottom = (x,y))
    text_rect = text_surf.get_frect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT -50))
    display_surface.blit(text_surf, text_rect)
    # BOX around padding, here you will have padding as inflate
    pygame.draw.rect(display_surface, (240,240,240), text_rect.inflate(28, 30).move(0,-2), 5,10)



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
    display_surface.fill("#2a0822")
    # sprites
    all_sprites.draw(display_surface)
    # DRAW the game ------

    # TEXT
    #display_surface.blit(text_surf, (0, 0))  # Blit the text at position (x, y)
    display_score()

    pygame.display.update()

pygame.quit()
```

<br>

## END of the tutorial

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>


---

### Adding Sound Effects for Player Damage

🟥 This is not in the tutorial. I felt a bit curious because the teacher decided not to add sounds for several hits or include a health management system..

<br>
<br>

## 🟡 9. Playing a Sound When the Player Gets Hit





### 🟠 Our Objective:

#### When the player is hit, we want to trigger a sound effect to emphasize the impact of that event.




### 🟢Implementation Steps:

<br>

**Integrate Sound Playback:**

- We’ll place the sound playback within the collision detection logic.

-  - This way, the sound plays at the exact moment the player is hit.


<br>

**Current Challenge:**

- 🟤 Right now, when a meteor hits the player, the game window closes automatically.

```python
   if collision_sprites:
        print("Player hit!")  # Debugging line
        damage_sound.play()  # Play the damage sound
        running = False  # End the game
```

> #### 🔴 This doesn't give enough time for the sound to play. Even if we add the sound, it won't be audible because of the immediate game closure.

<br>

## 🟠 Delay

### Introducing a Delay

> #### To allow the sound to be heard, we need to introduce a delay.

By adding a delay of **500 milliseconds** (half a second) after playing the sound, we give the game a brief pause before proceeding to the next action.

### Here’s how to modify the code:



```python
if collision_sprites:
    print("Player hit!")  # Debugging line
    damage_sound.play()  # Play the damage sound
    pygame.time.delay(500)  # Wait for half a second
    running = False  # End the game

```
### Output


https://github.com/user-attachments/assets/585138a8-4e91-4538-a3f9-b9edb2fec560


<br>

### the code




```python

def collitions():

    global running  # 🟡 This makes 'running' refer to the global variable


    # Check for collisions between the player sprite and meteor sprites.
    # (third argument is True) This will remove the meteors that collide with the player.
    collision_sprites =  pygame.sprite.spritecollide(player, meteor_sprites, True)

    # If there are any collisions (i.e., a meteor collided with the player), print the first meteor that collided.
    if collision_sprites:
        print("Player hit!")  # Debugging line
        #damage_sound.play()  # Play the damage sound
        hit_music.play()
        pygame.time.delay(500)  # Wait for half a second
        running = False  # End the game


    # a For each laser in the laser_sprites group, the code checks for collisions between that laser and all meteors in the meteor_sprites group.
    for laser in laser_sprites:
        # b If a collision is detected, the meteor is removed from the group (True tells the function to remove the colliding sprite).
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprites,  True)
        # c This allows individual lasers to interact with meteors, removing both if they collide.
        if collided_sprites:
            laser.kill()
            #laser.kill() removes the laser sprite from the game, effectively destroying it.
            AnimateExplosion(explosion_frames, laser.rect.midtop,all_sprites)

            #explosion_sound.play() # If a collision occurs, the laser is destroyed, an explosion animation is triggered, and the explosion sound plays.

```


<br>
<br>



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
# -----------------------

#------------------------
# Load explosion images

# explosion_frames = [pygame.image.load(join('images', 'explosion', f'{i}.png')).convert_alpha() for i in range(21)]
# explosion_frames = [join('images', 'explosion', f'{i}.png') for i in range(1, 21)]

# Load explosion frames
explosion_frames = []
for i in range(21):
    path = os.path.join(script_dir, '..', 'images', 'explosion', f'{i}.png')
    try:
        explosion_frames.append(pygame.image.load(path).convert_alpha())
    except pygame.error as e:
        print(f"Failed to load explosion image '{path}': {e}")
        # Optionally add a fallback surface if needed
        explosion_frames.append(pygame.Surface((50, 50)).fill((255, 0, 0)))  # Red square as fallback

print(explosion_frames)


# ----------
# FONT
font = pygame.font.Font(join('../fonts', 'NeutralFace-Bold.otf'), 30)
# font = pygame.font.Font('../../FONT/NeutralFace-Bold.otf', 20)

# ----------
# positioning of the imgaes with surfaces, we will no longer need the below, because we are adding it directly within the laser for each one of them, like laser, meteor etc
# center of the screen for the 2 items below
# meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
# laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 10))
# -----------
# AUDIO
laser_sound = pygame.mixer.Sound(join('../audio', 'laser.wav'))
laser_sound.set_volume(0.5)

explosion_sound = pygame.mixer.Sound(join('../audio', 'explosion.wav'))
damage_sound = pygame.mixer.Sound(join('../audio', 'damage.ogg'))

game_music = pygame.mixer.Sound(join('../audio', 'game_music.wav'))

hit_music = pygame.mixer.Sound(join('../audio', 'old-reactor-106146.mp3'))



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

        # self.image = pygame.transform.rotate(self.image, 90)
        # self.image = pygame.transform.scale2x(self.image)
        # rotation
        # self.rotation = 0



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

            # SOUND
            laser_sound.play()

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

            # 1 rotation
            self.original_surf = surf

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

        # 2 rotation
        self.rotation_speed = randint(40,100)
        #3
        self.rotation = 0


    def update(self, dt):
        #self.rect.centery += 400 * dt
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()

        # 4
        self.rotation += self.rotation_speed * dt

        # 5
        self.image = pygame.transform.rotozoom(self.original_surf, self.rotation, 1 )

        # 6
        self.rect = self.image.get_frect(center = self.rect.center)


#💥
class AnimateExplosion(pygame.sprite.Sprite):
    def __init__(self, frames,pos, groups):
        super().__init__(groups)
        try:
            self.frames = frames
            self.frame_index = 0
            self.image = self.frames[self.frame_index]


        except KeyError:
            print("Star image not found in images dictionary.")


        self.rect = self.image.get_frect(center = pos)


        explosion_sound.play() # 💥🔉 If a collision occurs, the laser is destroyed, an explosion animation is triggered, and the explosion sound plays.


    def update(self, dt):
        self.frame_index += 5 * dt
        # NO: self.image = self.frames[self.frame_index]
        # ALSO NO: self.image = self.frames[int(self.frame_index)]
        print(self.frame_index)

        if self.frame_index < len(self.frames):
            self.image = self.frames[int(self.frame_index)]
        else:
            self.kill()

        # self.image = self.frames[int(self.frame_index) % len(self.frames)]
# ------

# ------


# 💥 🪨 METEOR & LASER collitions LOGIC

def collitions():

    global running  # 🟡 This makes 'running' refer to the global variable


    # Check for collisions between the player sprite and meteor sprites.
    # (third argument is True) This will remove the meteors that collide with the player.
    collision_sprites =  pygame.sprite.spritecollide(player, meteor_sprites, True)

    # If there are any collisions (i.e., a meteor collided with the player), print the first meteor that collided.
    if collision_sprites:
        print("Player hit!")  # Debugging line
        #damage_sound.play()  # Play the damage sound
        hit_music.play()
        pygame.time.delay(500)  # Wait for half a second
        running = False  # End the game


    # a For each laser in the laser_sprites group, the code checks for collisions between that laser and all meteors in the meteor_sprites group.
    for laser in laser_sprites:
        # b If a collision is detected, the meteor is removed from the group (True tells the function to remove the colliding sprite).
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprites,  True)
        # c This allows individual lasers to interact with meteors, removing both if they collide.
        if collided_sprites:
            laser.kill()
            #laser.kill() removes the laser sprite from the game, effectively destroying it.
            AnimateExplosion(explosion_frames, laser.rect.midtop,all_sprites)

            #explosion_sound.play() # If a collision occurs, the laser is destroyed, an explosion animation is triggered, and the explosion sound plays.


# SCORE

def display_score():
    current_time = pygame.time.get_ticks() // 100
    text_surf = font.render(str(current_time), True, (255,255,255))
    # text_rect = text_surf.get_frect(midbottom = (x,y))
    text_rect = text_surf.get_frect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT -50))
    display_surface.blit(text_surf, text_rect)
    # BOX around padding, here you will have padding as inflate
    pygame.draw.rect(display_surface, (240,240,240), text_rect.inflate(28, 30).move(0,-2), 5,10)



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
    display_surface.fill("#2a0822")
    # sprites
    all_sprites.draw(display_surface)
    # DRAW the game ------

    # TEXT
    #display_surface.blit(text_surf, (0, 0))  # Blit the text at position (x, y)
    display_score()

    pygame.display.update()

pygame.quit()
```


<br>
<br>

## 🟡 Adding a basic health management 💓

To add a simple health system that allows the player to be hit three times before the game ends, we can **introduce a `life counter` 💓 in the `Player` class** and modify the collision logic accordingly.


### We'll also implement sound effects for losing lives.

#### Here’s how to do it:

- - **Add Health Variables:** We'll track the player's lives.

- - **Modify Collision Logic:** Decrease lives on collision and play the appropriate sounds.

- - **End Game Logic:** Trigger the game over sequence when lives reach zero.

- - -  **Display player lives**

<br>
<br>

# 🌈 Lets get started:



### 🟢 Add Health Variables:

We'll track the player's lives

```python
      # Initialize player health
        self.lives = 3  # Set initial lives
        self.is_alive = True  # Track if the player is alive
```



<br>


### 🟢 Modify Collision Logic:

- Decrease lives on collision and play the appropriate sounds.

```python
    # Method to handle taking damage
    def take_damage(self):
        if self.is_alive:
            self.lives -= 1
            if self.lives == 1:  # Play sound when player loses the second life
                hit_sound.play()
            elif self.lives <= 0:  # Play game over sound when player loses all lives
                game_over_sound.play()
                self.is_alive = False  # Mark player as dead
```

#### I didnt like the above version, i wanted to get a sound for every life lost:

```python
def take_damage(self):
    if self.is_alive:  # 🛡️ Check if the player is still alive

        # Play the hit sound immediately upon the first hit

        hit_sound.play()  # 🔊 Play sound for the first hit

        self.lives -= 1  # ➖ Decrease lives by 1


        if self.lives <= 0:
            # 💀 Play game over sound when player loses all lives
            game_over_sound.play()
            self.is_alive = False  # ❌ Mark player as dead

```

<br>
<br>

### 🟢 End Game Logic:

-  Trigger the game over sequence when lives reach zero.

```python
   if self.lives <= 0:
            # 💀 Play game over sound when player loses all lives
            game_over_sound.play()
            self.is_alive = False  # ❌ Mark player as dead
```

- - #### 🟤 Within the `collitions()` class, call the damage method

```python
    if collision_sprites:

        player.take_damage()  # 💥 Call the player's method to take damage
        if not player.is_alive:  # ⚠️ If player is dead, end the game

           print("Player hit!")  # Debugging line
        #    game_over_sound.play()  # Play the damage sound
           pygame.time.delay(500)  # Wait for half a second
           running = False  # End the game
```


<br>
<br>


### 🟢 Display player lives


```python
# Display player lives
    lives_text = font.render(f'Lives: {player.lives}', True, (255, 0, 0))  # Red for emphasis
    lives_rect = lives_text.get_frect(topleft=(10, 10))
    display_surface.blit(lives_text, lives_rect)

    pygame.draw.rect(display_surface, (240, 240, 240), lives_rect.inflate(28, 30).move(0, -2), 5, 10)
```


<br>

#### code

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
# -----------------------

#------------------------
# Load explosion images

# explosion_frames = [pygame.image.load(join('images', 'explosion', f'{i}.png')).convert_alpha() for i in range(21)]
# explosion_frames = [join('images', 'explosion', f'{i}.png') for i in range(1, 21)]

# Load explosion frames
explosion_frames = []
for i in range(21):
    path = os.path.join(script_dir, '..', 'images', 'explosion', f'{i}.png')
    try:
        explosion_frames.append(pygame.image.load(path).convert_alpha())
    except pygame.error as e:
        print(f"Failed to load explosion image '{path}': {e}")
        # Optionally add a fallback surface if needed
        explosion_frames.append(pygame.Surface((50, 50)).fill((255, 0, 0)))  # Red square as fallback

print(explosion_frames)


# ----------
# FONT
font = pygame.font.Font(join('../fonts', 'NeutralFace-Bold.otf'), 30)
# font = pygame.font.Font('../../FONT/NeutralFace-Bold.otf', 20)

# ----------
# positioning of the imgaes with surfaces, we will no longer need the below, because we are adding it directly within the laser for each one of them, like laser, meteor etc
# center of the screen for the 2 items below
# meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
# laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 10))
# -----------
# AUDIO
laser_sound = pygame.mixer.Sound(join('../audio', 'laser.wav'))
laser_sound.set_volume(0.5)

explosion_sound = pygame.mixer.Sound(join('../audio', 'explosion.wav'))

# The music you will hear when you are playing
game_music = pygame.mixer.Sound(join('../audio', 'game_music.wav'))
game_music.set_volume(0.4)
game_music.play(loops= 5)
# game_music.play(loops= -1) #indefinitely
# Add imports for the sounds
hit_sound = pygame.mixer.Sound(join('../audio', 'dead_before_gameover.mp3'))  # 🎵 Sound for losing 2 lives
game_over_sound = pygame.mixer.Sound(join('../audio', 'dead_gameOver.wav'))  # 🎵 Sound for game over


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

        # self.image = pygame.transform.rotate(self.image, 90)
        # self.image = pygame.transform.scale2x(self.image)
        # rotation
        # self.rotation = 0
            # Initialize player health
        self.lives = 3  # ❤️ Set initial lives
        self.is_alive = True  # ✅ Track if the player is alive

            # Method to handle taking damage
    # def take_damage(self):
    #     if self.is_alive:  # 🛡️ Check if the player is still alive
    #         self.lives -= 1  # ➖ Decrease lives by 1
    #         if self.lives == 1:  # 🔊 Play sound when player loses the second life
    #             hit_sound.play()
    #         elif self.lives <= 0:  # 💀 Play game over sound when player loses all lives
    #             game_over_sound.play()
    #             self.is_alive = False  # ❌ Mark player as dead
    def take_damage(self):
        if self.is_alive:  # 🛡️ Check if the player is still alive
        # Play the hit sound immediately upon the first hit
            hit_sound.play()  # 🔊 Play sound for the first hit

            self.lives -= 1  # ➖ Decrease lives by 1

        if self.lives <= 0:  # 💀 Play game over sound when player loses all lives
            game_over_sound.play()
            self.is_alive = False  # ❌ Mark player as dead




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

            # SOUND
            laser_sound.play()

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

            # 1 rotation
            self.original_surf = surf

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

        # 2 rotation
        self.rotation_speed = randint(40,100)
        #3
        self.rotation = 0


    def update(self, dt):
        #self.rect.centery += 400 * dt
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()

        # 4
        self.rotation += self.rotation_speed * dt

        # 5
        self.image = pygame.transform.rotozoom(self.original_surf, self.rotation, 1 )

        # 6
        self.rect = self.image.get_frect(center = self.rect.center)


#💥
class AnimateExplosion(pygame.sprite.Sprite):
    def __init__(self, frames,pos, groups):
        super().__init__(groups)
        try:
            self.frames = frames
            self.frame_index = 0
            self.image = self.frames[self.frame_index]


        except KeyError:
            print("Star image not found in images dictionary.")


        self.rect = self.image.get_frect(center = pos)


        explosion_sound.play() # 💥🔉 If a collision occurs, the laser is destroyed, an explosion animation is triggered, and the explosion sound plays.


    def update(self, dt):
        self.frame_index += 5 * dt
        # NO: self.image = self.frames[self.frame_index]
        # ALSO NO: self.image = self.frames[int(self.frame_index)]
        print(self.frame_index)

        if self.frame_index < len(self.frames):
            self.image = self.frames[int(self.frame_index)]
        else:
            self.kill()

        # self.image = self.frames[int(self.frame_index) % len(self.frames)]







# ------

# ------


# 💥 🪨 METEOR & LASER collitions LOGIC

def collitions():

    global running  # 🟡 This makes 'running' refer to the global variable


    # Check for collisions between the player sprite and meteor sprites.
    # (third argument is True) This will remove the meteors that collide with the player.
    collision_sprites =  pygame.sprite.spritecollide(player, meteor_sprites, True)

    # If there are any collisions (i.e., a meteor collided with the player), print the first meteor that collided.
    if collision_sprites:
        player.take_damage()  # 💥 Call the player's method to take damage
        if not player.is_alive:  # ⚠️ If player is dead, end the game
           print("Player hit!")  # Debugging line
        #    game_over_sound.play()  # Play the damage sound
           pygame.time.delay(500)  # Wait for half a second
           running = False  # End the game


    # a For each laser in the laser_sprites group, the code checks for collisions between that laser and all meteors in the meteor_sprites group.
    for laser in laser_sprites:
        # b If a collision is detected, the meteor is removed from the group (True tells the function to remove the colliding sprite).
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprites,  True)
        # c This allows individual lasers to interact with meteors, removing both if they collide.
        if collided_sprites:
            laser.kill()
            #laser.kill() removes the laser sprite from the game, effectively destroying it.
            AnimateExplosion(explosion_frames, laser.rect.midtop,all_sprites)

            #explosion_sound.play() # If a collision occurs, the laser is destroyed, an explosion animation is triggered, and the explosion sound plays.


# SCORE

def display_score():
    current_time = pygame.time.get_ticks() // 100
    text_surf = font.render(str(current_time), True, (255,255,255))
    # text_rect = text_surf.get_frect(midbottom = (x,y))
    text_rect = text_surf.get_frect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT -50))
    display_surface.blit(text_surf, text_rect)

# Display player lives
    lives_text = font.render(f'Lives: {player.lives}', True, (255, 0, 0))  # 🔴 Red for emphasis
    lives_rect = lives_text.get_frect(topleft=(10, 10))
    display_surface.blit(lives_text, lives_rect)

    # 🟡 Box around the lives text for better visibility
    pygame.draw.rect(display_surface, (240, 240, 240), lives_rect.inflate(28, 30).move(0, -2), 5, 10)


    # BOX around padding, here you will have padding as inflate
    # pygame.draw.rect(display_surface, (240,240,240), text_rect.inflate(28, 30).move(0,-2), 5,10)



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
    display_surface.fill("#2a0822")
    # sprites
    all_sprites.draw(display_surface)
    # DRAW the game ------

    # TEXT
    #display_surface.blit(text_surf, (0, 0))  # Blit the text at position (x, y)
    display_score()

    pygame.display.update()

pygame.quit()
```



https://github.com/user-attachments/assets/735e0538-251a-45d7-a8eb-bfb0d801ed49

