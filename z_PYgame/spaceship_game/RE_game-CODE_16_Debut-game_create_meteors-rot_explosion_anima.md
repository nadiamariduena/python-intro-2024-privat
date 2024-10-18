
# 🟡 SPRITES 9.


### INTRO:

- - 894 🟤 **`modulo operator (%)`** [Go to section](#modulo_operator_)

-  - - Why Use the Modulo Operator [Go to section](#WHY_use_modulor_operator_)



<br>
<br>
<br>
<br>

---

### [3:30:55](https://youtu.be/8OMghdHP-zs?si=OVRzdB0hId6Nw8jX&t=12655)



## 🟡 Explosion Animation

<br>

###  In this Lesson we will be implementing an explosion animation.

> #### When a laser hits a meteor, we want to create a captivating explosion effect that will enhance the gameplay experience.

#### This will not only make the game more engaging but also provide players with satisfying feedback when they destroy enemies.

<br>
<br>

### 🟧 Steps Overview


**Import the Explosion Images:** Load the explosion images that will be used in the animation.

**Create the Explosion Class:** Develop the AnimatedExplosion class to handle the animation.

**Define the Constructor and Frames:** Set up the constructor to initialize the frames as a list of surfaces.

**Trigger the Animation:** Instantiate the explosion class when a laser hits a meteor.

**Update and Draw the Animation:** Manage the animation's progress and render it on the screen.

- **Clean Up:** Ensure that the explosion instance is removed after the animation completes.

<br>
<br>
<br>


## 🟦 Moving Forward:



## 🟠 1. Import the Explosion Images

### To get started, we need to gather the images that will form our explosion animation.

<br>

---

## 💥 Show the explosion at different stages

> #### We'll typically have a series of images that show the explosion at different stages.

> #### Make sure you have these images ready in your project directory, as we'll be loading them into our game to create a smooth animation.

---

<br>
<br>

## 🟠 2. Create the Explosion Class

> #### Next, we will create a class called `AnimatedExplosion`.

```python
#🪨 METEOR
class Meteor(pygame.sprite.Sprite):

# 💥
class AnimateExplosion(pygame.sprite.Sprite):

```

#### This class will be responsible for handling the animation of the explosion.

#### Here's how it will work:

> ### 🔫 When a laser hits a meteor, we will create an instance of the `AnimatedExplosion` class.

- - 💥 This instance will manage the sequence of explosion images, **playing them in order** to create the **illusion of an explosion**.


#### After the animation completes, the instance will disappear from the game, ensuring that it doesn't take up resources unnecessarily.

<br>

[3:31:46](https://youtu.be/8OMghdHP-zs?si=CeVjPZAfcRuuiPv4&t=12706)

### 🟠 3. Define the Constructor and Frames

🟫 **LIST of Surfaces: the teacher will call them Frames**

#### This is where we will initialize the explosion `frames`, which are crucial for creating the animation effect.

<br>

- -  🟢 **Each `frame`** represents a stage in the explosion sequence, and having them stored in a list allows us to easily cycle through them to create the illusion of movement.

<br>

- - Once the pygame class created, create the constructor init and add the frames, which is a list of surfaces

<br>

- 🔴 Add also the position and the groups: `pos, groups` to the constructor

```python
class AnimateExplosion(pygame.sprite.Sprite):
    def __init__(self, frames,pos, groups):
```

<br>

#### Purpose of Frames


- **Visual Fluidity:** By using multiple frames, we can create a fluid animation that mimics a real explosion.

> - - #### Instead of just showing a static image, cycling through several images gives the impression of motion.


- **Control Over Animation Speed:** The number of frames and the speed at which they are displayed can be adjusted to create different explosion effects.

>For instance, a faster transition can imply a more intense explosion.

- **Resource Management:**

> #### 🟢 Storing frames in a list makes it easy to manage the resources required for the animation, <u>as we can load them all at once</u>  and refer to them as needed.

<br>
<br>

### 🟠 4. Initialize the Sprite and Set the Initial Image


#### In this step, we will register the `AnimateExplosion` sprite with the specified groups and set the initial image for the explosion animation by using the first frame from the provided list of frames.


- i will add the version without the exception frst

```python
        super().__init__(groups)
            self.image = frames[0]

            self.rect = self.image.get_frect(center = pos)
```

### Explanation:

#### `super().__init__(groups)`:

**Calling the Parent Class Constructor:** This line calls the constructor of the parent class `(pygame.sprite.Sprite)` and passes the groups parameter to it.

- - This is important for adding the sprite to the specified groups, which lets Pygame keep track of it. This way, the sprite can be updated and drawn on the screen along with other sprites in the group.

<br>

### `self.image = frames[0]`

#### Setting the Initial Image:

- Here, we set the image attribute of the sprite to the first frame in the frames list. This will be the image displayed when the explosion animation starts.

```python
try:
    self.image = frames[0]

```
<br>
<br>

### 🟠 5. Importing the images

#### In the images folder, there is a subfolder called explosion that contains 20 images named from 1 to 20, all in PNG format.

<br>

### 🟩 You can create a list of the explosion image paths in two ways. Here’s the first method:



```python
# Load explosion images
explosion_frames = [i for i in range(21)] # Creates a list from 1 to 20
print(explosion_frames)
```
🔴 **Check your console:** you should see the numbers 1 through 20, confirming that the images are ready to be used!

#### output

```bash
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
```

<br>

#### 🟩 However, there’s another way that directly gives you the file paths for the images:

```python
from os.path import join

# Method 2: Create paths to the explosion images
explosion_frames = [join('images', 'explosion', f'{i}.png') for i in range(1, 21)]
print(explosion_frames)
```

### output

```python
['images/explosion/0.png', 'images/explosion/1.png', 'images/explosion/2.png', 'images/explosion/3.png', 'images/explosion/4.png', 'images/explosion/5.png', 'images/explosion/6.png', 'images/explosion/7.png', 'images/explosion/8.png', 'images/explosion/9.png', 'images/explosion/10.png', 'images/explosion/11.png', 'images/explosion/12.png', 'images/explosion/13.png', 'images/explosion/14.png', 'images/explosion/15.png', 'images/explosion/16.png', 'images/explosion/17.png', 'images/explosion/18.png', 'images/explosion/19.png', 'images/explosion/20.png']
```

<br>

### 🟫 Differences Explained


**Method 1:** This creates a list of numbers (`1 to 20`).

- - - It doesn't tell you where the images are located, **just their numbers**.

<br>

**Method 2:** This creates a list of complete **paths to the image files** (like `images/explosion/1.png`).

- - - It combines the folder names and the image numbers into a full path, which is very useful when you want to load the images later.

<br>
<br>



## 🟠 6.   <u>Loading Images into Pygame</u>

### 🔴 Path Considerations Based on Project Structure


#### 🟦 Teacher’s Structure:

```bash
Root Directory
audio
images
game
```


#### 🟦 My Structure:

```bash
PROJECTGAME (Root Directory)
audio
game
  |___main.py
images
  |___explosion
     |___0.png
        # and so on ...
```

<br>

## 🟫 Teachers structure  🟫 :

> ### In the previous code, you created a list of file paths to your explosion images.

- recap

```python
# Method 2: Create paths to the explosion images
explosion_frames = [join('images', 'explosion', f'{i}.png') for i in range(1, 21)]

```

#### output

```python
['images/explosion/0.png', 'images/explosion/1.png', # and SO ON...
```


 <br>

 ### Now, you’re going a step further by actually loading those images into Pygame so you can use them in your game.

```python
explosion_frames = [pygame.image.load(join('images', 'explosion', f'{i}.png')).convert_alpha() for i in range(1, 21)]
```

<br>

## 🟢  Explanation:

###  This line not only creates the file paths but also loads each image using `pygame.image.load()`.

**The `convert_alpha()` method is used to optimize the images** for Pygame, which improves performance and handles transparency correctly.

#### Now, `explosion_frames` ...

  **contains the actual image objects instead** of just their paths. This allows you to display the images in your game.

<br>

## 💡 Key Differences

**File Paths vs. Image Objects:**

- -  The first code creates paths, while the second code loads the images into memory.

<br>
<br>

## 🟫 My structure  🟫 :

### 🔴 Project Structure Differences


### In our project setups, the directory structures differ between the teacher’s example and my own.

### 🟡 This distinction is important to note:

>- - - #### if you follow the tutorial and use the teacher’s code, it may not work correctly if your structure resembles mine.

### Always be aware of how your directory is organized to ensure that the paths in your code are accurate.

#### My Structure:

```bash
PROJECTGAME (Root Directory)
audio
game
  |___main.py
images
  |___explosion
     |___0.png
        # and so on ...
```

### 🟡 Using a similar approach to how I imported the laser and meteor images.

```python
# Load explosion frames
explosion_frames = []


for i in range(21):
    path = os.path.join(script_dir, '..', 'images',
    'explosion', f'{i}.png')


    try:
        explosion_frames.append(pygame.image.load(path).convert_alpha())

    except pygame.error as e:
        print(f"Failed to load explosion image '{path}': {e}")
        # Optionally add a fallback surface if needed
        explosion_frames.append(pygame.Surface((50, 50)).fill((255, 0, 0)))  # Red square as fallback

print(explosion_frames)
```

## 🟨 After making this adjustment, you will notice in the console:

#### output

```python
[<Surface(50x50x32, global_alpha=255)>,
<Surface(50x50x32, global_alpha=255)>,
<Surface(50x50x32, global_alpha=255)>,
<Surface(50x50x32, global_alpha=255)>,
<Surface(50x50x32, global_alpha=255)>, # and so on ...
```

### 🔴  that instead of seeing the path `'images/explosion/0.png',` you will now see something like `[<Surface(50x50x32, global_alpha=255)>]`.

<br>

### 🟧🫐 Why the Output Shows "Surface"

#### This change occurs because when Pygame successfully loads an image, it returns a Surface object, which represents the image in memory.

> - - #### When you print this object, it displays the dimensions and properties of the surface instead of the file path.

### 🍭 In simpler terms, when you load an image, Pygame creates a Surface that contains the image data, and that’s what you see in the console.

---
<br>
<br>




## 🟦 Moving Forward:

#### [3:34:43](https://youtu.be/8OMghdHP-zs?si=jbUW6YJucPJfnI0k&t=12883)

### 🍭 Image Conversion

### 🟧 Now that we have successfully converted the images for our explosion animation, we can start using them in our game.

 -  ### To begin, we will select one image from our list of frames.

- - #### Specifically, we will take the `first image` in that list, which represents the initial frame of the explosion animation.

- This is done with the following line:

```python
 self.image = frames[0]
```
#### from the below class

- In our `AnimateExplosion` **class**, we **init**ialize the animation using the frames we have prepared.

```python
class AnimateExplosion(pygame.sprite.Sprite):
    def __init__(self, frames,pos, groups):
        super().__init__(groups)
        try:
            self.image = frames[0]
            # self.image = images['star']
        except KeyError:
            print("Star image not found in images dictionary.")

        self.rect = self.image.get_frect(center = pos)


```

<br>
<br>

## 🟠 7. Handling Collisions

### When the laser 🔫 hits a meteor 🪨

> ### When the laser collides with a meteor, we want to do two things:

- - - **Remove the laser from the game.**

- - - **Create one instance of the animated explosion.**

#### Here’s how to implement this in the collisions() method:

```python
if collided_sprites:
    laser.kill()  # This removes the laser sprite from the game
    AnimateExplosion()  # Create an explosion animation

```
>In this code, `laser.kill()` effectively destroys the laser sprite, and we call `AnimateExplosion()` to initiate the explosion.


<br>
<br>

## 🟠 8. Adding the Explosion Instance

### Next, we need to add the explosion frames and set its position.

> #### The position will be at the top of the laser, specifically using laser.rect.midtop, and the group will include all sprites:

```bash
AnimateExplosion(explosion_frames, laser.rect.midtop, all_sprites)
```
> #### This line of <u>code ensures that when the explosion occurs, it is positioned correctly at the top of the laser.</u>

- - The `all_sprites` **group** allows the explosion to be part of the overall game display.

<br>

## 🟤 Visualizing the Explosion

> **As you play the game and shoot a meteor**, you should see the smallest image in your explosion folder, which is 0.png. However, currently, you may not be able to see it.

<br>

[3:35:13](https://youtu.be/8OMghdHP-zs?si=Pp5wZJYk4Sh1-wZl&t=12913)

[<img src="../collision-meteor-explosion_firstimag-from-the-frames-list.gif"/>](https://youtu.be/8OMghdHP-zs?si=Pp5wZJYk4Sh1-wZl&t=12913)

<br>
<br>
<br>
