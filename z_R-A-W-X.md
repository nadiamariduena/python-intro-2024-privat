# 🟡 R.A.W.X


<br>

- Open() [Go to section](#_OPEN_operation)

- Close() [Go to section](#_CLOSE_operation)

- Append() [Go to section](#_APPEND_operation)





<br>
<br>

# 🌴 FILE operations

[Python File Handling for Beginners](https://youtu.be/BRrem1k3904?si=fT2tkkVBgT-9yn93&t=44)

<br>

## 🟠 Purpose of RAWX File Operations


- The purpose of using raw file operations is to have precise control over how data is read from or written to files.

- 👾 This level of control is **useful when dealing with binary data**, custom file formats, or when performance optimization is critical.






```bash
# Acronym for:

# r = Read  # Reading data from a file.
# a = Append # Adding data to the end of a file.
# w = Write # Writing data to a file, overwriting existing content
# x = Create # Extending the file with additional content or executing a file
```

#### 🟢 Examples from this tutorial: [min: 2:23 | Python File Handling for Beginners](https://youtu.be/BRrem1k3904?si=WMO2xCStRm5uiB8h&t=143)



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
<br>

<a name="_OPEN_operation"></a>

# 🟩 OPEN()

### Purpose of open() in File Operations

<br>

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

<a name="_CLOSE_operation"></a>

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

<br>

#### 🔴 Does adding `close()` at the end of the file ensure that, no matter how many changes I make to names.txt, the close() will protect it?

##### ✅ chatgpt:

Yes, using `f.close()` at the end of working with a file, as you have done in your code snippet, is a good practice for several reasons, including ensuring that any changes made to the file are properly saved and resources associated with the file are released.







<br>
<br>




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

<br>

  - Here's how you can modify your code to achieve this:

  <br>



## 1.


```javascript
project_root/
│
├── files.py
|── files_morenames.py
|── more_names.txt
```

### 2.

```python
# ✋ files_morenames.py

import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='file_operations.log', level=logging.INFO)

# Function to log when the file is opened
def open_file(filename):
    logging.info(f'File {filename} opened at {datetime.now()}')

# Function to log when the file is closed
def close_file(filename):
    logging.info(f'File {filename} closed at {datetime.now()}')

# Function to read and print the content of the file
def read_file(filename):
    #
    #
    #

    try:
        with open(filename, 'r') as f:
            open_file(filename)  # Log file open operation
             #
            #
            for line in f:
                print(line.strip())  # Print each line (strip to remove newline characters)
            print("----")
            #
            #
    except FileNotFoundError:
        logging.error(f'File {filename} not found at {datetime.now()}')

        print("The file you want to read doesn't exist")
    except Exception as e:
        logging.error(f'Error reading file {filename}: {str(e)} at {datetime.now()}')
        print(f"Error reading file: {str(e)}")
    finally:
        close_file(filename)  # Log file close operation
    #
    #
    #
    #
    #
    #
# Example usage 🌈
filename = "more_names.txt" # this is the file i will be using, i have added some quotes, instead of just names
read_file(filename)

  ```

  <br>

## 3. Within the `more_names.txt` file, add some content

```bash
# ✋ more_names.py
#
#

Ludovico Sforza

One believes things because one has been conditioned to believe them.

Stability isn’t nearly so spectacular as instability.

Most human beings have an almost infinite capacity for taking things for granted.

When the rich wage war it's the poor who die.


```

<br>

## 4. RUN the code

- Type this in your VS terminal `python files_morenames.py` (you can create a venv or you can just do it within the folder your are testing this, in my case is LESSON_18)

<br>

## 5. Once you run the code **A NEW FILE** will be generated

<br>

```javascript
project_root/
│
├── files.py
|── files_morenames.py
|── more_names.txt
|── file_operations.log ✋
```

### output on the console

- 🔴 Every time you add something new to the `more_names.txt`, it will appear on your console and it will show the log on the generated  `file_operations.log`

```javascript
Ludovico Sforza

One believes things because one has been conditioned to believe them.

Stability isn’t nearly so spectacular as instability.

Most human beings have an almost infinite capacity for taking things for granted.

When the rich wage war it's the poor who die.

----
```


## 6. THE Log

```javascript
INFO:root:File more_names.txt opened at 2024-07-16 02:58:57.851105
INFO:root:File more_names.txt closed at 2024-07-16 02:58:57.851381


```

<br>
<br>

### 🟡 I want something that logs the additions made to the file. Currently, I have the timestamp; I'm seeking additional data pertaining to these changes.

- the log is showing me the last change i made to the more_names files, but the data is messy, i want it clean and pretty, i know now its possible to structure the data in a json type of format, and indented using PPRINT (for clarity).

<br>
<br>

```python

import logging
import json
#
# time stamp
from datetime import datetime
# to indent the data and make it cleaner
from pprint import pprint

# Configure logging
# the logs will be generated in this file "file_operations.log"
logging.basicConfig(filename='file_operations.log', level=logging.INFO)

# Function to log when the file is opened
def open_file(filename):
    logging.info({'event': 'File opened', 'file': filename, 'timestamp': str(datetime.now())})

# Function to log when the file is closed
def close_file(filename):
    logging.info({'event': 'File closed', 'file': filename, 'timestamp': str(datetime.now())})

# Function to read and print the content of the file, and log each line
def read_file(filename):
    #
    #
    #
    # r for reading the f which is the file containing the data
    try:
        with open(filename, 'r') as f:
            open_file(filename)  # Log file open operation
            lines = []
            for line in f:
                line = line.strip()
                lines.append(line)
                logging.info({'event': 'Read line', 'file': filename, 'line': line, 'timestamp': str(datetime.now())})  # Log each line read
                print(line)  # Print each line (strip to remove newline characters)
            print("----")
            pprint({'event': 'File content', 'file': filename, 'lines': lines})  # Print all lines read in a structured way

            #
            #
            # different scenarios in case the data is not there
    except FileNotFoundError:
        logging.error({'event': 'File not found', 'file': filename, 'timestamp': str(datetime.now())})
        print("The file you want to read doesn't exist")
    except Exception as e:
        logging.error({'event': 'Error reading file', 'file': filename, 'error_message': str(e), 'timestamp': str(datetime.now())})
        print(f"Error reading file: {str(e)}")
    finally:
        close_file(filename)  # Log file close operation
    #
    #
    #
    #

# Example usage
filename = "more_names.txt"
read_file(filename)


```


### The Console result

<br>

```javascript

 python files_morenames.py
Ludovico Sforza

One believes things because one has been conditioned to believe them.

Stability isn’t nearly so spectacular as instability.

Most human beings have an almost infinite capacity for taking things for granted.

When the rich wage war it's the poor who die.

---- ✋ PPRINT
{'event': 'File content',
 'file': 'more_names.txt',
 'lines': ['Ludovico Sforza',
           '',
           'One believes things because one has been conditioned to believe '
           'them.',
           '',
           'Stability isn’t nearly so spectacular as instability.',
           '',
           'Most human beings have an almost infinite capacity for taking '
           'things for granted.',
           '',
           "When the rich wage war it's the poor who die.",
           '']}
```


<br>
<br>


```javascript
project_root/
│
├── files.py
|── files_morenames.py
|── more_names.txt
|── file_operations.log ✋
```


### The Log

```javascript
INFO:root:{'event': 'File opened', 'file': 'more_names.txt', 'timestamp': '2024-07-16 03:19:28.933175'}
INFO:root:{'event': 'Read line', 'file': 'more_names.txt', 'line': 'Ludovico Sforza', 'timestamp': '2024-07-16 03:19:28.933364'}
INFO:root:{'event': 'Read line', 'file': 'more_names.txt', 'line': '', 'timestamp': '2024-07-16 03:19:28.933475'}
INFO:root:{'event': 'Read line', 'file': 'more_names.txt', 'line': 'One believes things because one has been conditioned to believe them.', 'timestamp': '2024-07-16 03:19:28.933554'}
INFO:root:{'event': 'Read line', 'file': 'more_names.txt', 'line': '', 'timestamp': '2024-07-16 03:19:28.933640'}
INFO:root:{'event': 'Read line', 'file': 'more_names.txt', 'line': 'Stability isn’t nearly so spectacular as instability.', 'timestamp': '2024-07-16 03:19:28.933710'}
INFO:root:{'event': 'Read line', 'file': 'more_names.txt', 'line': '', 'timestamp': '2024-07-16 03:19:28.933811'}
INFO:root:{'event': 'Read line', 'file': 'more_names.txt', 'line': 'Most human beings have an almost infinite capacity for taking things for granted.', 'timestamp': '2024-07-16 03:19:28.933895'}
INFO:root:{'event': 'Read line', 'file': 'more_names.txt', 'line': '', 'timestamp': '2024-07-16 03:19:28.933967'}
INFO:root:{'event': 'Read line', 'file': 'more_names.txt', 'line': "When the rich wage war it's the poor who die.", 'timestamp': '2024-07-16 03:19:28.934038'}
INFO:root:{'event': 'Read line', 'file': 'more_names.txt', 'line': '', 'timestamp': '2024-07-16 03:19:28.934105'}
INFO:root:{'event': 'File closed', 'file': 'more_names.txt', 'timestamp': '2024-07-16 03:19:28.934735'}

```

<br>
<br>

---

<br>
<br>

<a name="_APPEND_operation"></a>

## 🟡 APPEND

### Purpose of append() in File Operations

- In Python, when dealing with file operations, the `append()` mode is a specific mode **used when opening a file**.

- When you open a file in append mode (`'a'`), it allows you to **write data** to the **end of the file** without truncating it.



-  This means any existing content in the file remains untouched, and new data is simply added at the end.

```python
# divider
print("_____ 👾 ______")
# ------
# APPEND
# ------
f = open('names.txt', 'a') ## a: append
f.write('David Lee Roth 🥥')
# from the moment you are going to run the code: python files.py , the David Lee Roth is going to be saved and automatically generated in your names.txt (without you having to type anything there)
f.close()

```

### Duplicate the above code and modify a couple of things

```python
# before: f = open('names.txt', 'a')
f = open("names.txt") # here we dont need to add the r, because by default it will READ 'r' it
#
#
# before: f.write('David Lee Roth 🥥')
print(f.read())

f.close()
```