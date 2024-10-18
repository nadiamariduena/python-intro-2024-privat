
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

## 🟠 9. Creating an Animation for the Explosion

### Using Different Frames for Animation

To create an animation, we need to display different images from our collection of frames.

> #### Initially, we might set the image like this: so to create an animation , we should assign a different index from self.frames

```python
 self.image = frames[0]
```

>### However, using a fixed index like [0] means we will always show the first frame of the animation.

- - #### 🔴 This approach does not allow the animation to change or progress,

- - which is crucial for creating a dynamic and engaging visual effect.

> - -  #### 🔴   Instead, we want to change the index over time so that different frames are displayed in sequence, creating the illusion of movement.


<br>

### 🟧 Implementing the Update Method

### `update()`

#### To enable the animation to progress, we need to implement an `update()` method in the `AnimateExplosion()` class.

- This method will be responsible for updating the displayed frame at regular intervals.

- #### It will require two parameters: self (to refer to the instance of the class) and dt (which represents the time since the last update).

We define the `update()` method like this:



```python
def update(self, dt):
```
<br>

## 🟧 Updating the Current Frame

Inside the `update()` method, we will **assign a new image** to `self.image` **based on a frame index** that we will manage.

#### 🔴 This index will change over time to cycle through the frames.

For example, you might think of it like this:

```python
self.image = frames[index]
```
#### 🔴 However, we need to ensure that index updates correctly to show different frames rather than being stuck at a single value.

<br>

## 🟧 Storing All Frames

### <u>Before we can cycle through the frames</u> , we must store them in an attribute.

- **This allows us to easily access the frames** in the `update()` method.

> #### We do this by assigning the frames to an attribute like this:

```python
self.frames = frames
```

<br>


## 🟧 Keeping Track of the Current Frame Index

### To manage which frame we are currently displaying, we will create an attribute called `frame_index`.

- This will start at **zero**, **indicating** that **we begin with** the **first** frame:

```python
self.frame_index = 0
```

### Now we can combine these pieces to initialize the class properly:

```python
self.frames = frames
self.frame_index = 0
self.image = self.frames[self.frame_index]
```
### 🟤 Updating the Image Reference

**Next,** we need to replace the initial image assignment:

#### replace this:

```python
self.image = frames[0]
```

#### 🟤 For this:

```python
self.image = self.frames[self.frame_index]
```

#### 🟤 We should also make the same update in the update() method:

```python
def update(self, dt):
    self.image = self.frames[self.frame_index]
```

<br>

## 🌈 Final Structure of the AnimateExplosion Class

### The complete structure of the AnimateExplosion class would look like this:

```python
class AnimateExplosion(pygame.sprite.Sprite):
    def __init__(self, frames, pos, groups):
        super().__init__(groups)
        try:
            self.frames = frames  # Store the frames
            self.frame_index = 0  # Initialize frame index

            self.image = self.frames[self.frame_index]
            # Set the initial image
        except KeyError:
            print("Star image not found in images dictionary.")  # Handle error

        self.rect = self.image.get_frect(center=pos)
        # Set the position

    def update(self, dt):
        self.image = self.frames[self.frame_index]
        # Update the image based on the frame index

```
### Before

```python
class AnimateExplosion(pygame.sprite.Sprite):
    def __init__(self, frames,pos, groups):
        super().__init__(groups)
        try:
            self.frames = frames
            self.frame_index = 0
            self.image = frames[0] 🔴


        except KeyError:
            print("Star image not found in images dictionary.")

        self.rect = self.image.get_frect(center = pos)

    def update(self, dt):
        self.image = frames[index]

```


<br>
<br>

## 🟠 10. Updating the Frame Index

### Incrementing the Frame Index

### To make the animation progress, we want to change the `frame_index` each time the `update()` method runs.

- - One way to do this is by adding a value to `self.frame_index`.

#### For example, we might write:

```python
self.frame_index += 5 * dt

```
### This line attempts to increase the `frame_index` based on the time that has passed since the last update (represented by dt).

  🟤 <u>The idea is that as time passes</u>  , the index will increase, allowing different frames to be shown in the animation.

```python
    def update(self, dt):
        self.frame_index += 5 * dt
        self.image = self.frames[self.frame_index]
```

<br><br>

### 🔴  <u>Why This Approach Doesn’t Work?</u>

### The problem with this approach:

 `self.frame_index` must always be an integer. **This means it can only hold whole numbers (`like 0, 1, 2, etc`.), 🔴 not fractions or decimals.**

