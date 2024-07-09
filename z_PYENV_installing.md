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
<br>

### 🟠 try again to install curl

```javascript
sudo apt install curl
```


#### output

```javascript
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following NEW packages will be installed:
  curl
0 upgraded, 1 newly installed, 0 to remove and 3 not upgraded.
Need to get 227 kB of archives.
After this operation, 532 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 curl amd64 8.5.0-2ubuntu10.1 [227 kB]
Fetched 227 kB in 1s (207 kB/s)
Selecting previously unselected package curl.
(Reading database ... 229525 files and directories currently installed.)
Preparing to unpack .../curl_8.5.0-2ubuntu10.1_amd64.deb ...
Unpacking curl (8.5.0-2ubuntu10.1) ...
Setting up curl (8.5.0-2ubuntu10.1) ...
Processing triggers for man-db (2.12.0-4build2) ...

```