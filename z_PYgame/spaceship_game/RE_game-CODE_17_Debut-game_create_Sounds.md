
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
