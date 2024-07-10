## 🔴 Unable to install tkinter using python3.8


- When installing python 3.8.18 for the first time by using:  `pyenv install 3.8.18` , i notice there were a lot of missing packets

<br>

#### 🟣 KEEP in mind that the ubuntu that installed, it came already with this version `python3.12` , this is the version my computer is actually using, the other versions you see below, were installed with pyenv i am using the 3.7.14 (for now, because i will be testing more)



#### Before installing, check the versions you already have

```javascript
  system
* 3.7.14 (set by /home/mycomputer/.pyenv/version)
  3.8.10
  3.8.18
  3.10.8


```


<br>

### 🟧  Missing packages from python3.8.18

- TO INSTALL: type this in your ubuntu console `pyenv install 3.8.18`

```javascript
// ✋ output
//
//
Downloading Python-3.8.18.tar.xz...
-> https://www.python.org/ftp/python/3.8.18/Python-3.8.18.tar.xz
Installing Python-3.8.18...
Traceback (most recent call last):
  File "<string>", line 1, in <module>

// --------  MISSING PACKAGES ---------------

   // ✋ curses
  File "/home/mycomputer/.pyenv/versions/3.8.18/lib/python3.8/curses/__init__.py", line 13, in <module>
    from _curses import *
ModuleNotFoundError: No module named '_curses'
WARNING: The Python curses extension was not compiled. Missing the ncurses lib?
Traceback (most recent call last):
  File "<string>", line 1, in <module>



   // ✋ ctypes  libffi
  File "/home/mycomputer/.pyenv/versions/3.8.18/lib/python3.8/ctypes/__init__.py", line 7, in <module>
    from _ctypes import Union, Structure, Array
ModuleNotFoundError: No module named '_ctypes'
WARNING: The Python ctypes extension was not compiled. Missing the libffi lib?
Traceback (most recent call last):




  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'readline'
WARNING: The Python readline extension was not compiled. Missing the GNU readline lib?
Traceback (most recent call last):





  // ✋ sqlite3.dbapi2
  File "<string>", line 1, in <module>
  File "/home/mycomputer/.pyenv/versions/3.8.18/lib/python3.8/sqlite3/__init__.py", line 23, in <module>
    from sqlite3.dbapi2 import *
  File "/home/mycomputer/.pyenv/versions/3.8.18/lib/python3.8/sqlite3/dbapi2.py", line 27, in <module>
    from _sqlite3 import *
ModuleNotFoundError: No module named '_sqlite3'
WARNING: The Python sqlite3 extension was not compiled. Missing the SQLite3 lib?
Traceback (most recent call last):





  // ✋  tkinter
  File "<string>", line 1, in <module>
  File "/home/mycomputer/.pyenv/versions/3.8.18/lib/python3.8/tkinter/__init__.py", line 36, in <module>
    import _tkinter # If this fails your Python may not be configured for Tk

ModuleNotFoundError: No module named '_tkinter'
WARNING: The Python tkinter extension was not compiled and GUI subsystem has been detected. Missing the Tk toolkit?
Traceback (most recent call last):




  // ✋  lzma.py  liblzma-dev
   File "<string>", line 1, in <module>
    File "/home/mycomputer/.pyenv/versions/3.8.18/lib/python3.8/lzma.py", line 27, in <module>
    from _lzma import *


ModuleNotFoundError: No module named '_lzma'
WARNING: The Python lzma extension was not compiled. Missing the lzma lib?
Installed Python-3.8.18 to /home/mycomputer/.pyenv/versions/3.8.18

```

<br>

### 🟧  check again your Pyenv version

```javascript
pyenv --version

// output
pyenv 2.4.7

```

<br>

 # 🟧 install `libncurses5-dev libncursesw5-dev`

```javascript
sudo apt-get install libncurses5-dev libncursesw5-dev
```


<br>

```javascript
// ✋ output
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Note, selecting 'libncurses-dev' instead of 'libncurses5-dev'
Note, selecting 'libncurses-dev' instead of 'libncursesw5-dev'

//
//
Suggested packages:
  ncurses-doc
The following NEW packages will be installed:
  libncurses-dev
0 upgraded, 1 newly installed, 0 to remove and 3 not upgraded.
Need to get 384 kB of archives.
After this operation, 2,417 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu noble/main amd64 libncurses-dev amd64 6.4+20240113-1ubuntu2 [384 kB]
Fetched 384 kB in 1s (324 kB/s)
Selecting previously unselected package libncurses-dev:amd64.
(Reading database ... 229441 files and directories currently installed.)
Preparing to unpack .../libncurses-dev_6.4+20240113-1ubuntu2_amd64.deb ...
Unpacking libncurses-dev:amd64 (6.4+20240113-1ubuntu2) ...
Setting up libncurses-dev:amd64 (6.4+20240113-1ubuntu2) ...
Processing triggers for man-db (2.12.0-4build2) ...


```


