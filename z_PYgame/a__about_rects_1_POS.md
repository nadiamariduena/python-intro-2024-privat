#  🟡 `Frect` Position


<br>


### 🟦 Rectangle: use `Frect`

#### To position it in specific places we will use the `frect` instead of rect (you will see later on why).



> - - #### 🟠 REMEMBER the Differences between rect & frect:

>**Rect** `uses integer` values(**20**), <u>while</u> **FRect**  uses` floating-point` values(**20.5**).

<br>


<br>
<br>



## 🟡 Create a square/rect to use for this example:

- To understand this section, I will start with a basic cube, later on i will continue with the plane


<br>

**1.** **create** a **new variable**, call it:

`kop`

>Assign it the:`pygame.Surface` to the variable

**2.**  **kop** is a small cube/square 🟧

`kop = pygame.Surface((50, 50))`

**3.** **Add** some color to **kop**

`kop.fill("orange")`

<br>

**4.** Before positioning where the square will be, this is what we have:

```python
kop = pygame.Surface((50, 50))
kop.fill("orange")
```


### a) 🟤 Positioning:

**5.** we will position it at the **center point** of the **CUBE**  (which give us the center of the cube, not the window).

>its a position **within**

```python
# ✋ the kop_rect variable, is taking the info of the cube(measurements & and color, to then create something new)
kop_rect = kop.get_frect(center=())
```

<br>

[<img src="nomove-entirecube_instead_it-points-at-center-of-thecube.gif"/>](  )
<br>

> - - #### Look at 🔴 the center  <u>blue dot</u>, this is the `center =` i am talking about.
> - - - this center can be changed to topleft, bottomright etc ... (check the options below)



<br>
<br>

### If you imagine a rectangle on the "screen" (the cube is inside the screen window):

 - - you can move a `central` **point** to different positions around it, but once you move it, it no longer be the `center =` but whatever you chose in the cube, like `topleft =` or `midleft =` etc.

 - - - For example, if you move the center dot of the rectangle to the "topleft" position, it will be placed at the top-left corner of the rectangle.

#### 🟤 The image below shows all the available position options for the rectangle:

- Here you can see the all the options

[<img src="./rect__points.png"/>](https://youtu.be/8OMghdHP-zs?si=wGX83WQl1sMWU8ra&t=2674/)

<br>
<br>

### a) 🟤 Positioning:

**6.** Now lets add the position in the coordinate, we need 2 arguments here **x and y:** like so `(0, 30))`, 0 means that we will pos the cube at 0 position on the window, as you can see, the cube is showing only the half of its surface, and its because we specified the **center**

```python
kop_rect = kop.get_frect(center=(0, 30))
```

- The value 30 represents the y-coordinate, which means the center of the rectangle is positioned 30 pixels down from the top of the screen.

### 🟤 which give us the below



[<img src="center_pos.jpg"/>]( )

<br>

 ```python
kop = pygame.Surface((50, 50))
kop.fill("orange")
kop_rect = kop.get_frect(center=(0, 30))
 ```

 <br>

### 🔴 Not Moving the Entire Cube:
