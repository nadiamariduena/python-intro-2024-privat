
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
