
- Requests

- Flask

- DJANGO

- FREEZE

<br>
<br>


---

<br>

## 🟡 PIP `REQUESTS`



<br>

### 🟣 ABOUT:


<br>

> The **requests** package in Python is a powerful tool used for making HTTP requests from your Python code. Here’s more detail on its purpose and some key features [ read more](../z_about_packages/pip_requests.md)

<br>



<br>
<br>

### 🟢 INSTALLING the request package

<br>

- **open** the terminal (of the project you want to install the pip request) example: `/LESSON_16_OOP$....`, **type:** `pip install requests`

- Normally the following command would suffice to install the package on your project but if it doesn't work, you have a couple of options

```javascript
// option 1
pip install requests
// option 2
python -m pip install requests
// option 3
python3 -m pip install requests
```

<br>

### 🔴 but if you get the following error:

`/usr/bin/python: No module named pip`


<a name="wget_get-pip-py"></a>

## 🟣 5. wget

### 01. got to your terminal (ubuntu), type this:

`wget https://bootstrap.pypa.io/get-pip.py`


##### output

```javascript
// .... SENSITIVE DATA (your ip and other stuff)
// .... then you will get the below
nnected.
HTTP request sent, awaiting response... 200 OK
Length: 2276232 (2,2M) [text/x-python]
Saving to: ‘get-pip.py’

get-pip.py          100%[===================>]   2,17M  3,11MB/s    in 0,7s

2024-06-21 21:15:05 (3,11 MB/s) - ‘get-pip.py’ saved [2276232/2276232]
// ✋ this seems okay
```

<br>

### 02. type this: `python3 get-pip.py`

##### output

```javascript
Traceback (most recent call last):
  File "get-pip.py", line 28541, in <module>
    main()
  File "get-pip.py", line 135, in main
    bootstrap(tmpdir=tmpdir)
  File "get-pip.py", line 111, in bootstrap
    monkeypatch_for_cert(tmpdir)
  File "get-pip.py", line 92, in monkeypatch_for_cert
    from pip._internal.commands.install import InstallCommand
  File "<frozen zipimport>", line 259, in load_module
  File "/tmp/tmp895wfcyr/pip.zip/pip/_internal/commands/__init__.py", line 9, in <module>
  File "<frozen zipimport>", line 259, in load_module
  File "/tmp/tmp895wfcyr/pip.zip/pip/_internal/cli/base_command.py", line 15, in <module>
  File "<frozen zipimport>", line 259, in load_module
  File "/tmp/tmp895wfcyr/pip.zip/pip/_internal/cli/cmdoptions.py", line 24, in <module>
  File "<frozen zipimport>", line 259, in load_module
  File "/tmp/tmp895wfcyr/pip.zip/pip/_internal/cli/parser.py", line 12, in <module>
  File "<frozen zipimport>", line 259, in load_module
  File "/tmp/tmp895wfcyr/pip.zip/pip/_internal/configuration.py", line 26, in <module>
  File "<frozen zipimport>", line 259, in load_module
  File "/tmp/tmp895wfcyr/pip.zip/pip/_internal/utils/logging.py", line 29, in <module>
  File "<frozen zipimport>", line 259, in load_module
  File "/tmp/tmp895wfcyr/pip.zip/pip/_internal/utils/misc.py", line 43, in <module>
  File "<frozen zipimport>", line 259, in load_module
  File "/tmp/tmp895wfcyr/pip.zip/pip/_internal/locations/__init__.py", line 66, in <module>
  File "<frozen zipimport>", line 259, in load_module
  File "/tmp/tmp895wfcyr/pip.zip/pip/_internal/locations/_distutils.py", line 20, in <module>
ModuleNotFoundError: No module named 'distutils.cmd' // 🔴 not good

```

<br>
<br>

## 🟠 If that failed, then try this:

- **a)** Install pip using apt (if available)

