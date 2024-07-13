## 🟡 Vulnerabilities

<br>
<br>


### I received a vulnerability message while pushing data to my repository.

<br>

```javascript
// urllib3's Proxy-Authorization request header isn't stripped during cross-origin redirects Moderate
// #2 opened 3 days ago • Detected in urllib3 (pip) • LESSON_17_PYENV_venv_test/requirements.txt
```

<br>

- 🟠 I'm currently learning about virtual environments **(venv)** in Python, and this project isn't critical.

- I believe this message could be due to two possible reasons: either the Python version I used to create the virtual environment is 3.10 and has bugs, or I didn't install the "requests" module correctly using the latest version of pip

<br>


### 🟦 chatgpt

- It sounds like you've encountered a vulnerability message related to the **urllib3** library and its handling of the Proxy-Authorization request header during cross-origin redirects. This issue is categorized as "Moderate" severity.

<br>



### Vulnerability Details:

- The message indicates that there's an issue where the **Proxy-Authorization** header is not properly stripped during cross-origin redirects.

- This could potentially lead to security vulnerabilities if the authorization credentials are unintentionally leaked or misused.

<br>
<br>


### 🟩 Cause of the Issue:

- Python Version: While Python versions themselves might have bugs, vulnerabilities in libraries like **urllib3** are more specific to the library version rather than the Python version (3.10 in your case).

- It's more likely related to the library's implementation.

- **Dependency Management:** The issue might also arise if you haven't updated your dependencies properly.

- Sometimes, vulnerabilities are fixed in newer versions of libraries like urllib3, and updating your dependencies (such as requests) could help mitigate such issues.

```javascript
// when you delete the venv with the cache, remove the requirements.txt also, check the python version you have within the interpreter and open the terminal with the + , dont split the terminal
// ✋
certifi==2024.7.4
charset-normalizer==3.3.2
idna==3.7
python-dotenv==1.0.1
requests==2.32.3
urllib3==2.2.2
//
//

certifi==2024.7.4
charset-normalizer==3.3.2
idna==3.7
python-dotenv==0.21.1
requests==2.31.0

// 🤾
urllib3==2.0.7
```

### update

```javascript
pip install --upgrade urllib3

```

#### 🔴 once you have updated or deleted the venv and re generated the venv and re installed the "requests" where this (urllib3) comes from

- you will have to go to the link that appears after you commit to your repo (https://github.com/yourgithub/yourfolderwheretheproblemcomesfrom/security/dependabot), once on the url of the issues, delete the issue related to what you just solved (only if you think you solved it)