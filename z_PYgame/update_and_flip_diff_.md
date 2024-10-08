
## 🟡 Update & Flip differences


- `update()` : [Go to section](#update_)

-  `flip()`: [Go to section](#flip_)


<br>
<br>
<br>



### 🟦 UPDATE()

####   `pygame.display.update()`

<br>

<a name="update_"></a>


📍 **Functionality:**

- -  Updates a **specific portion** of the **screen** or the **entire screen**.

📍 **Usage:**

- - You can **pass specific rectangles (or a list of rectangles)** to this function to **only update parts of** the **screen**.

<br>

#### 🔴 If no arguments are provided, it updates the whole screen.

```python
pygame.display.update()  # Updates the entire screen
pygame.display.update(rect)  # Updates only the specified rectangle

```

<br>

📍 **Performance:**

- - ✋ By updating only parts of the screen that have changed, it can be more efficient if you’re only changing a small portion of the display.



<br>
<br>




```python
#0
import pygame


# 1
pygame.init()
#2 --- window
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
#3
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#------

# 4 LOOP var
running = True
# 5 the Loop
while running:
 for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False

    # 7 --- DRAW the game ----
    pygame.display.flip()



# 6 EXIT
pygame.quit()
```

<br>

### DRAW: 🟦 `FLIP()`

 <a name="flip_"></a>


####   `pygame.display.flip()`


📍 **Functionality:**

- - **Updates the entire screen** with the new frame.


📍 **Usage:**

- -  Always updates the entire display surface. It's typically used when you are rendering the entire screen for each frame.

```python
pygame.display.flip()  # Updates the entire screen

```


📍 **Performance:**

- -  **Since it updates the entire screen, it might be less efficient compared to update()** if only part of the screen has changed.

 <br>

<br>

### 🟦 Summary of Differences


**Scope of Update:**

- - `update()` can update specific areas of the screen or the whole screen.


- - `flip()` updates the entire screen.

<br>

**Performance:**

`update()` can be more efficient if you only need to refresh part of the screen.


`flip()` always refreshes the whole screen, which can be less efficient if only small parts have changed.


<br>

**Typical Use Cases:**

**Use** `update()` when you need fine-grained control over which parts of the screen are updated.

**Use** `flip()` when you are redrawing the entire screen, such as in full-screen animations or games.

<br>
