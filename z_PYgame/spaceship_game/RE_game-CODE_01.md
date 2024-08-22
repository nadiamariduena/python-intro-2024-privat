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

