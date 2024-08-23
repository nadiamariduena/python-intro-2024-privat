
## 🟡 Draw: LINE  ___

### Sources:

https://pygame.readthedocs.io/en/latest/rect/rect.html

https://humberto.io/blog/exploring-pygame-2-drawing-on-screen/

<br>

- **also**, is SVG logic a bit similar to rect? [DRAW_line_svg-vs-rect](./z_DRAW_line_svg-vs-rect_.md)


<br>
<br>

### 🫐 First I will focus on drawing a `line` (like the one you see on the video below)

https://github.com/user-attachments/assets/af0f50cc-66b1-4cb3-a17f-719fe73436d2




### 🍊 In this Example, we are drawing a horizontal line on the screen:

<br>

```python

pygame.draw.line(screen, WHITE, [10, 100], [630, 100], 5)


```


- -  🍊 The line **starts** at **pos**ition (`10 x, 100 y`)on the screen.  **(what would give in pos absolute: 10% x axis, 20.83 y axis)**

<br>

>It's slightly different from using absolute positioning, but the concept is similar  [read more | DRAW_line-POS-ABSOl](./z_DRAW_line-POS-ABSOl_1.md)

<br>
<br>

- - 🍊 This means it **begins** `10` **pixels from the left edge** and `100` **pixels from the top edge** of the screen.




> - - #### 🟤 The line `extends to` position (630, 100), which places the end of the line 630 pixels from the left edge and still at 100 pixels from the top.

- -  Given the screen width of 640 pixels, this ensures the line is positioned well within the screen boundaries.
The line has a thickness of 5 pixels.

**starts** at 10,

**ends** at 630

>- - - (keep in mind that the **screen** 480, so the line will reache 630),

>`screen = pygame.display.set_mode((640, 480))`), i will be adding the entire code at the end



https://github.com/user-attachments/assets/af0f50cc-66b1-4cb3-a17f-719fe73436d2


<br>

<br>

## 🟦 The Code

### 🟠 Explanation:

#### screen:

This is the surface where the line will be drawn. Typically, this is your main game window or screen where all graphical elements are displayed.

#### WHITE:

This specifies the color of the line.

- - - In pygame, colors are often defined using RGB tuples. For example, WHITE is usually defined as (255, 255, 255), which represents white in RGB color space.


#### `[10, 100]`:

This is the starting point `(x, y)` of the line.

- - - Here, the line starts at the position (10, 100) on the screen. The x-coordinate is 10, and the y-coordinate is 100.


#### `[630, 100]`:

This is the ending point (x, y) of the line. The line will end at the position (630, 100) on the screen. The x-coordinate is 630, and the y-coordinate is 100.


### `5`:

This specifies the width (or **thickness**) of the line.

 - - - **In this case, the line will be 5 pixels wide**.



<br>
<br>

```python
import time
import pygame

# defining the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)



pygame.init()



screen = pygame.display.set_mode((640, 480))

# loading the font to be used at drawing time
# here you can add the size of the FONT, 55 is higher, 10 is lower
font = pygame.font.SysFont(None, 55)



pygame.display.set_caption('Drawing')



screen.fill(BLACK)



# drawing at the surface --------
# This is the surface where the line will be drawn. Typically, this is your main game window or screen where all graphical elements are displayed.

pygame.draw.line(screen, WHITE, [120, 100], [630, 100], 5)
pygame.draw.rect(screen, BLUE, [200, 210, 40, 20])
pygame.draw.ellipse(screen, RED, [300, 200, 40, 40])
pygame.draw.polygon(screen, GREEN, [[420, 200], [440, 240], [400, 240]])


# update
pygame.display.flip()


# 🔴 will launch the timer *to close** the window
# - the window will stay open for 10 milliseconds,
# but as you can notice, at the bottom there is also
# another timer, at the end it will addition those
# 5 milli secs to the 10, total 15 milli secs before its closes

# - the text = will be linked to this timer

time.sleep(10)



screen.fill(BLACK)
# writing pygame at the buffer
text = font.render('pygame', True, WHITE)
# coping the text to the screen
screen.blit(text, [250, 200])



pygame.display.flip()


# it will close after 5 milliseconds
time.sleep(5)

```

<br>

### 🟠 In the above example:

- i changed the x value for 120 instead of 10

```python
pygame.draw.line(screen, WHITE, [120, 100], [630, 100], 5)
```


https://github.com/user-attachments/assets/68975245-7944-4639-8e3a-3e479744a816



