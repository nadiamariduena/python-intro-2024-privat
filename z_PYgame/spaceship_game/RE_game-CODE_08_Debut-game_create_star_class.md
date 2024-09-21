
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

> - - #### This means you aren't actually loading the image into memory 20 times, but you are referencing the same loaded surface for each star.

> - - This is efficient because it prevents redundant loading and keeps memory usage optimized.

<br>

### 🔴 💥 Potential Issues:

#### 🔺 If there were an error in loading the image (e.g., if the file path was incorrect), 🔺 <u>each failed attempt would result in creating a new surface (the yellow rectangle in your code) for that star</u> .

> #### This could lead to unnecessary memory usage if many stars failed to load the intended image.


<br>

## 🌈 Solution

#### Import the `Surface` before we are creating the `Star`

<br>

[2:12:23](https://youtu.be/8OMghdHP-zs?si=Mxu_alNnM31TIn_m&t=7943)

<br>

## 🟠 1. Tutorial solution:

- 🟤 **a)**  First, **create a variable named `star_surf`** to store the star image.

- - Load the image and convert it for optimal rendering:

```python
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()

```

- 🟤 **b)**  **Next, pass this `star_surf` variable when creating instances** of the Star class:

```python
Star(all_sprites, star_surf)
```
## 🟩 The Advantages of Managing Images in One Place

#### By centralizing your image handling, you simplify your code.

> - - #### 🌈 Instead of loading the star image multiple times, you do it just once and reuse it wherever needed.

> - - #### This not only reduces redundancy—making your code cleaner—but also boosts performance because loading an image is a relatively expensive operation.

<br>

### 🟦 Think of it like this:

if you had to go grocery shopping every time you wanted a snack, you'd waste a lot of time.

- - Instead, you grab everything in one go and have it on hand! This approach not only saves resources but also makes it easier to manage changes.

> #### If you decide to update the star image later, you only need to do it in one place.

Your game runs smoother and stays more organized, allowing you to focus on creating exciting gameplay instead of getting bogged down in repetitive tasks.

Plus, a tidy codebase is easier to read, making collaboration and future updates a breeze!

<br>

- 🟤 **c)** Integrate the Star Surface into the Star Class


- - Now, we want to enhance our Star class by passing the star surface directly as an argument.


#### This allows for better organization and performance.

**Modify the Constructor:** Update the Star class to accept the star surface as an additional parameter: `(self, groups,star):`.


 ```python
 # BEFORE
 class Star(pygame.sprite.Sprite):
    def __init__(self, groups):



# AFTER
 class Star(pygame.sprite.Sprite):
    def __init__(self, groups,star):
             super().__init__(groups)
             try:

             self.image = surf
 ```

 > #### By implementing this change, we ensure that each star instance directly references the pre-loaded surface, improving efficiency and keeping our code organized!

<br>
<br>
<br>
<br>

### 🟠 2. My solution:

#### 🟣 QUESTION:

  **Since my previous code already includes a `for` loop to load images** from the `image_paths` dictionary and handle errors, should I be concerned about loading the surface 20 times?

> - - #### 🟨 The loop ensures each image is only loaded once, and if there's an error, it provides a fallback surface. Does this mean I don't need additional implementation to prevent redundant loading?

```python
# Load images and handle errors
# Notice how we grab the dictionary "image_paths"
for key, path_imgs in image_paths.items():
    try:
        #LOAD and CONVERT the image in one step
        images[key] = pygame.image.load(path_imgs).convert_alpha()

    except pygame.error as img_item:

        print(f"Failed to load image '{path_imgs}': {img_item}")
        # Fall img IF LOAD fails
        images[key] = pygame.Surface((50,50)) # square
        images[key].fill((249, 255, 51 )) # yellow acid
```

<br>

#### ✅ CHATGPT:

#### 🌈 you've correctly loaded the images in a separate loop before creating the Star instances.

- - This means that by the time you create the stars, the images are already in memory.

<br>

### 🟧 Clarification

**Initial Loading:**

The for loop you provided **<u>loads the images once </u> into** the `images` **dictionary**.

- - This is **efficient** because **it only attempts to load each image a single time**, ensuring that your assets are ready to be used.

<br>

## Conclusion

✅ CHATGPT: Your approach is efficient because you're loading all images once at the beginning, which minimizes memory usage and loading times during gameplay.

```python
#🟨 imgs -----
script_dir = os.path.dirname(__file__)
# img's path
image_paths = {
    'player': os.path.join(script_dir, '..', 'images', 'player.png'),
    'star': os.path.join(script_dir, '..', 'images', 'star.png'),
    'meteor': os.path.join(script_dir, '..', 'images', 'meteor.png'),
    'laser': os.path.join(script_dir, '..', 'images', 'laser.png')

}

# INIT the images dictionary
images = {}

# Load images and handle errors
# Notice how we grab the dictionary "image_paths"
for key, path_imgs in image_paths.items():
    try:
        #LOAD and CONVERT the image in one step
        images[key] = pygame.image.load(path_imgs).convert_alpha()

    except pygame.error as img_item:

        print(f"Failed to load image '{path_imgs}': {img_item}")
        # Fall img IF LOAD fails
        images[key] = pygame.Surface((50,50)) # square
        images[key].fill((249, 255, 51 )) # yellow acid
```

> #### By using a dictionary to store these images, you can easily access them later without the overhead of reloading.
