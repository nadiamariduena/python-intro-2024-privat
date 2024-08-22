

## 🟡 `convert()` &   `convert_alpha()`

<br>

###   🫐 When Importing an Image, you want to `convert` it to a format that PYgame can work more easily

<br>

- -  if the image has **no transparent** pixels: `.convert()`

- -  if the image **has transparent** pixels: `.convert_alpha()` , this will make your game run much faster.



<br>

### 🧶 Optimizing Image Import for Pygame


#### 🟠 When importing images into Pygame, converting them to a suitable format can significantly enhance performance. Here's how to handle different types of images:

<br>

##  `convert()`

🔸 **For images without transparency:**

- -  Use the `.convert()` **method**.

- - - This will optimize the image's color format for faster rendering, as it ✋ simplifies the image data without the need for transparency support.

<br>

### For example:

a simple `background image` or a `sprite` **with a solid color background.**

-  Use the `.convert()` method to optimize these images. This converts the image to a format that Pygame can quickly render because it doesn’t need to manage transparency.

```python
background = pygame.image.load('background.png').convert()
```
 <br>
 <br>

 - check the video by 🌟  [**Code with Russ**](https://youtu.be/z_tLkRMw-2Y?si=saYnzZFNh6kgGWdZ)


 [<img src="./convert_and_convertAlpha_00.gif"/>](https://youtu.be/z_tLkRMw-2Y?si=saYnzZFNh6kgGWdZ)



<br>
<br>



## `convert_alpha()`

🔸 **For images with transparency:**

- -  Use the `.convert_alpha()` **method**.

- - - This method **preserves the transparency info**rmation and **converts** the **image** into a **format** that **maintains** the `alpha channel`, ✋ **ensuring both quality and performance**.


<br>


### For example,


- `a character` **sprite** with a `transparent background` **or a UI icon** with **see-through areas**.

- - **Use** the `.convert_alpha()` **method for these images**.

- - - This method preserves the transparency of the image, ensuring that the alpha channel (which controls transparency) is maintained for accurate rendering.


```python
character = pygame.image.load('character.png').convert_alpha()
```

<br>

### 🧶 Properly converting your images ensures smoother gameplay and better performance by aligning image formats with Pygame's rendering capabilities.

<br>
<br>


## 🟤 Space Shooter example

 ### 🟦 Applying it to the code

 ```python
 # 18 - convert
player_surf = pygame.image.load(image_path).convert()
 ```


<br>

### 🟠 Output

 - - As you can see, the image **has a black background**, indicating that it contains alpha values.

 #### Therefore, we need to use `convert_alpha()` instead of `convert()`

https://github.com/user-attachments/assets/9d5d2496-5896-4a3c-a4d2-c6b05e621cfa


<br>

###  `convert_alpha()` instead of `convert()`

```python
player_surf = pygame.image.load(image_path).convert_alpha()
```
<br>
<br>

### 🧶 The code

```python
 import pygame

# from os.path import join / path for img (important!!)
import os

pygame.init()
# path for img (important!!)
script_dir = os.path.dirname(__file__)


#  --- window
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
#3
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#  --- window


pygame.display.set_caption("Space shooter")

running = True

surf = pygame.Surface((100,200))
surf.fill('orange')
x = 100




image_path = os.path.join(script_dir, '..', 'images', 'player.png')
# ✋
player_surf = pygame.image.load(image_path).convert_alpha()


while running:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            running = False

    display_surface.fill("lavenderblush2")
    x += 0.1

    display_surface.blit(player_surf, (x,150))

    pygame.display.update()




pygame.quit()
```


https://github.com/user-attachments/assets/56c3366f-dafa-4fdf-9c6d-013720bc587f
