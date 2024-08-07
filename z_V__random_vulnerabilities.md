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


<br>
<br>

---


<br>
<br>

## 🟣 REQUESTS

### 🔴 Session object does not verify requests after making first request


<br>

## 🌈 chatgpt Solution

- It seems like the error message you're encountering when pushing your repository is related to a security warning about using the requests library with verify=False. This warning is indicating that SSL certificate verification is disabled for requests made using verify=False, which can pose security risks, especially in production environments.



```javascript
Requests Session object does not verify requests after making first
request with verify=False Moderate
//
#1 opened 3 days ago • Detected in requests (pip) • LESSON_17_PYENV_venv_test/requirements.txt
```

<br>

### 🟩 Understanding the Issue

<br>

When you use `verify=False` in your requests library calls, SSL certificate verification is disabled.

This means that the **HTTPS connections made by requests will not verify the authenticity of the server's SSL certificate**.

> 🔴 This can lead to potential security vulnerabilities, such as man-in-the-middle attacks where an attacker could intercept or manipulate the communication between your application and the server.


### Solution

To address this issue, you should:

Avoid verify=False: Remove or avoid using **verify=False** in your requests calls, especially in scenarios where security is a concern.

**Proper SSL Certificate Verification:** Ensure that SSL certificate verification (verify=True by default) is enabled for all HTTPS requests made by your application.

**Example Code Update**

Here’s how you can modify your get_current_weather function to ensure proper SSL certificate verification:
<br>


```javascript
import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_current_weather():
    print("\n*** Get Current Weather Conditions ***\n")

    city = input("\nPlease enter a city name:\n")

    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY is not set in the environment variables.")
        return

    request_url = f'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'appid': api_key,
        'q': city,
        'units': 'imperial'
    }

    response = requests.get(request_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        print(f"Weather in {city}: {weather_data['weather'][0]['description']}, Temperature: {weather_data['main']['temp']}°F")
    else:
        print(f"Error fetching weather data: {response.status_code} - {response.text}")

get_current_weather()


```

<br>


# 🌈 github solution


When making requests through a Requests Session, if the first request is made with verify=False to disable cert verification, all subsequent requests to the same origin will continue to ignore cert verification regardless of changes to the value of verify. This behavior will continue for the lifecycle of the connection in the connection pool.

https://github.com/psf/requests/security/advisories/GHSA-9wx4-h78v-vm56



### Remediation
Any of these options can be used to remediate the current issue, we highly recommend upgrading as the preferred mitigation.

**Upgrade to** `requests>=2.32.0.`

**For** `requests<2.32.0`, **avoid** setting `verify=False` for the first request to a host while using a Requests Session.


**For** `requests<2.32.0`, call **close()*** on Session objects to clear existing connections if verify=False is used.

```javascript
// ✋ what i had

requests==2.32.3

// ---------------
// after i removed the venv and re installed all the stuff related to venv, i installed this version below by using this command: pip install requests, keep in  mind that its going to install the version related to the python version you have in your interpreter

requests==2.31.0
```


<br>

#### 🟡 After I removed the `.venv` and re installed all the stuff related to venv, I installed this version below by using this command: `pip install requests`


```javascript

requests==2.31.0

```

🤔 But I wasn't sure if it was going to install the **requests version** related to the **python version** I had in my interpreter at the moment of installing the **requests**, which was the `python 3.7.14 `

#### 🟦 chatgpt


The version of the requests module you installed (`requests==2.31.0`) is not directly tied to the Python version (`3.7.14`) you're using in Visual Studio Code.

- In Python projects, including those using virtual environments (venv), you can typically install the latest compatible version of a package unless you specify a version explicitly.

> 🟧 In your case, pip install requests without specifying a version fetched **requests==2.31.0**, which was the latest available version at the time you installed it.

<br>


### To clarify:

`requests==2.31.0` is the version of the requests module that was the latest available version when you ran pip install requests.


It does not specifically correlate with Python version `3.7.14.` Instead, it's the most recent stable version of the requests module that was available from the Python Package Index (PyPI) at that time.

<br>

🔸 If you want to verify the latest version of requests available currently, you can check the **PyPI** website or use pip with the **--upgrade** flag (`pip install --upgrade requests`) to get the latest version compatible with your Python environment.