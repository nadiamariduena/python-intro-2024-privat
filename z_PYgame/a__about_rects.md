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

<br>

- - - Some third-party libraries or extensions might provide an FRect class or similar functionality.

<br>

### `pygame.freetype`

-  One such library is `pygame.freetype` **for text rendering**, which **uses floating-point precision** for certain **operations**, but it does not provide a general FRect class.

<br>
<br>
<br>

## 🟠 Rects

https://www.pygame.org/docs/ref/rect.html

<br>

### In Pygame, a Rect is like a `nice 🧸 box` that helps us keep track of rectangular areas.

- - ✋ You can make a Rect by choosing where the box starts (its left side and top) and how big it is (its width and height).

<br>

> - -  #### 🔴 Placing surfaces is kind of messy

-  - -  Since we always place the top-left , it requires math to place it in a precise spot



<br>
<br>

### 🟠  Things You Can Do with `Rects`:

<br>
<br>

🟤 **Position Surfaces Precisely:** Use Rects to place images or shapes exactly where you want them on the screen.

- **WIDTH & HEIGHT:** Create a rectangle that is 20 pixels wide and 30 pixels tall

- **POSITION on the screen:** and place it at the position (100, 50) on the screen

<br>

```python

myRect = pygame.Rect(100, 50, 20, 30)

```
<br>

