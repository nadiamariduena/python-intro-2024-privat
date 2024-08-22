# 🟡 Phase 2

<br>

- **Load several img's** [Go to section](#load_severalimgs)


- **Avoid Unecessary computation**

- - - Understanding the issue [Go to section](#expensive_comp)


<!-- <a name="expensive_comp"></a> -->

<br>
<br>

## 🟠 In this section: I will follow the tutorial’s steps to implement <u>the image generation process</u> .

<br>

- - I will create and position **20 instances of images**.

<br>

- -  ✋ **Additionally, as a personal enhancement**, we will introduce a dictionary to manage multiple images more efficiently.

<br>



<br>
<br>

## 🌈 Steps:

- -  I will first **create a dictionary to manage** multiple **images** efficiently.

<br>

- - Following that, I will **implement a NEW loop** to generate 20 instances of these images.

<br>

- - - During this process, I will also address **potential issues** that might arise when handling the loop, such as ensuring unique positions and managing any possible conflicts or errors.

<br>

<br>




<a name="load_severalimgs"></a>


## 🟠 Importing several img's

### Option 1. Tutorial Approach

- -  First, import the image **star**

```python

star_surf = os.path.join(script_dir, '..', 'images', 'star.png')

```

<br>
<br>


### 🍍 Option 2. Implementing a `Dictionary` of image paths

### as a personal enhancement, i will introduce a dictionary to manage multiple images.

-  This approach mirrors the way JavaScript arrays can be used

```python
# 16
# Build the path to the image file
# ✋ BEFORE
# image_path = os.path.join(script_dir, '..', 'images', 'player.png')
# -----


# ✋ AFTER
# 19 import several images, so to not repeat the above line
# Dictionary of image paths
image_paths = {
    'player': os.path.join(script_dir, '..', 'images', 'player.png'),
    'star': os.path.join(script_dir, '..', 'images', 'star.png')
}
```

<br>
<br>


### 🟠 Load the images




```python
# ✋ BEFORE
# 17 Load the image
# player_surf = pygame.image.load(image_path)
# 18 - convert
# player_surf = pygame.image.load(image_paths).convert_alpha()


# ✋ AFTER
# 20 Load the images
player_surf = pygame.image.load(image_paths['player']).convert_alpha()
star_surf = pygame.image.load(image_paths['star']).convert_alpha()

```

<br>
<br>

## 🟠 The loop

<br>

### The position of the star 🌟

- -  If you add the below line within the while loop, its not going to animate, because the **300** is replacing the **x**


```python
display_surface.blit(star_surf, (300,150))
```

- To ensure the animation works correctly, **avoid hardcoding** the position value in the blit function.

- -  #### 🟤 Instead of using a `fixed` value like the `300` like 300, use the could use the variable `x` that changes over time, just like we did for the plane, but WE DONT WANT that, `we want to add a random position for 20 stars`


<br>

```python
# ✋ We are not going to use the value of the X here below
x = 100


image_paths = {
    'player': os.path.join(script_dir, '..', 'images', 'player.png'),
    'star': os.path.join(script_dir, '..', 'images', 'star.png')
}


player_surf = pygame.image.load(image_paths['player']).convert_alpha()
star_surf = pygame.image.load(image_paths['star']).convert_alpha()


# LOOP
while running:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            running = False


    display_surface.fill("lavenderblush2")

    x += 0.1

    display_surface.blit(player_surf, (x,150))
    # ✋ we dont need this animation
    display_surface.blit(star_surf, (x,150))
```
<br>

- As you can see, the star also features animation

https://github.com/user-attachments/assets/b77eaa6b-2f63-477f-a144-e9f2231a0897



<br>
<br>

<a name="loop_vers_01"></a>

### 🌟 LOOP:  Place 20 stars Randomly 🌟

- import **randint**

```python
# after you add the images within the WHILE loop, import the star and randomize it
from random import randint
```

<br>

### 🟤 Create the `for` loop within the `While` loop and nest the `star` img



```python
for i in range(20):
# for the_star in range(20)
```

<br>

### 🟠 Since we are using random, we don't need the `x and y` values, like we have been using here below:

```python
for i in range(20):
    display_surface.blit(star_surf, (300,150)) # 🔴 We don't need the x:300, and y:150 values
```

<br>

### 🟤 Instead we need to grab the `X and Y` position of the window

- - in most graphical **coordinate systems**,

- - - **the origin (0, 0)** <u>is typically at the top-left corner of the window or canvas.</u>


```python

 0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)
```

 <br>
 <br>

##  🍨 Here’s how the coordinates usually work:

<br>

**x-coordinate:**

- -  This starts at **0** on the **left edge of the window** or canvas and increases as you move to the right. So, 0 for the x-coordinate is the far left.

**y-coordinate:**

- -  This starts at **0** on the **top edge of the window** or canvas and increases as you move downward. So, 0 for the y-coordinate is the top, and the value increases as you move towards the bottom.

<br>

#### READ MORE:  [Cartesian coordinate](../../z_Cartesian_coordinate_plane.md)


<br>
<br>
<br>

## 🟠 The Line below


- - **The Line Below Draws** the `star_surf` surface at a random position on the display_surface, where `(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT))` generates random coordinates within the dimensions of the window.

```python
 display_surface.blit(star_surf, (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))
```


https://github.com/user-attachments/assets/99e33a31-87c6-46f7-b7d1-2c2950d092dc


<br>
<br>

---

<br>
<br>

<a name="expensive_comp"></a>

### 🔴 At this point, we have the stars ✋ <u>but its not exactly how it should be</u>

<br>




## 🟦  Expensive

- In the code, We have a section where we're `blitting` stars onto the display surface using random **coordinates**:


```python
   for i in range(20):
        display_surface.blit(star_surf, (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT) ))
```
<br>
<br>

## 📌 Why its expensive?



### 🟦 Understanding the issue

The **`randint`** function in this line: `(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT) )`, **is responsible for generating random integers for the X and Y coordinates**.

> ### Since this function is called  every frame, it generates new random positions for the stars <u>each time the game loop iterates</u> 🎠 .

<br>
<br>


```python

while running:
for event in

# 🔴 In this loop, the randint function is invoked
# on each frame update, causing new random coordinates
#  for the stars to be calculated every frame.
# 🔴 This results in the stars appearing at different
#  positions each frame, which can make them look like
#  they are flickering or moving unpredictably.
```

<br>

###  🟤 How This Affects our Game

The issue arises because this line of code is inside a loop (while loop) that runs continuously, typically within a game loop structured like this:

```python
# 5 the Loop
while running:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            running = False
```
<br>

### 🟤 As a result:

- - Each time the game loop iterates, new random positions are generated for the stars.

- - - #### 🌟 This causes the stars to appear in different locations with every frame, <u>which can make them look like they are flickering or constantly moving.</u>

<br>

```python
  for i in range(20):
        display_surface.blit(star_surf, (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT) ))
```
