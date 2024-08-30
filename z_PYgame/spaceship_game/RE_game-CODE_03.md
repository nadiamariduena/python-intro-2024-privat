
## 🟡 ANIMATION


- move the plane from right to left &  vice versa

- clock

 - - FPS (frames per second)



<br>
<br>

### 💥 Make the player bounce from left to right

- at the moment we have the player moving to the right until it reaches the end of the screen on the right side

```python
 if player_rect.right < WINDOW_WIDTH:
        player_rect.left  += 2
```

<br>

### 🟦 1. Moving it LEFT & RIGHT

  Create a new variable and assign the value of 1:

- - `player_direction = 1`

- - Use the player direction within the loop, hide the old animation

```python
    # player movement💥
    player_rect.x += player_direction * 0.4

    # old anim
    # if player_rect.right < WINDOW_WIDTH:
    #     player_rect.left  += 2
```
<br>

### 🌈 Focus on the X axis

[<img src="../lefttoright_0_pos_frect.gif"/>]( )



## 🟠 Explanation

<br>

### `player_rect.x += player_direction * 0.4`

`player_rect.x +=`

-  - **updates** the **x-coordinate** of the `player_rect` **by adding this calculated amount**.

> #### This effectively moves the player rectangle horizontally on the screen based on the direction and speed of movement.


 <br>
<br>

 🟤 **If** `player_direction` is **positive +=**,

 - - `player_rect.x` **will be increased**

 > - - - (moving the player right).

 <br>

 🟤 **If** `player_direction` is **negative -=**,

 - - `player_rect.x` **will be decreased**

 > - - - (moving the player left).

<br>

####   🟤 `player_direction * 0.4`

- - calculates the amount to move the player horizontally.




<br>
<br>
<br>

## 2. 🌈🦄 Now I want to check if the player is OUTSIDE of the window

<br>

- Means that the player reaches the right edge and is now out of the window

```python
if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:

        player_direction *= -1
```
<br>


[<img src="../lefttoright_1_pos_frect.gif"/>]( )

## 🟠 Explanation

<br>

## 🫐 `if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:`
<br>

### 🟤  `player_rect.right > WINDOW_WIDTH:`

- -  **This** condition **checks** `if` **the right edge** of the `player_rect` **has moved beyond the  `right` ➡️ edge** of the **screen.**

> - - - #### 🍨 If it has, the plane has reached the right boundary.

<br>

### 🟤  `player_rect.left < 0:`

 - - **This** condition **checks** `if` **the left edge** of the `player_rect` **has moved beyond the ⬅️`left` edge** of the window.

 > - - - #### 🍨 If it has, the plane has reached the left boundary.

### 🟤 `or`:

- - This `logical operator` **ensures** that **if either** boundary **condition** is `true`

 > - - - ####  (i.e., the plane is **either** at the **right** edge **or left edge** of the window),

- - **the action inside** the `if` **block will be executed**.

<br>

```python
if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:

        player_direction *= -1
```

### 🍊 `player_direction *= -1:`

- -  This line reverses the direction of movement.

<br>

- - **If** `player_direction` **was `1`** (moving right),

- - - **it becomes `-1`** (moving left).

<br>

- - **If** `player_direction` **was `-1`**,

- - - **it becomes** `1`.

> #### This effectively ✋ <u>*changes*  the plane's movement direction when it hits either boundary</u>.


<br>
<br>

### 🟢 In other words

- The player_direction starts at 1 , moves the player to the right, and once it hits the edge, it changes to -1 to move the player to the left.

