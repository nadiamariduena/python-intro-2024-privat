# 🟡 VIRTUALENV

<br>

- Before installing anything related to the VIRTUALENV, check if you already have this: [z\_\_ENV_PATH_issue](./z__ENV_PATH_issue.md), if you have it, you can continue, but if not, just go the link and follow the steps.

<br>
<br>

## 🟠 VirtualEnv

- **virtualenv** is a third-party tool that allows more flexibility in specifying Python versions and has different default behaviors compared to `python -m venv`.

- The `bin/` directory within `env/` **includes** ✋ activation scripts (activate, activate.bat for Windows) and other necessary files for managing the virtual environment.

<br>
<br>

### 🟣 Question: what are the differences between python -m venv & virtualenv?

<br>

##### chatgpt: 🟧 Key Differences:

<br>

`python -m venv` **is part** of Python's standard library (venv module), **while** <u>virtualenv</u> is a third-party tool.

**Activation Scripts:** <u>virtualenv</u> typically provides more comprehensive activation scripts (activate, activate.bat) within the `bin/` directory, making it easier to activate the virtual environment.

**Python Version:** virtualenv ✋ allows specifying the Python interpreter version explicitly (-p python3), whereas python -m venv uses the default Python interpreter in your system's PATH.

<br>

### 🟢 Conclusion:

Preferred Tool: If you need more control over Python versions or desire a more consistent activation experience across different platforms, virtualenv with explicit Python version (-p) is often preferred.

> Standard Library vs. Third-Party: Both python -m venv and virtualenv are widely used for creating virtual environments. Your choice may depend on specific project requirements or personal preference.

<br>
<br>

## 🟡 installation & common issues

<br>

#### Works on ubuntu

- **vistualenv** works on the ubuntu terminal.

- **ubuntu terminal:** when i type the `~$ virtualenv --version` command, i get this:

```javascript
// output
virtualenv 20.26.3 from /home/mycomputer/.local/lib/python3.8/site-packages/virtualenv/__init__.py

```

<br>

#### Don't work on VS

- BUT when i try the same command `~$ virtualenv --version` in my **visual studio** , on that specific project `LESSON_17_Virtual_Environment_and_pip`, i get this:

```javascript
virtualenv: command not found
```

<br>
<br>

### 🟣 Question: why this command vistualenv, work on the global but not on a local project in VS ?

#### ✅ chatgpt:

It seems like there might be an issue with the environment
variables or **PATH configuration** in your Visual Studio terminal, which is causing the **virtualenv** command not to be found.

<br>

### Here’s how you can troubleshoot and potentially resolve this issue:

- First check if you have any output after you type this `echo $PATH` in your ubuntu terminal:

```javascript
// type this:
echo $PATH
// OUTPUT
/usr/local/bin:/usr/bin:/bin:/home/mycomputer/.local/bin:/snap/bin
```

#### ✅ chatgpt:

- Based on the output of echo $PATH, it appears that /home/dci-st119/.local/bin is already included in your PATH variable. This is where virtualenv is installed according to your previous messages.

<br>

#### 🔴 But if you dont get the above output

[ FOLLOW THIS STEPS](./z__ENV_PATH_issue.md)

#### after the above steps

<br>

1. 🔸 Verify Visual Studio Terminal Shell

- Check which shell Visual Studio's integrated terminal is using and ensure it matches your expectations for running virtualenv commands.

```javascript
// type this in your VS terminal
echo $SHELL
//
// ✋ Output Interpretation:
// This command will display the shell currently active in your terminal session.
output:
/bin/bash, /usr/bin/zsh, /usr/bin/powershell, etc.
```

<br>

2. 🔸 Restart Visual Studio

- Restart Visual Studio to clear any temporary configuration issues that might be affecting virtualenv recognition.

<br>

3. 🔸 Directly Invoke virtualenv

- Attempt to directly execute **virtualenv** using its absolute path to confirm it's executable.

Command: `/home/mycomputer/.local/bin/virtualenv --version`