<br>

<br>

 # 🟧 install `libffi-dev`

```javascript
sudo apt-get install libffi-dev
```


```javascript
// ✋ output
//
//
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following NEW packages will be installed:
  libffi-dev
0 upgraded, 1 newly installed, 0 to remove and 3 not upgraded.
Need to get 62.8 kB of archives.
After this operation, 331 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu noble/main amd64 libffi-dev amd64 3.4.6-1build1 [62.8 kB]
Fetched 62.8 kB in 1s (91.9 kB/s)
Selecting previously unselected package libffi-dev:amd64.
(Reading database ... 229522 files and directories currently installed.)
Preparing to unpack .../libffi-dev_3.4.6-1build1_amd64.deb ...
Unpacking libffi-dev:amd64 (3.4.6-1build1) ...
Setting up libffi-dev:amd64 (3.4.6-1build1) ...
Processing triggers for install-info (7.1-3build2) ...
Processing triggers for man-db (2.12.0-4build2) ...
```


<br>

<br>

### 🟧 install `libreadline-dev`

```javascript
sudo apt-get install libreadline-dev
```


```javascript
// ✋ output
//
//
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Suggested packages:
  readline-doc
The following NEW packages will be installed:
  libreadline-dev
0 upgraded, 1 newly installed, 0 to remove and 3 not upgraded.
Need to get 167 kB of archives.
After this operation, 814 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu noble/main amd64 libreadline-dev amd64 8.2-4build1 [167 kB]
Fetched 167 kB in 1s (137 kB/s)
Selecting previously unselected package libreadline-dev:amd64.
(Reading database ... 229557 files and directories currently installed.)
Preparing to unpack .../libreadline-dev_8.2-4build1_amd64.deb ...
Unpacking libreadline-dev:amd64 (8.2-4build1) ...
Setting up libreadline-dev:amd64 (8.2-4build1) ...
Processing triggers for install-info (7.1-3build2) ...

```



<br>

<br>

 # 🟧 install `sqlite3 libsqlite3-dev`

```javascript
sudo apt-get install sqlite3 libsqlite3-dev
```


```javascript
// ✋ output
//
//
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Suggested packages:
  sqlite3-doc
The following NEW packages will be installed:
  libsqlite3-dev sqlite3
0 upgraded, 2 newly installed, 0 to remove and 3 not upgraded.
Need to get 1,055 kB of archives.
After this operation, 3,983 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu noble/main amd64 libsqlite3-dev amd64 3.45.1-1ubuntu2 [911 kB]
Get:2 http://archive.ubuntu.com/ubuntu noble/main amd64 sqlite3 amd64 3.45.1-1ubuntu2 [144 kB]
Fetched 1,055 kB in 2s (540 kB/s)
Selecting previously unselected package libsqlite3-dev:amd64.
(Reading database ... 229572 files and directories currently installed.)
Preparing to unpack .../libsqlite3-dev_3.45.1-1ubuntu2_amd64.deb ...
Unpacking libsqlite3-dev:amd64 (3.45.1-1ubuntu2) ...
Selecting previously unselected package sqlite3.
Preparing to unpack .../sqlite3_3.45.1-1ubuntu2_amd64.deb ...
Unpacking sqlite3 (3.45.1-1ubuntu2) ...
Setting up libsqlite3-dev:amd64 (3.45.1-1ubuntu2) ...
Setting up sqlite3 (3.45.1-1ubuntu2) ...
Processing triggers for man-db (2.12.0-4build2) ...

```




<br>

<br>

 # 🟧 install `liblzma-dev`

```javascript
sudo apt-get install liblzma-dev
```


```javascript
// ✋ output
//
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Suggested packages:
  liblzma-doc
The following NEW packages will be installed:
  liblzma-dev
0 upgraded, 1 newly installed, 0 to remove and 3 not upgraded.
Need to get 176 kB of archives.
After this operation, 801 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu noble/main amd64 liblzma-dev amd64 5.6.1+really5.4.5-1 [176 kB]
Fetched 176 kB in 1s (276 kB/s)
Selecting previously unselected package liblzma-dev:amd64.
(Reading database ... 229736 files and directories currently installed.)
Preparing to unpack .../liblzma-dev_5.6.1+really5.4.5-1_amd64.deb ...
Unpacking liblzma-dev:amd64 (5.6.1+really5.4.5-1) ...
Setting up liblzma-dev:amd64 (5.6.1+really5.4.5-1) ...

```


<br>

<br>

<br>

# 🟧 install `python3-tk`

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

## 🍭 Remove cache from the version below

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

----

<br>


## 🟡 Install Python`3.8.18` again

```javascript
pyenv install 3.8.18
```


<br>

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