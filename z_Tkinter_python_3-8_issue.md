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

### 🟠 Missing packages from python3.8.18

- TO INSTALL: type this in your ubuntu console `pyenv install 3.8.18`

```javascript
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




  // ✋  lzma.py
   File "<string>", line 1, in <module>
    File "/home/mycomputer/.pyenv/versions/3.8.18/lib/python3.8/lzma.py", line 27, in <module>
    from _lzma import *


ModuleNotFoundError: No module named '_lzma'
WARNING: The Python lzma extension was not compiled. Missing the lzma lib?
Installed Python-3.8.18 to /home/mycomputer/.pyenv/versions/3.8.18

```

#### check again your Pyenv version

```javascript
pyenv --version

// output
pyenv 2.4.7

```

<br>

#### install sudo apt-get install libncurses5-dev libncursesw5-dev