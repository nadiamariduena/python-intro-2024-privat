
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



 ### 🟤 Parameters: (self, surf, pos, groups)


 These parameters will help us **specify** the meteor's **surface, position**, and the **sprite group it belongs** to.

 ```python
 #🪨 METEOR
 class Meteor(pygame.sprite.Sprite):
     def __init__(self, surf, pos, groups):
         super().__init__(groups)

         try:
             self.image = surf
 ```
 <br>
 <br>

 <br>

 ---

 ### ⚫ RECAP:

 ### 🍭 self:

 This refers to the current instance of the Player class.

 > - - ####  When you call `Laser(laser_surf, self.rect.midtop, all_sprites)`, self is implicitly passed when invoking methods from the Player instance.

 <br>


 ### 🍭 surf 🖼️

 This corresponds to laser_surf, which is the surface you want the Laser to use.

 > - - #### 🌞 It’s the image that you’ve loaded for the laser.


 <br>

 ### 🍭 pos:

 This is `self.rect.midtop`, which provides the position where the laser will be created.

 >  - - #### It uses the player’s current position (specifically the midpoint of the top edge of the player’s rectangle).


 <br>

 ### 🍭 groups:

 > - - #### This refers to all_sprites, which is the group you want the laser instance to be added to.

 - - This allows the laser to be part of the sprite management system for updates and drawing.


 <br>

 ### 🍭 pos:

 This is `self.rect.midtop`, which provides the position where the laser will be created.

 >  - - #### It uses the player’s current position (specifically the midpoint of the top edge of the player’s rectangle).


 <br>

 ### 🍭 groups:

 > - - #### This refers to all_sprites, which is the group you want the laser instance to be added to.

 - - This allows the laser to be part of the sprite management system for updates and drawing.

 ---

<br>
<br>
<br>

## 🟦 Moving Forward:

## 🟧 4.  Set the Image and Position

In this step, we set the**meteor's image** using the provided surface.

- - If the image **isn’t found, we create a fallback** surface. We also define the **position** of the meteor using its rectangle.

```python
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
```


<br>
<br>
<br>

<a name="event_meteor_1_"></a>

## 🟧 5. Handle Meteor Events



### In this step, we listen for events in the game `loop`.

- - #### 🏁 When a `meteor_event` is triggered, we create a new `Meteor` instance using `meteor_surf`, specifying its position and adding it to the sprite group.

> #### This step is crucial for bringing meteors into the game, allowing them to appear on the screen.

```python
# 🧶 GAME LOOP ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # METEOR event ----
        if event.type == meteor_event:
            # print('create meteor 🪨')
            Meteor(meteor_surf, (400,500),all_sprites)


```

<br>

## 🟧 6. Test It Out!

After implementing **step 4**, run the game to see the meteors appear on the screen.

> #### You should now see the meteor in action!

[<img src="../meteor_1_class.gif"/>]()



<br>
<br>


## 🟧 7. Customize the Meteor Position

### 🟤 Define the Position Coordinates

To position the meteor accurately, we need to customize the **coordinates:**

```python
(400,500)
```


### 🟤   X and Y Coordinates

The coordinates correspond to the X and Y positions on the screen:

```python
# x
randint(0, WINDOW_WIDTH),
#y
randint(0, WINDOW_HEIGHT)
```
<br>

### 🟤  Randomize the Position
We can generate random X and Y values like this:

```python
x, y = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)
```

<br>

### 🟤  Update Meteor Creation

> #### Now, let’s replace the hardcoded position with our randomized values

```python
# BEFORE

            Meteor(meteor_surf, (400,500),all_sprites)

# AFTER --------

            Meteor(meteor_surf, (x, y),all_sprites)
```
[<img src="../meteor_2_class.gif"/>]()

<br>


> ### 🟧 Update the event handling to create meteors at random positions:

```python
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        # --------- METEOR ----------
        if event.type == meteor_event:
            # print('create meteor 🪨')
            x, y = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)
            Meteor(meteor_surf, (x,y),all_sprites)
```


[<img src="../meteor_3_class.gif"/>]()

<br>
<br>

## 🟧 8.  Animate the Meteor

### To animate the meteor, we’ll add an update() function to the Meteor class, similar to what we did for the laser:



```python
class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        # .. more code here (related to the init)

    def update(self, dt):
```
<br>
<br>

## 🟧 9. Make the meteors move 👾

#### Now, let’s implement the movement logic inside the update() method:

```python
    def update(self, dt):
        self.rect.centery += 400 * dt
```

#### This code moves an object vertically (up or down) on the screen.

- - `self.rect.centery` is the **center** of the object.

- - `400 * dt` makes the **object move 400 pixels** per **second**.


- - `dt` **adjusts the movement** based on how fast the game is running.

> #### This ensures smooth, consistent movement regardless of frame rate.

<br>
<br>
<br>


## 🟦 Moving Forward:

### 🟧 10. Right now, when we create a meteor, it appears at a random position within the entire window. For example:

```python
x, y = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)
```

> #### 👎 This means the user can see the meteor immediately as it appears in a visible area of the screen.





<br>
<br>

## 🟧 11. Adjusting the Y Position



#### 🟤 This means the user can see the meteor immediately as it appears in a visible area of the screen.

> ### To avoid that, we want to create the meteors above the visible area of the screen.

> - - #### 🟢 Specifically, we want them to start from a random position at the top, which means `adjusting the Y coordinate` to be a `bit higher than the window's top edge`.

- In other words, we want to be in a position `randomly` **between -200 & -100**

```python
x, y = randint(0, WINDOW_WIDTH), randint(-200, -100)
```

<br>

### 🟩 Output


