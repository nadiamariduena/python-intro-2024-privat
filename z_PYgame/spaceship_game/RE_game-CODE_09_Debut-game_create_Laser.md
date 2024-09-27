
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
