# 🟡Virtual Environment and pip

- Pip Global [Go to section](#pip_global)

- Pip Local packages [Go to section](#pip_local)

<br>
<br>

### 🟠 ABOUT: Virtual Environment

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
<br>

# 🟡 INSTALLATION

- before starting with the installation of the virtual environment in your project, check a couple of things:

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

### dpkg / APT


>This **can lead to errors**, especially with **dpkg** (the package manager used by **apt**) if dependencies are not properly managed. ✋ [check the type of errors you will get](https://askubuntu.com/questions/1329514/how-can-i-resolve-dpkg-error-after-uninstalling-python3)

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

---

<br>
<br>





# 🟡 1. PIP

PIP **(Python Package Installer)** is the standard package manager for Python. It is used to install and manage additional libraries and dependencies that are not part of the Python standard library. Here's a breakdown of its key aspects and its link to virtual environments:

- **Package Installation:** PIP is primarily used to install packages from the Python Package Index (PyPI) and other package indexes.

- **Package Management:** It helps in managing Python package dependencies for your projects.

- **Version Management:** PIP allows you to install specific versions of packages, ensuring compatibility with your code.

- **Upgrading Packages:** It provides commands to upgrade packages to their latest versions.

- **Uninstallation:** PIP can uninstall packages that are no longer needed.

<br>
<br>



<br>
<br>

<a name="pip_global"></a>

# 🟡 2. PIP global

<br>

 I recently reinstalled Ubuntu, and Python came pre-installed, so I didn't have to install it separately. Now I'm wondering: does the pip I installed globally (sudo apt install python3-pip) conflict with the one invoked using python -m pip install requests, or are they separate entities?

##### chatgpt:

**Global Installation:** When you install python3-pip using apt (Advanced Package Tool), it installs pip globally on your system. This means pip will be available for use by any user and any Python project on that machine.

```javascript
//global
// 1 install PIP
sudo apt install python3-pip
// 2 install pip.py
wget https://bootstrap.pypa.io/get-pip.py
```



#### Read more about the `get pip py` [Go to section](#wget_get-pip-py)


<br>

## 🍊 get-pip.py

#### If your Ubuntu installation already comes with Python, running `wget https://bootstrap.pypa.io/get-pip.py` should not cause any clashes or conflicts with the Python installation itself. Here’s why:

<br>

#### 🔸 Purpose of get-pip.py:

The get-pip.py script is specifically designed to install **pip for Python**. It does this by downloading the pip installer script from `PyPA` (Python Packaging Authority) and running it using the Python interpreter specified on your system.

#### 🔸 Ubuntu's Python Installation:

Ubuntu typically comes with a system-wide installation of Python. When you run `sudo apt install python3-pip`, it installs pip specifically for the system's Python installation (Python 3 in this case).

#### 🔸 Clash or Conflict:

Running `wget https://bootstrap.pypa.io/get-pip.py` followed by `python3 get-pip.py` is generally **safe and should not clash with the existing Python installation** on your Ubuntu system. This process will install pip for Python 3 if it's not already installed.


<br>
<br>

---

<br>
<br>



# 🟠 3. Virtual Environments and PIP:

 <br>

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


## 👾 HOW to use it

##### example SYS:

- check the code here [LESSON_03_tuples/rps3_whileLoop.py](../LESSON_03_tuples/rps3_whileLoop.py)

<br>

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

<a name="pip_local"></a>


## 🟡 PIP local

#### Packages that Can Be Installed with PIP:

<br>

**Third-Party Packages:** These are not included with Python by default but can be easily installed using PIP from repositories like PyPI (Python Package Index). Some examples include:

<br>

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

### 👾 check the numpy examples here [27_Virtual_1_numpy](27_Virtual_1_numpy_.md)

<br>

---

<br>

## 🟡 4. Installing packages using PIP into specific projects

<br>

- **open** the terminal (of the project you want to install the pip request) example: `/LESSON_16_OOP$....`, **type:** `pip install requests`

> The **requests** package in Python is a powerful tool used for making HTTP requests from your Python code. Here’s more detail on its purpose and some key features [ read more](../z_about_packages/pip_requests.md)

<br>

### installing the request package

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

### then check if you get the LIST (as that is what i want to obtain), type this to verify the whole process worked: `python -m pip list`

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
