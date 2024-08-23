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

**Child Element Positioning:** If you position a child element at 10% from the left and 20% from the top within this container, it translates to:

<br>

- - **Horizontal Position:** 10% of the container’s width.



> - - ####   Since the container is 100vw wide, 10% of this width is
`0.10 × 100 vw = 10 vw 0.10×100vw=10vw`.



> - -   **Vertical Position:** 20% of the container’s height. Since the container is 100vh tall, 20% of this height is 0.20 × 100 vh = 20 vh 0.20×100vh=20vh.

#### Thus, the element will be positioned 10vw from the left edge and 20vh from the top edge of the container.

<br>
<br>

## 🟦 Key Points:

**Viewport Units:**

- - The dimensions of the parent container are defined in viewport units (`vh and vw`). In this case, **100vh and 100vw mean** that the **parent container occupies the entire viewport** height and width, respectively.

**Percentage Conversion:**

- - When you use percentage values for positioning, they are calculated based on the size of the parent container. So if the container size is defined in viewport units, the percentage-based positions will also be in viewport units.

<br>


**Relative Positioning:**

- -  Regardless of whether the parent container’s size is in pixels, viewport units, or any other units, the percentage values you use for positioning will always be relative to the size of the parent container. This ensures that the child element’s position is proportional to the parent’s dimensions.