# 🟡 RAYCASTING




<br>

### 🟦 Before we get into raycasting, it's helpful to first understand Pygame's collision system.

### 🥥 Pygame

- #### Pygame uses a variety of methods to detect collisions between shapes, such as rectangles and circles, based on their boundaries.

- - These methods are primarily designed for simpler, axis-aligned shapes, which works well for many 2D games.

<br>

### 🥥 Raycasting

#### Raycasting, on the other hand, is a more advanced technique used to simulate the behavior of light rays, determining what they intersect in a 2D or 3D space.

- - 💡 Understanding **Pygame's collision** system **will give** you a **solid foundation** to **better grasp** how **raycasting** can be applied.

> #### <u>raycasting sends out those rays to see what’s in front of you. 🧸 It’s like looking ahead and saying, **“There’s a wall there!”**</u>  🍯

#### READ MORE: [Go to section| RAYCASTING](#RAYCASTING_)


<br>
<br>
<br>

---


## 🫐 🟡 Understanding Collision Limitations

<br>

### When we talk about collisions in Pygame, it's important to know how they work.

> - - ### 🌈 Pygame is like a helper that checks if things are touching each other, but it has some limitations.

<br>

### 🟤 What Does Pygame Do?

>Pygame’s collision system mainly looks for overlaps between rectangles.


**Example:** `A Ball and a Wall` 🧶

> #### Imagine you’re playing with a bouncy ball in a room:

**The Ball:** This is like your player character.

**The Wall:** This represents an obstacle in the game.

#### What Happens When the Ball Hits the Wall?

> #### When you roll the ball towards the wall, you want to know if it touches the wall.

#### `Pygame` can tell us when the ball (the player) is touching the wall. It says, “The ball is hitting the wall!”

### 🔴 The Limitation

> #### However, just knowing that the ball is touching the wall doesn’t stop it from going through.

### 🟠 Rule

#### To make it realistic, you need to add a rule: “If the ball touches the wall, it should stop moving forward!”

### 🟧 Why Is This Important?

#### This means that while Pygame helps you see when two objects are touching, you need to add your own rules to make sure the ball (or player) behaves correctly in the game world.

<br>
<br>

### 🟣 QUESTIONS: Is this similar to raycasting?

#### ✅ chatgpt:

- - Yes, it's somewhat similar to raycasting!

<br>

<a name="RAYCASTING_"></a>
