


# 🟡 Unable to install tkinter using python3.8


<br>
<br>

- When installing `python 3.8.18` for the first time by using:  `pyenv install 3.8.18` , i noticed there were a lot of missing packets.

- i installed most of them [Python_err-install_packages](./z_Python_err-install_packages.md)


- But the **tkinter** was a bit complicated to solve- Here below you will find the solution.

<br>

#### 🟧 KEEP in mind that the ubuntu that installed, it came already with this version `python3.12` , this is the version my computer is actually using, the other versions you see below, were installed with pyenv i am using the 3.7.14 (for now, because i will be testing more)



#### Before installing, check the versions you already have

```javascript
  system
* 3.7.14 (set by /home/mycomputer/.pyenv/version)
  3.8.10
  3.8.18
  3.10.8


```


<br>
<br>


# 🟧 install `python3-tk`

 - about it: https://realpython.com/python-gui-tkinter/

 [visualize it: ](https://realpython.com/cdn-cgi/image/width=853,format=auto/https://files.realpython.com/media/17_4_tk_window.662fec42e4f9.jpg)

```javascript
sudo apt-get install python3-tk
```



```javascript


Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  blt libtk8.6 tk8.6-blt2.5
Suggested packages:
  blt-demo tk8.6 tix python3-tk-dbg
The following NEW packages will be installed:
  blt libtk8.6 python3-tk tk8.6-blt2.5
0 upgraded, 4 newly installed, 0 to remove and 3 not upgraded.
Need to get 1,516 kB of archives.
After this operation, 4,929 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://archive.ubuntu.com/ubuntu noble/main amd64 libtk8.6 amd64 8.6.14-1build1 [779 kB]
Get:2 http://archive.ubuntu.com/ubuntu noble/main amd64 tk8.6-blt2.5 amd64 2.5.3+dfsg-7build1 [630 kB]
Get:3 http://archive.ubuntu.com/ubuntu noble/main amd64 blt amd64 2.5.3+dfsg-7build1 [4,840 B]
Get:4 http://archive.ubuntu.com/ubuntu noble/main amd64 python3-tk amd64 3.12.3-0ubuntu1 [102 kB]
Fetched 1,516 kB in 2s (944 kB/s)
Selecting previously unselected package libtk8.6:amd64.
(Reading database ... 229586 files and directories currently installed.)
Preparing to unpack .../libtk8.6_8.6.14-1build1_amd64.deb ...
Unpacking libtk8.6:amd64 (8.6.14-1build1) ...
Selecting previously unselected package tk8.6-blt2.5.
Preparing to unpack .../tk8.6-blt2.5_2.5.3+dfsg-7build1_amd64.deb ...
Unpacking tk8.6-blt2.5 (2.5.3+dfsg-7build1) ...
Selecting previously unselected package blt.
Preparing to unpack .../blt_2.5.3+dfsg-7build1_amd64.deb ...
Unpacking blt (2.5.3+dfsg-7build1) ...
Selecting previously unselected package python3-tk:amd64.
Preparing to unpack .../python3-tk_3.12.3-0ubuntu1_amd64.deb ...
Unpacking python3-tk:amd64 (3.12.3-0ubuntu1) ...
Setting up libtk8.6:amd64 (8.6.14-1build1) ...
Setting up tk8.6-blt2.5 (2.5.3+dfsg-7build1) ...
Setting up blt (2.5.3+dfsg-7build1) ...
Setting up python3-tk:amd64 (3.12.3-0ubuntu1) ...
Processing triggers for libc-bin (2.39-0ubuntu8.2) ...

```

<br>
<br>

----

<br>

## 🟦 Uninstall Python`3.8.18` again

```javascript

pyenv uninstall 3.8.18

```

## 🍭 Remove cache from the Python`3.8.18` version

```javascript
rm -rf ~/.pyenv/cache/Python-3.8.18


```

### 🔸 Check PYenv version again

```javascript
pyenv --version

// output
pyenv 2.4.7

```

<br>

## 🟡 Install Python`3.8.18` again

```javascript
pyenv install 3.8.18
```



<br>
<br>

----

<br>

## 🟧 After installing Python



### 🔴 As you can see, all the other packages have been installed, ONLY the tkinter have issues

```javascript
Downloading Python-3.8.18.tar.xz...
-> https://www.python.org/ftp/python/3.8.18/Python-3.8.18.tar.xz
Installing Python-3.8.18...
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/home/mycomputer/.pyenv/versions/3.8.18/lib/python3.8/tkinter/__init__.py", line 36, in <module>
    import _tkinter # If this fails your Python may not be configured for Tk
ModuleNotFoundError: No module named '_tkinter'
WARNING: The Python tkinter extension was not compiled and GUI subsystem has been detected. Missing the Tk toolkit?
Installed Python-3.8.18 to /home/mycomputer/.pyenv/versions/3.8.18

```

<br>

<br>

# 🟧 install `tk-dev`



```javascript
sudo apt-get install tk-dev
// 🔴 not to be confused with the command that i used more at
///the top: sudo apt-get install python3-tk
// read after the code below

```


```javascript


Reading package lists... Done
Building dependency tree... Done
Reading state information... Done

//
The following additional packages will be installed:

//
//
//
  libbrotli-dev libfontconfig-dev libfontconfig1-dev libfreetype-dev libpkgconf3 libpng-dev libpng-tools libpthread-stubs0-dev libx11-dev libxau-dev
  libxcb1-dev libxdmcp-dev libxext-dev libxft-dev libxrender-dev libxss-dev pkgconf pkgconf-bin tcl-dev tcl8.6-dev tk tk8.6 tk8.6-dev uuid-dev
  x11proto-core-dev x11proto-dev xorg-sgml-doctools xtrans-dev
Suggested packages:
  freetype2-doc libx11-doc libxcb-doc libxext-doc tcl-doc tcl8.6-doc tk-doc tk8.6-doc
The following NEW packages will be installed:
  libbrotli-dev libfontconfig-dev libfontconfig1-dev libfreetype-dev libpkgconf3 libpng-dev libpng-tools libpthread-stubs0-dev libx11-dev libxau-dev
  libxcb1-dev libxdmcp-dev libxext-dev libxft-dev libxrender-dev libxss-dev pkgconf pkgconf-bin tcl-dev tcl8.6-dev tk tk-dev tk8.6 tk8.6-dev uuid-dev
  x11proto-core-dev x11proto-dev xorg-sgml-doctools xtrans-dev
0 upgraded, 29 newly installed, 0 to remove and 3 not upgraded.
Need to get 5,027 kB of archives.
After this operation, 19.5 MB of additional disk space will be used.
Do you want to continue? [Y/n] y

//
//
//
Get:1 http://archive.ubuntu.com/ubuntu noble/main amd64 libbrotli-dev amd64 1.1.0-2build2 [353 kB]
Get:2 http://archive.ubuntu.com/ubuntu noble/main amd64 libpng-dev amd64 1.6.43-5build1 [264 kB]
Get:3 http://archive.ubuntu.com/ubuntu noble/main amd64 libfreetype-dev amd64 2.13.2+dfsg-1build3 [575 kB]
Get:4 http://archive.ubuntu.com/ubuntu noble/main amd64 uuid-dev amd64 2.39.3-9ubuntu6 [33.5 kB]
Get:5 http://archive.ubuntu.com/ubuntu noble/main amd64 libpkgconf3 amd64 1.8.1-2build1 [30.7 kB]
Get:6 http://archive.ubuntu.com/ubuntu noble/main amd64 pkgconf-bin amd64 1.8.1-2build1 [20.7 kB]
Get:7 http://archive.ubuntu.com/ubuntu noble/main amd64 pkgconf amd64 1.8.1-2build1 [16.8 kB]
Get:8 http://archive.ubuntu.com/ubuntu noble/main amd64 libfontconfig-dev amd64 2.15.0-1.1ubuntu2 [161 kB]
Get:9 http://archive.ubuntu.com/ubuntu noble/main amd64 libfontconfig1-dev amd64 2.15.0-1.1ubuntu2 [1,840 B]
Get:10 http://archive.ubuntu.com/ubuntu noble/main amd64 libpng-tools amd64 1.6.43-5build1 [28.5 kB]
Get:11 http://archive.ubuntu.com/ubuntu noble/main amd64 libpthread-stubs0-dev amd64 0.4-1build3 [4,746 B]
Get:12 http://archive.ubuntu.com/ubuntu noble/main amd64 xorg-sgml-doctools all 1:1.11-1.1 [10.9 kB]
Get:13 http://archive.ubuntu.com/ubuntu noble/main amd64 x11proto-dev all 2023.2-1 [602 kB]
Get:14 http://archive.ubuntu.com/ubuntu noble/main amd64 libxau-dev amd64 1:1.0.9-1build6 [9,570 B]
Get:15 http://archive.ubuntu.com/ubuntu noble/main amd64 x11proto-core-dev all 2023.2-1 [2,444 B]
Get:16 http://archive.ubuntu.com/ubuntu noble/main amd64 libxdmcp-dev amd64 1:1.1.3-0ubuntu6 [26.5 kB]
Get:17 http://archive.ubuntu.com/ubuntu noble/main amd64 xtrans-dev all 1.4.0-1 [68.9 kB]
Get:18 http://archive.ubuntu.com/ubuntu noble/main amd64 libxcb1-dev amd64 1.15-1ubuntu2 [85.8 kB]
Get:19 http://archive.ubuntu.com/ubuntu noble/main amd64 libx11-dev amd64 2:1.8.7-1build1 [732 kB]
Get:20 http://archive.ubuntu.com/ubuntu noble/main amd64 libxext-dev amd64 2:1.3.4-1build2 [83.5 kB]
Get:21 http://archive.ubuntu.com/ubuntu noble/main amd64 libxrender-dev amd64 1:0.9.10-1.1build1 [26.3 kB]
Get:22 http://archive.ubuntu.com/ubuntu noble/main amd64 libxft-dev amd64 2.3.6-1build1 [64.3 kB]
Get:23 http://archive.ubuntu.com/ubuntu noble/main amd64 libxss-dev amd64 1:1.2.3-1build3 [12.1 kB]
Get:24 http://archive.ubuntu.com/ubuntu noble/main amd64 tcl8.6-dev amd64 8.6.14+dfsg-1build1 [1,000 kB]
Get:25 http://archive.ubuntu.com/ubuntu noble/main amd64 tcl-dev amd64 8.6.14build1 [5,782 B]
Get:26 http://archive.ubuntu.com/ubuntu noble/main amd64 tk8.6 amd64 8.6.14-1build1 [12.5 kB]
Get:27 http://archive.ubuntu.com/ubuntu noble/main amd64 tk amd64 8.6.14build1 [3,076 B]
Get:28 http://archive.ubuntu.com/ubuntu noble/main amd64 tk8.6-dev amd64 8.6.14-1build1 [788 kB]
Get:29 http://archive.ubuntu.com/ubuntu noble/main amd64 tk-dev amd64 8.6.14build1 [2,914 B]
Fetched 5,027 kB in 2s (2,140 kB/s)
Selecting previously unselected package libbrotli-dev:amd64.
(Reading database ... 229775 files and directories currently installed.)
Preparing to unpack .../00-libbrotli-dev_1.1.0-2build2_amd64.deb ...
Unpacking libbrotli-dev:amd64 (1.1.0-2build2) ...
Selecting previously unselected package libpng-dev:amd64.
Preparing to unpack .../01-libpng-dev_1.6.43-5build1_amd64.deb ...
Unpacking libpng-dev:amd64 (1.6.43-5build1) ...
Selecting previously unselected package libfreetype-dev:amd64.
Preparing to unpack .../02-libfreetype-dev_2.13.2+dfsg-1build3_amd64.deb ...
Unpacking libfreetype-dev:amd64 (2.13.2+dfsg-1build3) ...
Selecting previously unselected package uuid-dev:amd64.
Preparing to unpack .../03-uuid-dev_2.39.3-9ubuntu6_amd64.deb ...
Unpacking uuid-dev:amd64 (2.39.3-9ubuntu6) ...
Selecting previously unselected package libpkgconf3:amd64.
Preparing to unpack .../04-libpkgconf3_1.8.1-2build1_amd64.deb ...
Unpacking libpkgconf3:amd64 (1.8.1-2build1) ...
Selecting previously unselected package pkgconf-bin.
Preparing to unpack .../05-pkgconf-bin_1.8.1-2build1_amd64.deb ...
Unpacking pkgconf-bin (1.8.1-2build1) ...
Selecting previously unselected package pkgconf:amd64.
Preparing to unpack .../06-pkgconf_1.8.1-2build1_amd64.deb ...
Unpacking pkgconf:amd64 (1.8.1-2build1) ...
Selecting previously unselected package libfontconfig-dev:amd64.
Preparing to unpack .../07-libfontconfig-dev_2.15.0-1.1ubuntu2_amd64.deb ...
Unpacking libfontconfig-dev:amd64 (2.15.0-1.1ubuntu2) ...
Selecting previously unselected package libfontconfig1-dev:amd64.
Preparing to unpack .../08-libfontconfig1-dev_2.15.0-1.1ubuntu2_amd64.deb ...
Unpacking libfontconfig1-dev:amd64 (2.15.0-1.1ubuntu2) ...
Selecting previously unselected package libpng-tools.
Preparing to unpack .../09-libpng-tools_1.6.43-5build1_amd64.deb ...
Unpacking libpng-tools (1.6.43-5build1) ...
Selecting previously unselected package libpthread-stubs0-dev:amd64.
Preparing to unpack .../10-libpthread-stubs0-dev_0.4-1build3_amd64.deb ...
Unpacking libpthread-stubs0-dev:amd64 (0.4-1build3) ...
Selecting previously unselected package xorg-sgml-doctools.
Preparing to unpack .../11-xorg-sgml-doctools_1%3a1.11-1.1_all.deb ...
Unpacking xorg-sgml-doctools (1:1.11-1.1) ...
Selecting previously unselected package x11proto-dev.
Preparing to unpack .../12-x11proto-dev_2023.2-1_all.deb ...
Unpacking x11proto-dev (2023.2-1) ...
Selecting previously unselected package libxau-dev:amd64.
Preparing to unpack .../13-libxau-dev_1%3a1.0.9-1build6_amd64.deb ...
Unpacking libxau-dev:amd64 (1:1.0.9-1build6) ...
Selecting previously unselected package x11proto-core-dev.
Preparing to unpack .../14-x11proto-core-dev_2023.2-1_all.deb ...
Unpacking x11proto-core-dev (2023.2-1) ...
Selecting previously unselected package libxdmcp-dev:amd64.
Preparing to unpack .../15-libxdmcp-dev_1%3a1.1.3-0ubuntu6_amd64.deb ...
Unpacking libxdmcp-dev:amd64 (1:1.1.3-0ubuntu6) ...
Selecting previously unselected package xtrans-dev.
Preparing to unpack .../16-xtrans-dev_1.4.0-1_all.deb ...
Unpacking xtrans-dev (1.4.0-1) ...
Selecting previously unselected package libxcb1-dev:amd64.
Preparing to unpack .../17-libxcb1-dev_1.15-1ubuntu2_amd64.deb ...
Unpacking libxcb1-dev:amd64 (1.15-1ubuntu2) ...
Selecting previously unselected package libx11-dev:amd64.
Preparing to unpack .../18-libx11-dev_2%3a1.8.7-1build1_amd64.deb ...
Unpacking libx11-dev:amd64 (2:1.8.7-1build1) ...
Selecting previously unselected package libxext-dev:amd64.
Preparing to unpack .../19-libxext-dev_2%3a1.3.4-1build2_amd64.deb ...
Unpacking libxext-dev:amd64 (2:1.3.4-1build2) ...
Selecting previously unselected package libxrender-dev:amd64.
Preparing to unpack .../20-libxrender-dev_1%3a0.9.10-1.1build1_amd64.deb ...
Unpacking libxrender-dev:amd64 (1:0.9.10-1.1build1) ...
Selecting previously unselected package libxft-dev:amd64.
Preparing to unpack .../21-libxft-dev_2.3.6-1build1_amd64.deb ...
Unpacking libxft-dev:amd64 (2.3.6-1build1) ...
Selecting previously unselected package libxss-dev:amd64.
Preparing to unpack .../22-libxss-dev_1%3a1.2.3-1build3_amd64.deb ...
Unpacking libxss-dev:amd64 (1:1.2.3-1build3) ...
Selecting previously unselected package tcl8.6-dev:amd64.
Preparing to unpack .../23-tcl8.6-dev_8.6.14+dfsg-1build1_amd64.deb ...
Unpacking tcl8.6-dev:amd64 (8.6.14+dfsg-1build1) ...
Selecting previously unselected package tcl-dev:amd64.
Preparing to unpack .../24-tcl-dev_8.6.14build1_amd64.deb ...
Unpacking tcl-dev:amd64 (8.6.14build1) ...
Selecting previously unselected package tk8.6.
Preparing to unpack .../25-tk8.6_8.6.14-1build1_amd64.deb ...
Unpacking tk8.6 (8.6.14-1build1) ...
Selecting previously unselected package tk.
Preparing to unpack .../26-tk_8.6.14build1_amd64.deb ...
Unpacking tk (8.6.14build1) ...
Selecting previously unselected package tk8.6-dev:amd64.
Preparing to unpack .../27-tk8.6-dev_8.6.14-1build1_amd64.deb ...
Unpacking tk8.6-dev:amd64 (8.6.14-1build1) ...
Selecting previously unselected package tk-dev:amd64.
Preparing to unpack .../28-tk-dev_8.6.14build1_amd64.deb ...
Unpacking tk-dev:amd64 (8.6.14build1) ...
Setting up tk8.6 (8.6.14-1build1) ...
Setting up libpng-tools (1.6.43-5build1) ...
Setting up tcl8.6-dev:amd64 (8.6.14+dfsg-1build1) ...
Setting up libpng-dev:amd64 (1.6.43-5build1) ...
Setting up libpthread-stubs0-dev:amd64 (0.4-1build3) ...
Setting up xtrans-dev (1.4.0-1) ...
Setting up libpkgconf3:amd64 (1.8.1-2build1) ...
Setting up uuid-dev:amd64 (2.39.3-9ubuntu6) ...
Setting up pkgconf-bin (1.8.1-2build1) ...
Setting up tcl-dev:amd64 (8.6.14build1) ...
Setting up xorg-sgml-doctools (1:1.11-1.1) ...
Setting up tk (8.6.14build1) ...
Setting up libbrotli-dev:amd64 (1.1.0-2build2) ...
Setting up pkgconf:amd64 (1.8.1-2build1) ...
Setting up libfreetype-dev:amd64 (2.13.2+dfsg-1build3) ...
Setting up libfontconfig-dev:amd64 (2.15.0-1.1ubuntu2) ...
Setting up libfontconfig1-dev:amd64 (2.15.0-1.1ubuntu2) ...
Processing triggers for libc-bin (2.39-0ubuntu8.2) ...
Processing triggers for man-db (2.12.0-4build2) ...
Processing triggers for sgml-base (1.31) ...
Setting up x11proto-dev (2023.2-1) ...
Setting up libxau-dev:amd64 (1:1.0.9-1build6) ...
Setting up libxdmcp-dev:amd64 (1:1.1.3-0ubuntu6) ...
Setting up x11proto-core-dev (2023.2-1) ...
Setting up libxcb1-dev:amd64 (1.15-1ubuntu2) ...
Setting up libx11-dev:amd64 (2:1.8.7-1build1) ...
Setting up libxext-dev:amd64 (2:1.3.4-1build2) ...
Setting up libxrender-dev:amd64 (1:0.9.10-1.1build1) ...
Setting up libxft-dev:amd64 (2.3.6-1build1) ...
Setting up libxss-dev:amd64 (1:1.2.3-1build3) ...
Setting up tk8.6-dev:amd64 (8.6.14-1build1) ...
Setting up tk-dev:amd64 (8.6.14build1) ...


```

<br>

## 🟣 Differences

#### The packages `python3-tk` and `tk-dev` ✋ serve different purposes, although they are related to tkinter and Tkinter development.



<br>
<br>

## python3-tk

```javascript
sudo apt-get install python3-tk
```
🍫 **python3-tk:** This package provides the Tkinter module for Python 3.x.

🔸 Tkinter is Python's standard **GUI (Graphical User Interface)** toolkit, based on the **Tk GUI toolkit** originally developed for the Tcl scripting language. Installing python3-tk allows you to use Tkinter in your Python scripts to create graphical interfaces.

<br>

<br>

## tk-dev

🍰 **tk-dev:** This package (tk-dev) **provides development files and headers for the Tk GUI toolkit**.

- These files are **needed if you want to compile and build applications that use Tk**, such as when you're developing applications in languages other than Python that utilize Tk directly.


<br>

#### Installing tk-dev is useful if you're developing applications in C, C++, or other languages that interface with Tk directly.

>It provides the necessary files and headers to compile and link your applications against the Tk library.


<br>
<br>

----

<br>

## 🟦 Uninstall Python`3.8.18` again

```javascript

pyenv uninstall 3.8.18

```

## 🍭 Remove cache from the Python`3.8.18` version

```javascript
rm -rf ~/.pyenv/cache/Python-3.8.18


```

### 🔸 Check PYenv version again

```javascript
pyenv --version

// output
pyenv 2.4.7

```


<br>

<br>
<br>
<br>

## 🟡 Install Python`3.8.18` again

```javascript
pyenv install 3.8.18
```
#### outcome

- Seems like there are no more issues

```javascript
Downloading Python-3.8.18.tar.xz...
-> https://www.python.org/ftp/python/3.8.18/Python-3.8.18.tar.xz
Installing Python-3.8.18...
Installed Python-3.8.18 to /home/mycomputer/.pyenv/versions/3.8.18
```

<br>

## 🔸 Verify if the `Tkinter` has been installed

```javascript

dpkg -l python3-tk
```

#### outcome

- ✅ Seems like there are no more issues

```javascript
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name             Version         Architecture Description
+++-================-===============-============-=================================================
ii  python3-tk:amd64 3.12.3-0ubuntu1 amd64        Tkinter - Writing Tk applications with Python 3.x

```
<br>
<br>

- 🌈 The output you provided indicates that `python3-tk` version **3.12.3-0ubuntu1** is installed on your system.

>In summary, the presence of python3-tk version 3.12.3-0ubuntu1 means that Tkinter is installed and available for use with Python 3 on your Ubuntu system. You'll need to ensure that python3-tk or its equivalent is installed for each Python version you use with Pyenv, as Pyenv manages Python environments independently.

<br>

### Let's break down what this means:


<br>

**Name:** python3-tk is the package name for Tkinter for Python 3.
Version: 3.12.3-0ubuntu1 is the version of python3-tk that is installed.

**Architecture:** amd64 indicates that the package is built for 64-bit systems.

**Description:** "Tkinter - Writing Tk applications with Python 3.x" is a brief description of what the package provides.

<br>


### 🔴 If you switch to a different Python version using Pyenv (pyenv global, pyenv local, pyenv shell)..


- 🟥 you will need to ensure that **python3-tk** is installed for that **specific Python version** as well.

- 🟥 Installing **python3-tk** for one Python version does not automatically install it for other Python versions managed by Pyenv.

<br>