[<img src="pygame-coords.png"/>](https://sigon.gitlab.io/post/2018-10-10-pygame-rect/)

> Source [Pygame Rect Object, a basic guide](https://sigon.gitlab.io/post/2018-10-10-pygame-rect/)

<br>
<br>

🟤 **Detect Collisions:** Check if two objects are touching or overlapping, which is useful for games and interactive applications.

<br>

 - - #### `.colliderect()` method:

- - is a useful function in Pygame for detecting collisions between rectangular areas. It's part of the pygame.Rect class, which is used to handle rectangular regions for positioning and collision detection.

<br>

```python
    # Check if the character is inside the play area
    if not play_area.colliderect(character):
        # Print message if the character is outside the play area
        print("The character is outside the play area!: 🟨")

        # Move the character back inside
        if character.left < play_area.left:
            character.left = play_area.left
```
<br>

 - **Purpose:** The `.colliderect()` method checks if two pygame.Rect objects overlap or intersect with each other.

 <br>

 ### 🩷 Collisions / raycaster

 - Examples: [collisions  | UNITY](https://youtu.be/E6bac9YP6Jc?si=zZqCiGNGthN-fZnh)



 <br>
 <br>


**Check Boundaries:** Ensure objects stay within certain limits by checking if they are inside or outside of specific Rects.

#### example:



```python
import pygame
import sys
#sys.exit() is a good practice for handling program
# termination gracefully, especially when the user closes
#  the game window.

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Rectangle Boundary Example")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create the play area as a rectangle (left, top, width, height)
play_area = pygame.Rect(50, 50, 400, 300)

# Create a character as a rectangle (left, top, width, height)
character = pygame.Rect(100, 100, 20, 20)

# Clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movement speed
    speed = 5

    # Get pressed keys / USE the  arrows
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character.x -= speed
    if keys[pygame.K_RIGHT]:
        character.x += speed
    if keys[pygame.K_UP]:
        character.y -= speed
    if keys[pygame.K_DOWN]:
        character.y += speed

    # Check if the character is inside the play area
    if not play_area.colliderect(character):
        # Print message if the character is outside the play area
        print("The character is outside the play area!: 🟨")

        # Move the character back inside
        if character.left < play_area.left:
            character.left = play_area.left
        if character.right > play_area.right:
            character.right = play_area.right
        if character.top < play_area.top:
            character.top = play_area.top
        if character.bottom > play_area.bottom:
            character.bottom = play_area.bottom

    # Clear the screen
    screen.fill(WHITE)

    # Draw the play area (boundary)
    pygame.draw.rect(screen, GREEN, play_area, 2)  # Draw the boundary of the play area

    # Draw the character
    pygame.draw.rect(screen, RED, character)

    # Update the display
    pygame.display.flip()

    # Limit frames per second
    clock.tick(30)

```
<br>

https://github.com/user-attachments/assets/3397c1ba-e011-49a0-a8c9-f9f915067076


<br>

## 🟡 Other Exercises

 - 🟦 Drawing lines [z_DRAW_line_0](./z_DRAW_line_0.md)

<br>

<br>
<br>

 ### The table

 source [Pygame Rect Object, a basic guide](https://sigon.gitlab.io/post/2018-10-10-pygame-rect/)

```bash
+----------------+---------------------------------------------------------------+
| Attribute      | Description                                                   |
+----------------+---------------------------------------------------------------+
| myRect.left    | Integer, x-coordinate of the left side of the rectangle       |
| myRect.right   | Integer, x-coordinate of the right side of the rectangle      |
| myRect.top     | Integer, y-coordinate of the top side of the rectangle        |
| myRect.bottom  | Integer, y-coordinate of the bottom side of the rectangle     |
| myRect.centerx | Integer, x-coordinate of the center of the rectangle           |
| myRect.centery | Integer, y-coordinate of the center of the rectangle           |
| myRect.width   | Integer, value of the width of the rectangle                  |
| myRect.height  | Integer, value of the height of the rectangle                 |
| myRect.size    | A tuple of two integers: (width, height)                      |
| myRect.topleft | A tuple of two integers: (left, top)                          |
| myRect.topright| A tuple of two integers: (right, top)                         |
| myRect.bottomleft| A tuple of two integers: (left, bottom)                      |
| myRect.bottomright| A tuple of two integers: (right, bottom)                     |
| myRect.midleft | A tuple of two integers: (left, centery)                      |
| myRect.midright| A tuple of two integers: (right, centery)                     |
| myRect.midtop  | A tuple of two integers: (centerx, top)                       |
| myRect.midbottom| A tuple of two integers: (centerx, bottom)                    |
+----------------+---------------------------------------------------------------+

```

<br>

## 🟦 Rect

#### In `Pygame`, a Rect is like a special box that helps us keep track of rectangular areas.

- - You can make a Rect by choosing where the box starts (its left side and top) and how big it is (its width and height).



<br>
<br>

### Equivalent react three fiber

- This is a chatgpt generated code, i think i have an old code (i will be adding it soon)

<br>

```javascript

    <Canvas>
    //pos light x y z
      <ambientLight />
      <pointLight position={[10, 10, 10]} />
// ----------- lights


      <MovableCharacter position={[0, 0, 0]} onCollide={handleCollision} />

      // ---------
      // front screen at x0 y0 on the z axis (will pos frontal)
      <mesh position={[0, 0, 2]}>
        <boxGeometry args={[1, 1, 1]} />
        <meshStandardMaterial color='green' />
      </mesh>
    </Canvas>
```


<br>

```javascript
import React, { useRef, useState, useEffect } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import * as THREE from 'three';

const MovableCharacter = ({ position, onCollide }) => {
  const meshRef = useRef();
  const [collision, setCollision] = useState(false);

  useFrame(({ clock }) => {
    // Movement controls
    const speed = 0.05;
    const move = new THREE.Vector3();

    if (keyboardState['ArrowLeft']) move.x -= speed;
    if (keyboardState['ArrowRight']) move.x += speed;
    if (keyboardState['ArrowUp']) move.z -= speed;
    if (keyboardState['ArrowDown']) move.z += speed;

    // Update character position
    meshRef.current.position.add(move);

    // Collision detection
    const boundingBox1 = new THREE.Box3().setFromObject(meshRef.current);

    // For simplicity, assuming a fixed position for other object
    const boundingBox2 = new THREE.Box3().setFromCenterAndSize(
      new THREE.Vector3(0, 0, 0), // Position of the other object
      new THREE.Vector3(1, 1, 1)  // Size of the other object
    );

    const isColliding = boundingBox1.intersectsBox(boundingBox2);

    if (isColliding && !collision) {
      setCollision(true);
      onCollide();
    } else if (!isColliding && collision) {
      setCollision(false);
    }
  });

  return (
    <mesh ref={meshRef} position={position}>
      <boxGeometry args={[1, 1, 1]} />
      <meshStandardMaterial color={collision ? 'red' : 'blue'} />
    </mesh>
  );
};

const keyboardState = {};

window.addEventListener('keydown', (event) => {
  keyboardState[event.key] = true;
});

window.addEventListener('keyup', (event) => {
  keyboardState[event.key] = false;
});

const App = () => {
  const handleCollision = () => {
    alert('Collision detected!');
  };

  return (
    <Canvas>
    //pos light x y z
      <ambientLight />
      <pointLight position={[10, 10, 10]} />
// ----------- lights


      <MovableCharacter position={[0, 0, 0]} onCollide={handleCollision} />

      // ---------
      // front on the z axis
      <mesh position={[0, 0, 2]}>
        <boxGeometry args={[1, 1, 1]} />
        <meshStandardMaterial color='green' />
      </mesh>
    </Canvas>
  );
};

export default App;

```