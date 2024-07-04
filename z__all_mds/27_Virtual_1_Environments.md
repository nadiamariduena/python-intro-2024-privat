


# 🟡 Virtual Environment


- GENERATE the environment [Go to section](#generate_the_environments)

- ACTIVATE the environment [Go to section](#activate_the_environments)

<br>


<br>

<br>
<br>


## 🟢 Why Multiple environments ?

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