- If **apt** is giving you trouble, you might try installing pip via the Ubuntu package manager directly, although this method may not always yield the most recent version of pip: `sudo apt install python3-pip`

```javascript
// OUTPUT
Reading package lists... Done
Building dependency tree
Reading state information... Done
Package python3-pip is not available, but is referred to by another package.
This may mean that the package is missing, has been obsoleted, or
is only available from another source

E: Package 'python3-pip' has no installation candidate
// 🔴 NOT GOOD
```

- **b)** Type this `sudo apt update` to update everything (just to be sure)

```javascript
// output
// ...
Reading package lists... Done
Building dependency tree
Reading state information... Done
21 packages can be upgraded. Run 'apt list --upgradable' to see them.
```

<br>

- **c)** ✋ Since this is the module `'distutils.cmd'` that is causing the issue, i will install it:

```javascript
sudo apt install python3-distutils
```

#### once installed

- read the last 5 lines, if there is nothing wrong (like missing package etc...) then it worked!, i go this:

```javascript
Selecting previously unselected package python3-distutils.
(Reading database ... 226770 files and directories currently installed.)
Preparing to unpack .../python3-distutils_3.8.10-0ubuntu1~20.04_all.deb ...
Unpacking python3-distutils (3.8.10-0ubuntu1~20.04) ...
Setting up python3-distutils (3.8.10-0ubuntu1~20.04) ...

```

<br>
<br>

### TYpe this again:

- 1 `wget https://bootstrap.pypa.io/get-pip.py`

- 2 then this `python3 get-pip.py`

```javascript
// output of step 2
Successfully installed pip-24.1 setuptools-70.1.0 wheel-0.43.0
```

<br>
<br>

### 🌈 Now TRY to install the `requests` again, type the following: `python -m pip install requests`

```javascript
 // OUTPUT
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: requests in /usr/lib/python3/dist-packages (2.22.0)
```

<br>

### then check if you get the LIST with lots of packages including the requests  , type this to verify the whole process worked: `python -m pip list`

```javascript
// ✅ GOOD!! it works. 🌈

Package                Version
---------------------- --------------------
apturl                 0.5.2
bcrypt                 3.1.7
blinker                1.4
Brlapi                 0.7.0
certifi                2019.11.28
chardet                3.0.4
Click                  7.0
colorama               0.4.3
command-not-found      0.3
cryptography           2.8
cupshelpers            1.0
dbus-python            1.2.16
defer                  1.0.6
distro                 1.4.0
distro-info            0.23+ubuntu1.1
duplicity              0.8.12.0
entrypoints            0.3
fasteners              0.14.1
future                 0.18.2
httplib2               0.14.0
idna                   2.8
keyring                18.0.1
language-selector      0.1
launchpadlib           1.10.13
lazr.restfulclient     0.14.2
lazr.uri               1.0.3
lockfile               0.12.2
louis                  3.12.0
macaroonbakery         1.3.1
Mako                   1.1.0
MarkupSafe             1.1.0
monotonic              1.5
netifaces              0.10.4
oauthlib               3.1.0
olefile                0.46
paramiko               2.6.0
pexpect                4.6.0
Pillow                 7.0.0
pip                    24.1
protobuf               3.6.1
pycairo                1.16.2
pycrypto               2.6.1
pycups                 1.9.73
PyGObject              3.36.0
PyJWT                  1.7.1
pymacaroons            0.13.0
PyNaCl                 1.3.0
pyRFC3339              1.1
python-apt             2.0.1+ubuntu0.20.4.1
python-dateutil        2.7.3
python-debian          0.1.36+ubuntu1.1
pytz                   2019.3
pyxdg                  0.26
PyYAML                 5.3.1
reportlab              3.5.34
requests               2.22.0 ✋
requests-unixsocket    0.2.0
SecretStorage          2.3.1
setuptools             70.1.0
simplejson             3.16.0
six                    1.14.0
ssh-import-id          5.10
systemd-python         234
ubuntu-advantage-tools 8001
ubuntu-drivers-common  0.0.0
ufw                    0.36
unattended-upgrades    0.1
urllib3                1.25.8
usb-creator            0.3.7
wadllib                1.3.3
wheel                  0.43.0
xkit                   0.0.0
```

