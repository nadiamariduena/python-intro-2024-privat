
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

