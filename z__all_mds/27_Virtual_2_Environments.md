
## 🔴 ACTIVATION issue

#### 🌈 REASON: the below happened because i had installed python on the python that already comes with some version of ubuntu, so at the end they clashed.

<br>

#### explanation:

- When i tried to **CREATE** the **env** folder by using this command `python -m venv .venv` , like you see in in the tutorial [6:25 | Python Virtual Environment and pip for Beginners](https://youtu.be/eDe-z2Qy9x4?si=lsQnQ4eoy07Caa1v&t=385), so to create the venv folder, **it works BUT ✋** it DOESN'T CREATE the **SCRIPTS** folder that also comes within the **`.venv` folder:**

```javascript
//  If it fails, you will only have the below, but inside the bin you will only have some binary python files, not the activation & pip files, such as: pthon and python3

- bin

- include

- lib

- lib64

- pyvenv.cfg
```



🟥 this `/SCRIPT` **folder** is important because it comes with some **activation files** , the ones you will always need to generate the **virtual environment** `(env)`.

- check the example: [6:35 | Python Virtual Environment and pip for Beginners](https://youtu.be/eDe-z2Qy9x4?si=3Bg6wM1cXGlaqqh-&t=395)

<br>

<br>
<br>

## 🟡 PATH issue

#### Path issue i though it was connected with the environment not generating the activation files

<br>

- In the beginning i thought the problem had something to do with this **warning** i was getting every time i try to install something using **PIP**:

```javascript
 WARNING: The script virtualenv is installed in '/home/myComputer/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

```

#### [READ MORE: z\_\_ENV_PATH_issue](../z__ENV_PATH_issue.md)

- 🟡 once your read that, continue with the below

<br>
<br>

<br>



## 🔴 POSSIBLE reasons


### After reading about the TOPIC, i found the following:

1. It appears that the `python3-venv` package is not available in your current package repositories. This can happen for a few reasons, such as repository **misconfiguration** or changes in **package availability**.

<br>
<br>

---

<br>

## 🟡 Other Options:


####  🟢 Other options you can use instead of the VIRTUAL environment offered by PYTHON

<br>

- Either by using **PyEnv** so to have the possibilities to have several python versions, or by using a **library/tool** such as **VIRTUALENV**

<br>
<br>


### 🟢 PyENV

- PyEnv for multiple python versions (one option)

[ENV_ubuntu-version-issue, install PyEnv for multiple python versions](../z__ENV_ubuntu-version-issue.md)

 <br>

### 🟢 VirtualENV

- Before installing anything related to the VIRTUALENV, check if you already have this: [z\_\_ENV_PATH_issue](../z__ENV_PATH_issue.md), if you have it, you can continue" but if not, just go the link and follow the steps. ✋ to install [VIRTUALENV click here](../z__ENV_VIRTUALENV%20.md)

<br>
<br>

---

<br>


## 🌈 GENERATING VIRTUAL env with virtualenv