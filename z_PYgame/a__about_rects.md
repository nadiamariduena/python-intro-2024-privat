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
