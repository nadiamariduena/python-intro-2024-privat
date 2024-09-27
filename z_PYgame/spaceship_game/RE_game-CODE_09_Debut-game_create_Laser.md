
# 🟡 SPRITES 4.

<br>

### Intro


- - What **We’ll Be Doing:** [Go to section](#What_We_will_Be_Doing_)



<br>
<br>


<br>
<br>
<br>
<br>
<br>

---









<br>



<a name="What_We_will_Be_Doing_"></a>

# 🟡 What We will Be Doing

###    Now that our `Player` and `Star` Classes are in place, we’re ready to level up our game  with `two key mechanics that Depend on timing`:



<br>

> - - #### 💥 Laser cooldowns



> - - #### 🪨 meteor generating


---

<br>
 <br>





# 🟡 Steps to Implement the Key Mechanics

<br>

## 🟩 1. Laser Cooldown logic


> - - #### 🔫 Just like any high-tech weapon, it can’t fire continuously without overheating.

> - - #### 🧊 After each shot, we’ll enforce a brief cooldown period before it can fire again 🥶.

<br>

- - ###  🎯 Effective Timing Strategies

- - **Timing is Key:** Utilize Pygame’s timing functions to synchronize meteor spawns and manage laser cooldowns effectively.

> -  - - Mastering shot timing becomes essential as you fend off meteors while monitoring your laser’s firing rate.



> - -  -    We'll make sure meteors appear at the right moment  and   control how often the laser can shoot.









##  🟩 2. Meteor Spawning System


- -    we’re going to **implement a meteor** spawning **system** that **creates new meteors** at regular intervals.

> - -  ####   We’ll use Pygame’s timing functions to control the spawn rate—this means every few seconds, a meteor will appear on the screen, adding intensity to your gameplay.

> - - This **Laser Class** will define the laser's properties, including its appearance, movement, and interactions with other game elements.









---

<br>
<br>
<br>
<br>

#### [2:14:14](https://youtu.be/8OMghdHP-zs?si=3rY3VNpwAeH26EiE&t=8054)

<br>

## 🟦 Moving Forward:

<br>

# 🟡  Timing Techniques

### As we continue to build our game, we need to manage time effectively.


#### We’ll be using time in two main ways:

- Spawn a meteor every X seconds 🪨

- Implement a cooldown for the laser 💥

> #### These two tasks will require different approaches, so let’s dive into each one!



<br>




## 🟡 Different Approaches for Different Tasks

### 🟢 1.   Meteors:

- - To generate meteors at regular intervals, we need a timer that ticks every X seconds.



### Here’s how to set it up:



### 🟫 Create an Event:

<br>

**Define a Meteor Event:** This event will signal when it's time to create a meteor.

**🟤 Set a Timer:** Establish a countdown timer that triggers the meteor event at the specified interval.
<br>

#### 🟫 Capture the Event:

- - ✋ In the event loop of your game, we’ll listen for this meteor event and generate a new meteor whenever it occurs.

<br>



##  🟢  2. Laser:


### 🔴 For the laser 🧊 cooldown, we’ll need a different type of timer:

<br>

#### Short Duration Timer:

- - This timer will activate briefly each time the laser fires, creating a short cooldown period.

#### Get a Starting Point  :

- - When the laser is fired, record the current time. 🔺 This will be our starting point.


#### Measure Time Passed  :

- - To check if the laser can fire again, measure the time that has passed since that starting point.

> #### Ensure it meets the cooldown requirement before allowing another shot.




<br>
<br>
<br>

---


# 🫐 🟡 Creating an <u>Interval Timer</u>



### Set Up Your Event:

- - Start by defining an event that we’ll
trigger for spawning/generating meteors.


### Initialize the Timer:

- - Use `pygame.time.set_timer(event, milliseconds)` to set up your timer. This will allow your event to fire every X seconds.


<br>

## 🟧 Custom `Timer` with `Pygame`

#### 🟢 Pygame has a <u>useful feature</u>  that tracks the time since your game started.



### Here’s how to leverage it:

<br>

#### 🔶 Capture Game Time:

- - #### Use `pygame.time.get_ticks()` to retrieve the total milliseconds since the game began.

> #### This will help you create a custom timer that you can use for your laser cooldown.

<br>

#### 🔶 Implement the Cooldown Logic:

- - When the laser is fired, record the current time.

- - - When checking if the laser can fire again, compare the current time to the recorded time to see if enough time has passed.



<br>
<br>

## Steps

## 🟧 1. Create the timer event

#### The below two lines, set up a mechanism to regularly create or manage "meteor" events in your game loop, helping to control game dynamics over time.

```python
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)
```



#### 🟤 `meteor_event = pygame.event.custom_type():`

This line creates a new custom event in Pygame, which is assigned to the variable `meteor_event`.

 <br>

 #### 🟤 `pygame.time.set_timer(meteor_event, 500)`:

 This line **sets a timer** for the custom **event** defined in the previous line.

 - - The **timer will trigger** the `meteor_event` **every 500 milliseconds (or half a second)**.

- - This is **useful for creating** regular occurrences in your game, like spawning meteors or other actions at fixed intervals.



```python
# CUSTOM EVENTS /timer
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)


running = True
while running:
```

>##### recap: `Pygame` has a built-in system for handling events (like key presses, mouse movements, etc.), and this allows you to define your own events that can be triggered at specific times or conditions in your game.



##  Now add it to the loop:

### 🟧 Integrating  <u>Custom Events</u>: `Creating Meteors`


### `if event.type == meteor_event:`

- -  This line **checks if the current event being processed is the custom `meteor_event`** that we defined earlier.

- - **If it is**, the code executes the print statement, indicating that a meteor should be created.

```python

        if event.type == meteor_event:
            print('create meteor 🪨')
```




### 🟧 2. add it within the `while` loop

```python
running = True
while running:
    dt = clock.tick() / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            print('create meteor 🪨')
```
<br>

### 🟢 How It Contributes to the Event System

#### Linking Events to Actions:

- - **By adding this line within the event loop**, we create a direct link between the timer set for `meteor_event` and the action of creating a meteor. Every time the timer triggers, the game recognizes it as an event and responds accordingly.




<br>

### 🟩 In the video, you may have noticed that the console shows "create meteor 🪨" printed continuously during the game.

- - ✋ **This behavior occurs** because the `meteor_event` is being **triggered repeatedly at every frame, not just once every 500** milliseconds.

<br>

### 🟩 Why This Happens?

> #### The below line is placed inside the `event loop`, which <u>runs for every event Pygame detects</u> .

<br>

- -  **Since `pygame.time.set_timer(meteor_event, 500)` sends a new `meteor_event` every `500` milliseconds**, it **gets processed every time** the **event loop iterates** and **finds it**.

```python
if event.type == meteor_event:
    print('create meteor 🪨')
```
<br>
<br>

## 🟧 What You Should Do?

### To manage meteor creation properly:

🟤 **Ensure Controlled Frequency:**

 -  🔺 You may want to **limit the creation to once per timer event**.

> - - - #### This way, it doesn't flood the console every frame.

<br>

🟤 **Implement a Meteor Spawn Function:**

 -  **Instead of just printing** to the **console, you can replace that line with actual code that spawns a meteor in your game**.

<br>
<br>

## Laser 🚀

### 🟦 Enhancing Laser Functionality

In our `Player` **class**, specifically in the `update()` **function**, we currently have this line of code:

```python
        recent_keys = pygame.key.get_pressed()
        if recent_keys[pygame.K_SPACE]:
            print('fire laser')
```

### 🟦 to Test it, temporarily hide our debugging line for meteor creation::

```python
 # loop
        if event.type == meteor_event:
            print('create meteor 🪨')
```
#### 🎋 🐦‍⬛ Observing the Behavior

When you press the `SPACE key`, you'll notice that the console displays **print('fire laser')** for every single tap.

> - - #### This means your player is `firing lasers as fast` as you can press the key!

> - - 🔺 While this may seem correct, it’s not quite how we want our game to function.

<br>

> - - #### 👾 There should be some KIND of delay between different  laser shots, one thing we can do, is to create a timer inside the Player class.

<br>
<br>


### 🟦 💥 Delay between different  laser shots:

To create a more balanced game play experience, we need to introduce a delay between laser shots.

> - - #### This will give each shot some weight and prevent the player from spamming the fire button.





[2:17:43](https://youtu.be/8OMghdHP-zs?si=HE6UH-f8_j_fne-L&t=8263)


---

<br>
<br>
<br>
<br>

## 🟦 Moving Forward:

## 🟡 Create a timer inside the `Player` class

> - - #### Implement a timer in the Player class to control how frequently the player can shoot lasers.

>- - - - #### 🦩 This will ensure a more strategic and enjoyable game experience by preventing rapid, uncontrolled firing.

<br>
<br>

### 🟤 Step 1: Setting Up the Timer

#### Inside the Player class, add the following lines:

```python
        # 🥶 cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400
        # -------------
```

## Explanation of Each Line:

#### 🔶 `self.can_shoot = True:`

-  - This boolean variable controls whether the player can shoot.

> - - #### By default, it's set to True, meaning the player can shoot lasers initially.


#### 🔶 `self.laser_shoot_time = 0`:

- - This variable will keep track of the time since the last laser was fired. It starts at 0 milliseconds.

#### 🔶 `self.cooldown_duration = 400`:

- - This sets the cooldown period to `400 milliseconds`.

> - - #### 🔴  After firing a laser, the <u>player must wait  this amount of time before they can shoot again</u> .

<br>
<br>
<br>
<br>

## 🟦 Moving Forward:

## 🟡 Integrating the Timer in the `update()` Function

#### Now, let’s modify the  `shooting condition` within the `update()` function.

- -  The below is what we currently have:

```python
# --------- CURRENT CODE -------
        recent_keys = pygame.key.get_pressed()
        if recent_keys[pygame.K_SPACE]:
            print('fire laser')
```

<br>
<br>
<br>

## 🥥 🔫  Let's Begin!

### 🟦 Conditional Firing:Shoot When Permitted:

#### In the `Player` Class, within the  <u>update()</u>  function, enhance the condition `if recent_keys[pygame.K_SPACE]` by appending and `self.can_shoot`: to it.

```python
        recent_keys = pygame.key.get_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            print('fire laser')
```



## Explanation

### 🔴  `self.can_shoot`:

> - - ###  This additional condition **ensures that the laser only fires 🔫 if** `self.can_shoot` is **True**.

  - - #### 👾  If the player tries to shoot during the cooldown period, this condition will 👾  prevent the laser from firing.


<br>
<br>
<br>


## 🟡 Implementing the 🧊 Cooldown Logic

- **Next**, we need to set `self.can_shoot` to **False** when the player fires a laser 🔫.

```python
        recent_keys = pygame.key.get_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            print('fire laser')
            self.can_shoot = False
```
<br>

## Explanation:

###   `self.can_shoot = False`:

  This line **changes** the shooting **status to** `False` **as soon as the player fires**.

> ### 🛑 It means the player cannot shoot again until the cooldown duration has passed.

<br>
<br>

---

##   🏁 Remember:

### As we mentioned previously:



#### 🔶 `self.laser_shoot_time = 0`:

- - This variable will keep track of the time since the last laser was fired. It starts at 0 milliseconds.

#### 🔶 `self.cooldown_duration = 400`:

- - This sets the cooldown period to `400 milliseconds`.

> - - #### 🔴  After firing a laser, the <u>player must wait  this amount of time before they can shoot again</u> .

---

<br>
<br>



## 🟨 Next Steps

### `self.laser_shoot_time`

In the upcoming steps, we will utilize `self.laser_shoot_time` to **check if** the **cooldown** duration has elapsed, allowing the player to shoot again.

<br>

### 🟤 Step 1: Create the Timer Function

- - Create a new function within the `Player` class and name it `laser_timer`.


```python
    def laser_timer(self):
```

### 🟤 Step 2: Implementing the Function

- - Add the following code to define the function:

```python
def laser_timer(self):
    if not self.can_shoot:
        current_time = pygame.time.get_ticks()
        print(current_time)

```
### 🟤 Step 3: Call the Function

Now, call this function inside the update() method:

```python
self.laser_timer()
```

### 🟤 Step 4: Placement of the Function

- - The `laser_timer` function should be positioned at the top of the update() function.

#### Here’s how your structure should look:

```python
class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        try:

            self.image = images['player']
        except KeyError:
            print("Player image not found in images dictionary.")

            self.image = pygame.Surface((50, 50))
            self.image.fill((0, 56, 175 ))

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
            print(current_time)


    # UPDATE -----------
    def update(self, dt):
        keys = pygame.key.get_pressed()

        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])


        self.direction = self.direction.normalize() if self.direction else self.direction



        self.rect.center += self.direction * self.speed * dt

        recent_keys = pygame.key.get_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            print('fire laser')
            self.can_shoot = False

        # CALLING
        self.laser_timer()

#---------
class Star(pygame.sprite.Sprite):
```

<br>

## 🟢  Explanation



### `laser_timer`

- - checks if the player is currently in a cooldown state (self.can_shoot is False).



### `pygame.time.get_ticks()`:

- - This function retrieves the current time in milliseconds since Pygame was initialized.

<br>
<br>
<br>

## 🟡 Marking the Moment of the Last Laser Shot

- This line **updates the `self.laser_shoot_time` variable with the current time in milliseconds since** Pygame was initialized, captured by `pygame.time.get_ticks().`


<br>

```python
self.laser_shoot_time = pygame.time.get_ticks()
```


<br>

## 🟢 Explanation of Its Functionality

### 🟧 Tracking the Last Shot Time:

- - By setting `self.laser_shoot_time` to the current ticks, this variable will now represent the exact moment when the player last fired a laser.

> ### This is crucial for managing the cooldown period effectively.

<br>

### 🟧 Enabling Cooldown Logic:

In subsequent logic (likely in the `laser_timer` function), you will compare `current_time` (obtained during the cooldown check) to `self.laser_shoot_time`.

🔴 This comparison will help **determine whether enough time** has **passed since the last** shot, **allowing you to reset `self.can_shoot` to `True` when the cooldown period has elapsed**.



<br>


```python
# WITHIN the Payer Class, update() function
if recent_keys[pygame.K_SPACE] and self.can_shoot:
            print('fire laser')
            self.can_shoot = False


            self.laser_shoot_time = pygame.time.get_ticks()

        self.laser_timer()

#---------
class Star(pygame.sprite.Sprite):python
```

<br>
<br>
<br>


<br>

## 🟡 Laser Fire logic Explained

### 🍭 Single Trigger Logic vs. Ongoing Timer



 #### 🟤 Note:

 - `if` Statement Allows **One-Time Triggering** for Laser Fire

 ```python

        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            print('fire laser')
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()

        # Call the Laser_timer function from line 74
        self.laser_timer()
```


### 🟤 However this code below is running continuously


```python

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            print(current_time)
```

<br>
<br>
<br>

---


### 🟣 How do the two pieces of code behave differently, even though they are both inside the `update()` function?

#### 🟣 <u>why they differentiate in behavior?</u>

<br>


## 🟫 Why the Difference?



## 🟨 One-time Trigger vs. Continuous Check:

- - 🔶 **The first block** of code (the laser firing) only runs when you press **SPACE** and can shoot.

```python
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            print('fire laser')
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()

        # Call the Laser_timer function from line 74
        self.laser_timer()
```

- - 🔶 **In contrast**, the `laser_timer` function keeps running as long as the game is updating, checking the shooting state each frame.

```python
  def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            print(current_time)
```




## 🟨 Event vs. State:

- - 🟤 Firing lasers is an event (it happens once when you press a button),

- - while the timer is checking a state (it keeps checking if shooting is allowed or not).



### 🌈 Summary

> #### 🔫 So, in short, the laser firing happens once per key press, while the laser timer runs continuously to monitor the cooldown state.

```python
class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        try:

            self.image = images['player']
        except KeyError:
            print("Player image not found in images dictionary.")

            self.image = pygame.Surface((50, 50))
            self.image.fill((0, 56, 175 ))

        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        self.direction = pygame.Vector2()
        self.speed = 300

        # 🥶 cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400


    # 🟡
    def laser_timer(self):
        if not self.can_shoot:
            # 🟡
            current_time = pygame.time.get_ticks()
            print(current_time)

    # 🟡
    def update(self, dt):
        keys = pygame.key.get_pressed()

        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

        self.direction = self.direction.normalize() if self.direction else self.direction

        self.rect.center += self.direction * self.speed * dt

        recent_keys = pygame.key.get_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            print('fire laser')
            self.can_shoot = False

            # 🟡
            self.laser_shoot_time = pygame.time.get_ticks()

        # Call the Laser_timer function from line 74
        self.laser_timer()

```

> ###   This difference allows your game to have responsive controls while still managing the shooting logic effectively!

---

<br>

<br>
<br>
<br>
<br>




## 🟦 Moving Forward:

## 🟡 Resetting the Shot: The Cooldown Logic

<br>

### 🟤 Step 1. Add the below lines within the `laser_timer` function:

```python
     if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True
```
<br>

### 🟧 Let’s take a closer look at the added conditional in the `laser_timer` function

 <br>

#### 🟢 Checking the Time Since Last Shot:



#### 🟤 `current_time - self.laser_shoot_time`

- - **calculates how much time has passed** since the player last fired a laser.

#### Subtracts the time stored

- - - This **uses the current time** (from `pygame.time.get_ticks()`) and **subtracts the time stored in** `self.laser_shoot_time`, <u>which is when the player last shot.</u>



 <br>

 <br>

## 🟩 Comparing to the Cooldown Duration:

#### 🟤 `>= self.cooldown_duration`



>**checks if the time elapsed is greater than or equal to the cooldown period** we set (400 milliseconds).



#### This means we’re asking:

> #### 🧶 “Has enough time passed since the last shot?”

<br>

### 🟩 Unlocking the Shooting Ability:

- #### `If` the condition is `true`

> #### (enough time has passed),

- #### then `self.can_shoot` is set to `True`.


> ####  ✅  This effectively "unlocks" the ability for the player to shoot again!

<br>