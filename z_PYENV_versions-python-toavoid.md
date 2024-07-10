## 🟡 Avoid Latest Releases

<br>
<br>

### read this [the-art-of-choosing-stable-python-version](https://medium.com/@rishabhojha11/the-art-of-choosing-stable-python-version-70a7c755467b)

> 🔴 If you are trying to develop a python web-based application using Django. It is best to identify which Django version will suit your requirements before rushing to identify the python version. This is because 👾 **some Django versions are only available for latest python releases**.

- For instance, **Django 4 requires python version 3.8+.** Older python releases are not supported. So, if you want to use Django 4, it does not make sense to do analysis of the python versions before 3.8.

## 🟠 Conclusion
There is no fixed metrics that can be used to identify an appropriate python version for you. The “correct” python version might be different for different use case.

<br>
<br>
<br>

#### It's advisable to steer clear of the most recent Python releases for several reasons:


  🔸 Firstly, while most **new versions** of Python are generally stable, there's always a possibility of **undiscovered bugs** that could pose challenges as your application nears deployment.

 🔸 Secondly, not all Python packages may have caught up to the latest releases, potentially causing **compatibility issues**.


<br>

<br>

## 🔴 Avoid Very Old Releases


🔸 Similarly, **it's wise to avoid very old Python** releases. For instance, unless you have compelling reasons to use Python 2.7 in 2022, it's not recommended.

🔸 Likewise, `Python 3.7`, slated to reach its **end-of-life in 2023**, isn't ideal for long-term projects requiring ongoing maintenance. By the time development concludes, transitioning to a newer Python version will likely be necessary.
import-error / E0401


<br>
<br>

---

<br>



### 🟣 versions i have installed

- i will continue to test to see the different type of issues

```javascript
// 3.7.14 (with this version the red underline is gone)
  system
* 3.7.14 (set by /home/mycomputer/.pyenv/version)
  3.8.10 //(red underline)
  3.8.18 //(i had several issues with this one, missing packages, red underline)
  3.10.8 // (red underline)

```

<br>
<br>

---


<br>
<br>


#### 🟡 Determining the "best" Python version depends on several factors, including your specific project requirements, compatibility with libraries and frameworks you intend to use, and whether you prioritize stability or newer features.

<br>
<br>

##### chatgpt:

### 🟠As of my last update in January 2022, here are some considerations for Python versions:

<br>

### 🔸 PYTHON 3.9

Python **3.9.x:** `Python 3.9` is a stable release with a good balance of new features and stability.

- ✅ It includes performance improvements and new syntax **features like the merge operator** `(|)` for dictionaries. Many libraries and frameworks support Python 3.9 well.


<br>

### 🔸 Python 3.8

Python **3.8.x:** `Python 3.8` is another stable release with Long Term Support (LTS) until October 2024.

- ✅ It's widely used and generally considered stable and reliable. It **introduced the assignment expressions** `(walrus operator :=)` and optimizations in various areas.

<br>


### 🔸 Python 3.7

Python **3.7.x:** `Python 3.7` is also a solid choice with many libraries and frameworks supporting it.

- ✅ It **introduced data classes and various performance improvements**. It's still maintained, with security fixes being provided until mid-2023.

<br>

### 🔸 Python 3.10

Python **3.10.x:** `Python 3.10` is the latest stable release as of now (July 2024).

- ✅ It **includes new features like pattern matching and improved error messages**.

- - 👎 However, being relatively new, some libraries and frameworks may not fully support it yet, so compatibility should be verified.


<br>
<br>

### 🔸 Python 3.6

Python **3.6.x:** `Python 3.6` is older but still supported with security updates until December 2021.

-  It's generally stable, but newer Python versions have added significant improvements and features since then.

### is Python 3.6 compatible with Django?

##### chatgpt:

- - Yes, Python 3.6 is compatible with Django. Django officially supports a range of Python versions, and Python 3.6 is within that supported range for most versions of Django.


<br>

### 🟣 What Python version can I use with Django?

https://docs.djangoproject.com/en/5.0/faq/install/

```javascript
3.2	3.6, 3.7, 3.8, 3.9, 3.10 (added in 3.2.9)
4.0	3.8, 3.9, 3.10
4.1	3.8, 3.9, 3.10, 3.11 (added in 4.1.3)
4.2	3.8, 3.9, 3.10, 3.11, 3.12 (added in 4.2.8)
5.0	3.10, 3.11, 3.12
```

#### 🔴 However, it's important to note that Python 3.6 reached its end-of-life status in December 2021, which means it no longer receives official support or updates from the Python core development team.

- - While Django may still officially support Python 3.6 in its older releases, it's advisable to consider upgrading to a supported Python version (like Python 3.7 or newer) for security and compatibility with other libraries and tools in the Python ecosystem.