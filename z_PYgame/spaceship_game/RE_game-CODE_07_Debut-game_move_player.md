
# 🟡 SPRITES 2.

<br>
<br>


### 🟠 Intro:



- - What **We’ll Be Doing** [Go to section](#What_We_will_Be_Doing_)



<br>
<br>

### 🧶 Global Accessibility of Delta Time (dt)

- -  Global Accessibility of Delta Time (dt):  [Go to section](#Global_Accessibility_of_DT)

- -  - **Global Scope** to access Delta Time:  ( 🔺 **not a good practice in some scenarios**) [Go to section](#Global_Accessibility_of_DT_not_good_inthis_situation)

- - - - - **`Global Scope` issue**  <u>check the solution here </u>  [Go to section](#Global_Accessibility_solution) )


<br>
<br>

<!-- ### 🟦 Final Touches Before Creating the `Star Class`

- - - The **Issue with `get_just_pressed()`** [Go to section](#get_just_pressed_)



> -  - - - 🔺  In the upcoming part of the lesson, the teacher will demonstrate the use of `get_just_pressed()`, but be aware that this might lead to an error: -->


<br>
<br>
<br>
<br>
<br>
<br>

---

<br>

<a name="What_We_will_Be_Doing_"></a>

## 🫐🟡 <u>What We’ll Be Doing </u>




 <br>



<!-- ## 🟦   Moving Forward: -->

### 🟠 Let’s Recreate Our Previous Movements!

### 🔸 Remember What We Had Before?

> #### In the upcoming steps, we will reintroduce the movement logic that allows the player to navigate smoothly.

<br>

- - **First**, we’ll copy the key direction input code into the update() method of the Player class.

- - - **Next**, we’ll ensure that we **`normalize`** the direction vector to maintain consistent speed.

- - - **We’ll also define the `speed` variable** to control how fast the player moves.

> - - #### Finally, we’ll incorporate delta time to ensure movement remains fluid across different frame rates.



<br>

### Here’s the movement logic we were using:

 ```python

#   print(pygame.mouse.get_pos())
   # ---------KEY  ---------
   keys = pygame.key.get_pressed()

    player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    # # `int()` is the function doing the conversion. int converts this boolean value into an integer. In Python, True is equivalent to 1 and False is equivalent to 0. Therefore, int(keys[pygame.K_RIGHT]) gives 1 if the key is pressed and 0 if it is not
     player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

    # # to normalize the vector, after the issue when pressing top and left at the same time
    player_direction = player_direction.normalize() if player_direction else player_direction


    # player_rect.center += player_direction * player_speed * dt

    # #MAGNITUDE
    # print((player_direction * player_speed).magnitude())
    # -----------------
    # -----------------
 ```
---

<br>
<br>
 <br>
 <br>

##  🟠 Transforming the Player Class for Smooth Movement!

<br>

### 🧶 Step 1:

### 💥 Move the Logic into the `Player` Class


- - -   **Instead of having movement** logic <u>in the main loop (WHILE loop)</u> , let’s **encapsulate it in the Player class!** This will make our code cleaner and more organized.

<br>

### 🧶 Step 2:

### 💥 `Update` the `Player` Class

> - - - ####   We’ll modify the Player class to include the movement logic directly in its `update()` method.

- - ####  This way, we can call it easily from our main game loop.

<br>
<br>
<br>
<br>

#### [2:04:10](https://youtu.be/8OMghdHP-zs?si=lDJzumH66g9rAMgc&t=7450)

## 🟠 Here’s How We’ll Do It:

### Add Movement Logic:

- - **Incorporate `key` presses to control the player’s** direction and **normalize** the **vector**.


### Update Position:

- - Adjust the player’s position based on the calculated direction and speed.

<br>
<br>

## 🟫 STEPS

<br>

## 🔶 1.  Move the Movement Logic

- - **Take the entire commented section** related to movement from the `WHILE` loop and paste it below the **`def update` method** in the `Player` class.
