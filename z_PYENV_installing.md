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