[<img src="../start_METEOR_from_a__random_pos_at_the_top.gif"/>]()

<br>

### 🔴 Understanding the `Position Values` By setting the `Y position randomly` between `-200 and -100`, we achieve the following:


```python


                |                    |   <-- Meteor Spawn Area

                                         <-- (Y = -200)

                |                    |   (Y = -500)
                |                    |
                |                    |   <-- (Y = -100)
                |                    |
                |                    |
                |                    |
                |                    |
                |                    |
                +--------------------+   <-- Visible Area (Y = 0)
                |                    |
                |                    |
                |                    |
                +--------------------+
```

<br>





### 🟤 `-200`: the meteor can start as high as 200 pixels above the top of the window.

- - - When it **begins** up here, it’s completely **hidden from view**. This way, players have a moment to see the meteor as it starts to fall down.

### 🟤 `-100`: This number is the highest point where the meteor can start.

---

<br>
<br>
<br>
<br>

## 🟧 12. CUSTOMIZE the 🪨 meteor class

[2:32:42](https://youtu.be/8OMghdHP-zs?si=1-IlXIXDaRiQOLef&t=9162)



### In this customization, we want to do two things:

#### 🟢 1.  Destroy Every Meteor Sprite

>  We want each meteor sprite to disappear after 2 seconds.

> - - #### This way, they vanish before they reach the bottom of the screen.

> - - #### To do this, we’ll add the following line:

- **Destroy every  meteor** sprite **after 2 seconds** (we want the rocks to vanish before they reach the edge of the bottom of the screen), we will be doing it by adding the below line:



#### 🟤 Timer

- First, we need to set up the timer:

```python
# This line tells us when the TIMER should start
self.start_time = pygame.time.get_ticks()
```

<br>

### 🟠 Explanation:

-  - **Here**, `pygame.time.get_ticks()` gives us the current time in milliseconds since the game started.

> - - #### By saving this time in self.start_time, we can track how long the meteor has been alive.

<br>

### 🟤 Lifetime

- **Defining Lifetime:** Next, we set how long the meteor should live before it disappears.

```python
self.lifetime = 2000
```
<br>

> #### 🟠 Explanation:

This line means the meteor will last for 2000 milliseconds, or 2 seconds.

> #### This connects to our timer because it tells us how long we should wait before the meteor is removed.


### 🟦 Putting It All Together


```python
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

        # Timer 🟡
        self.start_time = pygame.time.get_ticks()
        # duration
        self.lifetime = 2000
```


### 🔴 Conditional

### 🟧 Update Function:

- Now, we’ll add a conditional statement in the update function to check if the meteor should disappear.

```python
    if pygame.time.get_ticks() - self.start_time >= self.lifetime:
        self.kill()
```


###  🟤 Explanation:

- This line **checks** `if` the `current time` **minus** the time when the meteor started (`self.start_time`) is greater than or equal to `self.lifetime`.



### 🟤 Understanding Each Part:

- - - `pygame.time.get_ticks()`: This part gives us the current time in milliseconds (like counting how many seconds have gone by since the game started).

- - - `self.start_time`: This is the time when the meteor was created. We saved it earlier, so we know when it started.

- -  - `self.lifetime`: This is the time we set for how long we want the meteor to live (in our case, 2000 milliseconds, or 2 seconds).

<br>

- - **If it is**, we use `self.kill()` **to remove the meteor**.

> #### 🌈 It’s like saying, “If 2 seconds have passed since the meteor was created, make it disappear!”



<br>

### 🔴 Why Is This Important?

#### This code helps control how long things stay in the game.

- - - It’s like having rules in a game: if you follow them, everything works smoothly!

<br>
<br>

### 🟦 Putting It All Together


```python
    def update(self, dt):
        self.rect.centery += 400 * dt
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()

```
<br>

### Output

[<img src="../start_METEOR_from_a__random_pos_at_the_top_2.gif"/>]()


<br>
<br>
<br>

## 🟧 13. Giving Meteors a Direction

### 🟤 Right Now:

- #### the meteors are moving in a straight line down the screen (watch the above img).

> - - ####  This can get a bit boring because they all follow the same path.


<br>

### 🟤 What We Want to Do?:

####  <u> We want each meteor to move in a different direction! </u>

- This will make the game more exciting and fun to play.



### 🟤 How We Do It:

- - #### To give each meteor its own direction, we’ll use `pygame.Vector2()`.

- - This tool is perfect for defining movement because it allows us to represent both the direction and speed of the meteor as a single object.

```python
pygame.Vector2(x, y)
```



<br>
<br>
<br>

---

## ⚫ Recap `Vector2()`:


### What is `pygame.Vector2()`?

### 🟧 `pygame.Vector2(x, y)`: This function creates a vector, which is like an <u>arrow that points in a specific direction</u> .

- `x` is how far to the side (left or right).

- `y` is how far up or down.


### 🌈 🟡 For example:

- - - If we use `pygame.Vector2(1, 0)`, the meteor will move to the right.

- - - If we use `pygame.Vector2(0, 1)`, the meteor will move down.

- -  - If we use `pygame.Vector2(1, 1)`, it will move diagonally down and to the right!

---

<br>
<br>
<br>


## 🟧 14. `uniform`

### `uniform` function to generate a random floating-point number for the `X` direction

- -  ### Now that `we have established a direction for our meteors` using `pygame.Vector2(x, 1)`, <u>we need to make the X value dynamic</u>.

<br>

- - 🌈 To achieve this, we’ll use the uniform function to generate a random floating-point number for the X direction.

<br>

>   #### 🌈 This will allow each meteor to have a unique horizontal movement, enhancing the game’s excitement and unpredictability.