```javascript
// should look like this:
LESSON_17_Virtual_Environment_and_pip$ /home/mycomputer/.local/bin/virtualenv --version
//
// Output Interpretation:
// If virtualenv is found and executable, it will output its version number.

virtualenv 20.26.3 from /home/mycomputer/.local/lib/python3.8/site-packages/virtualenv/__init__.py
```

<br>

4. 🔸 Check Visual Studio Terminal Settings

- (OPTIONAL) Review Visual Studio's terminal settings to ensure it has the correct permissions and environment settings to execute commands from `/home/dci-st119/.local/bin.`

<br>

5. 🔸 Update Visual Studio Terminal **PATH**

🔴If Visual Studio's terminal does not recognize virtualenv, manually update its PATH setting.

##### type this on VS terminal of your project

- ✋ Command (temporary update):

```javascript
export PATH=$PATH:/home/mycomputer/.local/bin
```

<br>

6. 🔸 option

##### Command (permanent update in .bashrc for Bash):

```javascript
//1
echo 'export PATH=$PATH:/home/mycomputer/.local/bin' >> ~/.bashrc

//2
source ~/.bashrc
//
//This command uses source to execute (or "source") the commands from the .bashrc file in the current shell session. By doing so, it updates the PATH environment variable immediately in your current terminal session without the need to start a new shell.

//
// So, you would typically run these two commands consecutively in your terminal. The first command updates .bashrc to include /home/mycomputer/.local/bin in your PATH, and the second command refreshes your current shell session to apply this change.
```

<br>

7.  🔸 now check it:

TYPE: `virtualenv --version`

```javascript

OUTPUT
virtualenv 20.26.3 from /home/mycomputer/.local/lib/python3.8/site-packages/virtualenv/__init__.py
```

<br>
<br>

## 🌈 Continue with the activation

<br>

#### 🍭 creating the env

- creating the **env** with **virtualEnv**

- choose the project where you are going to install the env folder, in my case i will choose `/LESSON_16_OOP` , once you have cd into that project, type the following:

```javascript
virtualenv -p python3 env

// -  -p python3: This specifies that you want to use Python 3 as the interpreter for creating the virtual environment.
//
// - If you omit the -p option, virtualenv will use the default Python interpreter that is available on your system when creating the virtual environment.
//

```

#### output

```javascript
created virtual environment CPython3.8.10.final.0-64 in 307ms
  creator CPython3Posix(dest=/home/mycomputer/Documents/ALL_SITE_3D_STUFF/3D-UNITY-BLENDER-REACTVR-ALL/0_PYTHON-all/PYTHON-PRIVAT/python-intro-2024-privat/LESSON_16_OOP/env, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/mycomputer/.local/share/virtualenv)
    added seed packages: pip==24.1, setuptools==70.1.0, wheel==0.43.0
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
```

<br>

## 🍭 Once the `ENV` has been created, you will see the following:

- 📌 env (folder)
  - bin (folder, it includes the **activation files** and other stuff)
  - lib (folder)
  - gitignore
  - pyvenv.cfg

## 🍭 Activate

- type the following command (you have to be on your project root)

```javascript
source env/bin/activate
//
// like so:
LESSON_16_OOP$ source env/bin/activate
```

#### output

```javascript
// the env is there, it means it works
/LESSON_16_OOP$ source env/bin/activate
(env) dci-st119@mycomputer:
```

#### Now tht i am inside the virtual environment like you can see in the below code, you can check the packages, type this command:

```javascript
pip list
```

#### output

```javascript
Package    Version
---------- -------
pip        24.1
setuptools 70.1.0
wheel      0.43.0

```

#### like so:

```javascript
/LESSON_16_OOP$ pip list
Package    Version
---------- -------
pip        24.1
setuptools 70.1.0
wheel      0.43.0
(env) dci-st119@mycomputer:~/
```

<br>

---

<br>

### 🟠 Installing other packets

- Now that I have the env setup, i can install stuff but **ONLY** in this env (environment)

```javascript
pip install flask
```

### What is flask?
