## 🔴 Red underline



<br>


<br>

### 🧶Why? 🧶 🧶

#### I encountered an issue when trying to run the code on the  [weather api](./z_weather-API.md) exercise

<br>

 **the issue:**

 - red underline due to packages not being installed in the environment

 -  later on i will discover that not only this type of red underline appears because the packages are not well installed but also because even if the packages are installed, 🔴 the **Pylint** will recognize other type of issues (so here the **pylint is not the bad guy but the good one, its only telling you that something is wrong [Pylint-errs](./z_PYlint-errs.md)** so its a good thing to have it.

<br>

 - ⚠️ check also the issues you can possibly have in different python versions [python-toavoid](./z_PYENV_versions-python-toavoid.md)


```python
import requests
from dotenv import load_dotenv
#
import os
```

<br>

#### Somehow i always ended up having the red underline on the `Weather.py`

<br>

- So i checked the requirements.txt of the project, and when I hovered under the dotenv (you will see 3 dots ) and the charset, I could see the below:

```javascript
Package `charset-normalizer` is not installed in the selected environment.Python-InstalledPackagesCheckernot-installed
//
//
Package `python-dotenv` is not installed in the selected environment.Python-InstalledPackagesCheckernot-installed

```
<br>

 - ⚠️ check also the issues you can possibly have in different python versions [python-toavoid](./z_PYENV_versions-python-toavoid.md)



<br>
<br>

## 🌈 solution

- After reading about the [different types of issues](./z_PYENV_versions-python-toavoid.md) you can have with python versions, I DECIDED to test a couple of them, keeping in mind that in the above link it says also that for DJANgo you will need the latest  versions


<br>


### 🟣 versions i have installed

- i will continue to test to see the different type of issues

```javascript
// 3.7.14 (with this version the red underline is gone)
  system
* 3.7.14 (set by /home/mycomputer/.pyenv/version)
  3.8.10 //(red underline)
  3.8.18 //(i had several issues with this one, missing packages, red underline)
  3.10.8 // (red underline)

```

## 🔴 [](z_Python_err-install_packages.md)

<br>
<br>


#### 🟡 Determining the "best" Python version depends on several factors, including your specific project requirements, compatibility with libraries and frameworks you intend to use, and whether you prioritize stability or newer features.

<br>
<br>

##### chatgpt:

### 🟠As of my last update in January 2022, here are some considerations for Python versions:

<br>

### 🔸 PYTHON 3.9

Python **3.9.x:** `Python 3.9` is a stable release with a good balance of new features and stability.

- ✅ It includes performance improvements and new syntax **features like the merge operator** `(|)` for dictionaries. Many libraries and frameworks support Python 3.9 well.


<br>

### 🔸 Python 3.8

Python **3.8.x:** `Python 3.8` is another stable release with Long Term Support (LTS) until October 2024.

- ✅ It's widely used and generally considered stable and reliable. It **introduced the assignment expressions** `(walrus operator :=)` and optimizations in various areas.

<br>


### 🔸 Python 3.7

Python **3.7.x:** `Python 3.7` is also a solid choice with many libraries and frameworks supporting it.

- ✅ It **introduced data classes and various performance improvements**. It's still maintained, with security fixes being provided until mid-2023.

<br>

### 🔸 Python 3.10

Python **3.10.x:** `Python 3.10` is the latest stable release as of now (July 2024).

- ✅ It **includes new features like pattern matching and improved error messages**.

- - 👎 However, being relatively new, some libraries and frameworks may not fully support it yet, so compatibility should be verified.


<br>
<br>

### 🔸 Python 3.6

Python **3.6.x:** `Python 3.6` is older but still supported with security updates until December 2021.

-  It's generally stable, but newer Python versions have added significant improvements and features since then.

### is Python 3.6 compatible with Django?

##### chatgpt:

- - Yes, Python 3.6 is compatible with Django. Django officially supports a range of Python versions, and Python 3.6 is within that supported range for most versions of Django.


<br>

### 🟣 What Python version can I use with Django?

https://docs.djangoproject.com/en/5.0/faq/install/

```javascript
3.2	3.6, 3.7, 3.8, 3.9, 3.10 (added in 3.2.9)
4.0	3.8, 3.9, 3.10
4.1	3.8, 3.9, 3.10, 3.11 (added in 4.1.3)
4.2	3.8, 3.9, 3.10, 3.11, 3.12 (added in 4.2.8)
5.0	3.10, 3.11, 3.12
```

#### 🔴 However, it's important to note that Python 3.6 reached its end-of-life status in December 2021, which means it no longer receives official support or updates from the Python core development team.

- - While Django may still officially support Python 3.6 in its older releases, it's advisable to consider upgrading to a supported Python version (like Python 3.7 or newer) for security and compatibility with other libraries and tools in the Python ecosystem.