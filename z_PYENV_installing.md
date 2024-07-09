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

### 🟠 try to install pyenv again

```javascript
sudo curl https://pyenv.run | bash

```
#### output


```javascript



```javascript
% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   270  100   270    0     0    198      0  0:00:01  0:00:01 --:--:--   198
Cloning into '/home/mycomputer/.pyenv'...
remote: Enumerating objects: 1267, done.
remote: Counting objects: 100% (1267/1267), done.
remote: Compressing objects: 100% (698/698), done.
remote: Total 1267 (delta 747), reused 723 (delta 436), pack-reused 0
Receiving objects: 100% (1267/1267), 627.16 KiB | 965.00 KiB/s, done.
Resolving deltas: 100% (747/747), done.
Cloning into '/home/mycomputer/.pyenv/plugins/pyenv-doctor'...
remote: Enumerating objects: 11, done.
remote: Counting objects: 100% (11/11), done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 11 (delta 1), reused 5 (delta 0), pack-reused 0
Receiving objects: 100% (11/11), 38.72 KiB | 388.00 KiB/s, done.
Resolving deltas: 100% (1/1), done.
Cloning into '/home/mycomputer/.pyenv/plugins/pyenv-update'...
remote: Enumerating objects: 10, done.
remote: Counting objects: 100% (10/10), done.
remote: Compressing objects: 100% (6/6), done.
Receiving objects: 100% (10/10), done.
remote: Total 10 (delta 1), reused 5 (delta 0), pack-reused 0
Resolving deltas: 100% (1/1), done.
Cloning into '/home/mycomputer/.pyenv/plugins/pyenv-virtualenv'...
remote: Enumerating objects: 64, done.
remote: Counting objects: 100% (64/64), done.
remote: Compressing objects: 100% (56/56), done.
remote: Total 64 (delta 10), reused 29 (delta 1), pack-reused 0
Receiving objects: 100% (64/64), 42.50 KiB | 414.00 KiB/s, done.
Resolving deltas: 100% (10/10), done.

WARNING: seems you still have not added 'pyenv' to the load path.

# Load pyenv automatically by appending
# the following to
# ~/.bash_profile if it exists, otherwise ~/.profile (for login shells)
# and ~/.bashrc (for interactive shells) :

export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# Restart your shell for the changes to take effect.

# Load pyenv-virtualenv automatically by adding
# the following to ~/.bashrc:

eval "$(pyenv virtualenv-init -)"

```

<br>


### 🟠 edit the initialization

```javascript
// 1
sudo apt-get update

//2
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

```
 <br>


 ## 🟣 nano

- this will open the nano

```javascript
nano ~/.bashrc
```

<br>

- 🟧 Paste the below at the end of the **nano** file, if you have no idea check this [freecodecamp.org/news/how-to-save-and-exit-nano-in-terminal]
(https://www.freecodecamp.org/news/how-to-save-and-exit-nano-in-terminal-nano-quit-command/)

<br>

```bash
# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
<br>

#### 🟧  to save: `strg + O`, check the file you are saving on (be careful), if its correct press ENTER, then.. to get out press `strg + X`


<br>


### 🟠 Applying Changes

<br>

- After adding the lines to your initialization script, save the file and close the text editor.

- To apply these changes, you typically need to reload the shell or source the initialization script:

```javascript
source ~/.bashrc
```

<br>
<br>


### 🟢 Verify Installation
To verify that pyenv is installed correctly, you can check its version:

```javascript
pyenv --version
```
#### output

```javascript
pyenv 2.4.7

```

<br>
<br>

---

<br>
<br>
<br>

## 🟡  check the list of Python versions

<br>
<br>


The `pyenv install --list` command is used to list all the versions of Python that can be installed using pyenv, a popular tool for managing multiple Python versions on a single system.


```javascript
pyenv install --list
```

#### Here's a breakdown of its purpose:


Listing Available Python Versions: When you run `pyenv install --list`, pyenv fetches and displays a list of all available Python versions that it supports. This list includes both stable releases and pre-release versions.

**Version Selection:** This command helps you decide which specific version of Python you want to install. It provides information such as version numbers and release dates, which can be useful for making an informed choice.

**Managing Python Environments:** 🔴 pyenv allows you to install multiple versions of Python on your machine and easily switch between them. By listing available versions, you can see which ones are compatible with your applications or projects.

<br>


#### ✋(this is just a short list, you have a lot more, but from here i will pick the versions i want to test, so to see if i have the same red underline issue when trying to import the DOTENV)

