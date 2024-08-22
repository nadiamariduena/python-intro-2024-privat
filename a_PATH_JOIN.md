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
