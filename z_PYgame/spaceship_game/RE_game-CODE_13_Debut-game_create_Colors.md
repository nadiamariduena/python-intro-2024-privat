
# 🟡 SPRITES 8.


- COLORS

<br>
<br>

## INTRO



<br>
<br>
<!-- <br>
<br>
<br> -->


## 🟦  Working with Colors in Pygame


#### In this lesson, we’ll learn how to work with colors in Pygame to make your game more vibrant and visually appealing.

> #### Colors can be added to your game elements like backgrounds, text, and images. Pygame allows you to define colors in a few different ways.

<br>
<br>
<br>

#### [2:57:15](https://youtu.be/8OMghdHP-zs?si=GVH2d5YJminpGKqT&t=10635)


# 🟡 Colors in Pygame

### 🫐 In Pygame, you can define colors in <u>`three` main ways</u> :


## 🟩 Built-in Color Names

#### Pygame provides a list of predefined color names that you can use directly in your code without needing to remember the specific RGB or hex values.

- These color names are simple to use and are great for quick, common colors like red, green, blue, black, white, and others

### In the code


```python
text_surf = font.render('whatever text: HELLO', True, 'red')
```



<br>

## 🟩 RGB

#### Built-in color names like 'red' or 'green'.

- -    **RGB tuples**, where each color is made up of three numbers: Red, Green, and Blue.

> - - - Each number must be between `0 and 255`.

```python
(red, green, blue)
```

- - -  🟠 A value of 0 means no color, and 255 is the full color.
Here’s how the RGB system works:

<br>

#### Examples:


`(255, 0, 0)` = Pure red
`(0, 255, 255)` = Light blue
`(200, 200, 200)` = Grey

<br>

### In the code

- In a tuple(), specify 3 values (red, green , blue) for example

```python
text_surf = font.render('text', True, 'r,g,b')
```
#### like so

```python
text_surf = font.render('text', True, '200,50,100')
```





#### You can mix and match these values to create a wide range of colors. The higher the number, the more intense that color becomes.



---

<br>

## 🟩 Hexadecimal Color Codes:

### Another way to define colors is by using hexadecimal (hex) values.

#### Hex is a base-16 system that uses numbers `0-9` and letters `A-F`.

- - - **0-9:** These digits represent values from **0 to 9** (just like in regular numbers).

- - - **A-F:** These letters represent values from **10 to 15**

<br>

> #### In Pygame, you can use hex values by prefixing them with `#` and then a `6-digit` code, where each pair of digits represents the red, green, and blue components.

### Example:

#### 🟧  `#FF5733`

`FF` **(Red) = 255** in decimal (the maximum value for red).

`57` **(Green) = 87** in decimal.

`33` **(Blue) = 51** in decimal.

<br>

> #### Hexadecimal values give you more precision and can sometimes be easier to pick when using color pickers in design tools.

<br>

### In the code

```python
text_surf = font.render('text', True, '#FF5733')
```

<br>

---

## 🟦 🟡 Which Method to Use?

- #### `Built-in names` are simple and quick but limited in color options.

- #### `RGB` tuples give you the most flexibility, as you can create any color by adjusting the numbers.

- #### `Hex` codes are another popular option, especially if you're used to working with web colors or design tools.

---

<br>



