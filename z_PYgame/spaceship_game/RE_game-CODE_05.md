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

