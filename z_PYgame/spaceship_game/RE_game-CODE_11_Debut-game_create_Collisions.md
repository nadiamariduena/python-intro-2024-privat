
 # 🟡 SPRITES 6.

 <br>

- #### collision 🔫 🪨 💥 [DOCS](https://www.pygame.org/docs/ref/sprite.html)




<br>
<br>
<br>
<br>
<br>

---




# 🟡  Collisions




## 🟧 Understanding collisions


### 🫐  How to Check Collisions in Pygame



### ⚫ <u>There are `two main ways to handle collisions`</u>  in Pygame:

<a name="two_ways_to_handle_collisions"></a>

<br>

## 🟩 Way 1: Rectangle Collisions

> #### What It Is: You can use rectangles to check for collisions.

- - Each game object (like our meteors and player) can be represented as a rectangle.

<br>

**How It Works:** A rectangle can check for collisions in `three ways`:


<br>

- - - **With a Single Point:** Determine if a specific point is inside the rectangle.

- - - **With Another Rectangle:** Check if two rectangles overlap.

- - - **With a List of Rectangles:** See if a rectangle intersects with any rectangle in a list.



<br>

### Pygame offers several methods to check for collisions.

#### Common Collision Methods

> 🟤 Although there are quiet a few variations, check the  [documentation](https://www.pygame.org/docs/ref/rect.html)

<br>
<br>



## 🟩 Way 2: <u>Sprite Collisions</u>




**What It Is:** Sprite collisions focus on checking interactions between individual sprites (like our meteors) and groups of sprites.

**How It Works:** You can easily check if one sprite collides with any other sprite in a group, which is useful for detecting collisions in complex scenes.


### `spritecollide()`

>##### Check the  [documentation](https://www.pygame.org/docs/ref/sprite.html)


---

<br>
<br>
<br>
<br>
<br>





## ⬛ Before Moving on

### 💡 Before Implementing Group Collision Logic:

>Before diving into the full group collision logic, we’ll run some tests.

- 🔴 **Don’t skip** this step it’s important because **it will help you understand why we don’t use certain collision methods** in our game.

<br>

### 🟡  <u>Differences Between collidepoint and colliderect</u>

<a name="Differences_Between_collidepoint_and_colliderect"></a>



### 🟢 collidepoint:

- - Checks if a **specific point** (like (100, 200)) is inside the player's rectangle.

> #### It’s great for **precise checks**, like seeing if the player clicked on an object.

### 🟢 colliderect:

#### Checks if two rectangles overlap.

> #### It’s better for situations where you want to know if two objects (like the player and an obstacle) are touching or intersecting.

<br>