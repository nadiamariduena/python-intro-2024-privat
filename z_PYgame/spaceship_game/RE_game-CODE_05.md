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