### You can also install a specific Version of a packet:

[2:47 | Python Virtual Environment and pip for Beginners](https://youtu.be/eDe-z2Qy9x4?si=LT-ynKPd_9Yfkueb&t=167)

<br>

- Currently i have the: `2.22.0` version fo the **requests**

```javascript
requests               2.22.0 ✋
```

- But i could change it to something else, example:

```javascript
// in my machine: python -m pip install requests==2.30.0
py -m pip install requests==2.30.0
// OUTPUT
  WARNING: The script normalizer is installed in '/home/myComp/.local/bin' which is not on PATH. // 🔴 i will be solving this later
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  // 🌈 success!!
Successfully installed charset-normalizer-3.3.2 requests-2.30.0
```

### Verify the changes

- type this again: `python -m pip list`

```javascript
Package                Version
---------------------- --------------------
apturl                 0.5.2
bcrypt                 3.1.7
blinker                1.4
Brlapi                 0.7.0
certifi                2019.11.28
chardet                3.0.4
charset-normalizer     3.3.2
Click                  7.0
colorama               0.4.3
command-not-found      0.3
cryptography           2.8
cupshelpers            1.0
dbus-python            1.2.16
defer                  1.0.6
distro                 1.4.0
distro-info            0.23+ubuntu1.1
duplicity              0.8.12.0
entrypoints            0.3
fasteners              0.14.1
future                 0.18.2
httplib2               0.14.0
idna                   2.8
keyring                18.0.1
language-selector      0.1
launchpadlib           1.10.13
lazr.restfulclient     0.14.2
lazr.uri               1.0.3
lockfile               0.12.2
louis                  3.12.0
macaroonbakery         1.3.1
Mako                   1.1.0
MarkupSafe             1.1.0
monotonic              1.5
netifaces              0.10.4
oauthlib               3.1.0
olefile                0.46
paramiko               2.6.0
pexpect                4.6.0
Pillow                 7.0.0
pip                    24.1
protobuf               3.6.1
pycairo                1.16.2
pycrypto               2.6.1
pycups                 1.9.73
PyGObject              3.36.0
PyJWT                  1.7.1
pymacaroons            0.13.0
PyNaCl                 1.3.0
pyRFC3339              1.1
python-apt             2.0.1+ubuntu0.20.4.1
python-dateutil        2.7.3
python-debian          0.1.36+ubuntu1.1
pytz                   2019.3
pyxdg                  0.26
PyYAML                 5.3.1
reportlab              3.5.34
requests               2.30.0 // ✅ it works!
requests-unixsocket    0.2.0
SecretStorage          2.3.1
setuptools             70.1.0
simplejson             3.16.0
six                    1.14.0
ssh-import-id          5.10
systemd-python         234
ubuntu-advantage-tools 8001
ubuntu-drivers-common  0.0.0
ufw                    0.36
unattended-upgrades    0.1
urllib3                1.25.8
usb-creator            0.3.7
wadllib                1.3.3
wheel                  0.43.0
xkit                   0.0.0
```

<br>

```javascript
// before
requests               2.22.0 ✋
// after
requests               2.30.0 // ✅ it works!
```

<br>

### To Go back to what i had

- this command below is going to update the package to the currect release

```javascript
// -U for update
// in my machine: python -m pip install -U requests
py -m pip install -U requests
```

##### output

```javascript
requests               2.32.3 // ✋ different to what i had before, the first change
```

<br>

#### Uninstall

- If you want to uninstall and repeat the whole process:

```javascript
// -U for update
// in my machine: python -m pip uninstall requests
py -m pip uninstall requests
```


<br>
<br>
<br>

---

<br>
<br>
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