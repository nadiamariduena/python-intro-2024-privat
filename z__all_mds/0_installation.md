## 🟡 INSTALLATION


<br>

### ⚠️  before starting with the installation of the virtual environment in your project, check a couple of things:

<br>
<br>


### 🟠 Check if you already have PYTHON

#### 🔸 1. Before start, check if PYTHON is already installed in your machine

```javascript
python --version
// OR
python3 --version
//Remember, it's good practice to use Python 3 (python3) for most purposes as Python 2 is no longer supported.
```

#### 🔸 2. To check your Ubuntu version, you can use:

```javascript
lsb_release -a
```
<br>

<br>

### 🔴  Consequences of installing PYTHON

  If you install another version of Python alongside the one already on your machine, it can lead to significant issues. In some cases, resolving these issues may require a complete system wipe and reinstallation of Ubuntu. I once encountered a dpkg error and, out of curiosity, tried reinstalling Ubuntu to see if it would fix the problem. After the reinstall, Python worked without needing to be installed again.



<br>

### 🔴 WHY?:

<br>

 - Ubuntu ✋comes pre-installed with Python because **many system tools and applications depend on it.**

 - Typically, Python 2.x or Python 3.x (depending on the Ubuntu version) is installed by default.

 <br>


 - 🛑 **If you try to install another version of Python** using **apt**, such as python3.9, it can sometimes cause conflicts with the existing Python installation.

### dpkg / APT