```javascript
Available versions:
  2.1.3
  2.2.3
  2.3.7
  2.4.0
  2.4.1
  2.4.2
  2.4.3
  2.4.4
  2.4.5
  2.4.6
  2.5.0
  2.5.1
  2.5.2
  2.5.3
  2.5.4
  2.5.5
  2.5.6
  2.6.0
  2.6.1
  2.6.2
  2.6.3
  2.6.4
  2.6.5
  2.6.6
  2.6.7
  2.6.8
  2.6.9
  2.7.0
  2.7-dev
  2.7.1
  2.7.2
  2.7.3
  2.7.4
  2.7.5
  2.7.6
  2.7.7
  2.7.8
  2.7.9
  2.7.10
  2.7.11
  2.7.12
  2.7.13
  2.7.14
  2.7.15
  2.7.16
  2.7.17
  2.7.18
  3.0.1
  3.1.0
  3.1.1
  3.1.2
  3.1.3
  3.1.4
  3.1.5
  3.2.0
  3.2.1
  3.2.2
  3.2.3
  3.2.4
  3.2.5
  3.2.6
  3.3.0
  3.3.1
  3.3.2
  3.3.3
  3.3.4
  3.3.5
  3.3.6
  3.3.7
  3.4.0
  3.4-dev
  3.4.1
  3.4.2
  3.4.3
  3.4.4
  3.4.5
  3.4.6
  3.4.7
  3.4.8
  3.4.9
  3.4.10
  3.5.0
  3.5-dev
  3.5.1
  3.5.2
  3.5.3
  3.5.4
  3.5.5
  3.5.6
  3.5.7
  3.5.8
  3.5.9
  3.5.10
  3.6.0
  3.6-dev
  3.6.1
  3.6.2
  3.6.3
  3.6.4
  3.6.5
  3.6.6
  3.6.7
  3.6.8
  3.6.9
  3.6.10
  3.6.11
  3.6.12
  3.6.13
  3.6.14
  3.6.15
  3.7.0
  3.7-dev
  3.7.1
  3.7.2
  3.7.3
  3.7.4
  3.7.5
  3.7.6
  3.7.7
  3.7.8
  3.7.9
  3.7.10
  3.7.11
  3.7.12
  3.7.13
  3.7.14
  3.7.15
  3.7.16
  3.7.17
  3.8.0
  3.8-dev
  3.8.1
  3.8.2
  3.8.3
  3.8.4
  3.8.5
  3.8.6
  3.8.7
  3.8.8
  3.8.9
  3.8.10
  3.8.11
  3.8.12
  3.8.13
  3.8.14
  3.8.15
  3.8.16
  3.8.17
  3.8.18
  3.8.19
  3.9.0
  3.9-dev
  3.9.1
  3.9.2
  3.9.4
  3.9.5
  3.9.6
  3.9.7
  3.9.8
  3.9.9
  3.9.10
  3.9.11
  3.9.12
  3.9.13
  3.9.14
  3.9.15
  3.9.16
  3.9.17
  3.9.18
  3.9.19
  3.10.0
  3.10-dev
  3.10.1
  3.10.2
  3.10.3
  3.10.4
  3.10.5
  3.10.6
  3.10.7
  3.10.8
  3.10.9
  3.10.10
  3.10.11
  3.10.12
  3.10.13
  3.10.14
  3.11.0
  3.11-dev
  3.11.1
  3.11.2
  3.11.3
  3.11.4
  3.11.5
  3.11.6
  3.11.7
  3.11.8
  3.11.9
  3.12.0
  3.12-dev
  3.12.1
  3.12.2
  3.12.3
  3.12.4
  3.13.0b3
  3.13.0b3t
  3.13-dev
  3.13t-dev
  3.14-dev
  3.14t-dev

```

<br>

### 🟢 i will choose this:

```javascript
pyenv install 3.8.18
```

<br>

#### 🟠 Once you type this command `pyenv install 3.8.18` you will have to ✋ WAIT ✋ like 3 minutes (depends on your connection)

```javascript
mycomputer@usercomp:~$ pyenv install 3.8.18
Downloading Python-3.8.18.tar.xz...
-> https://www.python.org/ftp/python/3.8.18/Python-3.8.18.tar.xz
Installing Python-3.8.18...
Traceback (most recent call last):

```

<br>

### 🟣 check the python versions you have on your computer

 ```javascript
 pyenv versions
 ```

 ### output

```javascript
pyenv versions
  system
  3.8.10
* 3.8.18 (set by /home/mycomputer/.pyenv/version)
  3.10.8

```
