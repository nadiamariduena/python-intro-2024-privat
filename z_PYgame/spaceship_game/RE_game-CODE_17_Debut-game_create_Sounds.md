
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

