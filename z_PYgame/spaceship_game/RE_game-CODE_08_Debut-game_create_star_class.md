
# 🟡 SPRITES 3.

<br>
<br>

<!--

<a name="What_We_will_Be_Doing_"></a>

## 🫐🟡 <u>What We’ll Be Doing </u>

-->

### 🟠 Intro:


- - What We’ve **Accomplished:**  [Go to section](#What_We_ve_Accomplished_)

- - What **We’ll Be Doing:** [Go to section](#What_We_will_Be_Doing_)



<br>
<br>



<br>
<br>
<br>
<br>
<br>
<br>

---

<br>

<a name="What_We_ve_Accomplished_"></a>

## 🫐 What We’ve Accomplished:

- -  In Lesson 8, we focused on enhancing player movement and understanding input handling in our game.

<br>

### Here’s a brief recap of what we accomplished:

**Reintroduced Movement Logic:** We copied the key direction input code into the update() method of the Player class to enable smooth navigation.

**Normalized the Direction Vector:** We ensured that the direction vector is normalized, which helps maintain consistent speed, especially when multiple keys are pressed.

**Defined the Speed Variable:** We set a speed variable to control how fast the player moves, enhancing the responsiveness of the gameplay.

**Incorporated Delta Time:** We integrated delta time (dt) to ensure that movement remains fluid and consistent across different frame rates, improving the overall game experience.

<br>
<br>

#### ⚫ Global Accessibility

**Explored Global Accessibility of Delta Time (dt):** We discussed how dt can be accessed globally and its implications for our code.

-  **Global Scope** to access Delta Time:  ( 🔺 **not a good practice in some scenarios**)

<br>

#### ⚫ `Issues with get_just_pressed()`

**Identified Issues with get_just_pressed():** We recognized that using pygame.key.get_just_pressed() might lead to errors in recent Pygame versions and noted this as a caution for future lessons.

<br>
<br>
<br>
<br>
<br>
<br>


---

<a name="What_We_will_Be_Doing_"></a>

## 🫐 🟠 <u>What We’ll Be Doing </u>

<br>

## 🟨  Creating and Optimizing the Star Class

In this lesson, we will focus on enhancing our game by implementing a `Star class` with efficient image handling and sprite management.



###  Summary of Today's Lesson:

<br>

🟤 **Define the Star Class:**


- - We will create a new class for our stars that inherits from `pygame.sprite.Sprite`, laying the foundation for our star objects.

🟤 **Initialize the Star Class:**

- - Inside the `Star` class, we will set up an `__init__` method to load the star image and define its rectangle for positioning, ensuring each star has its own properties.

🟤 **Implement Random Positioning:**

- - ✋ Instead of generating star positions during the game loop, we will move this logic to the Star class, creating each star at a random location directly when it’s initialized.

🟤 **Integrate Random Positioning:**

- -  ✋ We will assign random `x and y coordinates` **for each star using** the `get_frect` method, ensuring a dynamic visual experience.

🟤 **Remove Redundant Code:** We will eliminate unnecessary lines that previously generated star positions, streamlining our code and improving performance.

🟤 **Batch Create Stars:** We will use a for loop to efficiently create 20 star sprites in one go, enhancing performance by reducing processing in the main game loop.

🟤 **Ensure Correct Player Positioning:**

- - ✋ We will ensure the player instance is created after the stars, preventing visual overlap and maintaining a clean layer structure in the game.

🟤 **Centralize Image Loading:** We will discuss loading the star image only once, creating a variable `(star_surf)` to manage it, and passing this variable when creating star instances to enhance performance and reduce redundancy.

🟤 **Optimize the Star Class:**

- - We will modify the Star class to accept the star surface as a parameter, ensuring each instance uses the same loaded image, improving efficiency and organization.


 <br>
<br>
<br>
<br>
<br>
<br>
<br>


---

# 🟦 Let’s Get Started:

# 🟡 Creating the Star Class

<br>

<br>

## 🟫 Step 1. Create the Star Class

#### Start by defining a new class for our stars that inherits from `pygame.sprite.Sprite`.

<br>
<br>



## 🟫 Step 2. Initialize the Star Class

#### Inside the Star class, create an __init__ method to initialize each star.

<br>

 - - Here, **you'll load the star image** and **set its rectangle (rect)** for positioning.



> - - ####  This setup ensures that each star has its own properties and can be individually controlled, making your code cleaner and more organized.


<br>
<br>

## 🟫 Step 3. Create 20 Star Sprites in Random Positions

- - **Instead of generating star positions** in the **main** game **loop**,  we’ll generate them during the initialization of each star.

#### Previously, we used:


```python
# before
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]


# and on the WHILE loop
#
  display_surface.fill("lavenderblush2")
    for pos in star_positions:
        display_surface.blit(star_surf, pos)
```

