## 🟡 INSTALLATION

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

// pick this one
Download XZ compressed source tarball


```

### Once the zip has been saved in your downloads(depending on your settings), extrait it there

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

- after **CD** on the Python folder, use the following command

```javascript
nproc;
```

<br>

- The **nproc** command displays the number of processing units available to the current process. If it returns 4, it means your system has 4 processing units (usually CPU cores or threads) available.

#### is 4 cores good?
