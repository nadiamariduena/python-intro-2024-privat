## 🟡 After reading about the TOPIC, i found the following:

- 🔴 read this [0_installation](./z__all_mds/0_installation.md) before the below

- It appears that the `python3-venv` package is not available in your current package repositories. This can happen for a few reasons, such as repository **misconfiguration** or changes in **package availability**.

#### So i checked the source LIST

check your `/etc/apt/sources.list` and `/etc/apt/sources.list.d/` **directory** to ensure they contain the correct repositories for your Ubuntu version. Here’s how you can examine them:

```javascript
// type first this:
cat /etc/apt/sources.list
// and then this:
ls -l /etc/apt/sources.list.d/

```

- output: lots of data about the ubuntu version i have

> ✋ **chatgpt**: It appears that your current sources **list** is primarily configured for Ubuntu 18.04 (Bionic Beaver) with some references to focal (Ubuntu 20.04) repositories. 🔴 **This mix might be causing issues with package availability, including python3-venv**.

<br>

### So i either change the UBUNTU version or I USE something that gives me the possibility to change the python version for each project

 <br>
 <br>

## 🧶 PYENV

#### 🟡 before installing it, check this video to see how you will be able to change the versions [min: 5:40 / Manage Multiple Python Versions with PyEnv](https://youtu.be/3my06DUnApM?si=0Mu3vQvbToF5hLUA&t=340)

<br>

**PYENV** is a great tool for managing multiple Python versions on your system, regardless of the system's default Python installation or available packages.

[How to Install and Run Multiple Python Versions on Ubuntu/Debian | pyenv & virtualenv Setup Tutorial](https://youtu.be/1Zgo8M9yUtM?si=lPx1WQTX8_hQsu8D)

## Here's a step-by-step guide to installing pyenv and setting it up to manage Python versions and virtual environments:

### 🍨 Installing pyenv on Ubuntu

#### Install Prerequisites:

1. 🔸 Before installing pyenv, make sure you have the necessary packages installed on your system: [Python Pyenv: how to install Pyenv and Python in just 2 clicks on Ubuntu | Pyenv tutorial | min 1:40](https://youtu.be/p2Ojd3M7iPk?si=P_rdT3MNcOf4FUZ3&t=100)

```javascript
// check this video: https://youtu.be/p2Ojd3M7iPk?si=P_rdT3MNcOf4FUZ3&t=100
sudo apt update
sudo apt install git curl wget make build-essential libssl-dev zlib1g-dev libbz2-dev \
                 libreadline-dev libsqlite3-dev llvm libncurses5-dev libncursesw5-dev \
                 xz-utils tk-dev libffi-dev liblzma-dev python-openssl

```

<br>

#### Install pyenv via GitHub:

2.  🔸 Clone the pyenv repository from GitHub into your home directory (~):

```javascript
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

```

<br>

#### Set Up Environment Variables:

3.  🔸 Add pyenv to your **shell's** environment variables by appending the following lines to your `~/.bashrc (or ~/.bash_profile, ~/.zshrc for zsh users`) file:

```javascript
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

```

<br>

4. 🔸 Apply these changes to your current shell session:

```javascript
source ~/.bashrc

```

<br>

#### Verify pyenv Installation:

5. 🔸 Verify that pyenv is properly installed by running:

```javascript
pyenv --version
//This command should display the pyenv version number, confirming a successful installation.


```

<br>
<br>

## 🟡 Installing Python Versions with pyenv

- Now that pyenv is installed, you can use it to install and manage different versions of Python. Here's how you can install Python 3.8.12 as an example:

#### 🟢 List Available Python Versions:

First, list all available Python versions that can be installed using pyenv:

```javascript
pyenv install --list

```

#### 🟢 Install a Specific Python Version:

- Choose a Python version from the list and install it with pyenv. For example, to install Python 3.8.12:

```javascript
pyenv install 3.8.12
//This command downloads and installs Python 3.8.12 into pyenv's version management directory.
```

### 🌈 Set Global Python Version:

Set Python 3.8.12 as your global default Python version for your user:

```javascript
pyenv global 3.8.12
// This command sets the global Python version to 3.8.12, which will be used in your shell sessions by default.
```

<br>
<br>

# 🔴 Managing Virtual Environments with pyenv-virtualenv

**pyenv** also integrates with ✋ **pyenv-virtualenv**, a plugin that allows you to create and manage virtual environments 👾 **based on pyenv's Python installations**.

### 1 🔸 Install pyenv-virtualenv:

- 🔸 Install pyenv-virtualenv using git:

```javascript
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv

```

### 2 🔸 Activate pyenv-virtualenv Plugin:

- Add **pyenv-virtualenv** initialization to your shell configuration file (`~/.bashrc, ~/.bash_profile, ~/.zshrc`):

```javascript
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

```

### 3 🔸 Apply changes to your current shell session:

```javascript
source ~/.bashrc

```

### 4 🔸Create and Use a Virtual Environment:

- Now, you can create a virtual environment using a specific Python version managed by pyenv:

```javascript
pyenv virtualenv 3.8.12 myenv // you can replace myenv for whatever you LIKE, but its better if ou stick to the convention of ENV on lowercase
// This command creates a virtual environment named myenv based on Python 3.8.12.


```

<br>

### 5 🔸Activate and Use the Virtual Environment:

- Activate the virtual environment myenv

```javascript
pyenv activate myenv

```

> Once activated, your shell prompt should indicate that you are now using the myenv virtual environment. Install packages and work within this isolated environment as needed.
