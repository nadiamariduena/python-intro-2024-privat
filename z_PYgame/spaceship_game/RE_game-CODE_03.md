
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
