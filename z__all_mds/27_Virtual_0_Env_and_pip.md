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

### 👾 check the numpy examples here [27_Virtual_1_numpy](27_Virtual_1_numpy_.md)

<br>

---

<br>

### 🟡 Installing packages using PIP

- open the terminal, type: `pip install requests`

> The **requests** package in Python is a powerful tool used for making HTTP requests from your Python code. Here’s more detail on its purpose and some key features [ read more](../z_about_packages/pip_requests.md)

### installing the request package

- Normally the following command would suffice to install the package on your project but if it doesn't work, you have a couple of options

```javascript
// option 1
pip install requests
// option 2
python -m pip install requests
```

<br>

### 🔴 but if you get the following error:

`/usr/bin/python: No module named pip`

### 1. got to your terminal (ubuntu), type this:

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

### 2. type this: `python3 get-pip.py`

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

- **1)** Install pip using apt (if available)

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

- **2)** Type this `sudo apt update` to update everything (just to be sure)

```javascript
// output
// ...
Reading package lists... Done
Building dependency tree
Reading state information... Done
21 packages can be upgraded. Run 'apt list --upgradable' to see them.
```

<br>

- **3)** ✋ Since this is the module `'distutils.cmd'` that is causing the issue, i will install it:

```javascript
sudo apt install python3-distutils
```
