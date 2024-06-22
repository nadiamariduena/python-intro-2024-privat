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

1. check the project ou are on, in m case i will `cd LESSON_17_Virtual_Environment_and_pip`

2. Now type the command below:

```javascript
// venv: will help me  to create the 'virtual environment
// .venv: will create a folder inside of the project
py -m venv .venv // ✋ or:  python -m venv .venv
// once you type the above command, press ENTER, this will automatically generate a folder (check it at the left bar)
```

```python
LESSON_17_Virtual_Environment_and_pip
   ▶️.venv # ✋ this is how it should look like
```

<br>

#### the content of the `.venv` folder

> within the .venv folder you will find the below folders:

- bin

- include

- lib

- lib64

- pyvenv.cfg

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
