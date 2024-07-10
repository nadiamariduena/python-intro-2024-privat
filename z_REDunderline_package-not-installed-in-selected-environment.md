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


<br>
<br>


#### 🟡 Determining the "best" Python version depends on several factors, including your specific project requirements, compatibility with libraries and frameworks you intend to use, and whether you prioritize stability or newer features.

<br>
<br>

### 🟠As of my last update in January 2022, here are some considerations for Python versions:

<br>

Python **3.9.x:** `Python 3.9` is a stable release with a good balance of new features and stability. It includes performance improvements and new syntax features like the merge operator (|) for dictionaries. Many libraries and frameworks support Python 3.9 well.
