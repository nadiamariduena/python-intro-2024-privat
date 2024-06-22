## 🔴 PATH / ENV

- When i tried to **CREATE** the **env** folder by using this command `python -m venv .venv` , like you see in in the tutorial [6:25 | Python Virtual Environment and pip for Beginners](https://youtu.be/eDe-z2Qy9x4?si=lsQnQ4eoy07Caa1v&t=385), so to create the venv folder, **it works BUT ✋** it DOESN'T CREATE the **SCRIPTS** folder that also comes within the **.venv folder**, 🟥 this script folder is important because it comes with some **activation files**

#### In the beginning i thought the problem had something to do with this warning i was getting every time i try to install something using PIP:

```javascript
 WARNING: The script virtualenv is installed in '/home/myComputer/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

```

### So i decided to add what was missing

#### 1. 🔶 Open your shell configuration file `(~/.bashrc for Bash or ~/.zshrc for Zsh)` in a text editor <u>ubuntu terminal etc...</u>. For example:

```javascript

nano ~/.bashrc

```

#### 2. 🔶 Add the following line at the end of the file:

```javascript
export PATH="$HOME/.local/bin:$PATH"
```

#### 3. Save and close the file ✋ (in Nano, press `Ctrl + X, then Y, then Enter`).

#### 4. After saving the file, apply the changes by running:

```javascript
source ~/.bashrc
```
