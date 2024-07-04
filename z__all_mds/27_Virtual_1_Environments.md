# 🟡 Virtual Environment

<br>


## 🟠 Check if you already have PYTHON

#### 🔸 1. Before start, check if PYTHON is already installed in your machine

```javascript
python --version
// OR
python3 --version
//Remember, it's good practice to use Python 3 (python3) for most purposes as Python 2 is no longer supported.
```

#### 🔸 2. To check your Ubuntu version, you can use:

```javascript
lsb_release -a
```
<br>

<br>

## 🟠  Consequences of installing PYTHON

  If you install another version of Python alongside the one already on your machine, it can lead to significant issues. In some cases, resolving these issues may require a complete system wipe and reinstallation of Ubuntu. I once encountered a dpkg error and, out of curiosity, tried reinstalling Ubuntu to see if it would fix the problem. After the reinstall, Python worked without needing to be installed again.



<br>

### 🔴 WHY?:

<br>

 - Ubuntu ✋comes pre-installed with Python because **many system tools and applications depend on it.**

 - Typically, Python 2.x or Python 3.x (depending on the Ubuntu version) is installed by default.

 <br>


 - 🛑 **If you try to install another version of Python** using **apt**, such as python3.9, it can sometimes cause conflicts with the existing Python installation.

>This **can lead to errors**, especially with **dpkg** (the package manager used by apt) if dependencies are not properly managed. ✋ [check the type of errors you will get](https://askubuntu.com/questions/1329514/how-can-i-resolve-dpkg-error-after-uninstalling-python3)

<br>
<br>




## 🟠 When can you install PYTHON



### 🟢 Ubuntu <u>Versions</u>  with Python Included by Default


<br>

- ✋Python is typically included by default in most Ubuntu versions, especially in the desktop versions. However, to be specific:

<br>

>Ubuntu `16.04 LTS` and later versions include Python by default.


>Ubuntu `18.04 LTS` and later versions include Python 3.x by default. **Python 2.x** is not included by default in Ubuntu 18.04 LTS and later, as Python 2.x reached its end of life.

<br>


🔴 If you're using an Ubuntu version **older** than **16.04 LTS**, Python might not be included by default, or it might be an older version.


 > It's recommended to upgrade to a supported version to ensure you have access to the latest Python features and security updates.

<br>

#### 🔸 To check your Ubuntu version, you can use:

```javascript

lsb_release -a
```
<br>
<br>

---


<br>

## WHY Multiple environments ?

<br>

### 🟠 It's pretty normal to have multiple Python applications running on your computer.

> ✋Sometimes, one app wants a specific version of a module, while another app wants a different version of the exact same module.

<br>

### 🔸 How can you provide 2 VERSIONS of the same module?

<br>

 🏁 Remember, when you use **pip** to install updates, it affects all Python programs on your computer.

> 🔴 **For example**, if you update a module like requests using pip, every Python program that uses requests will now use the updated version.

<br>
 <br>

## 🟠 Using VIRTUAL environments to prevent this

##### chatgpt:

### One solution to manage different versions of Python modules for different applications is to use virtual environments. Here’s how it works:

<br>

### 🟢 generate the environment

<br>

1. check the project you are on, in my case i will **cd** into the following folder: `cd LESSON_17_Virtual_Environment_and_pip`

2. Keep in mind that after the **step 3** here below, you will have to **ACTIVATE** the environment.

3. Now type the command below:

<br>

### 🟪 CREATE

```javascript
// venv: will help me  to create the 'virtual environment
// .venv: will create a folder inside of the project
py -m venv .venv //
//✋ or :
python -m venv .venv //()
// once you type the above command, press ENTER, this will automatically generate a folder (check it at the left bar)
```

### 🟣 `.venv` is optional. you can type: `.env` , `.myvenv` etc etc...

<br>

##### output

```python
LESSON_17_Virtual_Environment_and_pip
   ▶️.venv # ✋ this is how it should look like
```

<br>
<br>

## 🟧 the content of the `.venv` folder

<br>

- 🟢 If it Works: within the **.venv** (or whatever name you put) folder you will find the below folders:


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

#### 🍰 ACTIVATION issue

- When i tried to **CREATE** the **env** folder by using this command `python -m venv .venv` , like you see in in the tutorial [6:25 | Python Virtual Environment and pip for Beginners](https://youtu.be/eDe-z2Qy9x4?si=lsQnQ4eoy07Caa1v&t=385), so to create the venv folder, **it works BUT ✋** it DOESN'T CREATE the **SCRIPTS** folder that also comes within the **`.venv` folder**, 🟥 this script folder is important because it comes with some **activation files** , the ones you will always need, check the example: [6:35 | Python Virtual Environment and pip for Beginners](https://youtu.be/eDe-z2Qy9x4?si=3Bg6wM1cXGlaqqh-&t=395)

<br>

#### In the beginning i thought the problem had something to do with this warning i was getting every time i try to install something using PIP:

```javascript
 WARNING: The script virtualenv is installed in '/home/myComputer/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

```

#### [READ MORE: z\_\_ENV_PATH_issue](../z__ENV_PATH_issue.md)

- 🟡 once your read that, continue with the below

<br>

## 🔴 POSSIBLE reasons

<br>

### After reading about the TOPIC, i found the following:

1. It appears that the `python3-venv` package is not available in your current package repositories. This can happen for a few reasons, such as repository **misconfiguration** or changes in **package availability**.

<br>
<br>

### 🟡 There are many was ou can solve this:

- Either by using PyEnv so to have the possibilities to have several python versions, or by using a library/tool such as VIRTUALENV

<br>

<br>

#### 🟢 PyENV

- PyEnv for multiple python versions (one option)

[ENV_ubuntu-version-issue, install PyEnv for multiple python versions](../z__ENV_ubuntu-version-issue.md)

 <br>

#### 🟢 VirtualENV

- Before installing anything related to the VIRTUALENV, check if you already have this: [z\_\_ENV_PATH_issue](../z__ENV_PATH_issue.md), if you have it, you can continue" but if not, just go the link and follow the steps. ✋ to install [VIRTUALENV click here](../z__ENV_VIRTUALENV%20.md)

<br>
<br>

---

<br>

## 🌈 Continue with the activation

- After installing the **virtualEnv** i can continue with the activation but before that, i will create the ENV folder using a different command [min: 3:23 | Entornos Virtuales con Python (Módulo virtualenv) ✅ | Curso Python 3 🐍 # 63](https://youtu.be/TNtrAvNNxTY?si=Ek5y67rtAx4DWwQP&t=203) , **as i am now using virtualenv** instead of the python env, it's different to what you can see in the tutorial i have been watching [min: 7:16 | Python Virtual Environment and pip for Beginners](https://youtu.be/eDe-z2Qy9x4?si=rLciMOjDfQO8l3sg&t=436)

<br>

#### 🍭 creating the env

- creating the **env** with **virtualEnv**

- choose the project where you are going to install the env folder, in my case i will choose `/LESSON_16_OOP` , once you have cd into that project, type the following:

```javascript
virtualenv -p python3 env

// -  -p python3: This specifies that you want to use Python 3 as the interpreter for creating the virtual environment.
//
// - If you omit the -p option, virtualenv will use the default Python interpreter that is available on your system when creating the virtual environment.
//

```

#### output

```javascript
created virtual environment CPython3.8.10.final.0-64 in 307ms
  creator CPython3Posix(dest=/home/mycomputer/Documents/ALL_SITE_3D_STUFF/3D-UNITY-BLENDER-REACTVR-ALL/0_PYTHON-all/PYTHON-PRIVAT/python-intro-2024-privat/LESSON_16_OOP/env, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/mycomputer/.local/share/virtualenv)
    added seed packages: pip==24.1, setuptools==70.1.0, wheel==0.43.0
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
```

<br>

## 🍭 Once the `ENV` has been created, you will see the following:

- 📌 env (folder)
  - bin (folder, it includes the **activation files** and other stuff)
  - lib (folder)
  - gitignore
  - pyvenv.cfg

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
