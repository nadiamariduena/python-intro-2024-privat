


# 🟡 Virtual Environment


- GENERATE the environment [Go to section](#generate_the_environments)

- ACTIVATE the environment [Go to section](#activate_the_environments)

<br>


<br>

<br>
<br>


## 🟢 Why Multiple environments ?

<br>

https://medium.com/@adocquin/mastering-python-virtual-environments-with-pyenv-and-pyenv-virtualenv-c4e017c0b173

<br>


### 🟠 It's pretty normal to have multiple Python applications running on your computer.

> ✋Sometimes, one app wants a specific version of a module, while another app wants a different version of the exact same module.



### 🟠 How can you provide 2 VERSIONS of the same module?

<br>

 🏁 Remember, when you use **pip** to install updates, it affects all Python programs on your computer.

> 🔴 **For example**, if you update a module like requests using pip, every Python program that uses requests will now use the updated version.

<br>
 <br>

 ---


 <br>
 <br>

### 🟠 Using VIRTUAL environments to to manage different versions of Python modules for different applications

##### chatgpt:

- One solution to manage different versions of Python modules for different applications, is to use virtual environments. Here’s how it works:

<br>
<br>


<a name="generate_the_environments"></a>

# 🌈 Generate 🌈

### 🍰 to Generate the environment, follow the below steps:


<br>

🔸 1. check the project you are on, in my case i will **cd** into the following folder: `cd LESSON_17_Virtual_Environment_and_pip`

🔸 2. Keep in mind that after the **step 3** here below, you will have to **ACTIVATE** the environment.

🔸 3. Now type the commands `python3 -m .env` (depending if you are using py instead of python3 or python), also the `.env` is my choice, you can use it exactly how you see in on the tutorial [6:20 | Python Virtual Environment and pip for Beginners
](https://youtu.be/eDe-z2Qy9x4?si=WxJwgqwVc-bEeOAD&t=380):

<br>
<br>

## 🟪 CREATE 🌟




```javascript
// venv: will help me  to create the 'virtual environment
// .venv: will create a folder inside of the project
py -m venv .venv //
//✋ or :
python -m venv .venv
//✋ or :
python3 -m venv .myvenv //()
// once you type the above command, press ENTER, this will automatically generate a folder (check it at the left bar)
```

### 💅 `.venv` is optional. you can type: `.env` , `.myvenv` etc etc...

#### output:

```python
LESSON_17_Virtual_Environment_and_pip
   ▶️.venv # ✋ this is the created folfer after you typed the above commands
```

<br>
<br>


## 🟧 the content of the `.venv`

- 🟢 If it Works: within the **.venv** (or whatever name you put) folder you will find the below folders:


<a name="result_of_the_generated_environment"></a>


```javascript
project_folder/
├── env/
  └── bin/
     └── activate
     └── activate.csh
     └── activate.fish
     └── activate.ps1
     └── pip
     └── pip3
     └── pip3.12
     └── python
     └── python3
     └── python3.12

  └── include/
  └── lib/
  └── lib64/
  └── pyvenv.cfg

```

<br>

### 🟧 Inspecting the `.venv` (or whatever name you used, in my case, i named it `.env`) content

```python
# You can check what the folder contains with the command below, but check that you are in the correct directory (the project you are installing the venv)
ls -l .venv   # Linux/macOSs
```
#### output

```javascript
total 16
drwxrwxr-x 2 mycomputer mycomputer 4096 Jul  3 02:45 bin
drwxrwxr-x 3 mycomputer mycomputer 4096 Jul  3 02:45 include
drwxrwxr-x 3 mycomputer mycomputer 4096 Jul  3 02:45 lib
lrwxrwxrwx 1 mycomputer mycomputer    3 Jul  3 02:45 lib64 -> lib
-rw-rw-r-- 1 mycomputer mycomputer  233 Jul  3 02:45 pyvenv.cfg
//
// use the below command to return back on the tree
// cd ../
```

### cd `.env` , then type `ls`

```javascript
// 1 cd .env
LESSON_16_OOP$ cd .env
// output
LESSON_16_OOP/.env$
// 2 ls to check the .env content
LESSON_16_OOP/.env$ ls
// output
bin  include  lib  lib64  pyvenv.cfg
// 3 cd .env
LESSON_16_OOP/.env$ cd bin
// output
LESSON_16_OOP/.env/bin$
// 4 ls to check the .bin content
LESSON_16_OOP/.env/bin$ ls
// output
activate      activate.fish  pip   pip3.12  python3
activate.csh  Activate.ps1   pip3  python   python3.12
```



<br>


### 🔴 If it fails, you will only have the below, but inside the bin you will only have some binary python files, not the activation & pip files

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


---


<br>
<br>

<a name="activate_the_environments"></a>

# 🌈 ACTIVATION

>Once you activate the environment, you will be able to install specific modules, such as flask and more, **check this:** [27_Virtual_3_Environments_other-packages](./27_Virtual_3_Environments_other-packages.md)

<br>

🔸 **1.**  After you generated the environment   [Go to section](#result_of_the_generated_environment)

🔸 **2.** Activate the environment


```javascript
source .env/bin/activate


```
#### output

```javascript
// ✋ here you can notice the the (env) is part present
(.env) mycomputer@mycomputer:~/Documents/0_PYTHON-all/LESSON_16_OOP$
```

<br>
<br>

## 🟣 DEACTIVATION

- type `deactivate`

```javascript
// ✋  while activated you can see the (.env) present
(.env) mycomputer@mycomputer:~/Documents/0_PYTHON-all/LESSON_16_OOP$ deactivate
```
#### output

```javascript
// ✋  once you have typed deactivated and press enter, you will notice that the (.env) is no longer present
  mycomputer@mycomputer:~/Documents/0_PYTHON-all/LESSON_16_OOP$ deactivate
```

#### remove cache

- if for some reason you want to remove the **.env or .venv**

```javascript
rm -rf .venv
```


<br>


### 🍭 Check the packages you have in your project While you are in the ACTIVATION mode

```javascript
//(.env) mycomputer@mycomputer:~/Documents/0_PYTHON-all/LESSON_16_OOP$
python3 -m pip list
```

#### output

```javascript
Package Version
------- -------
pip     24.0
```

### Check the packages you have once you are no longer in the Activation mode


```javascript
// mycomputer@mycomputer:~/Documents/0_PYTHON-all/LESSON_16_OOP$
python3 -m pip list
```

```javascript
Package               Version
--------------------- --------------
attrs                 23.2.0
Babel                 2.10.3
bcc                   0.29.1
blinker               1.7.0
Brlapi                0.8.5
Brotli                1.1.0
certifi               2023.11.17
chardet               5.2.0
click                 8.1.6
cloud-init            24.1.3
colorama              0.4.6
command-not-found     0.3
configobj             5.0.8
cryptography          41.0.7
cupshelpers           1.0
dbus-python           1.3.2
defer                 1.0.6
distro                1.9.0
distro-info           1.7+build1
gyp                   0.1
httplib2              0.20.4
idna                  3.6
Jinja2                3.1.2
jsonpatch             1.32
jsonpointer           2.0
jsonschema            4.10.3
language-selector     0.1
launchpadlib          1.11.0
lazr.restfulclient    0.14.6
lazr.uri              1.0.6
louis                 3.29.0
markdown-it-py        3.0.0
MarkupSafe            2.1.5
mdurl                 0.1.2
mutagen               1.46.0
netaddr               0.8.0
netifaces             0.11.0
oauthlib              3.2.2
olefile               0.46
pexpect               4.9.0
pillow                10.2.0
pip                   24.0
ptyprocess            0.7.0
pycairo               1.25.1
pycryptodomex         3.20.0
pycups                2.0.1
Pygments              2.17.2
PyGObject             3.48.2
PyJWT                 2.7.0
pyparsing             3.1.1
pyrsistent            0.20.0
pyserial              3.5
python-apt            2.7.7+ubuntu1
python-dateutil       2.8.2
python-debian         0.1.49+ubuntu2
pytz                  2024.1
pyxdg                 0.28
PyYAML                6.0.1
requests              2.31.0
rich                  13.7.1
setuptools            68.1.2
six                   1.16.0
systemd-python        235
typing_extensions     4.10.0
ubuntu-drivers-common 0.0.0
ubuntu-pro-client     8001
ufw                   0.36.2
unattended-upgrades   0.1
urllib3               2.0.7
wadllib               1.3.6
websockets            10.4
wheel                 0.42.0
xdg                   5
xkit                  0.0.0
yt-dlp                2024.4.9

```

### 🟠 if you dont have the result, try installing the `requests` while it s not ✋ activated

```javascript

python3 -m pip install requests
```

<br>

### 🟠 Check if you have the package


```javascript
pip show requests
```
<br>
<br>


---


<br>
<br>
<br>

## 🔴 ACTIVATION issue

#### ✋ the below happened because i had installed python on the python that already comes with some version of ubuntu

- READ MORE: [27_Virtual_2_Environments](./27_Virtual_2_Environments.md)

<br>
<br>
<br>
<br>

---

<br>

## 🟠 Installing other packets

- Now that I have the env setup, i can install other stuff but **ONLY** in this env (environment) **EITHER** with the VENV or the VIRTUAL ENV (you can install it globally but its better to have a different version of the packages for each  project, but it will depends on the project )

<br>


- READ MORE:[27_Virtual_3_Environments_other-packages](./27_Virtual_3_Environments_other-packages.md)

<br>
<br>