> ####   When we multiply `5 * dt`, we may end up with a decimal value.  For example, **if** `dt is 0.1`, **then `5 * dt` would equal 0.5**.

> #### 🔴 **If we add `0.5` to `self.frame_index`, it would turn into a non-integer value**, which is not allowed.

<br>

## 🫐 Current Code (Before Testing):

- Here is the current code for the `AnimateExplosion` class:

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

    def update(self, dt):
        self.frame_index += 5 * dt
        self.image = self.frames[self.frame_index]
```
### 🟧Output

###  If you execute the code, you will observe that the game halts and the screen closes as soon as we hit a meteor.

<br>


## 🌈 Solution



### Ensuring the Frame Index is an Integer `int`

 To ensure that `self.frame_index` remains an integer, we need to adjust how we increase it.

 <br>

 ##  `int()`

<!-- ###   🟨 One common approach is to use the `int() function` <u>to convert the result to an integer</u>

>#### This way, we can ensure that our frame index is always a valid integer, allowing our animation to work correctly. -->


### 🟨 A common method to ensure our frame index is a valid integer is by utilizing the int() function.

> #### By converting the result to an integer, we guarantee that our animation operates smoothly without any errors.

- To incorporate this into your code, you can modify it as follows:

```python
        # self.image = self.frames[self.frame_index]
        self.image = self.frames[int(self.frame_index)]
```

#### Here’s how the updated code looks in context:




```python
    def update(self, dt):
        self.frame_index += 5 * dt

        # self.image = self.frames[self.frame_index]
        self.image = self.frames[int(self.frame_index)]
```

<br>

### 🟩 Summary

#### In summary, while the idea of incrementing `self.frame_index` with `5 * dt` is a good start for controlling animation speed, we need to ensure that `self.frame_index` stays an integer.

<br>




## Observing the Behavior

> ### 🔺 Take a look at the image below. When we collide with a meteor, an explosion effect occurs, but shortly after, the game crashes.

[<img src="../collision-meteor-explosion_explosion_conitnous_anima.gif"/>]( )




## 🔴 Identifying the Issue

### The underlying problem is that the list index is out of range.

> #### This means that the code is trying to access a part of the list that doesn’t exist.

<br>


<br>

### 🟢 Breaking Down the Code

Specifically, the following **line is causing `frame_index` to increase indefinitely**:

```python
self.frame_index += 5 * dt
```

### 🔴 WHY?

####  As `frame_index` continues to grow, it eventually points to a `non-existent index in the list`, ✋which leads to the crash.

<br>


## 🟤 Let's see it on the console

- add this line **`print(self.frame_index)`** on the code below:

<br>

```python
    def update(self, dt):
        self.frame_index += 5 * dt


        # self.image = self.frames[self.frame_index]
        self.image = self.frames[int(self.frame_index)]
        print(self.frame_index)

```
<br>

### 🟣 Console Output Observations

 floating-point numbers are typical in Python due to how it handles decimal values, and while they might seem unusual, they are generally not problematic unless they affect the logic or visuals of your project.

#### This created a stream of numbers in the following format:

```python
1.1500000000000004
20.904999999999884
6.199999999999996
1.1750000000000003
20.934999999999885
6.229999999999996
1.2050000000000003
20.979999999999887
6.274999999999996
1.2500000000000002

```

### 🔴 b) Game Crash Details

- the real issue

> ####  The game crashed a few seconds later, even when no meteor had hit the player.


#### the err :

```python
Traceback (most recent call last):
  File "main.py", line 389, in <module>
    all_sprites.update(dt)
  File "/0_SPACESHIP-game/game/.venv/lib/python3.6/site-packages/pygame/sprite.py", line 556, in update
    sprite.update(*args, **kwargs)
  File "main.py", line 274, in update
    self.image = self.frames[int(self.frame_index)]
IndexError: list index out of range

```



#### 🔴 This error means the program tried to access an index in a list that doesn’t exist.

<br>


[<img src="../explosion-anima__problem_is_that_the_list_index_is_out_of_range.gif"/>]( )






## 🌈 Solution:

<a name="modulo_operator_"></a>

### To resolve the issue, we can use the *modulo* `%` operator in conjunction with the `length` of `self.frames`.

This is how it works:

```python
        self.image = self.frames[int(self.frame_index) % len(self.frames)]
