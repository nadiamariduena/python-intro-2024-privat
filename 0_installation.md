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
