# 🧶 Path `/` issue

#### When working with file paths in a Pygame project, the `path` you use to `load assets` like images depends on the directory structure of your project.

- - Initially, the teacher used a relative path with `../images/player.png`, but then **switched** to using `join('images', 'player.png')`.

#### 🍊 The success of these paths depends on where your script is located relative to the assets.

<br>

Here's a summary of the issue and solution based on different project structures:

### 🟤 Initial Path Example:

```python
player_surf = pygame.image.load('../images/player.png')

```

<br>

### 🟤 Alternative Path Example:

```python
player_surf = pygame.image.load(join('images', 'player.png'))
```

<br>
<br>
<br>

### 🟤 Project Structure

```python
PROJECTFolder
   ├── images
   ├── audio
   └── game
       └── game.py

```



- - 🔴 In this structure, using `join('images', 'player.png')` **does not work** because `game.py` is **located** in the game **subfolder**, requiring a relative path ✋ **to move up one level** to **access the images folder**.

<br>

### Avoiding the `..` in Different Scenarios

If you want to avoid using `..`, you need to **make sure that your working directory is always set to PROJECTFolder when you run the script**.

This way, you can use relative paths based on the current working directory:

```python
import pygame
from os.path import join

# Define the path relative to the working directory (PROJECTFolder)
image_path = join('images', 'player.png')

# Load the image
player_surf = pygame.image.load(image_path)

```

<br>
<br>
<br>

## 🫐 Options

- If you're working on a project where the folder containing your assets is nested inside another project with many other games, you might be using a relative path like this:

🟠  Direct Path String (**EASY but not good**)

```python
player_surf = pygame.image.load('../images/player.png')
```

<br>

### 🔴 Issue with Using Relative Paths:


- This approach may work perfectly on your development machine, where the relative path `../images/player.png` correctly points to the image file.

 - - #### However, if you share your project with a colleague or deploy it on a different machine, the directory structure might differ.

 - - ✋ In such cases, the relative path may no longer be accurate, leading to broken image loads.

 - - #### 🔴 This can cause your game to crash or display missing assets if the expected path does not match the actual location of the files.

 <br>

 ### 🔴 Cross-Platform Issues:

 <br>

 The project may be developed on a Windows machine where paths use backslashes `(..\\images\\player.png)`, but **if it needs to be deployed on a Unix-based system (like macOS or Linux), the backslashes won’t work and will cause errors**.

 - - ✋ Hardcoding paths doesn’t account for platform-specific path separators.

 <br>

### 🔴 Version Control Conflicts:

<br>

 ✋ When working in a team, different members might use different folder structures or make changes that affect the paths.

 - - ✋ Hardcoded paths can lead to conflicts and confusion, as other team members might not have the same directory layout.

 #### This complicates collaboration and maintenance.

 <br>

### 🔴 Deployment Complexity:

<br>

**For deployment in different environments** (e.g., a **production server** or a packaged executable), hardcoded **paths might not be valid**.

- - It requires additional configuration to adjust paths, making the deployment process more complex and error-prone.

<br>
<br>

### 🌈 Solution

- IF your `game.py` is **located** in the game **subfolder** , example

```python
# in the below scenario i need to use the ../ to reach the images folder
allPygame
       subFolderGame ✋
        ├── images
        ├── audio
        ├── gameFolder
             └── game.py
```

<br>

#### And not like this:

```python

allPygame
    ├── images
    ├── audio
    └── game.py
```


<br>

### 🌈 THEN the solution for such scenario:


```python
import os
import pygame

# Get the directory of the current script
script_dir = os.path.dirname(__file__)
# Build the path to the image file
image_path = os.path.join(script_dir, '..', 'images', 'player.png')

# Load the image
player_surf = pygame.image.load(image_path)

```

<br>

### 🟦 In my code (within the Subfolder)


```python
import pygame


# ✋
import os

pygame.init()

# ✋
script_dir = os.path.dirname(__file__)


# --- window
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#------
 # title
pygame.display.set_caption("Space shooter")


running = True
surf = pygame.Surface((100,200))
surf.fill('orange')
x = 100



# BEFORE
# player_surf = pygame.image.load(join('../images', 'player.png'))


# ✋
image_path = os.path.join(script_dir, '..', 'images', 'player.png')
# ✋
player_surf = pygame.image.load(image_path)



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


<br>
<br>


#### 🟠 If your project set up looks like the below, then you can use this path `(join('images', 'player.png'))`

```python

allPygame
    ├── images
    ├── audio
    └── game.py
```

<br>

```python

import pygame

from os.path import join


pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Space shooter")

running = True

surf = pygame.Surface((100,200))
surf.fill('orange')

x = 100

player_surf = pygame.image.load(join('images', 'player.png'))


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

<br>
<br>

## 🟡 On the root folder


```python
#0
import pygame
#14
from os.path import join


# 1
pygame.init()
#2 --- window
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
#3
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#------
# 9 change the window caption:
pygame.display.set_caption("Space shooter")
# change icon
# add an img to the project folder and insert it below
# pygame.display.set_icon('')


# 4 LOOP var
running = True


#10 create a surface
# w:100 px & h: 200px
# size of the shape
surf = pygame.Surface((100,200))
# Add color to the shape/Surface
surf.fill('orange')
# 11 anima
x = 100


#15 using join to concatenate
# path = join('images', 'player.png')
# print(path)
#13 IMporting img
player_surf = pygame.image.load(join('images', 'player.png'))

# 5 the Loop
while running:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            running = False


 # FILL the window with a red color
 # player = pygame.Rect((300, 250, 50, 50))
 # https://pyga.me/docs/ref/pygame.html

 # 7 --- DRAW the game ----
 # list of colors: https://pyga.me/docs/ref/color_list.html
    display_surface.fill("lavenderblush2")


    # 12 anima
    # CAREFUL with the identation, otherwise it wont work
    # means **you are increasing** the **value of x by 0.1 each time the loop runs.**
    x += 0.1
    # pos of the shape
    #  Position: Top-left corner at (100, 150) on the display surface
    display_surface.blit(player_surf, (x,150))
    #`Blit()` is a fancy way of saying **You want to put ONE surface on ANOTHER surface**
    pygame.display.update()




# 6 EXIT
# - if you dont add the below, its not going to cause a problem but it will behave
pygame.quit()
```

<br>
<br>

## 🧶 Conclusion

If The teacher’s code works without `..`, it’s likely due to their **working directory being set to the project root when running the script**.

#### Ensuring that your working directory is correctly set or adjusting the script’s path handling to account for directory differences should resolve the issue.