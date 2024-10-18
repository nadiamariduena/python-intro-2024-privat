
# 🟡 SPRITES 9.





[3:01:49](https://youtu.be/8OMghdHP-zs?si=CX6sc2Zze0JsHHXn&t=10909)

<br>

## 🟦 Score

### 🟠 In this lesson, we’re going to learn how to set up a score system for our Pygame space shooter game!

<br>

> #### So far, we’ve worked on important things like handling collisions and even setting up text colors.

> #### Now, it’s time to bring everything together by adding a score that keeps track of how well the player is doing.

<br>

### 🟠 A score will make the game more exciting by rewarding players for shooting down enemies or surviving for longer.

#### In this lesson, you’ll learn how to display the score on the screen and update it as the game progresses.

---

<br>
<br>
<br>

##  🟦 Lets get started:

### 🟤 1. Create a Function to Display the Score

> #### To show the score on the screen, we first need to create a function dedicated to displaying the score.

This will allow us to manage and update the score as needed during gameplay.

```python
def display_score():
```
<br>

### Why a function?

Functions help us organize the code, making it easier to call the same block of code multiple times. This is useful if we need to update the score at different points in the game.

#### What’s inside the function?
Inside the function, we will use Pygame's font.render() method to create a text surface (the score text) that we can then draw on the game screen.

<br>

### 🟤 2. re position the text within the function score

- When you add the **`text_surf`** inside the function, it will **no longer be accessible within the `while`** loop. (just for now)
```python
def display_score():
    text_surf = font.render('text', True, (255,255,255))


```

<br>

### 🟤 3. Track the Elapsed

### `pygame.time.get_ticks()`



#### 🟧 To keep track of time within your game or application, it is essential to capture the number of milliseconds since pygame was initialized.

> ####  This is where `pygame.time.get_ticks()` comes in.

### `current_time = pygame.time.get_ticks()`

#### This line gets the current time in milliseconds (thousandths of a second) since the game started.

> - - ####  Think of it like a **stopwatch** ⏱️ that has been running since you launched your game.

- - -  **You can use this value to see how much time has passed**, which is **useful for** things like **delays, animations, or when you want** to **do something after a certain amount of time**.



```python
def display_score():
    current_time = pygame.time.get_ticks()
    text_surf = font.render('text', True, (255,255,255))
```

<br>

### 🟤 4 Replace the `'text'` with `current_time`

 When you want to display the time (in milliseconds) instead of a simple static text like "text", you need to pass the current time to the `font.render()` function.

```python
#before
    text_surf = font.render('text', True, (255,255,255))
```

<br>
<br>

 > ### In this case, you're replacing the `'text'` with `(current_time)`.

  This ensures that the surface now shows the actual time in milliseconds, retrieved by `pygame.time.get_ticks()`.

```python
#after
    text_surf = font.render(current_time), True, (255,255,255))
 ```

<br>

### 🟤 5. Convert it with `str()`

#### 🔴 If you tried to test it, you will see you will get an error, to solve this add the `str()`

```python
    text_surf = font.render(str(current_time), True, (255,255,255))
```



#### 🟠 Why use `str()` here?

`pygame.font.render()` expects the text to be displayed as a string.

🟢 However, **`current_time` (the result of `pygame.time.get_ticks()`)** is a number (an integer representing milliseconds).

-  - 🟢 `str(current_time)` **converts the integer value of `current_time` into a string**, so it can be rendered as text on the screen.


### Putting it together:

```python
def display_score():
    current_time = pygame.time.get_ticks()
    text_surf = font.render(str(current_time), True, (255,255,255))
```

<br>
<br>
<br>
<br>

---

## 🟤 6.  Creating a Rectangle for the Text:

- This is just for testing purposes but it has a goal, we will see it later

```python

def display_score():
    current_time = pygame.time.get_ticks()
    text_surf = font.render(str(current_time), True, (255,255,255))
    # text_rect = text_surf.get_frect(midbottom = (x,y))
    text_rect = text_surf.get_frect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT -50))
    display_surface.blit(text_surf, text_rect)
```


<br>


### RECAP & Explanation:

#### `(text_rect = text_surf.get_frect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 50)))`

> #### This line is responsible for defining where the text will be displayed on the screen. Let's go through it in detail:



#### `text_surf.get_frect()`:

- - This gets the rectangle (or Rect object) that fits the text surface.

> - - This rectangle will help us position the text on the screen.

<br>

#### `midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 50)`:

- - This places the text at the center horizontally (WINDOW_WIDTH / 2) and 50 pixels above the bottom of the screen.

> - - The midbottom property positions the text so that its bottom center is exactly where you want it, which ensures the text is centered horizontally but placed a little above the bottom edge of the window.

---

<br>
<br>

<br>
<br>

## 🟤 7.   Update the Game Loop to Display the Score

#### Now that we have set up the function to display the score, it's time to integrate it into the game loop.


#### Replace the old text blitting with the following:

-  Previously, you might have used something like this to display text:

```python
    display_surface.blit(text_surf, (0, 0))  # Blit the text at position (x, y)
```

>However, instead of directly blitting the text onto the screen, we will now use the display_score() function we created earlier to handle displaying the score.

#### For this

#### call the `display_score()` function to render the score at the proper position on the screen.

```python
    display_surface.fill("#2a0822")
    all_sprites.draw(display_surface)


    display_score() #🟡
    pygame.display.update()

pygame.quit()
```


#### If you changed this value

```python
# before
   current_time = pygame.time.get_ticks()
# after
      current_time = pygame.time.get_ticks() // 100
```

### 🟠 What Does // 100 Do?

#### The `//` operator is integer division, which divides two numbers and returns the whole number result, discarding any remainder.

- So, when you divide `pygame.time.get_ticks()` by 100, you are effectively converting milliseconds into "hundredths of a second."

- - `pygame.time.get_ticks() // 100` **divides the time in milliseconds by 100**, which reduces the number of units we’re working with.

> #### This converts milliseconds into hundredths of a second (0.01 seconds).




<br>
<br>
<br>

---

[3:08:46](https://youtu.be/8OMghdHP-zs?si=FCLKZKyeo9IS1zja&t=11326)

## 🟡 Draw a Box Around the Score Text (with Rounded Corners)

#### In this step, we'll add a visual border around the score text to make it stand out more clearly on the screen.



### 🟩  What We’re Achieving:

- - A **rectangle** will be drawn around the score text to highlight it.

- - The rectangle will have **rounded corners** for a softer appearance.


- - We’ll also add **padding between the text and the rectangle** to make sure there’s space around the score, improving the overall aesthetics.


<br>
<br>

### 🟤 1.  Drawing a Rectangle Around the Text




```python
    pygame.draw.rect(display_surface, (240,240,240), text_rect.inflate(28, 30).move(0,-2), 5,10)
```


#### `text_rect.inflate(28, 30):`

- ####  This changes the size of the rectangle by expanding it. inflate(28, 30) means the rectangle will grow 28 pixels wider and 30 pixels taller than its original size.


- #### `.move(0,-2):`

- -  This shifts the position of the rectangle slightly. move(0,-2) moves the rectangle 0 pixels horizontally (left or right), and -2 pixels vertically (up), so it moves a little bit upwards.


### `5:`

- -  This is the thickness of the rectangle's border, meaning how thick the lines of the rectangle will be.

### `10:`

- - This is the corner radius of the rectangle, which controls how rounded the corners are. A value of 10 means the corners will be slightly rounded.

```python
# SCORE

def display_score():
    current_time = pygame.time.get_ticks() // 100
    text_surf = font.render(str(current_time), True, (255,255,255))
    # text_rect = text_surf.get_frect(midbottom = (x,y))
    text_rect = text_surf.get_frect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT -50))
    display_surface.blit(text_surf, text_rect)
    # BOX around padding, here you will have padding as inflate
    pygame.draw.rect(display_surface, (240,240,240), text_rect.inflate(28, 30).move(0,-2), 5,10)

```




<br>
<br>
<br>
<br>


---
