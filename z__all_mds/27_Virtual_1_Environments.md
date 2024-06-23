## 🟠 Virtual Environment

#### It's pretty normal to have multiple Python applications running on your computer. Sometimes, one app wants a specific version of a module, while another app wants a different version of the exact same module.

🔸 So how can you provide 2 VERSIONS of the same module?

- 🔴 Remember, when you use pip to install updates, it affects all Python programs on your computer. For example, if you update a module like requests using pip, every Python program that uses requests will now use the updated version.

<br>

### 🟡 Using VIRTUAL environments to prevent this

##### chatgpt

✋ One solution to manage different versions of Python modules for different applications is to use virtual environments. Here’s how it works:

<br>

#### generate the environment

1. check the project ou are on, in my case i will cd into the following folder: `cd LESSON_17_Virtual_Environment_and_pip`

2. Keep in mind that after the step 3 here below, you will have to **ACTIVATE** the environment.

3. Now type the command below:

#### 🍰 CREATE

```javascript
// venv: will help me  to create the 'virtual environment
// .venv: will create a folder inside of the project
py -m venv .venv //
✋ or :  python -m venv .venv
// once you type the above command, press ENTER, this will automatically generate a folder (check it at the left bar)
```

```python
LESSON_17_Virtual_Environment_and_pip
   ▶️.venv # ✋ this is how it should look like
```

<br>

## the content of the `.venv` folder

> within the .venv folder you will find the below folders:

- bin

- include

- lib

- lib64

- pyvenv.cfg

```python
# You can check what the folder contains with the command below, but check that you are in the correct directory (the project you are installing the venv)
ls -l .venv   # Linux/macOSs
```

<br>
<br>

#### 🟠 `pyvenv.cfg`

The **pyvenv.cfg** file is a configuration file automatically generated when you create a virtual environment using the `pyvenv` or `python -m venv` command in Python. It contains settings that define the behavior of the virtual environment.

```javascript
// within the pyvenv.cfg you will find this:
>home = /usr/bin
include-system-site-packages = false
version = 3.8.10
```

<br>

#### Description:

```javascript
// home = /usr/bin:

// This line specifies the location of the Python interpreter that the virtual environment is associated with. In this case, it indicates that the virtual environment is using the Python interpreter located at /usr/bin.

// ---------------
//
// include-system-site-packages = false:

// This setting determines whether the virtual environment includes access to the system-wide installed Python packages (site-packages). When set to false, which is the default behavior, the virtual environment will not inherit packages installed globally on your system. This ensures isolation and prevents conflicts with system-wide Python packages.

// ---------------
//
//  include-system-site-packages = false:

// This setting determines whether the virtual environment includes access to the system-wide installed Python packages (site-packages).

// 🔴 When set to false, which is the default behavior, the virtual environment will not inherit packages installed globally on your system. This ensures isolation and prevents conflicts with system-wide Python packages.
```

<br>

### 🟠 Purpose of `pyvenv.cfg`:

<br>

**Configuration:** `pyvenv.cfg` provides essential configuration details for the virtual environment, such as the Python interpreter path and version. These settings ensure that when you activate the virtual environment, it uses the correct Python interpreter and maintains isolation from the global Python environment.

**Isolation:** By specifying `include-system-site-packages = false`, the virtual environment **ensures** that <u>only packages installed within the virtual environment are accessible to Python scripts executed within that environment.</u> This isolation prevents conflicts and allows different applications to use different versions of packages without interference.

<br>
<br>

#### 🍰 ACTIVATE

- When i tried to **CREATE** the **env** folder by using this command `python -m venv .venv` , like you see in in the tutorial [6:25 | Python Virtual Environment and pip for Beginners](https://youtu.be/eDe-z2Qy9x4?si=lsQnQ4eoy07Caa1v&t=385), so to create the venv folder, **it works BUT ✋** it DOESN'T CREATE the **SCRIPTS** folder that also comes within the **`.venv` folder**, 🟥 this script folder is important because it comes with some **activation files** , the ones you will always need, check the example: [6:35 | Python Virtual Environment and pip for Beginners](https://youtu.be/eDe-z2Qy9x4?si=3Bg6wM1cXGlaqqh-&t=395)

<br>

#### In the beginning i thought the problem had something to do with this warning i was getting every time i try to install something using PIP:

```javascript
 WARNING: The script virtualenv is installed in '/home/myComputer/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

```

#### [READ MORE: z\_\_ENV_PATH_issue](../z__ENV_PATH_issue.md)

- 🟡 once your read that, continue with the below

<br>

## 🔴 POSSIBLE reasons

### After reading about the TOPIC, i found the following:

1. It appears that the `python3-venv` package is not available in your current package repositories. This can happen for a few reasons, such as repository **misconfiguration** or changes in **package availability**.

<br>
<br>

### 🟡 There are many was ou can solve this:

- Either by using PyEnv so to have the possibilities to have several python versions, or by using a library/tool such as VIRTUALENV

<br>

<br>

#### 🟢 PyENV

- PyEnv for multiple python versions (one option)

[ENV_ubuntu-version-issue, install PyEnv for multiple python versions](../z__ENV_ubuntu-version-issue.md)

 <br>

#### 🟢 VirtualENV

- Before installing anything related to the VIRTUALENV, check if you already have this: [z\_\_ENV_PATH_issue](../z__ENV_PATH_issue.md), if you have it, you can continue" but if not, just go the link and follow the steps. ✋ to install [VIRTUALENV click here](../z__ENV_VIRTUALENV%20.md)

<br>
<br>

---

<br>

## 🌈 Continue with the activation

- After installing the **virtualEnv** i can continue with the activation but before that, i will create the ENV folder using a different command [min: 3:23 | Entornos Virtuales con Python (Módulo virtualenv) ✅ | Curso Python 3 🐍 # 63](https://youtu.be/TNtrAvNNxTY?si=Ek5y67rtAx4DWwQP&t=203) , **as i am now using virtualenv** instead of the python env, it's different to what you can see in the tutorial i have been watching [min: 7:16 | Python Virtual Environment and pip for Beginners](https://youtu.be/eDe-z2Qy9x4?si=rLciMOjDfQO8l3sg&t=436)

<br>

#### creating the env

- creating the **env** with **virtualEnv**

- choose the project where you are going to install the env folder, in my case i will choose `/LESSON_16_OOP` , once you have cd into that project, type the following:

```javascript
virtualenv -p python3 env

// - -p python3: This specifies that you want to use Python 3 as the interpreter for creating the virtual environment.
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
