 ## 🟡 Handling Input in Pygame: Mouse and Keyboard Controls

- 🟦 In this lesson, we'll explore how to handle player input using both the mouse and keyboard.


 [1:29:46](https://youtu.be/8OMghdHP-zs?si=RPr8620UkCOLDoFS&t=5386)

 <br>



### 🫐 <u>Index</u> :



#### 🟤 What is Input in game programming: [Go to section](#input_in_game_programming_)

<br>

#### 🧶 Choosing the Best Way to Get Input: [Go to section](#best-way-to-get-input_)



#### 🧶 There are two main ways to check for input in Pygame:

- - **event-based and continuous checking:**  [Go to section](#event-based-and-continuous-checking_)

- - - 🟠 **event-based:**

- - - 🟠 **continuous checking:**

<br>
<br>

#### 🧶   Event Loop limitations [Go to section](#Event-Loop-limitations_)

- -  -  it’s okay to use more than one game loop?  [Go to section](#okay-to-use-more-than-one-loop_)



#### 🟡 Also in the same section

- - -  - Challenges with a Single Event Loop

- - -  - Polling

- - -  - Using `pygame.key` and `pygame.mouse` for Better Flexibility

- - -  - Procedural Games



<br>
<br>



<!-- <a name="_Event_Loop_and_Input_Handling_"></a> -->

#### 🟧 `Event`Loop and Input Handling


- -  (theory) `Event`Loop and Input Handling [Go to section](#_Event_Loop_and_Input_Handling_)

<br>

- - - **Understanding the** `Event` Loop and Input Handling  [Go to section](#Understanding_the_Event_Handling_Section_)



- - - **(recap)** Understanding the Event Handling Section [Go to section](#Understanding_the_Event_Handling_Section_)



- - - - **Remove** the `Player Movement section`  [Go to section](#remove_Player_Movement_section_)

<br>


#### 🟧 Handling Key Events:

- -  - Handling Key Events: [Go to section](#Handling_Key_Events_)

- - - -  **Event key**

- - - -  **Event type**

<br>

- - - Handling Specific Key Presses  [Go to section](#Handling_Specific_Key_Presses_)

- - - Handling **MOUSE Motion**  [Go to section](#Handling_MOUSE_Motion_)


- - -  👾 **Tracking Mouse Movement** to Control the Player  [Go to section](#Tracking_mouse_motion_)

<br>


#### 🟧 Using Input Outside the Event Loop

- -  - **`pygame.mouse.get_pos()`:** [Go to section](#get_position_)

- - -  **`pygame.mouse.get_pressed()`:** [Go to section](#get_pressed_)


- - -   **Other events** [Go to section](#other_events_)

- - -  Using **KEY PRESSED with a variable** and WHY? [Go to section](#get_pressed_with_variable_)


<br>
<br>
<br>
<br>
 <br>

 ---



##  🌟 Lesson 5: Mastering User Input and Events 🌟

<br>

### 🌈 In this lesson, we’ll focus on how to handle user inputs such as keyboard and mouse events to create interactive gameplay.

- - #### We'll refine our understanding of capturing and responding to user actions, which is crucial for making engaging and responsive games.

<br>

#### 🟦 What You’ll Learn:

- - - How to detect and respond to keyboard inputs.

- - - How to track and use mouse movements and clicks.

- - - How to handle various other events that can occur in your game.

<br>
<br>
<br>
<br>

<br>
<br>

---

<a name="input_in_game_programming_"></a>

# 🟧 Input?

In programming, **"input"** refers to any data or signal that comes from a user or device and is used by the program to perform actions.



- - When you move a player with the keyboard or mouse, the program is receiving data (the key presses or mouse movements) from the user.

- - This data is called "input" because it is fed into the program to control or change something.

### 🟤 Here’s a simplified breakdown:

**Keyboard Input:** When you press a key, the program receives that key press as input. It then uses this input to move the player or perform other actions.

**Mouse Input:** When you move the mouse or click, the program receives this as input and can use it to control the player or interact with objects.

> #### 🟩 In both cases, the term "input" describes the data or commands being sent from the user to the program, which then processes that data to produce a response or action in the game.



<br>
<br>

<br>
<br>

---

<a name="best-way-to-get-input_"></a>

## 🟠 1. Choosing the Best Way to Get Input


#### 🟤 When it comes to handling input,  `integrating input checks with classes` is often the most efficient approach.

- - **By incorporating input methods** into your game classes, you can easily manage and access player controls throughout your code.

- - **This method allows** for more organized and flexible control handling.



## 🟠 2. Checking Button States

<a name="event-based-and-continuous-checking_"></a>

### 🫐 There are two main ways to check for input in Pygame:

- 🍍 event-based and

- 🍍 continuous checking.

<br>
<br>
<br>
<br>


## 🟢 Event Loop Input:

  **This method reacts to specific events**, such as a button press or release.

> - - #### However, it only detects when an action occurs, not if a button remains pressed.




## 🟢 Continuous Checking:

**For smoother and more responsive controls**, you can continuously check the state of buttons or keys.

> - - #### This approach allows your game to detect and respond to inputs at all times, ensuring a more fluid gameplay experience.

<br>
<br>
<br>
<br>
<br>
<br>



---



<a name="Event-Loop-limitations_"></a>

# 🫐 🟠 Event Loop limitations

### 🟣 The teacher explained that we can only use a single event loop, which might become quite cumbersome in complex games.

> - -  As an alternative, we could use `pygame.key` and `pygame.mouse`, which are more flexible and can be accessed from anywhere in the code.

<br>
<br>

## ⚠️ Understanding the Event Loop

In Pygame, `the event loop is responsible for handling various events`, such as key presses, mouse movements, and other user interactions.

<br>

> ### 📌   However, it's important to know that `Pygame` supports `only a single event loop per program`  .



>**This can become a limitation**, especially in more complex games where managing multiple events might lead to a cluttered and difficult-to-maintain codebase.


<br>
<br>
<br>

---




# 🟡 Using Multiple Loops?

> #### 🟣 Question: In game development, especially with big and complex games, I’m wondering if it’s okay to use more than one game loop?



<a name="okay-to-use-more-than-one-loop_"></a>

> #### ✅ chatgpt: Using multiple game loops in a single game is generally not a common practice, especially in large and complex games.

- - The traditional approach is to use a single game loop that handles all aspects of the game’s update and rendering processes.

- - However, there are some scenarios where a multi-loop approach might be considered, such as managing different game states or systems independently.

<br>

### 🧶 🟨 Here’s a detailed breakdown of the considerations and best practices: [MULTIPLE_game_LOOPS](../a__about__MULTIPLE_game_LOOPS.md)



### 🟤 Also:

- Challenges  [with a Single Event Loop:](../a__about__MULTIPLE_game_LOOPS.md)

- [Polling](../a__about__Btn-Events__polling.md)

- Using  [`pygame.key` and `pygame.mouse` for Better Flexibility:](../a__about__MULTIPLE_game_LOOPS.md)

- Procedural Games [a__about_Procedural_Generation_games](../a__about_Procedural_Generation_games.md)



<br>
<br>
<br>
<br>
<br>
<br>

---


## 🟡 `Event`Loop and Input Handling

<a name="_Event_Loop_and_Input_Handling_"></a>

## 🫐 Understanding the `Event` Loop and Input Handling

#### 🟧 When using the EVENT loop, you are checking for specific actions, like a button press, rather than constantly checking if the button is pressed.


<br>

- - **If you hold down a button** and use the `event` loop to **capture input**, you **only get one capture** of **that action**.



- - **In contrast, using** `pygame.key` **to check for button presses** will give you continuous input, which is useful for moving objects on the screen.


<br>
<br>
<br>

## 🫐 🟡 When to Use the Event Loop


### Using the event loop is fine and sometimes necessary.

#### 🟤 For instance, it's essential for accessing touch input or the mouse wheel.

However, **remember that your game needs to be structured around the event loop**, but this approach is manageable with practice.

<br>
<br>

<br>
<br>
<br>

---


## 🧶 Before Proceeding with the Input Lesson, We'll Be Modifying the while Loop Section of the Code:



```python

#🟨 before input changes (around WHILE LOOP section)
import pygame
import os
from random import randint


pygame.init()
script_dir = os.path.dirname(__file__)



WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space shooter")


#while loop related
running = True
#✋ CLOCK:  FPS (frame per second)
clock = pygame.time.Clock()




# img's path
image_paths = {
    'player': os.path.join(script_dir, '..', 'images', 'player.png'),
    'star': os.path.join(script_dir, '..', 'images', 'star.png'),
    'meteor': os.path.join(script_dir, '..', 'images', 'meteor.png'),
    'laser': os.path.join(script_dir, '..', 'images', 'laser.png')

}



player_surf = pygame.image.load(image_paths['player']).convert_alpha()
meteor_surf = pygame.image.load(image_paths['meteor']).convert_alpha()
laser_surf = pygame.image.load(image_paths['laser']).convert_alpha()

# (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
# Will pos the plane at the center of the screen/window
player_rect = player_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 10))

# start
star_surf = pygame.image.load(image_paths['star']).convert_alpha()
# star pos
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

# 1. -----  move right to left loop  ---

#
##20 X, - 10Y axis
#🤚 VECTOR
player_direction = pygame.math.Vector2(1, 1) # This vector represents the direction and speed at which the player is moving:
# player speed
#🟡 actual movement
player_speed = 1000
# -----  move right to left loop  ---

while running:

    # ✋ DELTA time
    dt = clock.tick() / 1000
    # print(dt)


    # 🔴 Event Handling Section
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            running = False
    # ---

    display_surface.fill("lavenderblush2")


    for pos in star_positions:
        display_surface.blit(star_surf, pos)


   # player
    display_surface.blit(player_surf, player_rect)

    # meteor
    display_surface.blit(meteor_surf, meteor_rect)
    # laser
    display_surface.blit(laser_surf, laser_rect)



    # CONDITION for player to bounce when reaching the walls of the window, we wont be using elif, instead i will add a second "if" so to evaluate them independently

    # --- no good
    # if player_rect.bottom > WINDOW_HEIGHT or player_rect.top < 0:
    #       player_direction.y *= -1

    # if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:
    #     player_direction.x *= -1
    #------

    #--- short term solution
    if player_rect.bottom >= WINDOW_HEIGHT or player_rect.top <= 0:
          player_direction.y *= -1

    if player_rect.right >= WINDOW_WIDTH or player_rect.left <= 0:
        player_direction.x *= -1
    # ---------





    # vector
    # The line below updates the position of the player's sprite by adding the player_direction vector to the current center position of player_rect
    player_rect.center += player_direction * player_speed * dt

    #

    # The += operator modifies player_rect.center in-place, so the player's position changes according to player_direction

    # # ----- the multiplication
    # For a direction vector (2, -1) and a speed of 10, the result of this multiplication is (20, -10). This means that in each frame, the player should move 20 units to the right and 10 units up.
    # By adding player_direction * player_speed to player_rect.center, you’re effectively moving the player’s position by (20, -10) pixels each frame.
    # ----- the multiplication

    pygame.display.update()



pygame.quit()
```


<br>
<br>
<br>


<br>
<br>

---

[1:32:06](https://youtu.be/8OMghdHP-zs?si=yroN_cRZQzF6iL6h&t=5526)

- check also other type of events [EVENTS pygame](https://www.pygame.org/docs/ref/event.html)


<br>
<br>

<a name="Understanding_the_Event_Handling_Section_"></a>

#  🟡 Understanding the Event Handling Section

### ⚫ RECAP lesson

<br>



## 🫐 🟠 `pygame.event.get():`

This **gets a list of all the events that have happened since the last frame**.

- - Events can be things like keyboard presses, mouse movements, or system messages.


<br>

```python
while running:
    # DELTA time
    dt = clock.tick(120) / 1000
    # print(dt)


    # 🔴 Event Handling Section
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            running = False
    # ---
```
<br>

##   for event in `pygame.event.get():`:

-  - 🟧 This loop **goes through each event** in the list.

<br>

###    `if event.type == pygame.QUIT:`:

- -  🟧 This checks if the event is a quit event, which usually happens when you close the game window.

<br>

###   `running = False`:

- -  🟧 If a quit event is detected, this line stops the while running: loop, which ends the game.



  ## In summary:

> ### 🌈 this section is used <u>to check if the player has closed the game window and then stop the game loop</u>  when that happens.



<br>
<br>
<br>
<br>

---

<br>

##  🟡 <u>Removing Player Movement</u>  section




## 🟦 Before moving forward, let's remove the player movement logic from the while loop.

```python

    if player_rect.bottom >= WINDOW_HEIGHT or player_rect.top <= 0:
          player_direction.y *= -1

    if player_rect.right >= WINDOW_WIDTH or player_rect.left <= 0:
        player_direction.x *= -1
    # ---------

    player_rect.center += player_direction * player_speed * dt
```

<br>


<br>



<br>
<br>
<br>

---



<a name="Handling_Key_Events_"></a>

# 🟡 Handling Key Events

## Event Type & Event Key:


<br>

## 🫐 🟠 `event.type`

### To start working with key events, you can use `event.type` <u>to check if a key has been pressed</u> .

- For testing purposes, you can add a **print statement** to see if it's working:


<br>

```python
if event.type == pygame.KEYDOWN:
   print("key down")
```


##  🟦  Here's how to set it up:



 ### 🔴 Make Sure You're in the Correct Environment:

>Verify that you are running your code in the correct **environment** to avoid errors.

 ### 🟤 Test the Key Event Handling:

>Add the below to see if it detects key presses:

```python
# 🌈 Event Handling Section
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            running = False
       if event.type == pygame.KEYDOWN:
        print("key down")
```

### 🟦  This will print "key down" every time a key is pressed, allowing you to confirm that your key event handling is working.

<br>
<br>
<br>

## 🫐 🟠 `event.key`

### 🟢 To see which key is pressed, you can print `event.key`.

<br>

- -  🟫 **When you run the code**, you'll notice numbers appearing in your terminal.

- -  🟫 **These numbers correspond** to different keys on the keyboard.



```python
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            running = False
       if event.type == pygame.KEYDOWN:
            print(event.key)
```

- 🟡 When you press different keys, the terminal will display different numbers, each representing a specific key.



<br>
<br>
<br>

<br>

---


<a name="Handling_Specific_Key_Presses_"></a>

# 🟡 Handling Specific Key Presses

<br>

## 🫐 🟠 `pygame.K_1`

<br>

### 🟩 To check for specific   `key presses`,  you can use `event.key` in combination with `event.type`.



 - 🟢 Here’s an example of how to detect if the `1` key is pressed:

```python
 if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            print(1)
```


### `event.type == pygame.KEYDOWN`:

- - This checks if a key press event has occurred.

### `event.key == pygame.K_1`:

- - This checks if the specific key pressed is the 1 key on the keyboard.

<br>

### `print(1)`:

- - **If both conditions are true** (the event is a key press and the key is 1), it prints 1 to the terminal.

### Putting It All Together

```python
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            running = False
       if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            print(1)
```


<br>
<br>
<br>

<br>

---


<a name="Handling_MOUSE_Motion_"></a>

# 🟡 Handling MOUSE Motion

<br>

## 🫐 🟠 `pygame.MOUSEMOTION`

<br>

- **To detect when the mouse is moving**, you can check for the `pygame.MOUSEMOTION` **event**.

#### Here's how you can do it:

```python
if event.type == pygame.MOUSEMOTION:
   print("mouse is moving")
```
> The pygame.MOUSEMOTION event type is triggered whenever the mouse moves within the window.

<br>

## 🟡 Printing the Mouse Position

To get and print the position of the mouse when it moves, **you can use the `event.pos` attribute**.

 Here’s how you can do it:

```python
# This checks if the event is a mouse movement event.
if event.type == pygame.MOUSEMOTION:
   print(event.pos)

# event.pos: This attribute contains the current position of the mouse. It is a tuple with two values: the x and y coordinates of the mouse pointer relative to the top-left corner of the window.
```


### 🟤 Putting It in Context

Here’s how to use it in your event handling loop:

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.MOUSEMOTION:
        print(event.pos)
```

> 🟦 This allows you to see the exact coordinates of the mouse pointer in real-time, which can be **useful for tasks like tracking mouse movement or implementing interactive features**. (Think about the drawing pen of the google site)



<br>
<br>

<br>

<a name="Tracking_mouse_motion_"></a>


## 🫐 🟡 Tracking Mouse Movement to Control the Player

### When the mouse moves, the player’s position updates to match the mouse's location.

<br>

- In this part of the code, we’re using the mouse position to control the player's position:

```python
if event.type == pygame.MOUSEMOTION:
    #  print("mouse is moving")
    #  print(event.pos)
    player_rect.center = event.pos

```
<br>

#### Explanation

#### 🟤 if `event.type == pygame.MOUSEMOTION:`:

- - This checks if the event is a mouse movement event

#### 🟤 `player_rect.center = event.pos`:

-  - This line sets the center of the player rectangle (player_rect) to the current mouse position (event.pos).

<br>

> ### 🌈 This means that as you move the mouse, the player will follow the mouse pointer.



<br>
<br>

### 🔴 Next Step: Hide the Code Below

- This code was just to demonstrate it's usage.

#### You can hide it for now:



```python
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            print(1)
        if event.type == pygame.MOUSEMOTION:
            #  print("mouse is moving")
            #  print(event.pos)
             player_rect.center == event.pos
```



<br>

---

<br>
<br>

 <a name="get_position_"></a>

 ## 🫐 🟠 `pygame.mouse.get_pos()`



## 🌈 Accessing Mouse Position Outside the Event Loop

> #### 🟤 Use pygame.mouse.get_pos() to directly retrieve the current position of the mouse cursor


```python
while running:
    #🤚 DELTA time
    # frame rate / division
    dt = clock.tick() / 1000
    # print(dt)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #  🔴 the line below, is out of the  EVENT loop "for event in"
    print(pygame.mouse.get_pos())
```

## 🟤 Explanation


#### Event Loop:

- - The `pygame.event.get()` **loop** handles events like key presses and mouse movements, but you can also access input data outside this loop.

#### Direct Input Access:

- - By using `pygame.mouse.get_pos()`, you can get the current position of the mouse anywhere in your code, not just inside the event loop. This can be useful for tasks that need continuous access to mouse position or other inputs.

#### Testing It:

- - The example code prints the current mouse position every frame.

>This lets you see where the mouse is located on the screen, even if you’re not handling mouse motion events directly within the loop.

<br>
<br>
<br>
<br>
<br>
<br>

---

## 🟡 Visualizing Mouse Coordinates


<a name="pos_coordinates_visualization_"></a>

### When you test your code, you'll see different mouse coordinates in the terminal.

#### 🟤  Here’s how it works:

The **`pygame.mouse.get_pos()`** function returns the mouse coordinates relative to the window.

> - #### These coordinates range from `(0, 0) in the top-left corner to (1280, 720) in the bottom-right corner`, corresponding to the dimensions defined in the WINDOW_WIDTH and WINDOW_HEIGHT variables:

```python
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
```


<br>

>  - #### 🟦 When you test the code, you’ll see different mouse coordinates printed to the terminal based on where the mouse is on the screen.

#### Here's what to expect:

- **Top Left Corner:** Near the top-left of the screen, you will see coordinates close to `(0, 0)`.


<br>

- **Middle of the Screen:** As you move the mouse towards the middle, you'll notice coordinates like `(600, 300)`, depending on your screen size and resolution.

<br>

- **Right Edge of the Screen:** Near the right edge of the screen, you will see coordinates close to (1279, y). For example, if 1279 is the x-coordinate, 151 might be the y-coordinate.




### 🟤 What You’ll See in the Terminal


**Initially**, the coordinates may all be `(0, 0)` if the mouse is at the top-left.


- - 🌈 As you move the mouse, you'll see coordinates change accordingly, such as `(600, 300)` or `(1279, 151)` when nearing the right edge.


#### Example Output

```python
(0, 0)
(0, 0)
...
(1279, 151)
(1279, 151)
... etc
```
> #### 🟦 This helps you understand how the mouse position updates in real-time, giving you insight into how to use these coordinates in your game development projects.

<br>
<br>
<br>
<br>
<br>
<br>

---


<a name="get_pressed_"></a>



## 🫐 🟠  `pygame.mouse.get_pressed()`

#### In addition to tracking the mouse position, you can also check if any mouse buttons are being pressed.

- - The function `pygame.mouse.get_pressed()` helps with this.


```python
while running:
    #🤚 DELTA time
    # frame rate / division
    dt = clock.tick() / 1000
    # print(dt)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    print(pygame.mouse.get_pressed())
```

<br>
<br>

## 🫐 🟡 How It Works:

### `pygame.mouse.get_pressed()` returns a tuple with three values:

```bash
True or False for whether the left mouse button is pressed.
True or False for whether the middle mouse button is pressed.
True or False for whether the right mouse button is pressed.
```


<br>
<br>
<br>
<br>
<br>
<br>

---


<a name="get_rel_"></a>



## 🫐 🟠  `pygame.mouse.get_rel()`

#### When you need to track how much the mouse has moved since the last frame, `pygame.mouse.get_rel()` is the function to use. It provides the relative movement of the mouse.

<br>

### 🟤 How It Works:

#### `pygame.mouse.get_rel()` returns a tuple with two values:

- The change in the x-direction.

- The change in the y-direction.

### 🟢 This tells you how far the mouse has moved from its last position.


```python
while running:
    #🤚 DELTA time
    # frame rate / division
    dt = clock.tick() / 1000
    # print(dt)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Print the mouse movement since the last frame
    print(pygame.mouse.get_rel())

```
<br>

### 🟠 What You’ll See:

The **output will be a tuple like `(dx, dy)`** where **dx** is the horizontal movement and **dy** is the vertical movement.

###  🧶For example:

- - **`(5, -3)`** means the mouse moved 5 pixels to the right and 3 pixels up.

<br>

- - **`(-2, 7)`** means the mouse moved 2 pixels to the left and 7 pixels down.


- - **`(0, 0)`** means the mouse hasn’t moved since the last frame.


####  🌈This is particularly useful for creating smooth and responsive mouse interactions, like dragging or camera control in games.

<br>
<br>
<br>
<br>
<br>
<br>

---

# 🌈 Other Pygame Events

### 🟩 There are many different events in Pygame that you can use to interact with your game. For now, we'll focus on the ones we've covered

- 🌴 check also other type of events [EVENTS pygame](https://www.pygame.org/docs/ref/event.html)



### 🟠 Here's a list of other events you might want to explore on your own:


#### 🟨 Commonly Used Pygame Events:

<br>

`pygame.QUIT`: Triggered when the user closes the window.

`pygame.KEYDOWN`: Triggered when a key is pressed.

`pygame.KEYUP`: Triggered when a key is released.

`pygame.MOUSEBUTTONDOWN`: Triggered when a mouse button is pressed.

`pygame.MOUSEBUTTONUP`: Triggered when a mouse button is released.

`pygame.MOUSEMOTION`: Triggered when the mouse is moved.

<br>

#### 🟨 Other Events You Can Test:


`pygame.ACTIVEEVENT`: Triggered when the window gains or loses focus.

`pygame.JOYAXISMOTION`: Triggered when a joystick axis changes.

`pygame.JOYBALLMOTION`: Triggered when a joystick ball moves.

`pygame.JOYHATMOTION`: Triggered when a joystick hat changes.

`pygame.JOYBUTTONDOWN`: Triggered when a joystick button is pressed.

`pygame.JOYBUTTONUP:` Triggered when a joystick button is released.

`pygame.VIDEORESIZE`: Triggered when the window is resized.

`pygame.USEREVENT`: A custom event that you can define in your program.


<br>
<br>
<br>
<br>
<br>
<br>

---

# 🟫 Let's Continue:


## 🟡 key.get_pressed()

🟦 Using ` pygame.key.get_pressed()`

### We’re going to use `pygame.key.get_pressed()` <u>to check which keys are currently being pressed</u> .

  We'll **assign its value to a variable** for easier access.

```bash
keys = pygame.key.get_pressed()
```



### 🟠 Why Do We Do This?

#### 🟤 Convenience:

- - **By storing the result** in a **variable** (`keys`), **you avoid repeatedly calling** `pygame.key.
get_pressed()` **every time** you need to check the state of the keys.

> #### This makes your code cleaner and more efficient.

<br>
<br>


<br>
<br>

---

### 🟦 As we saw it previously: `get_pressed()`


<br>

#### 🟠 Now that we have explored the most commonly used events, we can continue with more advanced input handling techniques.

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_1]:
    print(1)

```

<br>

## 🟤 Explanation



### `keys = pygame.key.get_pressed()`:

#### 🟡 This line retrieves the current state of all keyboard keys.

#### 🔴 each position corresponds to a key

- -  - `pygame.key.get_pressed()` **returns a list of boolean values**, where **each position corresponds to a key** on the keyboard. If a key is pressed, its value is True; otherwise, it's False.

<br>
<br>



### `if keys[pygame.K_1]:`:

  Here, `pygame.K_1` represents the **`"1"` key on the keyboard**.

  - - **We check the value** at **this position** in the keys list to see if the **"1" key is pressed**.

<br>

- - **If the value is** `True` (meaning the "1" key is being pressed), the condition evaluates to True, and the code inside the **if statement will run**.


### `print(1)`:

If the "1" key is pressed, this line prints the number 1 to the terminal.

<br>

## 🟠 Why Use `pygame.key.get_pressed()`?

#### Real-time Input Checking:

- -  Unlike event-based methods that check for specific events when they occur, **`pygame.key.get_pressed()`** lets us continuously check if keys are being pressed at any time.

> #### 🟡 This is useful for continuous actions, such as holding down a key to keep moving a player character


### Back to the code

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_1]:
    print(1)

```

### 🔴 OUTCOME:

- When you run this code, pressing any key will not produce any visible output.

> #### However, if you press the "1" key on your keyboard, you will see the number 1 printed in the console.

Additionally, if you hold down the "1" key, the number 1 will keep printing repeatedly as long as the key is held down

<br>


## 🟡 Differences

### 1. 🌈 Key Press Handling Inside the Event Loop

<br>

- - 🍦 This code **checks for key events** (such as pressing keys) **in the `for event`** in `pygame.event.get()` **loop**.



<br>

- - When you press the "1" key, it detects the KEYDOWN event and prints 1 to the console.

- - 🔴 **If you hold down the "1" key**, the number 1 **will be printed only once** because the event loop only detects each key press as an event.

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
        print(1)

```

#### 🔴 Limitations:

This method **only detects key presses when the KEYDOWN event is registered**, which **means you won't see continuous output if the key is held down**.

- - You will see the output only when the event loop processes a new KEYDOWN event.

<br>
<br>

### 2. 🌈 Key Press Handling Outside the Event Loop

#### What Happens:

- - 🍦 This code **checks the state of all keys in the keys array provided by `pygame.key.get_pressed()`**, which **tells** you **whether each key is currently pressed or not**.

<br>

- - 🔴 When the "1" key is held down, **it will continuously print 1 to the console** because `pygame.key.get_pressed()` returns a snapshot of the current state of all keys every frame.

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_1]:
    print(1)

```

### 🔴 Limitations:

> **If this code is outside the event loop, it might not work as expected**because it relies on the loop that handles the game events.

You should typically include it inside the game loop but outside the event handling to ensure it gets checked every frame.


## 🫐 Key Differences:

### 🟤 Event Loop Method:

-  - Detects key presses as discrete events.

-  - Prints 1 only once per key press event.


### 🟤 State Check Method:

- - Continuously checks if the key is pressed.

- - Prints 1 continuously as long as the key is held down.



<br>
<br>
<br>
<br>

---

# 🟡 🫐 Movement Concepts


 ## 1. 🫐 🟠 Update the Direction

- - First, let’s adjust how we set the player's direction. Change this line:

<br>

**From this**: `player_direction = pygame.math.Vector2(1, 1)` **to this**:  `player_direction = pygame.math.Vector2(0, 0)`.



###  🌈 **Why?**

- -  Since both values are 0, you can simplify it to: `player_direction = pygame.math.Vector2(0)`

### 🔴 This means the player starts with no movement in any direction.

<br>
<br>

### 2. 🫐 🟠 Change the Speed

#### Next, we need to adjust the player’s speed. Change this line:

- from this: `player_speed = 1000` to this: `player_speed = 300`

<br>
<br>


### 3. 🫐 🟠 Handle Movement with Keys


### 🟩 Conditional: `player_direction.x = 1`

<br>

### Now let’s make the player move with keyboard input.

- - **Add this** to check if the key 1 is pressed and set the direction:

- - #### 🌈 This code checks if the 1 key is pressed and, if so, sets the player’s movement direction along the x-axis.

<br>

```python
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
    #     print(1)
        player_direction.x = 1
```
<br>
<br>

### 4. 🫐 🟠 Movement with `dt`

#### To ensure smooth movement regardless of the frame rate, we need to use dt (delta time). Bring back this line:

```bash
player_rect.center += player_direction * player_speed * dt
```


## 🫐 🟡 Putting It All Together


### Here’s how everything fits into your game loop:

## a) Initialization:

```python
player_direction = pygame.math.Vector2(0)  # Start with no movement
player_speed = 300  # Set the speed

```
## b) Main Loop:

```python
while running:
    dt = clock.tick() / 1000  # Get time since last frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ✋ ---------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        player_direction.x = 1  # Move right when '1' is pressed

    player_rect.center += player_direction * player_speed * dt  # Update player position
    # ✋ ---------

    # Draw everything
    display_surface.fill("lavenderblush2")
    for pos in star_positions:
        display_surface.blit(star_surf, pos)

    display_surface.blit(player_surf, player_rect)
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)

    pygame.display.update()

pygame.quit()

```



## 🟡What’s Happening:

#### 🟢 `player_direction = pygame.math.Vector2(0)`


- -  initializes the player’s movement to zero.


#### 🟢 `player_speed = 300`

- -  sets a reasonable speed for the player.


#### 🟢 `keys[pygame.K_1]`

- -  checks if the 1 key is pressed and moves the player right if it is.


#### 🟢 `player_rect.center += player_direction * player_speed * dt`

- -  updates the player’s position, ensuring smooth movement even if the frame rate changes.

<br>

## 🔴 Problem:


###   When you run the code, pressing the 1 key will move the player to the right,

- - 🔴 **but it might continue moving uncontrollably.**

- - -  That’s because we haven’t added logic to stop the movement or handle other directions yet. You’ll need to add more key checks to handle stopping or changing directions.


## 🍊 Comparing

### Before

```python
    #---
    if player_rect.bottom >= WINDOW_HEIGHT or player_rect.top <= 0:
          player_direction.y *= -1

    if player_rect.right >= WINDOW_WIDTH or player_rect.left <= 0:
        player_direction.x *= -1
    # ---------
    # vector
    # The line below updates the position of the player's sprite by adding the player_direction vector to the current center position of player_rect
    player_rect.center += player_direction * player_speed * dt

```

### After


```python
    # ---------KEY  ---------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
    #     print(1)
        player_direction.x = 1

    player_rect.center += player_direction * player_speed * dt
    # ------------------
```


<br>
<br>
<br>


## 🫐 🟡 Key Press Handling and Movement

 ## 🟢 Move to the RIGHT

 <br>

## `player_direction.x = 0`



#### 🍊 This code checks if the `1` key is pressed. `If it is`, `player_direction.x` is set to 1, moving the player right.

<br>

- - If the key is not pressed, player_direction.x is set to 0, stopping horizontal movement.

> #### The line with 0 ensures that the player stops moving when the key is released.

<br>

### Using the `K_1`

```python
   # ---------KEY  ---------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
    #     print(1)
        player_direction.x = 1
    else:
        player_direction.x = 0

    player_rect.center += player_direction * player_speed * dt
    # ------------------

```
## 🔴 Output

> - - Try pressing 1 and then 0 from your computer , this also stop it

### 🟡 Key Not Pressed (else):

- - 🟧 When the 1 key is not pressed, `player_direction.x is set to 0`.


<br>
<br>

### 🟡 Using the the ARROWS `K_RIGHT`

- You will have the same effect

```python
   # ---------KEY  ---------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
    #     print(1)
        player_direction.x = 1
    else:
        player_direction.x = 0

    player_rect.center += player_direction * player_speed * dt
    # ------------------

```

<br>
<br>

<br>
<br>




# 🫐 🟡 Making it cleaner

## 🟢 Move to Right


###  You can use a more concise method to handle key input.


<br>

- - 🌈 **Instead of** writing a **full `if-else`** statement **to set** `player_direction.x`, **you can directly convert the boolean value** from `keys[pygame.K_RIGHT]` **to an integer**.

<br>

> #### This way, `player_direction.x` will be 1 if the right key is pressed, and 0 otherwise.


### 🟠 USE THIS:

```python
player_direction.x = int(keys[pygame.K_RIGHT])
```


### 🟠 INSTEAD of this:

```python
    if keys[pygame.K_RIGHT]:
    #     print(1)
        player_direction.x = 1
    else:
        player_direction.x = 0
```

<br>
<br>

>### ⚠️  If you’re familiar with JavaScript and React, there’s no direct equivalent for this line:

```python
player_direction.x = int(keys[pygame.K_RIGHT])
```

<br>
<br>

## 🫐🟡 `int()`

### 🟡 the conditional logic happens when `keys[pygame.K_RIGHT]` evaluates whether the right arrow key is pressed.

### 🐦‍⬛ `int()` is the function doing the conversion.

- - `int()`  converts the boolean value (True or False) into an integer (1 or 0 respectively).


<br>

- - - #### 🟫 In Python, True is equivalent to 1 and False is equivalent to 0. Therefore, `int(keys[pygame.K_RIGHT])` gives 1 if the key is pressed and 0 if it is not.

<br>

> - - -  🔴 **This conversion itself acts as a condition**, so **you avoid** explicit **if statements** by relying on this built-in boolean-to-integer conversion.

<br>
<br>



## 🫐 🟡Understanding keys and int in Pygame


## ⚫  <u>Recap</u>

### 🟠 `pygame.key.get_pressed()`:

This function **returns a sequence (like a list) of boolean values** representing the state of every key on the keyboard.

<br>


#### 🔴 For instance, `keys[pygame.K_RIGHT]` <u>is True `if` the right arrow key is pressed</u>  , 🔴 and False otherwise.

### 🟠 `int(keys[pygame.K_RIGHT])`:

#### This converts the boolean value (True or False) into an integer (1 or 0 respectively).

- - 🔴 In Python, True is equivalent to `1` and False is equivalent to `0`. Therefore, `int(keys[pygame.K_RIGHT])` gives `1` if the key is pressed and 0 if it is not.


<br>

```python
while running:
    #🤚 DELTA time
    # frame rate / division
    dt = clock.tick() / 1000
    # print(dt)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
        #     print(1)


    # print(pygame.mouse.get_pos())
   # ---------KEY  ---------
    keys = pygame.key.get_pressed()

    player_direction.x = int(keys[pygame.K_RIGHT])

    player_rect.center += player_direction * player_speed * dt
    # -----------------
    # -----------------
    display_surface.fill("lavenderblush2")

    for pos in star_positions:
        display_surface.blit(star_surf, pos)

    display_surface.blit(player_surf, player_rect)
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)

    pygame.display.update()



pygame.quit()
```

<br>
<br>
<br>

## 🟡 Move X: LEFT & RIGHT

### 🟩 🟡 This line controls the horizontal movement of the player character by setting

```python
    player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])

```


### 🟨 Explanation:



🟤 **Subtraction (-)**: Subtracts the integer value of the left key state from the right key state.

<br>

🟢 **Result:** If only the right key is pressed, player_direction.x will be 1.

> - - #### 🌈 If only the left key is pressed, it will be -1. If both or neither are pressed, it results in 0.


🟢 **Purpose**: This line effectively sets player_direction.x to 1, -1, or 0 based on whether the right or left arrow keys are pressed, allowing for movement in both directions.

<br>
<br>
<br>


## 🟡 Move X: UP & DOWN

### 🟩 🟡 This line controls the vertical movement of the player character by setting



```python
 player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

```
### like so:

```python
##20 X, - 10Y axis
#🤚 VECTOR
player_direction = pygame.math.Vector2(0) # This vector represents the direction and speed at which the player is moving:
# player speed
#🟡 actual movement
player_speed = 300



while running:
    #🤚 DELTA time
    # frame rate / division
    dt = clock.tick() / 1000
    # print(dt)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
        #     print(1)


    # print(pygame.mouse.get_pos())
   # ---------KEY  ---------
    keys = pygame.key.get_pressed()

    # LEFT & RIGHT
    player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    # DOWN & UP
    player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

    player_rect.center += player_direction * player_speed * dt
    # -----------------
    # -----------------
    display_surface.fill("lavenderblush2")

    for pos in star_positions:
        display_surface.blit(star_surf, pos)

    display_surface.blit(player_surf, player_rect)
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)

    pygame.display.update()



pygame.quit()
```
<br>

## 🟩 Test it:

- - 🟡 1. **Press** (up, down, left and right), notice the values in your console

- - 🟡 2. Then, **Try pressing up and left at the same time**

<br>

### 🔴 Issue

- -  - 🔺 This time, **the values you'll see jump from (`0, 0`) to around `424.26406871192853`**

<br>

> - - -  #### 👾 What’s happening here is that without normalization, the diagonal movement makes the vector length longer than when moving straight in one direction, causing this unexpected jump in values.

<br>

## 🫐 🟡  SPEED inconsistency


 Now that I’ve implemented movement for the X and Y axes, I’m noticing an inconsistency with the speed.


## 🔴 speed isn’t right:

- - When pressing left and right, the speed behaves as expected. However, when pressing the up and left arrows simultaneously, the speed isn’t right.



- - #### 🟦 Related to the <u>diagonal movement</u>  speed:

- - #### 🔴 The issue you're encountering is related to the diagonal movement speed.

- - - When you move diagonally (e.g., **pressing the `up and left` arrows simultaneously**), the speed is inconsistent due to how 🟩 **vector** magnitudes work.

### Currently I have the below on Speed

```python
#🟡 actual movement
player_speed = 300
```

<br>