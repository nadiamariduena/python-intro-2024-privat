

# 🟡 FRAME Rate independence

<br>

- Frame rate independence is a concept in game development that **ensures the game's behavior and movement remain consistent regardless of the frame rate**.



 - - #### 🔴  Essentially, it means that the speed and smoothness of animations and movements are <u>not directly tied to how many frames per second (FPS) the game is running at</u> 🔴 .

<br>

# 🟡 Why It Matters



### Consistent Experience Across Different Systems:

<br>

- - 🟤**Different systems** may run games at different frame rates.

<br>

- - 🔴 **Frame rate independence ensures that** the game behaves the same way on a high-end system running at 120 FPS and on a lower-end system running at 30 FPS.

<br>
<br>

# 🫐 🟡 Why It Matters

### Consistent Experience Across Different Systems:

<br>

- - 🟤**Different systems** may run games at different frame rates.

<br>

- - 🔴 **Frame rate independence ensures that** the game behaves the same way on a high-end system running at 120 FPS and on a lower-end system running at 30 FPS.




<br>

### 🟫 Smooth Gameplay:

- -  **Without frame rate independence, if the frame rate drops**, movements and animations might slow down or become jerky. With frame rate independence, movement speed remains consistent even if the frame rate varies.

<br>
<br>

# 🫐 🟡 How It’s Achieved

- 🔴 (I’ll show you a simple example of how delta is useful soon. For now, just check out the information below)

<br>
<br>

## 🟡 DELTA

- recap

#### To achieve frame rate independence, you typically need to use the concept of delta time.


-  - **DELTA is a way to measure how much time has passed since the last frame** (or screen update) in a game.

> - - #### This helps in making sure that the game moves the same way regardless of how fast or slow the computer is running the game.

<br>

- - 🟦  **Delta** time refers to the time elapsed since the last frame.

> - - - ###  🧸 By incorporating delta time into your movement calculations, you ensure that movement is <u>based on real time rather than the number of frames.</u>



<br>
<br>
<br>
