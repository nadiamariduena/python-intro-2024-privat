### 🍊 It's slightly different from using absolute positioning (FRONTEND), but the concept is similar.

-  Always be mindful of the size of the parent container when setting positions.  **[check this before reading the below](./z_DRAW_line_0.md)**


<br>
<br>

### 🟦 In this Example, we are drawing a horizontal line on the screen:

- The line **starts** at **pos**ition (`10 x, 100 y`)on the screen.  **(what would give in pos absolute: 10% x axis, 20.83 y axis)**

<br>

- It's slightly different from using absolute positioning, but the concept is similar. Always be mindful of the size of the parent container when setting positions. [read more]()

```bash
Percentage=(
480
___
100 )×100 ≈ 20.83%
```

<br>

### 🟠 Absolute Positioning

<br>

**Absolute Positioning:** Elements are placed at **specific coordinates** `relative` to their `containing block` **or** the `viewport` (**in the case of web development**).

> #### The position does not change unless the coordinates are modified.

<br>

### 🟠 Relative to Parent Container

**Relative to Parent Container:** Elements are positioned based on their parent container's dimensions and position. This means that the position of an element is dependent on the size and position of the parent container.

<br>

### 🟣 QUESTION:

- - **WHEN YOU SAID: Relative to Parent Container:** Placing an element at (10, 100) within a container means it will be 10 pixels from the left and 100 pixels from the top of the container, which might be different from the screen coordinates if the container itself is positioned differently

> #### 🟣 but imagine it s not 10 in px, but 10% of a parent component that isn't 400 px but 100vh & vw, then the 10 its equivalent to 10%

<br>

### ✅ chatgpt

 **Yes**, when using percentage-based positioning within a **parent container** sized in **viewport units** (`vh and vw`), the percentages are **calculated relative to those viewport units**.
>  This means that a percentage value translates directly to a portion of the container’s dimensions, maintaining proportional positioning.

<br>

<br>

## 🟠 Explanation:

### Example Scenario Parent Container Size:

#### Let’s say you have a parent container that is 100vh tall and 100vw wide.

  This means the container spans the full height and `width of the viewport`.

  <br>