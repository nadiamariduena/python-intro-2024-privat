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

# 🟩 OPEN()

- Use the **open()** operation to access the content of the files.py file (which contains 4 names). Once you are done, remember to `close()` the `open()` operation ✋ (its important to close it, read it here: [Go to section](#close_the_operation))



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

<br>

<br>

### LOOP



```python
# for the line in f ,(which is the names.txt), print the line
for line in f:
    print(line)

# output
#
# Dave

# Jane

# Eddie

# Jimmie
```

<br>
<br>

# 🟩 CLOSE()

- 🔴 its important that you close the file, because it might be that you have some changes done, and its not going to show up until you **close()** it

```python
#  f is the data coming from the (names.txt)
f.close()
```

<br>
<br>

### 🟠 Try

- The `try, except, and finally` blocks in your code snippet are used to handle file operations, specifically reading from a file named **"names.txt"**.


```python

# ✋ you will see the names twice
f = open("names.txt")


for line in f:
    print(line)
    # this "line" here will create a sort of divider

print("----")

f.close()

#  ------------
# This part BELOW attempts to open and read from a file named "names.txt". It includes error handling "TRY" to manage cases where the file does not exist or cannot be opened.

try:
    f = open("names.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exists")
finally:
    f.close()
```
<br>

#### 🔴 Does adding `close()` at the end of the file ensure that, no matter how many changes I make to names.txt, the close() will protect it?

##### chatgpt:

Yes, using f.close() at the end of working with a file, as you have done in your code snippet, is a good practice for several reasons, including ensuring that any changes made to the file are properly saved and resources associated with the file are released.

<br>

#### output

```javascript
Dave

Jane

Eddie

Jimmie
----
Dave
Jane
Eddie
Jimmie
```








<a name="close_the_operation"></a>

## 🫐 Closing a file in Python after performing operations on it is crucial for several reasons:

<br>
<br>

### 🔶 Flush Buffer to Disk:

When you write to a file in Python, the data is often buffered in memory before being physically written to the file on disk.

 🔴 If you do not close the file properly using **close()**, the buffered data may not be written to the disk.

 Closing the file ensures that any remaining data in the buffer is flushed (written) to the file.

<br>
<br>

### 🔶 Release System Resources:

  Opening a file **consumes system resources** (file descriptors in operating systems).

   🔴 If you keep a file open unnecessarily, you might reach the **limit of maximum open file descriptors allowed by the operating system**.

   🟦 Closing the file releases these resources, allowing other parts of your program or other programs to use them.


<br>
<br>

### 🔶 Ensure Data Integrity:

  If you are performing operations that modify the contents of a file (e.g., writing, appending, etc.),
  closing the file ensures that all modifications are finalized and saved to the file.

  <br>

  🔴 If you do not close the file properly, some changes may not be written completely or correctly, leading to potential data corruption or loss.


  #### 🤔 So, close() in Python is like locking a door with a key before leaving. But if someone else with a key opens the door while I'm not home, can I track these movements with timestamps or logs?

  <br>

  ##### ✅ chatgpt:

  - Yes, you can track these movements (operations on files or resources) in Python using various logging mechanisms or libraries.

  <br>
  <br>

  ###  🟦 Here are some approaches and libraries you can use:



  #### Logging Module:

  - - Python's built-in logging module **allows you to record detailed information about events, including timestamps.**

  - -  You can **log messages when resources are accessed (opened) and when they are closed.** ✋

  <br>
  <br>

  ### 🟡 To create a tracking system that logs when the open() and close() operations occur for the file names.txt, you can integrate logging into the open() and close() actions.

  - Here's how you can modify your code to achieve this:

  ```python
#

  ```