```


[<img src="../explosion_anima__solved_with_modulo-operator.gif"/>]( )


---

<br>
<br>
<br>



### 🟣Why Use the Modulo Operator?

<a name="WHY_use_modulor_operator_"></a>

#### 🌈 [MODULO operator ](../a__about_MODULO-operator.md)





### 🟠 1. Preventing Index Out of Range

As `frame_index increases` (like counting up), it can sometimes go beyond the number of frames available in our list.

<br>

> #### For instance, if we have a list of 5 frames, they are indexed from 0 to 4.

**Example:**

- - 🟤  **If `frame_index` becomes 6, that’s an invalid index** <u>because there is no frame</u>  **6**.

- #### Using the `modulo` operator helps us avoid this problem.


- #### When we apply the modulo operation like this:

```python
index = frame_index % len(self.frames)
```

#### If `frame_index` is 6, and `len(self.frames)` is 5, we calculate:

```python

6 % 5 = 1
```
#### 🟢 This means the index wraps around to 1, which is a valid position in the list.

<br>

### 🟠 2. Continuous Animation

#### Using the modulo operator allows the animation to keep going smoothly without crashing.

<br>

> #### Instead of stopping the game when `frame_index` is too high, it loops back to the start of the list.

<br>

**Example:**

- - 🌟 If `self.frames` has 10 frames, they are indexed from 0 to 9.

#### If `frame_index` becomes 10, we calculate:

```python
10 % 10 = 0
```
---

<br>
<br>
<br>

## 🟦 Moving Forward:

## 🟠 11. Control the Meteor Explosion Animation:

<br>

### Overview of the Current Situation:

- The explosion animation is currently set to loop indefinitely due to the following line of code:

```python
      self.image = self.frames[int(self.frame_index) % len(self.frames)]
```

## 🔴 Why This Is a Problem:

#### While continuous animations can create a sense of persistence, they can detract from gameplay by making it feel stagnant or unresponsive.

> - ### In this case, once the explosion starts, it never stops, which is not the intended effect.

<br>

## 🔴 Why We No Longer Use the `Modulo` Operator:

> it's the use of the modulo operator that causes the animation to loop infinitely.

>#### The `modulo operator (%)` is typically used to loop through a list of frames by wrapping around when the index exceeds the number of frames.

#### In the context of an explosion animation, this means once the last frame is reached, it jumps back to the first frame without stopping, <u>resulting in a never-ending cycle</u> .

 <br>

## 🌈 Solution

### Controlling the Looping Explosion Animation with Conditionals

<br>

- - 🔴 To solve the issue of the looping explosion animation, we can implement a conditional structure.

This approach will allow us to start and stop the explosion based on player interactions, ensuring a more dynamic gameplay experience.

<br>

## 🟦 Moving Forward:


###     Explanation of the Conditional:

#### 🟤  Define a Trigger Condition:

> #### We need to establish `when the explosion should start and when it should stop`.

-  - #### This could be based on the frame index reaching the end of the explosion frames.

<br>

- #### replace the below line:

```python
self.image = self.frames[int(self.frame_index) % len(self.frames)]
```
- #### for the conditional:

```python
if self.frame_index < len(self.frames):
    self.image = self.frames[int(self.frame_index)]
else:
    self.kill()  # Stop the explosion animation
```


### Explanation of the Code:

🟫 1. `if self.frame_index < len(self.frames):`

#### This conditional checks if `self.frame_index` is less than the total number of frames. `If true`, it updates `self.image` to the current frame.

<br>

🟫 2. `self.image = self.frames[int(self.frame_index)]`

<br>

> - - #### 🔴 If `self.frame_index` is equal to or exceeds the number of frames, the explosion animation ends by calling self.kill(), which removes the explosion object from the game.

🟫 3. `self.kill() `

<br>
<br>

### Current code

```python
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



```

### Output

[<img src="../explosion_anima__solved_with_modulo-operator.gif"/>]( )

### code

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
        self.cooldown_duration = 400

    def laser_timer(self):
        if not self.can_shoot:

            current_time = pygame.time.get_ticks()
            # print(current_time)
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True

    def update(self, dt):
        keys = pygame.key.get_pressed()

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

    def update(self, dt):
        self.frame_index += 5 * dt


        # NO: self.image = self.frames[self.frame_index]
        # ALSO NO: self.image = self.frames[int(self.frame_index)]
        print(self.frame_index)

        if self.frame_index < len(self.frames):
            self.image = self.frames[int(self.frame_index)]
        else:
            self.kill()




# 💥 🪨 METEOR & LASER collitions LOGIC

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
            AnimateExplosion(explosion_frames, laser.rect.midtop,all_sprites)

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


---

<br>
<br>

### Next step: Sounds