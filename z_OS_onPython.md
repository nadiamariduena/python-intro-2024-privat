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










<br>
<br>

## 🟦 fs and multer


- In modern Node.js applications, there's a shift towards using more specialized libraries and tools for specific tasks that were traditionally handled directly by the fs (File System) module. Here are some areas where traditional file system operations are being replaced or augmented by alternative approaches:


<br>

#### File Uploads:

-  multer is used to handle incoming file uploads, storing uploaded files temporarily on the server. It abstracts away the complexities of parsing multipart/form-data and provides methods to control where and how uploaded files are stored.

<br>
<br>

#### File System Operations:

🔴 **After multer has stored the uploaded files temporarily, you can use fs to manage these files** further—such as moving them to a permanent location, renaming them, checking their properties, etc. This is demonstrated in the previous examples where fs.rename is used to move the uploaded file to a designated directory.


### Why Use multer with fs?

**Efficiency:** multer handles the complexities of parsing file uploads efficiently, allowing your application to focus on business logic rather than low-level file handling.

**Flexibility:** After multer stores files temporarily, fs gives you the flexibility to perform any additional file system operations needed—such as validating file types, resizing images, or organizing files into directories.

**Best Practices:** Using multer alongside fs follows best practices for handling file uploads securely and efficiently in Node.js applications.

```javascript
//  i will be adding an example from an old project
// - YOu dont do it in this way but this is a short example
const express = require('express');
const multer = require('multer');
const fs = require('fs'); ✋
const path = require('path');

const app = express();
const port = 5000;

// Multer configuration
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, './uploads'); // Destination directory where uploaded files will be stored
  },
  filename: function (req, file, cb) {
    cb(null, Date.now() + path.extname(file.originalname)); // Rename file with timestamp + original extension
  }
});

const upload = multer({ storage: storage });

// Serve static files (for testing purposes)
app.use(express.static('public'));

// Endpoint for user registration
app.post('/register', upload.single('profileImage'), (req, res) => {
  const { username, email } = req.body;

  // Get uploaded file details
  const profileImage = req.file;

  // Validate and process the registration (e.g., save to database)
  // For demonstration, we're just logging the details
  console.log('User registered:');
  console.log('Username:', username);
  console.log('Email:', email);
  console.log('Profile Image:', profileImage);

  // Move uploaded file to a permanent location (if needed)
  if (profileImage) {
    const oldPath = profileImage.path;
    const newPath = path.join(__dirname, 'uploads', profileImage.filename);


//  ✋
    fs.rename(oldPath, newPath, (err) => {
      if (err) {
        console.error(err);
        return res.status(500).send('Error uploading image');
      }

      console.log('Image uploaded successfully');
    });
  }

  res.status(200).send('Registration successful');
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});


```

<br>
<br>

### 🟠 Another example

- Handling file uploads traditionally involved using the **fs** module to write files to disk. Nowadays, developers prefer using middleware libraries like multer for handling multipart/form-data, which simplifies the process of file uploads:


