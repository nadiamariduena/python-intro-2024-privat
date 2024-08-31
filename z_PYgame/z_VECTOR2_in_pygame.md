# 🟡 VECTORS


- Why to use vectors?

- Vector Multiplication

- Mutable and Flexible

<br>
<br>

 ### 🟦 Using a vector can be a good solution  to handle position updates more flexibly and avoid the issues you encountered with directly modifying the:

  `center` attribute of a `Rect` **object**.

<br>


### 🟠 Vectors are mathematical objects used to represent quantities with both magnitude and direction.

- -  In 2D space, a vector has two components: `x (horizontal) and y (vertical)`.

> - -  #### 🟢 Operations like addition, subtraction, and scaling (multiplying by a scalar) are performed element-wise("element-wise" means that each component of the vector is operated on individually.).

#### 🍊 Vectors simplify calculations and transformations in graphics and physics by managing direction and distance efficiently.


<br>

### 🟨 `Vectors` can be thought of as `lists` with `two` values: `x and y`, `representing coordinates in a 2D` space.

<br>

### 🟤 Vector Multiplication

**Multiplying a Vector by a Number:**

- -  When you multiply a vector by a ✋ `scalar` **(a single number)**, each component of the vector is multiplied by that number.

```python
vector = Vector2(4, 2)  # A vector with x = 4 and y = 2
scaled_vector = vector * 2  # Multiply both x and y by 2
# 4 x 2 = 8
# 2 x 2 = 4

# 👍 output of the multiplication
# This results in a new vector: Vector2(8, 4)


```