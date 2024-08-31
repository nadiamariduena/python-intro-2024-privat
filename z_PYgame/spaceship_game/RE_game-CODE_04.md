
## 🟡 ANIMATION 2.


- Up & down animation

- delta

- vectors

- - Vector Multiplication

- - 🔴 (very important) Why do we need vectors if we have lists?




<br>
<br>

<br>

### 🟦 Vectors & Delta

- using vectors to store a direction, including **DELTA** to make the movement frame rate independent


<br>

### 🟠 At the moment I'm using the below code to move the player left & right, but i no longer want to do that, so lets remove the below



```python
    # Continuously check if the player's rectangle has moved past the window's boundaries.
    if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:
    # If the rectangle's right edge exceeds the window width or its left edge is less than 0,
    # it means the player has reached one of the screen edges.

     player_direction *= -1
    # Reverse the movement direction by multiplying `player_direction` by -1 to make the plane move in the opposite direction.
```

### 🟠 Modify this line


