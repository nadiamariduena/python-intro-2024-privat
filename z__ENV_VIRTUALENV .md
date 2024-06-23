## 🟡 VIRTUALENV

<br>

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

It seems like there might be an issue with the environment variables or **PATH configuration** in your Visual Studio terminal, which is causing the **virtualenv** command not to be found.

<br>

### Here’s how you can troubleshoot and potentially resolve this issue:
