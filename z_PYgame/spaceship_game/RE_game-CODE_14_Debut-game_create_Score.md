
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
