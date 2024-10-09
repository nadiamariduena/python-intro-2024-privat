
# 🟡 SPRITES 5.

<br>

### Intro


- - What **We’ll Be Doing:** [Go to section](#What_We_will_Be_Doing_)



<!--


#### 🟨 create the meteor class

- - create the meteor class [Go to section](#create_class_)


- - -  #### 🟨 create the event

- - - - create the event to make the meteor appear [Go to section](#event_meteor_1_)

<br>


 -->


<br>
<br>
<br>
<br>

---

<br>


# 🟡 What We will Be Doing

<a name="What_We_will_Be_Doing_"></a>


## 🫐 🟡 Adding Meteor Rains to Our Space Shooter

### In this lesson, we will be focusing on adding meteors to our space shooter game.

> -  ### Specifically, we will set up a system where meteors fall from the top of the screen, <u>creating obstacles for the player to avoid</u> 💥.

<br>

### 🟤 This will involve using Python's random module, specifically the `range() and uniform()` functions, to control the position and speed of the meteors as they appear and move downwards.

<br>

## 🟡 NEXT

###  After completing this lesson, we'll also be ready to tackle meteor collisions!

- You'll learn how to detect when a meteor hits the player’s spaceship and how to handle those collisions (either) by taking damage or ending the game.

---

<br>
<br>
<br>
<br>
<br>



# 🟦 Let's Start:


## 🟡 Steps to Implement the *Key* LOGIC


<a name="create_class_"></a>


<br>

### 🟧 1. Create the 🪨METEOR  class

```python
class Meteor(pygame.sprite.Sprite):
```

### 🟧 2.  Now Create a Meteor for Every Meteor event

Here, we set up the `constructor` for the **Meteor** class.

- In the next step We’ll pass all necessary **parameters** to define the meteor's behavior and appearance.

```python
class Meteor(pygame.sprite.Sprite):
    def __init__(self, )
```


<br>

### 🟧 3. Pass all the parameters



> 🟢 **Read more** about the **parameters**: `(self, surf, pos, groups)`





<br>


