# 🟡 Phase 3

## 🟠 Rects & Frects


- -  Read more [a__about_rects](../a__about_rects.md)

<br>

### What is the Difference between Rects & Frects

-  In Pygame, `Rect and frect (or FRect)` are **both used to represent rectangular areas**, but **they differ** mainly in the type of **precision** they **use for their coordinates and dimensions:**

<br>

## `rect` & `frect`

### ⚫  Differences

🔴 **Precision:** `Rect uses integer` values(20), while `FRect uses floating-point` values(20.5).



```python
# ✋ rect
import pygame
rect = pygame.Rect(10, 20, 30, 40)

#
# ✋ FRECT (great precision: 30.5)
import pygame.freetype
frect = pygame.freetype.FRect(10.5, 20.5, 30.5, 40.5)
```

<br>

> - - 🔴
it doesn't make sense to keep Rect with integers, it will be deprecated once FRect is released in 2.1.4. [Frect OR RECT](https://github.com/pygame/pygame/issues/3643)



<br>
<br>


## 🟠 About  Rect's

In Pygame, Rect objects represent rectangles with defined size and position.

- - They include a variety of **points** ⚫, such as **tuples with X and Y coordinates**.

- - - Additionally, Rect objects have properties for width, height, and overall size.

<br>

**Read More:** exercises and ways you can use the rect (collision example) [a__about_rects](../a__about_rects.md) , check the exercise below also there:

https://github.com/user-attachments/assets/3397c1ba-e011-49a0-a8c9-f9f915067076

<br>
<br>
<br>

### 🟤 In Pygame, Rect objects include several <u>key ⚫ points</u>  that help define their position and dimensions:


[<img src="../rect__dots.png"/>](https://www.youtube.com/watch?v=8OMghdHP-zs&t=821s)


<br>

**Top-left corner:** The `(x, y)` position of the rectangle's top-left corner.

```python
rect = pygame.Rect(30, 40, 100, 80)

# This creates a rectangle with:
# ✋
# Top-left corner at (30, 40)
# Width of 100 pixels
# Height of 80 pixels
```

<br>

**Top-right corner:** The `(x + width, y)` position of the rectangle's top-right corner.

<br>

**Bottom-left corner:** The `(x, y + height)` position of the rectangle's bottom-left corner.

**Bottom-right corner:** The `(x + width, y + height)` position of the rectangle's bottom-right corner.

<br>
<br>



<br>
<br>
<br>
<br>

## 🟠 POS & Dimensions:

<br>


- **WIDTH & HEIGHT:** Create a rectangle that is 20 pixels wide and 30 pixels tall

- **POSITION on the screen:** and place it at the position (100, 50) on the screen

```python
myRect = pygame.Rect(100, 50, 20, 30)
```

[<img src="../pygame-coords.png"/>](https://sigon.gitlab.io/post/2018-10-10-pygame-rect/)

<br>
<br>
<br>

## 🟠 `surface.get_rect()` / `pygame.Rect`

<br>

### 🟪 QUESTION: Which of the following options is more commonly used in Pygame development?


<br>

#### ✅ chatgpt:

- -  `pygame.Rect` is the most widely used and  [canonical](https://canonical.com/) way to handle rectangles in Pygame.

- - `surface.get_rect()` is a standard and commonly used method in Pygame to **obtain the bounding rectangle of a surface**.

<br>

```python
# OPT 1
pygame.Rect(pos, size)
pygame.Frect(pos, size)


# OPT 2
surface.get_rect(point = pos)
surface.get_frect(point = pos)
```

**Therefore**, `Option 1` is the **more standard and widely used approach in Pygame.**

- - If you are working with traditional Pygame development and need rectangles, you’ll typically use pygame.Rect and surface.get_rect().


<br>
<br>

<br>
<br>