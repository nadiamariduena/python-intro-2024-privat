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

- After reading about the [different types of issues](./z_PYENV_versions-python-toavoid.md) you can have with python versions, I DECIDED to test a couple of them, keeping in mind that even if

