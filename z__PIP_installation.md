### 🟡 Installing packages using PIP

- open the terminal, type: `pip install requests`

> The **requests** package in Python is a powerful tool used for making HTTP requests from your Python code. Here’s more detail on its purpose and some key features [ read more](../z_about_packages/pip_requests.md)

### installing the request package

- Normally the following command would suffice to install the package on your project but if it doesn't work, you have a couple of options

```javascript
// option 1
pip install requests
// option 2
python -m pip install requests
```

<br>

### 🔴 but if you get the following error:

`/usr/bin/python: No module named pip`

### 1. got to your terminal (ubuntu), type this:

`wget https://bootstrap.pypa.io/get-pip.py`

##### output

```javascript
// .... SENSITIVE DATA (your ip and other stuff)
// .... then you will get the below
nnected.
HTTP request sent, awaiting response... 200 OK
Length: 2276232 (2,2M) [text/x-python]
Saving to: ‘get-pip.py’

get-pip.py          100%[===================>]   2,17M  3,11MB/s    in 0,7s

2024-06-21 21:15:05 (3,11 MB/s) - ‘get-pip.py’ saved [2276232/2276232]
// ✋ this seems okay
```

<br>

### 2. type this: `python3 get-pip.py`

##### output

```javascript
Traceback (most recent call last):
  File "get-pip.py", line 28541, in <module>
    main()
  File "get-pip.py", line 135, in main
    bootstrap(tmpdir=tmpdir)
  File "get-pip.py", line 111, in bootstrap
    monkeypatch_for_cert(tmpdir)
  File "get-pip.py", line 92, in monkeypatch_for_cert
    from pip._internal.commands.install import InstallCommand
  File "<frozen zipimport>", line 259, in load_module
  File "/tmp/tmp895wfcyr/pip.zip/pip/_internal/commands/__init__.py", line 9, in <module>
  File "<frozen zipimport>", line 259, in load_module
  File "/tmp/tmp895wfcyr/pip.zip/pip/_internal/cli/base_command.py", line 15, in <module>
  File "<frozen zipimport>", line 259, in load_module
  File "/tmp/tmp895wfcyr/pip.zip/pip/_internal/cli/cmdoptions.py", line 24, in <module>
  File "<frozen zipimport>", line 259, in load_module
  File "/tmp/tmp895wfcyr/pip.zip/pip/_internal/cli/parser.py", line 12, in <module>
  File "<frozen zipimport>", line 259, in load_module
  File "/tmp/tmp895wfcyr/pip.zip/pip/_internal/configuration.py", line 26, in <module>
  File "<frozen zipimport>", line 259, in load_module
  File "/tmp/tmp895wfcyr/pip.zip/pip/_internal/utils/logging.py", line 29, in <module>
  File "<frozen zipimport>", line 259, in load_module
  File "/tmp/tmp895wfcyr/pip.zip/pip/_internal/utils/misc.py", line 43, in <module>
  File "<frozen zipimport>", line 259, in load_module
  File "/tmp/tmp895wfcyr/pip.zip/pip/_internal/locations/__init__.py", line 66, in <module>
  File "<frozen zipimport>", line 259, in load_module
  File "/tmp/tmp895wfcyr/pip.zip/pip/_internal/locations/_distutils.py", line 20, in <module>
ModuleNotFoundError: No module named 'distutils.cmd' // 🔴 not good

```

<br>
<br>

## 🟠 If that failed, then try this:

- **1)** Install pip using apt (if available)

- If **apt** is giving you trouble, you might try installing pip via the Ubuntu package manager directly, although this method may not always yield the most recent version of pip: `sudo apt install python3-pip`

```javascript
// OUTPUT
Reading package lists... Done
Building dependency tree
Reading state information... Done
Package python3-pip is not available, but is referred to by another package.
This may mean that the package is missing, has been obsoleted, or
is only available from another source

E: Package 'python3-pip' has no installation candidate
// 🔴 NOT GOOD
```

- **2)** Type this `sudo apt update` to update everything (just to be sure)

```javascript
// output
// ...
Reading package lists... Done
Building dependency tree
Reading state information... Done
21 packages can be upgraded. Run 'apt list --upgradable' to see them.
```

<br>

- **3)** ✋ Since this is the module `'distutils.cmd'` that is causing the issue, i will install it:

```javascript
sudo apt install python3-distutils
```

#### once installed

- read the last 5 lines, if there is nothing wrong (like missing package etc...) then it worked!, i go this:

```javascript
Selecting previously unselected package python3-distutils.
(Reading database ... 226770 files and directories currently installed.)
Preparing to unpack .../python3-distutils_3.8.10-0ubuntu1~20.04_all.deb ...
Unpacking python3-distutils (3.8.10-0ubuntu1~20.04) ...
Setting up python3-distutils (3.8.10-0ubuntu1~20.04) ...

```

<br>
<br>

### TYpe this again:

- 1 `wget https://bootstrap.pypa.io/get-pip.py`

- 2 then this `python3 get-pip.py`

```javascript
// output of step 2
Successfully installed pip-24.1 setuptools-70.1.0 wheel-0.43.0
```

<br>
<br>

### 🌈 Now TRY to install the `requests` again, type the following: `python -m pip install requests`

```javascript
 // OUTPUT
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: requests in /usr/lib/python3/dist-packages (2.22.0)
```

<br>

### then check if you get the LIST (as that is what i want to obtain), type this to verify the whole process worked: `python -m pip list`

