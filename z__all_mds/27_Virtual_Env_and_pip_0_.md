# 🟡Virtual Environment and pip

<br>
<br>

## 🟠 Virtual Environment

#### Question: what is a virtual environment in python?

##### chatgpt:

- A **virtual environment** in Python is a **self-contained directory** that contains a Python installation for a particular version of Python, as well as additional packages.

> 🎠 It allows you to isolate dependencies required by different projects by creating an environment that is separate from your system-wide Python installation.

<br>

#### 🔸 explanation

<br>

- 🧸 Imagine you have a **magical box** <u>just for your toys</u>.

- **Each box** is like a **virtual environment** for your toys 🎪.

- Inside this box, you can keep **one set of toys separate from another.**

> 🎁 This way, **the toys** from one box **don't mix** up with **toys from another**.

<br>

### In Python, a virtual environment is like one of these magical boxes, but for your computer programs instead of toys.

<br>

- 🟢 It helps keep different programs and their special tools (called libraries or packages) separate.

- 🟢 This is important because sometimes different programs need different versions of these tools, and we don't want them to get mixed up and cause problems.

<br>

### So, when you create a virtual environment for a program, it's like giving that program its own special box 🎪 where it can have its tools and play without disturbing other programs.

> This helps keep everything organized and makes sure each program has exactly what it needs to work properly.

<br>
<br>

### 🟠 Here are the key aspects of a virtual environment:

<br>

- **Isolation:** Each virtual environment is independent of others and of the system-wide Python installation. This means **you can have different versions of Python** <u>and</u> **different packages installed in different virtual environments** without them conflicting.

- **Dependency Management:** Virtual environments allow you to <u>manage dependencies</u> **for each project separately**. You can install specific versions of packages required for one project without affecting others.

- **Sandboxing**: They provide a sandboxed environment where you can experiment with packages or different Python versions without altering your main Python setup.

<br>

