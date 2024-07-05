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


# 🟡 PIP local

<br>

### Packages that Can Be Installed with PIP:

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

## 🟡 4.