```javascript
// ✅ GOOD!! it works. 🌈

Package                Version
---------------------- --------------------
apturl                 0.5.2
bcrypt                 3.1.7
blinker                1.4
Brlapi                 0.7.0
certifi                2019.11.28
chardet                3.0.4
Click                  7.0
colorama               0.4.3
command-not-found      0.3
cryptography           2.8
cupshelpers            1.0
dbus-python            1.2.16
defer                  1.0.6
distro                 1.4.0
distro-info            0.23+ubuntu1.1
duplicity              0.8.12.0
entrypoints            0.3
fasteners              0.14.1
future                 0.18.2
httplib2               0.14.0
idna                   2.8
keyring                18.0.1
language-selector      0.1
launchpadlib           1.10.13
lazr.restfulclient     0.14.2
lazr.uri               1.0.3
lockfile               0.12.2
louis                  3.12.0
macaroonbakery         1.3.1
Mako                   1.1.0
MarkupSafe             1.1.0
monotonic              1.5
netifaces              0.10.4
oauthlib               3.1.0
olefile                0.46
paramiko               2.6.0
pexpect                4.6.0
Pillow                 7.0.0
pip                    24.1
protobuf               3.6.1
pycairo                1.16.2
pycrypto               2.6.1
pycups                 1.9.73
PyGObject              3.36.0
PyJWT                  1.7.1
pymacaroons            0.13.0
PyNaCl                 1.3.0
pyRFC3339              1.1
python-apt             2.0.1+ubuntu0.20.4.1
python-dateutil        2.7.3
python-debian          0.1.36+ubuntu1.1
pytz                   2019.3
pyxdg                  0.26
PyYAML                 5.3.1
reportlab              3.5.34
requests               2.22.0 ✋
requests-unixsocket    0.2.0
SecretStorage          2.3.1
setuptools             70.1.0
simplejson             3.16.0
six                    1.14.0
ssh-import-id          5.10
systemd-python         234
ubuntu-advantage-tools 8001
ubuntu-drivers-common  0.0.0
ufw                    0.36
unattended-upgrades    0.1
urllib3                1.25.8
usb-creator            0.3.7
wadllib                1.3.3
wheel                  0.43.0
xkit                   0.0.0
```

### You can also install a specific Version of a packet:

[2:47 | Python Virtual Environment and pip for Beginners](https://youtu.be/eDe-z2Qy9x4?si=LT-ynKPd_9Yfkueb&t=167)

<br>

- Currently i have the: `2.22.0` version fo the **requests**

```javascript
requests               2.22.0 ✋
```

- But i could change it to something else, example:

```javascript
// in my machine: python -m pip install requests==2.30.0
py -m pip install requests==2.30.0
// OUTPUT
  WARNING: The script normalizer is installed in '/home/myComp/.local/bin' which is not on PATH. // 🔴 i will be solving this later
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  // 🌈 success!!
Successfully installed charset-normalizer-3.3.2 requests-2.30.0
```

### Verify the changes

- type this again: `python -m pip list`

```javascript
Package                Version
---------------------- --------------------
apturl                 0.5.2
bcrypt                 3.1.7
blinker                1.4
Brlapi                 0.7.0
certifi                2019.11.28
chardet                3.0.4
charset-normalizer     3.3.2
Click                  7.0
colorama               0.4.3
command-not-found      0.3
cryptography           2.8
cupshelpers            1.0
dbus-python            1.2.16
defer                  1.0.6
distro                 1.4.0
distro-info            0.23+ubuntu1.1
duplicity              0.8.12.0
entrypoints            0.3
fasteners              0.14.1
future                 0.18.2
httplib2               0.14.0
idna                   2.8
keyring                18.0.1
language-selector      0.1
launchpadlib           1.10.13
lazr.restfulclient     0.14.2
lazr.uri               1.0.3
lockfile               0.12.2
louis                  3.12.0
macaroonbakery         1.3.1
Mako                   1.1.0
MarkupSafe             1.1.0
monotonic              1.5
netifaces              0.10.4
oauthlib               3.1.0
olefile                0.46
paramiko               2.6.0
pexpect                4.6.0
Pillow                 7.0.0
pip                    24.1
protobuf               3.6.1
pycairo                1.16.2
pycrypto               2.6.1
pycups                 1.9.73
PyGObject              3.36.0
PyJWT                  1.7.1
pymacaroons            0.13.0
PyNaCl                 1.3.0
pyRFC3339              1.1
python-apt             2.0.1+ubuntu0.20.4.1
python-dateutil        2.7.3
python-debian          0.1.36+ubuntu1.1
pytz                   2019.3
pyxdg                  0.26
PyYAML                 5.3.1
reportlab              3.5.34
requests               2.30.0 // ✅ it works!
requests-unixsocket    0.2.0
SecretStorage          2.3.1
setuptools             70.1.0
simplejson             3.16.0
six                    1.14.0
ssh-import-id          5.10
systemd-python         234
ubuntu-advantage-tools 8001
ubuntu-drivers-common  0.0.0
ufw                    0.36
unattended-upgrades    0.1
urllib3                1.25.8
usb-creator            0.3.7
wadllib                1.3.3
wheel                  0.43.0
xkit                   0.0.0
```

<br>

```javascript
// before
requests               2.22.0 ✋
// after
requests               2.30.0 // ✅ it works!
```

<br>

### To Go back to what i had

- this command below is going to update the package to the currect release

```javascript
// -U for update
// in my machine: python -m pip install -U requests
py -m pip install -U requests
```

##### output

```javascript
requests               2.32.3 // ✋ different to what i had before, the first change
```

<br>

#### Uninstall

- If you want to uninstall and repeat the whole process:

```javascript
// -U for update
// in my machine: python -m pip uninstall requests
py -m pip uninstall requests
```
