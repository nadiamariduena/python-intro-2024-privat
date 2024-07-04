


# 🟡 Virtual Environment


- GENERATE the environment [Go to section](#generate_the_environments)

- ACTIVATE the environment [Go to section](#activate_the_environments)

<br>


<br>

<br>
<br>


## 🟢 Why Multiple environments ?

<br>


### 🟠 It's pretty normal to have multiple Python applications running on your computer.

> ✋Sometimes, one app wants a specific version of a module, while another app wants a different version of the exact same module.



### 🟠 How can you provide 2 VERSIONS of the same module?

<br>

 🏁 Remember, when you use **pip** to install updates, it affects all Python programs on your computer.

> 🔴 **For example**, if you update a module like requests using pip, every Python program that uses requests will now use the updated version.

<br>
 <br>

 ---


 <br>
 <br>

### 🟠 Using VIRTUAL environments to to manage different versions of Python modules for different applications

##### chatgpt:

- One solution to manage different versions of Python modules for different applications, is to use virtual environments. Here’s how it works:

<br>
<br>


<a name="generate_the_environments"></a>

# 🌈 Generate 🌈

### 🍰 to Generate the environment, follow the below steps:


<br>

🔸 1. check the project you are on, in my case i will **cd** into the following folder: `cd LESSON_17_Virtual_Environment_and_pip`

🔸 2. Keep in mind that after the **step 3** here below, you will have to **ACTIVATE** the environment.

🔸 3. Now type the commands `python3 -m .env` (depending if you are using py instead of python3 or python), also the `.env` is my choice, you can use it exactly how you see in on the tutorial [6:20 | Python Virtual Environment and pip for Beginners
](https://youtu.be/eDe-z2Qy9x4?si=WxJwgqwVc-bEeOAD&t=380):

<br>
<br>

## 🟪 CREATE 🌟




```javascript
// venv: will help me  to create the 'virtual environment
// .venv: will create a folder inside of the project
py -m venv .venv //
//✋ or :
python -m venv .venv
//✋ or :
python3 -m venv .myvenv //()
// once you type the above command, press ENTER, this will automatically generate a folder (check it at the left bar)
```

### 💅 `.venv` is optional. you can type: `.env` , `.myvenv` etc etc...

#### output:

```python
LESSON_17_Virtual_Environment_and_pip
   ▶️.venv # ✋ this is the created folfer after you typed the above commands
```

<br>
<br>


## 🟧 the content of the `.venv`

- 🟢 If it Works: within the **.venv** (or whatever name you put) folder you will find the below folders:


<a name="result_of_the_generated_environment"></a>


```javascript
project_folder/
├── env/
  └── bin/
     └── activate
     └── activate.csh
     └── activate.fish
     └── activate.ps1
     └── pip
     └── pip3
     └── pip3.12
     └── python
     └── python3
     └── python3.12

  └── include/
  └── lib/
  └── lib64/
  └── pyvenv.cfg

```

<br>

### 🟧 Inspecting the `.venv` (or whatever name you used, in my case, i named it `.env`) content

```python
# You can check what the folder contains with the command below, but check that you are in the correct directory (the project you are installing the venv)
ls -l .venv   # Linux/macOSs
```
#### output

```javascript
total 16
drwxrwxr-x 2 mycomputer mycomputer 4096 Jul  3 02:45 bin
drwxrwxr-x 3 mycomputer mycomputer 4096 Jul  3 02:45 include
drwxrwxr-x 3 mycomputer mycomputer 4096 Jul  3 02:45 lib
lrwxrwxrwx 1 mycomputer mycomputer    3 Jul  3 02:45 lib64 -> lib
-rw-rw-r-- 1 mycomputer mycomputer  233 Jul  3 02:45 pyvenv.cfg
//
// use the below command to return back on the tree
// cd ../
```

### cd `.env` , then type `ls`

```javascript
// 1 cd .env
LESSON_16_OOP$ cd .env
// output
LESSON_16_OOP/.env$
// 2 ls to check the .env content
LESSON_16_OOP/.env$ ls
// output
bin  include  lib  lib64  pyvenv.cfg
// 3 cd .env
LESSON_16_OOP/.env$ cd bin
// output
LESSON_16_OOP/.env/bin$
// 4 ls to check the .bin content
LESSON_16_OOP/.env/bin$ ls
// output
activate      activate.fish  pip   pip3.12  python3
activate.csh  Activate.ps1   pip3  python   python3.12
```



<br>


### 🔴 If it fails, you will only have the below, but inside the bin you will only have some binary python files, not the activation & pip files

- bin

- include

- lib

- lib64

- pyvenv.cfg


<br>
<br>

#### 🟠 `pyvenv.cfg`

The **pyvenv.cfg** file is a configuration file automatically generated when you create a virtual environment using the `pyvenv` or `python -m venv` command in Python. It contains settings that define the behavior of the virtual environment.

```javascript
// within the pyvenv.cfg you will find this:
>home = /usr/bin
include-system-site-packages = false
version = 3.8.10
```

<br>

#### Description:

```javascript
// home = /usr/bin:

// This line specifies the location of the Python interpreter that the virtual environment is associated with. In this case, it indicates that the virtual environment is using the Python interpreter located at /usr/bin.

// ---------------
//
// include-system-site-packages = false:

// This setting determines whether the virtual environment includes access to the system-wide installed Python packages (site-packages). When set to false, which is the default behavior, the virtual environment will not inherit packages installed globally on your system. This ensures isolation and prevents conflicts with system-wide Python packages.

// ---------------
//
//  include-system-site-packages = false:

// This setting determines whether the virtual environment includes access to the system-wide installed Python packages (site-packages).

// 🔴 When set to false, which is the default behavior, the virtual environment will not inherit packages installed globally on your system. This ensures isolation and prevents conflicts with system-wide Python packages.
```

<br>

### 🟠 Purpose of `pyvenv.cfg`:

<br>

**Configuration:** `pyvenv.cfg` provides essential configuration details for the virtual environment, such as the Python interpreter path and version. These settings ensure that when you activate the virtual environment, it uses the correct Python interpreter and maintains isolation from the global Python environment.

**Isolation:** By specifying `include-system-site-packages = false`, the virtual environment **ensures** that <u>only packages installed within the virtual environment are accessible to Python scripts executed within that environment.</u> This isolation prevents conflicts and allows different applications to use different versions of packages without interference.

<br>
<br>


---


<br>
<br>

<a name="activate_the_environments"></a>

# 🌈 ACTIVATION

🔸 **1.**  After you generated the environment   [Go to section](#result_of_the_generated_environment)

🔸 **2.** Activate the environment


```javascript
source .env/bin/activate


```
#### output

```javascript
// ✋ here you can notice the the (env) is part present
(.env) mycomputer@mycomputer:~/Documents/0_PYTHON-all/LESSON_16_OOP$
```


<br>
<br>


---


<br>
<br>
<br>

## 🔴 ACTIVATION issue

#### ✋ the below happened because i had installed python on the python that already comes with some version of ubuntu

<br>


<br>

<br>

<br>


## 🍭 Activate

- type the following command (you have to be on your project root)

```javascript
//💡💡💡
source env/bin/activate
//💡💡💡
// like so:
LESSON_16_OOP$ source env/bin/activate
```

#### output

```javascript
// the env is there, it means it works
/LESSON_16_OOP$ source env/bin/activate
(env) dci-st119@mycomputer:
```

### deactivate

- if you want to log out of the **environment** , type: `deactivate`

```javascript
//💡💡💡
(env) dci-st119@wunderkatz:~ /LESSON_17_Virtual_Environment_and_pip$ deactivate
//💡💡💡

```

<br>

---

<br>

#### 🔴 Now tht i am inside the virtual environment like you can see in the below code, you can check the packages, type this command:

```javascript
pip list
```

#### output

```javascript
Package    Version
---------- -------
pip        24.1
setuptools 70.1.0
wheel      0.43.0

```

#### like so:

```javascript
/LESSON_16_OOP$ pip list
Package    Version
---------- -------
pip        24.1
setuptools 70.1.0
wheel      0.43.0
(env) dci-st119@mycomputer:~/
```

<br>

---

<br>

# 🟠 Installing other packets

- Now that I have the env setup, i can install stuff but **ONLY** in this env (environment)

<br>

## 🟡 Install FLASK

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

###