>This **can lead to errors**, especially with **dpkg** (the package manager used by **apt**) if dependencies are not properly managed. ✋ [check the type of errors you will get](https://askubuntu.com/questions/1329514/how-can-i-resolve-dpkg-error-after-uninstalling-python3)

<br>
<br>




## 🟠 When can you install PYTHON



### 🟢 Ubuntu <u>Versions</u>  with Python Included by Default


<br>

- ✋Python is typically included by default in most Ubuntu versions, especially in the desktop versions. However, to be specific:

<br>

>Ubuntu `16.04 LTS` and later versions include Python by default.


>Ubuntu `18.04 LTS` and later versions include Python 3.x by default. **Python 2.x** is not included by default in Ubuntu 18.04 LTS and later, as Python 2.x reached its end of life.

<br>


🔴 If you're using an Ubuntu version **older** than **16.04 LTS**, Python might not be included by default, or it might be an older version.


 > It's recommended to upgrade to a supported version to ensure you have access to the latest Python features and security updates.

<br>

#### 🔸 To check your Ubuntu version, you can use:

```javascript
lsb_release -a
```





<br>
<br>
<br>
<br>


---


<br>

https://www.youtube.com/watch?v=s8njoafRxCM

#### Open your terminal

<br>

- Before installing, update your system

```javascript
sudo apt update

```

<br>

### 🟡 Install packages that will help us to compile

```javascript
sudo apt install build-essential

```

<br>

### 🟡 Install also TAR, this will help us to decompress

```javascript
sudo apt install tar
// READ MORE:  https://www.cyberciti.biz/faq/tar-extract-linux/
```

<br>
<br>

---

## Download PYTHON

- go to their official site

https://www.python.org/downloads/source/

<br>

#### 🟡 Once there choose an actual version

```javascript
// I will pick up this one
Python 3.12.0 - Oct. 2, 2023
Download Gzipped source tarball

// 🍊 pick this one
Download XZ compressed source tarball


```

### 🍊 Once the zip has been saved in your downloads(depending on your settings), extrait it there

```javascript
// option 1: right click to the tar or zip and choose to 'extract here'

//option 2:
tar - xf; // xf is to extract the tar  file
// ls to the folder it was dowloaded an then use it like so:
tar -xf Python-3.12.0.tar.xz // presuming this is the version you downloaded
//
ls
//😀 once you check where the version of Python is , enter it ith CD
cd Python-3.12.0/
```

<br>

---

<br>

## 🍭 NPROC

https://www.geeksforgeeks.org/nproc-command-in-linux-with-examples/

<br>

- 🍊 after **CD** on the Python folder, use the following command

```javascript
nproc;
```

#### result:

- i got 6

<br>

- The **nproc** command displays the number of processing units available to the current process. If it returns 4, it means your system has 4 processing units (usually CPU cores or threads) available.

<br>

### is 4 or 6 cores good?

- Consider what you intend to do with Python.

- 4 to 6 cores are usually sufficient. However, if you're planning to run computationally intensive tasks or large-scale data processing, more cores could be beneficial.

#### 🔴 If your system's primary purpose is Python development or data processing, having more cores might offer performance benefits. However, for general usage, 4 cores are typically adequate.

<br>

### NEOFETCH

- Neofetch is a command-line system information tool written in bash 3.2+. Neofetch displays information about your operating system, software and hardware in an aesthetic and visually pleasing way.

##### 👍 example: https://github.com/dylanaraps/neofetch

<br>

🍊

#### install neofetch

```javascript
sudo apt install neofetch
```

- 🔴 it didnt work for me, and before you start installing it, keep in mind you can break your ubuntu if you dont know what you are doing:

https://askubuntu.com/questions/1350036/i-broke-ubuntu-while-installing-neofetch-error-code-keeps-appearing-in-terminal

<br>

## 🍊 HTOP

<br>

https://vitux.com/ubuntu-htop-command/

- if you are on ubuntu its probable that its already installed, to see if its already installed type this in your terminal `htop -v`, if you get a version it means you have it, so type this in your terminal to launch it `htop`

<br>

```javascript
sudo apt install htop
```

https://support.cloudways.com/en/articles/5120765-how-to-monitor-system-processes-using-htop-command

```javascript
// descript
PID:                 Unique Process ID.
USER:             Process Owner.
VIRT:               Virtual memory being consumed by the process
%CPU:            The percentage of the processor time used by the process.
%MEM:           The percentage of physical RAM used by the process.
COMMAND:   The name of the command that started the process.
```

<br>

#### another program to see the quantity of cores

In a nutshell, htop is a useful command-line tool in the Linux environment to determine the cause of load by each process. It is similar to Task Manager in the Windows OS environment. It can be used to troubleshoot and kill a process that is utilizing excessive server resources.

<br>
<br>

## 🍊 REad about this command `make -j $(nproc)` before typing it on the terminal

### The command make -j $(nproc) is used in software development, particularly when compiling code with the make build automation tool. Here's what each part of the command does:

```javascript
make -j $(nproc)
```

**make:** This command invokes the make tool, which is commonly used to automate the build process for software projects. It reads a file called Makefile and executes the commands listed in it to build the project.

**-j:** This option tells make to execute multiple build jobs simultaneously, which can significantly speed up the build process, especially on multi-core processors. The argument following -j specifies the maximum number of concurrent jobs that make should run.

**$(nproc):** This part of the command uses the nproc command to determine the number of available processing units (CPU cores) on the system dynamically. The output of nproc is substituted into the command, so make will run as many jobs concurrently as there are available **CPU cores**.

### ✋ In summary, make -j $(nproc) optimizes the build process by running multiple build jobs in parallel, with the number of jobs being equal to the number of CPU cores on the system. This can lead to faster compilation times, especially for large projects.

<br>

## 🔴 CONCERN:

- i have 6 cores and a lot of data on my comp, and i am installing python, so i dont want my computer gets to slow, i already added 20 of memory ✋ [more memory](MORE-memory.md) because the updated ubuntu version is messy, so what should i do, should i use `make -j $(nproc)`, or if i limit it to 3 cores `make -j3`?

<br>
<br>

```javascript
sudo make altinstall
```

So, "sudo make altinstall" is used to build and install software from source code, ensuring that it's installed with the appropriate permissions and without conflicting with other versions already installed on the system.

<br>

### type this in your terminal

```javascript
python3.12 --version
```

### like so

```javascript
// Downloads is where my python folder is
nadiamard@yepyep:~/Downloads/Python-3.12.0$ python3.12 --version
// result
Python 3.12.0
// 🌈 this means you have successfully installed python
```

<br>
<br>

---

<br>
<br>

# 🍭 Extensions

<br>

https://www.datasource.ai/es/data-science-articles/las-10-mejores-extensiones-de-python-para-visual-studio-code

- GO to the extensions in your visual studio code, look for **Python Microsoft** (it s the first on the list)

<br>
<br>

## 🍭 terminal shells

https://code.visualstudio.com/docs/terminal/basics
