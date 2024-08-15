
# 🟡 Color / fill

<br>
<br>

### 🟠 `surface.fill`

Colors in **Pygame** are typically managed using **RGB** values, where each color is represented by a combination of **Red, Green, and Blue** components. Here’s a detailed overview:


<br>

1. **Color Representation**
- - - Colors in Pygame are represented as tuples of three integers, each ranging from 0 to 255, corresponding to the RGB color model:


```bash
Red: [0-255]
Green: [0-255]
Blue: [0-255]
For example:

White: (255, 255, 255)
Black: (0, 0, 0)
Red: (255, 0, 0)
Green: (0, 255, 0)
Blue: (0, 0, 255)
```
<br>

### 🌈 all colors:

https://pyga.me/docs/ref/color_list.html


<br>

### 🟤 Adding a color to a shape

#### When creating graphics or backgrounds, you can use these RGB tuples to specify colors.

- Examples:

### 🟤 Fill a surface with a color:

```python
surface.fill((255, 0, 0))  # Fills the surface with red

# or
surface.fill("lavenderblush2")
#more colors: https://pyga.me/docs/ref/color_list.html
```
<br>
<br>


```python
import pygame
import sys

pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fill the background with white
screen.fill(WHITE)

# Draw shapes with different colors
pygame.draw.rect(screen, RED, (50, 50, 200, 100))   # Red rectangle
pygame.draw.circle(screen, GREEN, (400, 300), 75)   # Green circle
pygame.draw.line(screen, BLUE, (100, 400), (700, 400), 5)  # Blue line

# Update the display
pygame.display.flip()

# Event loop to keep the window open
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


# 6 EXIT
pygame.quit()
```

<br>
<br>
<br>



### 🟠 4. Color Manipulation

In addition to direct RGB values, you can manipulate colors in various ways:

**Blending Colors:** Mix colors using blending functions or by averaging RGB values.

<br>

**Transparency:**

- - Use **RGBA** values where A (Alpha) represents the transparency level.


#### Example with transparency:

```python
surface = pygame.Surface((100, 100), pygame.SRCALPHA)
# Create a surface with per-pixel alpha


surface.fill((255, 0, 0, 128))
# Fill with semi-transparent red

```

### Summary

- Colors in Pygame are specified using RGB tuples.


- Color Operations: You can fill surfaces, draw shapes, and manipulate colors using RGB values.

**Transparency:** Managed using **RGBA values** on surfaces with per-pixel alpha.
