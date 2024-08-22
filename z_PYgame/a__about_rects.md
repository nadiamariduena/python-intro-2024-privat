## 🟠 Rects & Frects



<br>

### Sources:

https://www.pygame.org/docs/ref/surface.html

https://www.pygame.org/docs/ref/rect.html


<br>
<br>





## 🟦 In this section:

### What is the Difference between Rects & Frects

-  In Pygame, `Rect and frect (or FRect)` are **both used to represent rectangular areas**, but **they differ** mainly in the type of **precision** they **use for their coordinates and dimensions**:


<br>

## 🟠  Differences

<br>

🔴 **Precision:** `Rect uses integer` values(20), while `FRect uses floating-point` values(20.5).

<br>


**Use Case:** Use `Rect` for most general purposes where integer precision is adequate, and `FRect` when you need finer control over positioning and dimensions that require floating-point precision.


#### It is ideal for pixel-perfect positioning and size definitions.

### `frect`

In Pygame, the frect type is part of the `pygame.freetype` module and is used in scenarios where you are working with text rendering and need sub-pixel accuracy. **For typical rectangle operations in Pygame, the Rect class is commonly used**.



**Example:**


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
<br>

### 🟣 QUESTION: Is `Frect` standard or commonly used in `Pygame` or related libraries?

<br>

#### ✅ chatgpt:

In Pygame, `Frect` (or frect) is **less commonly used compared** to `Rect`, **and it is not a standard** part **of** the core **Pygame library**.

> - - - ##### As of my last update, Pygame itself does not include an FRect class by default.

<br>

> #### However, the concept of floating-point rectangles is supported through certain extensions or external libraries, or you might use custom implementations. For example:

<br>

### 🟧 Pygame and Floating-Point Rectangles:

<br>

- - 🔴 The standard **Pygame** library **does not include a built-in** `Frect` **class** <u>for floating-point rectangles</u> .

<br>

- - If you need floating-point precision for rectangles, you might have to use or create **custom classes or rely on external libraries.
Third-Party Libraries:**
