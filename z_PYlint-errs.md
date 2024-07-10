# 🟡 Pylint


<br>

- 🔴 red underline when importing **dotenv or requests** SOLVED []()

<br>

- pylint / eslint in js [Go to section](#pylint_eslint)


- READ [python versions to avoid](./z_PYENV_versions-python-toavoid.md)


- READ [which-python-version-pylint-should-evaluate-for](https://stackoverflow.com/questions/23052637/specify-which-python-version-pylint-should-evaluate-for)


- Watch [Mastering Python Code Quality with Pylint](https://youtu.be/RqdhVaX50mc?feature=shared)

<br>

<br>

### 🟣 install Pylint  [Go to section](#install_pylint)

<br>
<br>

### 🟠 Pylint is a static code analysis tool used primarily for checking Python code for errors, style issues, and potential bugs.




<br>


- 🟦 When Pylint reports that packages are not well installed in the correct environment, it typically means one of the following:

<br>

**Incorrect Environment Setup:**

- Pylint might be running in an environment where the Python interpreter or the virtual environment (if used) does not have the necessary packages installed. This can happen if Pylint is configured to run in a different environment than where your application runs.

<br>

**Pylint's Perspective:**

- Pylint analyzes code statically, meaning it inspects the source code without executing it. If it detects import errors or missing packages based on its configured Python interpreter or environment, it will flag them as potential issues.



>This does not necessarily mean the application will fail to run because Pylint's checks are based on its own configuration and not on the runtime environment where your application will execute.

<br>
<br>

### 💁‍♀️ To address this issue:


<br>

**Verify Environment:**

- Ensure that Pylint is running in the same environment (Python interpreter and virtual environment) where your application dependencies are installed. If using a virtual environment, activate it before running Pylint.


**Pylint Configuration:**

- Check Pylint's configuration (pylintrc file or command-line options) to ensure it points to the correct Python interpreter and environment where your packages are installed.

<br>


**Ignore or Suppress Warnings:**

- 🍊 If you are confident that your application will work correctly despite Pylint's warnings...

- you can configure Pylint to ignore certain import errors or suppress specific warnings using directives in your code or in Pylint's configuration.


By ensuring that Pylint runs in the correct environment and its configuration matches your application's setup, you can reduce false positive warnings about package installations.


<br>

🔴 **Remember**, Pylint's warnings are intended to help maintain code quality and catch potential issues early, but they should be interpreted in the context of your specific development environment and application requirements.

<br>
<br>

---

<br>
<br>

<a name="pylint_eslint"></a>

### 🟣 so Pylint is the equivalent in javascript to Eslint?

##### chatgpt:

Yes, that's correct! Pylint and ESLint serve similar purposes in their respective languages (Python and JavaScript):

**Static Code Analysis:** Both Pylint and ESLint analyze code without executing it (statically) to find errors, enforce coding standards, and identify potential bugs.

**Code Quality and Style Checking:** They both provide checks for code quality, including style consistency, best practices, and potential issues that could lead to runtime errors.

**Configurability:** Both tools are highly configurable, allowing developers to customize rules, ignore certain warnings, and tailor the checks to fit specific project requirements.



#### Integration with Editors and CI/CD Pipelines:

- They can be integrated into development workflows, such as running them in code editors (like VS Code) or as part of continuous integration and deployment pipelines.

<br>



🍊 While Pylint is specific to Python and ESLint is specific to JavaScript, they share the common goal of helping developers write cleaner, more maintainable code by catching potential issues early in the development process. Each tool has its own set of rules and conventions tailored to the respective language's syntax and best practices.


<br>
<br>

<br>
<br>

<a name="install_pylint"></a>

## 🟡 install Pylint

- check if you already have it in your ubuntu

- OPEN your ubuntu terminal

```javascript
pylint --version
```

- update the system before installing

```javascript
sudo apt update
```

<br>

- install it

```javascript
sudo apt install pylint
```

#### output

```javascript
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-astroid python3-dill python3-importlib-metadata python3-isort python3-logilab-common python3-mccabe python3-more-itertools
  python3-mypy-extensions python3-platformdirs python3-toml python3-tomlkit python3-zipp
Suggested packages:
  python3-objgraph
The following NEW packages will be installed:
  pylint python3-astroid python3-dill python3-importlib-metadata python3-isort python3-logilab-common python3-mccabe python3-more-itertools
  python3-mypy-extensions python3-platformdirs python3-toml python3-tomlkit python3-zipp
0 upgraded, 13 newly installed, 0 to remove and 4 not upgraded.
Need to get 1,098 kB of archives.
After this operation, 8,349 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://archive.ubuntu.com/ubuntu noble/universe amd64 python3-astroid all 3.0.2-2 [174 kB]
Get:2 http://archive.ubuntu.com/ubuntu noble/universe amd64 python3-toml all 0.10.2-1 [16.5 kB]
Get:3 http://archive.ubuntu.com/ubuntu noble/universe amd64 python3-isort all 5.6.4-1 [63.1 kB]
Get:4 http://archive.ubuntu.com/ubuntu noble/main amd64 python3-more-itertools all 10.2.0-1 [52.9 kB]
Get:5 http://archive.ubuntu.com/ubuntu noble/main amd64 python3-zipp all 1.0.0-6 [6,090 B]
Get:6 http://archive.ubuntu.com/ubuntu noble/main amd64 python3-importlib-metadata all 4.12.0-1 [17.8 kB]
Get:7 http://archive.ubuntu.com/ubuntu noble/universe amd64 python3-mypy-extensions all 1.0.0-1 [6,148 B]
Get:8 http://archive.ubuntu.com/ubuntu noble/universe amd64 python3-logilab-common all 1.9.8-2 [280 kB]
Get:9 http://archive.ubuntu.com/ubuntu noble/universe amd64 python3-dill all 0.3.8-1 [83.0 kB]
Get:10 http://archive.ubuntu.com/ubuntu noble/universe amd64 python3-mccabe all 0.7.0-1 [8,678 B]
Get:11 http://archive.ubuntu.com/ubuntu noble/main amd64 python3-platformdirs all 4.2.0-1 [16.1 kB]
Get:12 http://archive.ubuntu.com/ubuntu noble/universe amd64 python3-tomlkit all 0.12.4-1 [37.5 kB]
Get:13 http://archive.ubuntu.com/ubuntu noble/universe amd64 pylint all 3.0.3-2 [337 kB]
Fetched 1,098 kB in 1s (911 kB/s)
//
// ..... more
```

<br>

### check the Version

```javascript
pylint --version
```

```javascript
pylint 3.0.3
astroid 3.0.2
// this python version below is the main python that i installed, when installing UBUNTU through the usb key, this one has nothing to do with the python versions i installed with PYENV
Python 3.12.3 (main, Apr 10 2024, 05:33:47) [GCC 13.2.0]
```