
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