```javascript
// 🔴 basic example
//
// The path module in Node.js provides utilities for working with file and directory paths. It offers methods to help construct, normalize, and resolve paths. Key functions of the path module include:
import express from "express";
import bodyParser from "body-parser";
import mongoose from "mongoose";
import cors from "cors";
import dotenv from "dotenv";
import multer from "multer";
import helmet from "helmet";
import morgan from "morgan";

//
// ** img
import path from "path";
import { fileURLToPath } from "url";

/*


✋ ROUTES 1

*/
import authRoutes from "./routes/auth.js";
import userRoutes from "./routes/users.js";
// ** 1 to post pictures
import postRoutes from "./routes/posts.js";
//
import { register } from "./controllers/auth.js";
//
// ** 5 controller post
import { createPost } from "./controllers/posts.js";
// ** 4 to post pictures
import { verifyToken } from "./middleware/auth.js";

//
//
// -------------------
// ** CONFIGURATIONS
// as you can see here below, we are using the import.
//and that is because the type:module inside the package.json

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
//
dotenv.config();
const app = express();
//
app.use(helmet());
app.use(helmet.crossOriginResourcePolicy({ policy: "cross-origin" }));
app.use(morgan("common"));
//https://stackoverflow.com/questions/19917401/error-request-entity-too-large
app.use(bodyParser.json({ limit: "30mb", extended: true }));
app.use(bodyParser.urlencoded({ limit: "30mb", extended: true }));
//
app.use(cors());
// here below is where we will keep out assets
app.use("/assets", express.static(path.join(__dirname, "public/assets")));

//
//
// -------------------
// *** FILE STORAGE
const storage = multer.diskStorage({
  // Every time will upload an img, it will be saved
  //inside the public/assets
  destination: function (req, file, cb) {
    cb(null, "public/assets");
  },
  filename: function (req, file, cb) {
    cb(null, file.originalname);
  },
});

//
//
// ** ------img GIF------- **
// Create a function to check image dimensions and file size
function fileFilter(req, file, cb) {
  const allowedTypes = ["image/jpeg", "image/png", "image/gif"];
  //
  //
  /*


In this code, file.mimetype is checked against the allowedTypes
array to ensure that the uploaded file is an image in either
JPEG or PNG format. If the mimetype doesn't match any of the
allowed types, an error is returned, indicating that the file type is invalid.

*/

  //
  //
  if (!allowedTypes.includes(file.mimetype)) {
    return cb(
      new Error("Invalid file type. Only JPEG, PNG, and GIF are allowed.")
    );
  }
  cb(null, true);
}
// ** ------img GIF------- **

const upload = multer({
  storage,
  fileFilter,
  limits: { fileSize: 1024 * 1024 * 50 },
});
//--------------------------------

//
//
//
/* ROUTES WITH FILES */
app.post("/auth/register", upload.single("picture"), register);
// app.post("/auth/register", upload.single("picture"), verifyToken, register); // the verify token here , causes errors
//
// ** 3 to post pictures
app.post("/posts", verifyToken, upload.single("picture"), createPost);
/*

✋ ROUTES 2

*/
app.use("/auth", authRoutes);
app.use("/users", userRoutes);
// ** 2 to post pictures
app.use("/posts", postRoutes);
//-----------------------------
//
//
/* MONGOOSE SETUP */
// by origin he added 3001 in his .env
// in case the port inside the dotenv doesn't work, the 6001 or whatever
//PORT you add after the || , will work(its a backup server)
const PORT = process.env.PORT || 6001;
mongoose
  .connect(process.env.MONGO_URL, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => {
    app.listen(PORT, () => console.log(`API Port: ${PORT}`, "🦀"));

    /* ADD DATA ONE TIME */
    // populate DONT DO IT
    // User.insertMany(users);
    // Post.insertMany(posts);
  })
  .catch((error) => console.log(`${error} did not connect`));

```


<br>
<br>
<br>

### 🟣 is multer used in python or are there better options?

##### chatgpt

- 🟢 Multer is actually not used in Python; it's a middleware for handling multipart/form-data, which is commonly used with Node.js.

-  In Python, especially in web development frameworks like **Flask and Django**, there are alternative libraries and built-in functionality for handling file uploads and multipart/form-data.

### For Flask

🔸 a popular choice is the **Flask-Uploads** extension, which provides easy file upload capabilities. It simplifies handling file uploads and integrates well with Flask's ecosystem.

### In Django

 🔸file uploads are handled through Django's form handling capabilities, which includes built-in support for file uploads and validation.


#### Here are a few alternatives and built-in options for handling file uploads in Python:

**Flask-Uploads:** Simplifies file uploads in Flask applications.

**Django File Uploads:** Built-in support for handling file uploads in Django.

**FastAPI:** A modern web framework for building APIs in Python, with built-in support for handling file uploads.



**Bottle:** Another lightweight web framework for Python that supports file uploads.