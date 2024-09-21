
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

<br>


## 🔴 But Now, We Don’t Have to Do That Anymore!

**By moving the random positioning logic into the `Star class`**, we can create each star in a random location directly in the __init__ method.

#### Extract the random position code:

```python
randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)

```

<br>


## 🟫 Step 4.  Integrate Random Positioning into the Star Class

#### In this step, we’ll focus on assigning random `x and y` positions for each star using the `get_frect method`.




### 🟠 Handling the X and Y Axes

#### For the X-axis, we’ll use:

```python
self.rect = self.image.get_frect(center=(randint(0, WINDOW_WIDTH), y))

```
#### For the Y-axis, we’ll include:

```python
randint(0, WINDOW_HEIGHT)
```




### 🟠 Implementation in the __init__ Method

- - Combine these concepts to set the star's rectangle as follows:

#### In the `__init__` method, set the star's rectangle using:

```python
self.rect = self.image.get_frect(center=(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))

```

### This means each star will be placed in a random location when it is created, ensuring a varied and dynamic visual experience while keeping performance optimized.

<br>
<br>
<br>
<br>

---

##  🟠 Why Random Positions Before the Game Runs?

#### Generating random positions before the game starts prevents stars from moving on every frame.

> #### By calculating their positions only once, we enhance performance and maintain a static background, allowing players to focus on the action without distracting movement.

---

<br>
<br>
<br>
<br>


 ## 🟫 Step 5. remove the previous line

 #### `star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]`

 - - Finally,  **remove the previous line that generated star_positions entirely.**

```python
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

```

 > #### This change simplifies the code and ensures that each star's position is set when it is created, eliminating unnecessary calculations during the game loop.

<br>
<br>
<br>
<br>

## 🟫  Step 6. Now to Actually Create the Stars:

<br>

###  In this step, we'll implement a `for` loop to `generate` our `star sprites` efficiently.

> #### 🌟 By initializing all stars at once, we maintain performance and avoid unnecessary processing in the main game loop.

### 🟢 Implementation Example

#### Here’s how the star creation will look in code:

```python
for i in range(20):
    Star(all_sprites)

```

<br>
<br>

## 🟧 Key Considerations

### 🟤 Remove the Previous Star Creation Loop

#### First, eliminate any previous loops that were creating stars within the while loop.

```python
# REMOVE the below 🔴 ------
    # for pos in star_positions:
    #     display_surface.blit(star_surf, pos)
# -------------------


    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)

    # ---- sprites ----
    all_sprites.draw(display_surface)



    pygame.display.update()

pygame.quit()
```

<br>

> - - #### ⚫ This change is crucial because `generating stars continuously in the main loop can lead to performance issues` and clutter the visual output.

#### We want to create our stars once at the beginning to streamline the rendering process.

<br>


## 🟧 Position the `Player` Instantiation Correctly

#### 🟤 Ensure that the line creating the player instance `(player = Player(all_sprites))` is placed after the star creation loop.

```python
all_sprites = pygame.sprite.Group()
# Create PLAYER class instance
#
for i in range(20):
    Star(all_sprites)
## the player line below, has to be positioned under the Star(all_sprites), otherwise the star will appear on top of the player and it doesnt look good
player = Player(all_sprites)


```

<br>

> - - #### 🌈 This ordering is important because if the player is instantiated first, stars may appear visually on top of the player, which disrupts the intended layering of game elements.


<br>





<br>
<br>

## 🟧 Understanding `Star(all_sprites)`

#### 🌈 🧸 When we instantiate stars using `Star(all_sprites)`, we're adding each star to the `all_sprites` group.

<br>

 - -   This centralized **`group`allows us to manage all sprites collectively updating and drawing them in a single call** .

 > #### It simplifies code maintenance and improves efficiency, ensuring our game runs smoothly as the number of objects increases.


 <br>
<br>
<br>
<br>

---

[2:12:00](https://youtu.be/8OMghdHP-zs?si=MbEixie5ucL7wma6&t=7920)


## 🟫  Step 7.  Performance issue related to loading the surface multiple times



<br>
<br>

🟣 **QUESTION:** The teacher mentioned that when we use a for loop to create 20 stars, **we are essentially rendering the star surface 20 times.** Is this correct?

<br>

✅ **CHATGPT:** When we use a for loop to create 20 stars in Pygame, **we are indeed instantiating 20 separate Star objects**.

> - - #### Each star requires its own image and surface, which can lead to increased memory usage.

> - - #### Additionally, if rendering is involved, the graphics pipeline processes each star individually, potentially impacting performance.

#### This means we are rendering the star surface 20 times. So, yes, the teacher's statement about charging 20 times for the surface is correct.

<br>

## 🟦 Explanation

🟠 **Surface Loading:**

**When you create an instance of the `Star` class**, **the `__init__` method runs**, which attempts to load the star image from the images dictionary.

- - If the image is loaded successfully, it uses that surface for all star instances.

<br>

**Efficiency Considerations:**

#### 🌈 If the image is successfully loaded the first time, all subsequent instances will reuse that same surface.
