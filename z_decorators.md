## 🧶 Python decorators

#### Python decorators are a powerful feature that allows you to modify or enhance the behavior of functions or methods.

- 🍊 Decorators are often used to **add functionality** to functions or methods.


<br>
<br>

### 🟧 Here's a list of common decorators and the most used ones in Python:

<br>

## 🟦 Built-in Decorators


#### `@staticmethod`:

- - Defines a method that does not operate on an instance or class. It behaves like a regular function but is associated with the class.

<br>

- - 🍍 I used it in this project [tic_tac_toe_0](./LESSON_19_PPROJECTS/tic-tac-toe/tic_tac_toe_0/README.md)

<br>
<br>

#### `@classmethod:`


- -  Defines a method that operates on the class itself, rather than on instances. It receives the class as its first argument (cls).

<br>

#### `@property:`

- -  Turns a method into a property, allowing you to access it like an attribute without calling it as a method.

<br>

#### `@abstractmethod`:


- - Used in abstract base classes to define abstract methods that must be implemented by any subclass.


<br>
<br>
<br>

## 🟦 Standard Library Decorators

<br>

#### `functools.lru_cache`:

- - Caches the results of expensive function calls to speed up subsequent calls with the same arguments. Useful for memoization.

<br>

####  `functools.total_ordering`:

- - Automatically generates missing comparison methods (<, <=, >, >=) based on the defined ones (==, !=).


<br>

#### `functools.singledispatch`:

- - Allows a function to behave differently based on the type of its first argument. It’s a form of generic function dispatch.


<br>



#### `functools.wraps`:


- - A helper decorator used to preserve the metadata of the original function when decorating functions. This is especially useful when creating custom decorators.
