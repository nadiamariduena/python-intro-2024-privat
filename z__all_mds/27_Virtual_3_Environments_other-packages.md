
- Flask

- DJANGO

- FREEZE


<br>
<br>


---

<br>

### 🟡 Install FLASK

#### What is flask?

- Click here to read about FLASK (it contains exercises) [z\_\_ENV-flask](../z__ENV-flask.md)

```javascript

pip install flask
```

<br>
<br>

### 🟡 When you install flask, it will also come with other packets

- type this command to see all the packages installed (when you installed flask): `pip list`

<br>

```javascript
$ pip list
Package            Version
------------------ -------
blinker            1.8.2
click              8.1.7
Flask              3.0.3
importlib_metadata 8.0.0
itsdangerous       2.2.0
Jinja2             3.1.4 // ✋ templates, read more here: ./z__ENV-flask.md
MarkupSafe         2.1.5
pip                24.1
setuptools         70.1.0
Werkzeug           3.0.3
wheel              0.43.0
zipp  3.19.2
```

<br>

#### 🟠 Purpose:

- These comments summarize the main purpose or functionality that each package typically serves in Python development, especially in the context of web frameworks like Flask.

<br>

```python
import blinker  # Implements a fast and simple object-to-object and broadcast signaling system.
import click   # A package for creating command-line interfaces.
from flask import Flask # Flask is a lightweight WSGI web application framework.
import importlib_metadata # Provides metadata reading for Python packages.
import itsdangerous  # Various helpers to pass data to untrusted environments securely.
from jinja2 import Jinja2  # Jinja2 is a full-featured template engine for Python.
import markupsafe  # Implements a XML/HTML/XHTML Markup safe string for Python.
import pip   # The package installer for Python.
import setuptools  # Library for packaging Python projects.
from werkzeug import Werkzeug  # Werkzeug is a comprehensive WSGI web application library.
import wheel    # A built-package format for Python.
import zipp     # A reasonable implementation of importlib.


```

<br>
<br>

## 🟡 Install DJANGo

<br>

1. 🔸 Presuming you are still inside the project you installed the **virtual environment**, within your terminal you see something like this (but with your own project)

```javascript
(env) mycomputer:~/LESSON_17_Virtual_Environment_and_pip$:
//This the name of the project where i installed the virtual environment
```

2. 🔸 Then you can proceed with DJANGO installation, type this command:

```javascript
pip install django

//
// Should look like this:
(env)  mycomputer$ pip install django
```

<br>

3. - 🔸 CHECK the packages again (once Django has been installed) , type this command: `pip list`

##### output

```javascript
Package            Version
------------------ -------
asgiref            3.8.1
backports.zoneinfo 0.2.1
blinker            1.8.2
click              8.1.7
Django             4.2.13 ✋ // it has been installed
Flask              3.0.3
importlib_metadata 8.0.0
itsdangerous       2.2.0
Jinja2             3.1.4
MarkupSafe         2.1.5
pip                24.1
setuptools         70.1.0
sqlparse           0.5.0
typing_extensions  4.12.2
Werkzeug           3.0.3
wheel              0.43.0
zipp               3.19.2
```

#### Extra command to check djanfo version:

`django-admin --version`

<br>
<br>

### 🟡 Once you have installed DJANGO

1. 🔸 Presuming you are still inside the project you installed the **virtual environment**

2. 🔸 create a new folder and name it **scr** , within the scr, create a new file and name it **app.py**

<br>

```javascript
project_folder/
├── env/
└── src/
    └── app.py

```

<br>

3. 🔸 Within the app.js, type this:

```python
print("hello world 👾")
```

<br>

4. 🔸 TO check the output

- in the tutorial you have to type the below, but i only have to click on the **arrow at the top** of the window to see the output

```javascript
//https://youtu.be/TNtrAvNNxTY?si=wyJYvcWocasOyEkR
python .\src\app.py
//
// 💡 check the console to see if it s showing the 'hello world'
```

<br>
<br>

---

<br>

## 🟡 Freeze

The **pip freeze** command in Python is used to generate a **list of all installed packages** and their versions in a **specific environment**.

- 🔸 once you type the command below, you will notice that within your project (the one you have created the environment), there is a new file

```javascript
//Presuming you are still inside the project you installed the **virtual environment**
pip freeze > requirement.txt
```

- When you run pip freeze, it outputs a list in the format `package==version` for each package installed in your current Python environment. For example:

```javascript
asgiref==3.8.1
backports.zoneinfo==0.2.1
blinker==1.8.2
click==8.1.7
Django==4.2.13
Flask==3.0.3
importlib_metadata==8.0.0
itsdangerous==2.2.0
Jinja2==3.1.4
MarkupSafe==2.1.5
sqlparse==0.5.0
typing_extensions==4.12.2
Werkzeug==3.0.3
zipp==3.19.2

```

<br>

### 🟠 Purpose of pip freeze

<br>

**Dependency Management:**

🔸 It helps you keep track of the exact versions of all installed packages in your project. This is crucial for reproducibility because different versions of packages might have different behaviors or introduce breaking changes.

**Creating Requirements Files:**

🔸 One common use of pip freeze is to generate a **requirements.txt file**.

> 💡 This file **lists all the packages and their versions that are required for your project to run correctly**. This is essential for sharing your project with others or deploying it to different environments, ensuring that everyone installs the same versions of packages.

**Environment Replication:**

🔴 By using **requirements.txt** created by **pip freeze**, you can **recreate** the ✋ **exact Python environment on another machine** or for a different user. This is particularly useful in collaborative projects or when deploying applications to production servers.

[ check the video to see MORE: 9:10min ||| Entornos Virtuales con Python (Módulo virtualenv) ✅ | Curso Python 3 🐍 # 63](https://youtu.be/TNtrAvNNxTY?si=GkseHLyA-HkqAY9U&t=550)

### or [min: 12:23 | Python Virtual Environment and pip for Beginners

](https://youtu.be/eDe-z2Qy9x4?si=U1HE23ljMVVBhpAD&t=743)


<br>
<br>
<br>

---

<br>