- 🔴 **Creation:** Virtual environments can be created using tools like venv (built-in to Python 3) [check this example: min 5:57 | Python Virtual Environment and pip for Beginners](https://youtu.be/eDe-z2Qy9x4?si=9Bw0tjgyRDIGM58M&t=357), virtualenv, or conda (for Anaconda environments).

- 🔴 **Activation:** To use a virtual environment, you need to activate it [check this example: min 6:31 | Python Virtual Environment and pip for Beginners](https://youtu.be/eDe-z2Qy9x4?si=6zHr3HrlvnZigJQF&t=391) . This modifies the shell's environment variables to point to the virtual environment's Python executable and libraries.

<br>
<br>

### 🟠 Why Use Virtual Environments?

<br>

- **Dependency Isolation:** Prevents conflicts between packages required by different projects.

- **Version Control:** Ensures each project uses the correct version of Python and dependencies. [check this example: min 2:46 | Python Virtual Environment and pip for Beginners](https://youtu.be/eDe-z2Qy9x4?feature=shared&t=166)

- **Reproducibility:** Makes it easier to replicate the development environment on different machines.

- **Cleanliness:** Keeps your system-wide Python installation clean and avoids cluttering it with project-specific packages.

<br>
<br>

### 🟣 Example Use Cases

**Web Development:** Different Flask or Django projects may require different versions of their respective frameworks or dependencies.

**Data Science:** Projects using different versions of libraries like NumPy, Pandas, or TensorFlow can be managed independently.

**Testing:** Ensuring that tests run consistently across different environments by isolating dependencies.

<br>
<br>

---

<br>

# 🟡 PIP

PIP **(Python Package Installer)** is the standard package manager for Python. It is used to install and manage additional libraries and dependencies that are not part of the Python standard library. Here's a breakdown of its key aspects and its link to virtual environments:

- **Package Installation:** PIP is primarily used to install packages from the Python Package Index (PyPI) and other package indexes.

- **Package Management:** It helps in managing Python package dependencies for your projects.

- **Version Management:** PIP allows you to install specific versions of packages, ensuring compatibility with your code.

- **Upgrading Packages:** It provides commands to upgrade packages to their latest versions.

- **Uninstallation:** PIP can uninstall packages that are no longer needed.

<br>
<br>

### 🟠 Virtual Environments and PIP:

Virtual environments are isolated environments for Python projects, allowing you to install packages independently of those installed globally on your system.

#### Here's a short list of Python packages (that Come Already Installed OR Packages that Can Be Installed with PIP):

<br>

> **Built-in Modules:** Python comes with a set of built-in modules that are available without needing to install anything extra. Some examples include:

```python
math: #Mathematical functions.
sys: # System-specific parameters and functions.
os: #Operating system interfaces.
datetime: #Basic date and time types.
json: #JSON encoder and decoder.
```

##### example SYS:

- check the code here [LESSON_03_tuples/rps3_whileLoop.py](../LESSON_03_tuples/rps3_whileLoop.py)

```python
✋
import sys
# ------
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print("")

sys.exit('Bye!')

```

<br>
<br>

#### Packages that Can Be Installed with PIP:

**Third-Party Packages:** These are not included with Python by default but can be easily installed using PIP from repositories like PyPI (Python Package Index). Some examples include:

```python
Requests: # HTTP library for making requests and working with APIs.
NumPy: # Fundamental package for numerical computing with arrays.
Pandas: # Data manipulation and analysis library.
Matplotlib: # Plotting library for creating static, animated, and interactive visualizations.
Django: # Web framework for building web applications.
Flask: # Lightweight web framework for building web applications.
TensorFlow: # Machine learning framework for building and training models.
Pytorch: # Deep learning framework for building and training neural networks.
SQLAlchemy: # SQL toolkit and Object-Relational Mapping (ORM) library for Python.
Beautiful Soup: # Library for parsing HTML and XML documents.
```

<br>

### 🥧 NumPy:

#### question: What is the numpy and what is the difference to not using it?

##### chatgpt:

🔸NumPy (Numerical Python) is a fundamental package for numerical computing in Python.

🔸It provides support for large, multi-dimensional **arrays and matrices**, along with a collection of mathematical functions to operate on these arrays efficiently.

> Here’s an overview of what NumPy offers and how it differs from not using it:

### What NumPy Provides:

**Multi-dimensional Arrays:** NumPy introduces the ndarray (N-dimensional array) object, which allows you to work with arrays of any dimensionality (1D, 2D, 3D, etc.).

[multi-dimensional-arrays-in-python/](https://www.freecodecamp.org/news/multi-dimensional-arrays-in-python/)

```python
import numpy as np

# Create a 2-dimensional array with 3 rows and 4 columns
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Print the array
print(arr)
#
#
# OUTPUT
# array([[ 1,  2,  3,  4],
#        [ 5,  6,  7,  8],
#        [ 9, 10, 11, 12]])
```

<br>

[arrays.ndarray](https://numpy.org/doc/stable/reference/arrays.ndarray.html)

<br>
<br>

### 🟣 Question: Give me an example comparing the use of the matrices on python and [threejs](https://threejs.org/)

#### chatgpt:

Let's compare how matrices (or arrays) are used in Python (specifically with NumPy) and in Three.js (JavaScript) for creating and manipulating a grid-based game environment.

### 🟢 Matrices in Python (NumPy)

In Python, **NumPy** provides powerful tools for working with multi-dimensional arrays, often referred to as matrices. Here's how you might use NumPy arrays to represent and manipulate a grid-based game environment:

#### Creating a Grid Map:

```python
import numpy as np

map_size = (5, 5)
game_map = np.zeros(map_size, dtype=int)  # Initialize a 5x5 grid map filled with zeros

# Example: Place obstacles
game_map[1, 1] = 1  # Put an obstacle at position (1, 1)
game_map[2, 3] = 1  # Put another obstacle at position (2, 3)

```

**Explanation:** Here, `np.zeros` creates a 5x5 array filled with zeros (dtype=int specifies integer type). Obstacles are represented by setting specific elements ([1, 1] and [2, 3]) to 1.

> ✋ Let's visualize the grid-based game map using NumPy arrays, where obstacles are represented by 1 and empty spaces by 0. Here's a simple diagram to illustrate the game map after placing obstacles:

```python
Initial Game Map (5x5):
# 5 col and 5 row

  0 0 0 0 0
  0 1 0 0 0
  0 0 0 1 0
  0 0 0 0 0
  0 0 0 0 0

```

- The grid represents a **5x5** game map initialized with zeros (0).

- 🔥 Obstacles are placed at positions `(1, 1)` and `(2, 3)`, represented by `1`.

<br>

#### Player Movement and Collision Detection:

```python
player_position = (2, 2)  # Player starts at position (2, 2)

# Example: Move the player up (subtract 1 from row index)
new_position = (player_position[0] - 1, player_position[1])

# Check if the new position is within bounds and not obstructed
if (0 <= new_position[0] < map_size[0] and
    0 <= new_position[1] < map_size[1] and
    game_map[new_position] != 1):  # Check if it's not an obstacle
    player_position = new_position

#
#
#Explanation: NumPy arrays allow efficient indexing and slicing (game_map[new_position]) for checking boundaries and conditions (e.g., obstacle presence) before allowing player movement.
```

<br>
<br>

### 🟢 Matrices in Three.js (JavaScript)

In **Three.js**, objects in a 3D scene are represented using matrices and vectors. While **not directly analogous to NumPy** arrays **( ✋ they serve different purposes and have different implementations despite both being data structures represented as matrices)**, matrices in Three.js play a crucial role in positioning and transforming objects within a 3D space:

Creating a Grid Map:

```javascript
var mapSize = 5;
var tileSize = 10;
var gameMap = [];

// Create tiles for the map
for (var i = 0; i < mapSize; i++) {
  gameMap[i] = [];
  for (var j = 0; j < mapSize; j++) {
    var tileGeometry = new THREE.BoxGeometry(tileSize, 1, tileSize);
    var tileMaterial = new THREE.MeshBasicMaterial({ color: 0x00ff00 }); // Green color for tiles
    var tileMesh = new THREE.Mesh(tileGeometry, tileMaterial);
    tileMesh.position.set(i * tileSize, 0, j * tileSize);
    scene.add(tileMesh);

    // ✋ Example: Place obstacles
    if (i === 1 && j === 1) {
      // the box obstacle
      var obstacleGeometry = new THREE.BoxGeometry(tileSize, 2, tileSize);
      // the mat of the box obstacle
      var obstacleMaterial = new THREE.MeshBasicMaterial({ color: 0xff0000 }); // Red color for obstacles
      //
      //
      var obstacleMesh = new THREE.Mesh(obstacleGeometry, obstacleMaterial);
      //
      obstacleMesh.position.set(i * tileSize, 1, j * tileSize);
      scene.add(obstacleMesh);
    }

    gameMap[i][j] = { type: "tile", mesh: tileMesh };
  }
}
```

**Explanation:** In Three.js, each object (like tiles and obstacles) is represented by a THREE.Mesh object with its own geometry (shape) and material (color).

- 🔴 The position of each object is set using position.set, calculated based on the grid indices (i and j) and tile size (tileSize).

#### Player Movement and Collision Detection:

```javascript
var playerMesh = new THREE.Mesh(playerGeometry, playerMaterial);
playerMesh.position.set(tileSize * 2, 1, tileSize * 2); // Starting position

function movePlayer(direction) {
  var newPosition = playerMesh.position.clone();
  switch (direction) {
    // KEYBOARD
    case "up":
      newPosition.z -= tileSize;
      break;
    case "down":
      newPosition.z += tileSize;
      break;
    case "left":
      newPosition.x -= tileSize;
      break;
    case "right":
      newPosition.x += tileSize;
      break;
    default:
      return;
  }

  // Check if the new position is within bounds and not obstructed
  var gridX = Math.floor(newPosition.x / tileSize);
  var gridZ = Math.floor(newPosition.z / tileSize);
  if (
    gridX >= 0 &&
    gridX < mapSize &&
    gridZ >= 0 &&
    gridZ < mapSize &&
    !(gridX === 1 && gridZ === 1)
  ) {
    // Check if it's not an obstacle
    playerMesh.position.copy(newPosition);
  }
}
```
