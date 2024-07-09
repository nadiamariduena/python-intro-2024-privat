## 🟡 PYENV installing

<br>
<br>

### I encountered an issue when trying to run the code on the  [weather api](./z_weather-API.md)


```python
import requests
from dotenv import load_dotenv
#
import os
```

<br>

### Somehow i always ended up having the red underline on the `Weather.py`

<br>

- So i checked the requirements.txt of the project, and when I hovered under the dotenv (you will see 3 dots ) and the charset, I could see the below:

```javascript
Package `charset-normalizer` is not installed in the selected environment.Python-InstalledPackagesCheckernot-installed
//
//
Package `python-dotenv` is not installed in the selected environment.Python-InstalledPackagesCheckernot-installed

```


<br>
<br>

----


<br>

## 🟣 PYENV installation


<br>

### 🟠 install

This command below installs **pyenv** ✋ globally on your system. It sets up pyenv in your home directory (`~/.pyenv`) and modifies your shell's initialization file (like `.bashrc, .zshrc, etc`.) to include **pyenv** commands.

```javascript
curl https://pyenv.run | bash
```


#### output

```javascript
$ sudo curl https://pyenv.run | bash
[sudo] password for mycomputer:
sudo: curl: command not found
```

<br>


### 🟠 update it

```javascript
sudo apt update
// you will have a long list of updated packages
```

<br>

### 🟠 try again to install curl

```javascript
sudo apt install curl
```