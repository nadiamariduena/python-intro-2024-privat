## 🟡 OS

### 🟣 what is os in python and why do you need to add it at the top?

```python
# import requests
# from dotenv import load_dotenv
import os
# 🔴 Similar TO FS (file system)
#The fs module in Node.js provides an API for interacting with the file system. It allows you to perform operations such as reading from and writing to files, creating and deleting files, modifying file permissions, and more. I WILL WRITE MORE below
```

<br>


##### chatgpt

- 🟢 In Python, **"os"** stands for the **operating system module**. It is a standard library module that provides a way of using operating system-dependent functionality such as manipulating files and directories, accessing environment variables, and executing system commands.

<br>

### 🟣 so this OS helps to get directories from my local machine?

##### chatgpt

- 🟢 Yes, the os module in Python provides several functions and methods that can help you work with directories (folders) and files on your computer.

<br>

 **Here are some** of the common directory-related tasks you can perform using the os module:

 ### 🔸 1. Listing Files and Directories:

 - You can use `os.listdir()` to get a list of all files and directories in a given directory.

```python
import os

# List all files and directories in the current directory
files_and_dirs = os.listdir('.')
print(files_and_dirs)
#
#
# ✋ OUTPUT
# The below is the content of my FOLDER containing all the python lessons
/bin/python3 /home/mycomputer/Documents/0_PYTHON-all/PYTHON-PRIVAT/python-intro-2024-privat/LESSON_16_OOP/weather.py
['.git', 'LESSON_12_CommandLineArgs', 'z__modules-methods.md', 'z__ENV_VIRTUALENV .md', 'LESSON_6_Functions', 'LESSON_9_closures', 'LESSON_16_OOP', 'z__ENV_PATH_issue.md', 'z__TEMPLATE-rendering.md', 'LESSON_17_Virtual_Environment_and_pip', 'LESSON_01', 'argsParse.py', 'LESSON_02', 'img', 'z_lifeCycles-JS_0.md', 'z_floating.md', '.vscode', 'LESSON_5_loops', 'MORE-memory.md', 'LESSON_7_recursion', 'z_identation-issues.md', 'LESSON_13_lambda_map_etc', 'z_ACTIVATE_ENV-deactivate.md', 'z__all_mds', 'LESSON_04_dictio', 'LESSON_10_f_Strings', 'LESSON_03_tuples', 'z_weather-API.md', 'z__smallTips.md', 'underscore_uses_tests.py', 'LESSON_8_Scope', 'z__Books-toread.md', 'z_args_&_kwargs.md', 'LESSON_15_err-exception-handling', 'z__ENV-flask.md', 'z_OS_onPython.md', 'README.md', 'new_directory', 'z_about_packages', 'z_underscore-uses_onPython.md', 'z__PIP_installation.md', 'z__ENV_ubuntu-version-issue.md', 'LESSON_11_modules', 'LESSON_14_classes']
```

<br>

### But what if i only wanted one specific lesson

 ```python
import os

# Specify the directory you want to explore
lesson_dir = 'LESSON_16_OOP'

# Join the current directory path with the lesson directory
lesson_path = os.path.join('.', lesson_dir)

# Check if the specified directory exists
if os.path.exists(lesson_path) and os.path.isdir(lesson_path):
    # List all files and directories inside the lesson directory
    lesson_contents = os.listdir(lesson_path)

    # Print the list of contents
    print(lesson_contents)
else:
    print(f"The directory '{lesson_dir}' does not exist or is not a directory.")
#
#
#
#
#
# ✋ output
/bin/python3 /home/mycomputer/Documents/0_PYTHON-all/PYTHON-PRIVAT/python-intro-2024-privat/LESSON_16_OOP/weather.py
['.myenv', '.env', 'BankingIntro', 'OOP_0_.py', 'requirements.txt', '.gitignore', 'OOP_intro.py', 'weather.py']
 ```


<br>
<br>

 ### 🔸 2. Creating Directories:

 - You can create a new directory using `os.mkdir()`.

 - when you run your code, it will automatically create a new directory(check the left bar, you will see this new directory appearing there)

 ```python
import os

# Create a new directory
os.mkdir('new_directory')
```

<br>



### 🔸 3. Change the current working directory to 'new_directory' `os.chdir('new_directory')`

```python
import os

# Change the current working directory to 'new_directory'
os.chdir('new_directory')

```

<br>

### 🔸 4. Checking if a Path is a Directory:

- You can check if a given path points to a directory using `os.path.isdir()`.

```python
import os

# Check if 'new_directory' is a directory
is_directory = os.path.isdir('new_directory')
print(is_directory)

```

<br>


### 🔸 5. Removing Directories:

- You can remove a directory using `os.rmdir()`.
>Note that the directory must be empty for this operation to succeed.

```python
import os

# Remove the directory 'new_directory'
os.rmdir('new_directory')
```
<br>

### 🔸 6. Walking Directory Trees:

- You can recursively iterate through a directory tree using `os.walk()`, which yields the path to each directory and its contents.

```python
import os

# Walk through the directory tree starting from the current directory
for root, dirs, files in os.walk('.'):
    print(f'Current directory: {root}')
    print(f'Subdirectories: {dirs}')
    print(f'Files: {files}')

```

<br>
<br>

<br>

## 🟡 OS / FS (file system)

<br>

- In the context of **React and JavaScript**, managing files and directories or interacting with the operating system is typically handled differently than in Python.

- JavaScript, **being primarily a language that runs in the browser**, has limited direct access to the operating system for security reasons. However, there are several ways and libraries that can help achieve similar functionality:

### 🫐 Node.js (File System Module):

- When JavaScript is used in a server-side environment like Node.js, you can use the built-in fs module **(File System)** to manipulate files and directories on the server's file system.

### 🫐 Browser APIs (limited):

- In browser-based JavaScript, access to the operating system is restricted due to security concerns. However, there are some APIs available that can interact with the user's file system in a limited way, such as the File API and FileSystem API.

<br>
<br>
<br>

## 🟠 fs (File System)


 #### The fs module in Node.js provides an API for interacting with the file system. It allows you to perform operations such as reading from and writing to files, creating and deleting files, modifying file permissions, and more.

Here are some common operations you can perform with fs:


```javascript

Reading Files: fs.readFile, fs.readFileSync, etc.
Writing Files: fs.writeFile, fs.writeFileSync, etc.
File and Directory Operations: fs.rename, fs.unlink, fs.mkdir, fs.rmdir, etc.
Working with Streams: fs.createReadStream, fs.createWriteStream, etc.
File Metadata: fs.stat, fs.lstat, etc.

```

<br>
<br>

## 🟦 fs and multer

#### File Uploads:

-  multer is used to handle incoming file uploads, storing uploaded files temporarily on the server. It abstracts away the complexities of parsing multipart/form-data and provides methods to control where and how uploaded files are stored.

#### File System Operations:

🔴 **After multer has stored the uploaded files temporarily, you can use fs to manage these files** further—such as moving them to a permanent location, renaming them, checking their properties, etc. This is demonstrated in the previous examples where fs.rename is used to move the uploaded file to a designated directory.

#### 🟣 is multer used in python or are there better options?

##### chatgpt

- 🟢 Multer is actually not used in Python; it's a middleware for handling multipart/form-data, which is commonly used with Node.js.

