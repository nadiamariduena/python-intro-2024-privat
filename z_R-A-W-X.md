# 🟡 R.A.W.X

[Python File Handling for Beginners](https://youtu.be/BRrem1k3904?si=fT2tkkVBgT-9yn93&t=44)

```bash
# Acronym for:

# r = Read  # Reading data from a file.
# a = Append # Adding data to the end of a file.
# w = Write # Writing data to a file, overwriting existing content
# x = Create # Extending the file with additional content or executing a file
```

<br>

**r** (**Read**): This mode allows reading from an existing file. It positions the file pointer at the beginning of the file.

**a** (**Append**): This mode allows appending data to the end of an existing file. It also creates a new file if it doesn't exist.

**w** (**Write**): This mode allows writing data to a file. It truncates the file to zero length if it exists or creates a new file for writing.


**x** (**Create**): This mode creates a new file and opens it for writing. If the file already exists, the operation will fail.

<br>

<br>

### 🟡 QUESTION: 🫐 "Explain 'rawx' in Python for file handling, using diagrams to illustrate its structure. I've heard it's similar to CRUD. Explain the purpose of 'rawx' and provide small examples of its use. Finally, conclude with an example involving ice cream."

<br>
<br>

#### 🔸 chatgpt:

In Python, when working with files, **"rawx"** operations typically refer to low-level file handling using functions like `open(), read(), write(), and close()`.

- - **These operations** give you direct control over:

>**reading from and writing** to files without higher-level abstractions that libraries like pandas or csv provide.






<br>
<br>


### 🟧 Let's break down the components and their similarities to CRUD operations, and then we'll use diagrams to illustrate their structure.

<br>


### 🟪 Structure of Raw File Operations

- Raw file operations involve the following key steps:

**Open:** Use `open()` function to open a file and obtain a file object.


**Read/Write:** Use `read(), write(), seek(), etc.`, to manipulate the file content directly.


**Close:** Use `close()` to release the file object and free up system resources.

<br>

### 🟪 Similarities to CRUD Operations


**Create (C):** Create new files or write data to existing files.

**Read (R):** Read data from files.

**Update (U)**: Modify existing data in files.

**Delete (D):** Remove files or specific data from files.

<br>
<br>

## 🟠 Purpose of Raw File Operations


- The purpose of using raw file operations is to have precise control over how data is read from or written to files.

- 👾 This level of control is **useful when dealing with binary data**, custom file formats, or when performance optimization is critical.

<br>
<br>

### 🟢 Examples (chatgpt)

#### Reading from a File ('r'):

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

```


<br>

### 🟢 Examples from this tutorial: [min: 2:23 | Python File Handling for Beginners](https://youtu.be/BRrem1k3904?si=WMO2xCStRm5uiB8h&t=143)


<br>

1. Create 3 files: `context.txt, more_names.txt names.txt`

2. add the following to all of them

<br>

```python
Dave
Jane
Eddie
Jimmie
```

<br>

3. Now create another file and call it `files.py`

#### it should look like this:

```javascript
project_folder/
├── Lesson_18/
     └── context.txt
     └── files.py
     └── more_names.txt
     └── names.txt



```

<br>


### 🟠 `files.py`

```bash
# Acronym for:

# r = Read
# a = Append
# w = Write
# x = Create

# Read - Error if the file doesn't exist
# f stands for FILE
# r stands for read, i will use it here below,  as the second argument

f = open("names.txt", "r")
```

<br>

### 🟠 this 2 are the same, you dont need to add the "r" (read), as it will automatically know that the operation is for reading

```python
# this is the same
f = open("names.txt")
#  as this
f = open("names.txt", "r")

```

<br>

### 🟠 but if you add a third argument like "b" to the "r", like so `rb` , then you are specifying that you will be reading a binary file, or an `rt` to read a "text file"

```python
f = open("names.txt", "rb")
```

<br>

<br>

### 🟠 reach the file `names.txt` content and show it

```python
f = open("names.txt")
print(f.read())
```

<br>

#### to try the code, type: `python files.py` on your terminal, like so

-

```javascript
mycomputer:~/LESSON_18$ python files.py
```

<br>

#### output

- you will have the content of the `file.py`

```javascript
// /LESSON_18_rawx_operations$ python files.py

# names

Dave
Jane
Eddie
Jimmie
```