## 🟡 VIRTUALENV

<br>

- **virtualenv** is a third-party tool that allows more flexibility in specifying Python versions and has different default behaviors compared to `python -m venv`.

- The `bin/` directory within `env/` **includes** ✋ activation scripts (activate, activate.bat for Windows) and other necessary files for managing the virtual environment.

<br>
<br>

#### 🟧 Key Differences:

**Tool Used:** `python -m venv` **is part** of Python's standard library (venv module), **while** <u>virtualenv</u> is a third-party tool.

**Activation Scripts:** <u>virtualenv</u> typically provides more comprehensive activation scripts (activate, activate.bat) within the `bin/` directory, making it easier to activate the virtual environment.

**Python Version:** virtualenv ✋ allows specifying the Python interpreter version explicitly (-p python3), whereas python -m venv uses the default Python interpreter in your system's PATH.

<br>
<br>

#### installation & common issues

```javascript

```
