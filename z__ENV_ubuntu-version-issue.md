## 🟡 After reading about the TOPIC, i found the following:

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

```
