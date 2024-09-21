## 🟡 Update and Update with arguments


 <br>
 <br>
 <br>


### 1. 👾 🟠 Now that we’ve created the Player class and added the group argument to its constructor, like this:

```python
class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        try:
            # self.image = pygame.image.load(image_paths['player']).convert_alpha()
            self.image = images['player']
        except KeyError:
```
<br>

### 2. 🌴 🟧 We can move on to incorporating the `update()` method for the sprite group within the main game loop.

#### Adding `update()` to the `While` Loop

- - **Next, we need to add `all_sprites.update()` to our while loop** to ensure that all sprites in the group are updated each frame.

#### Example Loop Integration:

```python
while True:
    all_sprites.update()
    # Update all sprites in the group

    display_surface.fill("lavenderblush2")
    # Clear the screen with a color

    all_sprites.draw(display_surface)
    # Draw all sprites on the display surface

    pygame.display.update()
    # Refresh the screen

```

<br>
<br>

## 🫐 🟡 In-Depth:

### 🧶 Understanding update()



> #### This line below, calls the `update()` method `on every sprite`  <u>in the all_sprites group.</u>

#### `all_sprites.update():`



**Purpose:** Typically used to handle game logic like movement, animations, or state changes for each sprite.

  > #### Each sprite’s update() method is responsible for updating its own state.

<br>

```python
    # 🟨 UPDATE sprite group
    all_sprites.update()


    display_surface.fill("lavenderblush2")

    for pos in star_positions:
        display_surface.blit(star_surf, pos)
```

<br>

## 🟠 Options for update() in Sprite Groups



### 🟦 Basic Update Without Arguments:

```python
group.update()  # Calls update() on every sprite in the group
```

- - **This will call the `update()` method on each** sprite in the group without passing any additional arguments.

- - **Each sprite’s `update()` method should be defined** to handle whatever updates are needed (e.g., movement, animation).

<br>

### 🟦  Update with Arguments:
