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


