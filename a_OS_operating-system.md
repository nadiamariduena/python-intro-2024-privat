## 🟡 Operating system `OS`

- example

`from os.path import join`

### In Python, os is a module that provides a way to interact with the operating system.

<br>

🟤 It **includes functions** for:

- - **file** and **directory** manipulation,

- -  **environment variables**,

- and other **OS-related tasks**.

<br>
<br>

<br>

## 🟡 `os.path`

#### 🟠 When you see `from os.path import join`,

- - it **means** that you're **importing** the `join` **function** from the `os.path` **submodule**  <u>of the os module</u> .

<br>
<br>
<br>

### 🫐 to concatenate

#### The `join` function is used to `concatenate` <u>parts of a file path</u>  in a way that is platform-independent.

- - This means it will **use** the **correct path separators for the operating system you're running your code** on `(e.g., / for Unix-based systems like Linux and macOS, and \ for Windows)`.

<br>

#### Here's a simple example of how you might use it:

```python
from os.path import join

# Define parts of the path
directory = 'folder'
filename = 'file.txt'

# Join them into a full path
full_path = join(directory, filename)

print(full_path)
```

<br>

**If** directory is **'folder'** <u>and filename is</u>  `'file.txt'`, **the** `full_path` **would be** `'folder/file.txt'` **on Unix-based systems** or `'folder\\file.txt'` on **Windows**.

> #### Using join ensures that your code works correctly across different operating systems.


<br>
<br>

### 🔴 Not to be confused with this `Join()`

### 🟠 `Join` the word

- `.join` will turn the list into a **string**, separated by whatever the string is.

-  you can add **white spaces, symbols, letters** , example:

-  `' '.join` or `', '.join` or `'/ '.join` etc...


```python
print("You have used these letters: ", ' '.join(used_letters))
# 🔴 output
"a", "b",
#
#https://github.com/nadiamariduena/python-intro-2024-privat/blob/master/LESSON_19_PPROJECTS/random_Hangman/README.md
```


<br>
<br>
<br>

### 🟦 Javascript / Nodejs/ React?

In React (or JavaScript in general), **you don't use** `os.path.join` **because JavaScript handles file paths** and directories **differently compared** to **Python**.

- - 🟠 **JavaScript** is primarily used for **web development**, where **file paths** are usually **managed differently than in a traditional file system**.
