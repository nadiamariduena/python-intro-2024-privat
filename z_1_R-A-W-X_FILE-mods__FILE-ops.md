# 🟡 FILE Operations & File Modes

<br>

### File operations include methods for reading, writing, managing positions, and handling file closures:


<br>
<br>

## 🟦 FILE Operations

### 🟠 open():

- Function to open a file and return a corresponding file object.

#### Takes the file path and mode as arguments.


```python
file = open('example.txt', 'r')
```

<br>
<br>

### 🟠  close():

- Method to close an opened file.

#### Ensures resources associated with the file are freed.


```python
file = open('example.txt', 'r')
file.close()

```

<br>



## 🟨 OPEN & CLOSE

- difference between option A and option B

```python
# A
# notice this: f = open
f = open('context.txt', 'w')
f.write('i deleted all of the context.txt content')
f.close() # 🔴 Failure to close the file properly can lead to issues like resource leaks or data not being fully written to the file in certain circumstances.

#
# B
# 🔴 You use a with statement, which automatically handles opening and closing the file.

with open('context.txt', 'w') as f:
f.write('Hello, world!\n')
# 🔴 No need to explicitly close() the file
# When the with block is exited (either normally or due to an exception), Python ensures that the file is properly closed.

```

<br>
<br>

---


<br>
<br>

### 🟠  `read(size=-1)`:

Method to read and return the entire file content or specified number of bytes (size).


```python
with open('example.txt', 'r') as file:
    content = file.read()
```
<br>

#### 🟤 Example 3: Handling Large Files in Chunks

- For larger files, reading in chunks is more efficient. Let's assume large_file.txt contains large amounts of data.

##### Here's how you can read and print it in chunks of 1024 bytes:

```python
# Open the large file in read mode
with open('large_file.txt', 'r') as file:
    while True:
        # Read 1024 bytes from the file
        chunk = file.read(1024)
        if not chunk:
            break
        # Print the chunk or process it
        print(chunk)
#
#
# OUTPUT
#Contents of large_file.txt printed in chunks of 1024 bytes.

```

<br>
<br>

### 🟠  write(string):

- Method to write a string to a file.


#### Returns the number of characters written.

Example

```python
with open('output.txt', 'w') as file:
    file.write('Hello, world!\n')

```

<br>
<br>

### 🟠 readline():

🔸 This line reads one line from the file object file and stores it in the variable line.

```python

with open('example.txt', 'r') as file:
    line = file.readline()
#
# output: # context, it will remove the rest

```
<br>

🔸 The **readline()** method reads characters from the file until it reaches a newline character ('**\n**') or the end of the file. It returns the line as a string including the newline character at the end, unless the end of the file has been reached.


<br>
<br>

### 🟠 readlines():

Method to **read all lines** from the file and return them as a list.

```python

# print all lines
with open('context.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

# output:
# ['# context\n', 'Rainbow\n', 'Horse\n', 'Zebra\n', 'Zonkey\n', 'Donkey']
```

<br>

### 🟠  SEEK() method

#### Method to move the file pointer to a specific position.

```python
with open('example.txt', 'r') as file:
    file.seek(10)  # Move to the 10th byte, you will see the table at the bottom
    content = file.read()
```

<br>

#### 👾 [READ MORE / Byte](./z_2_R-A-W-X_FILE-mods__BYTE.md)

<br>
<br>



<br>

## 🟦 FILE Modes

<br>


###  🔶  Read Mode (`'r'`) - Default mode.

Purpose: Opens a file for reading. Raises an error if the file does not exist.


```python
# - opt 1
file = open('menu.txt', 'r')
# You can use the "r" to specify that you want to read the menu.txt, but you can also remove, it will read it anyway
# or  opt 2
file = open('menu.txt', 'r')
# In this case its okay because the menu.txt is a txt but if you have a binary file, then you have to specify the "rb

```

<br>

###  🔶  Write Mode ('w')

Purpose: Opens a file for writing. Creates a new file or truncates an existing file.


```python
file = open('orders.txt', 'w')

```

<br>


###  🔶 Append Mode ('a')

Purpose: Opens a file for appending. Creates a new file if it does not exist.


```python
file = open('orders.txt', 'a')

```

<br>

###  🔶 Binary Mode ('b')

Purpose: Opens a file in binary mode for operations on binary files.


```python

file = open('data.bin', 'rb')

```

<br>

### 🍨 `rb` for images, audio files, or any non-textual data

- This mode is specifically used when **dealing with files that contain binary data**, such as images, audio files, or any non-textual data.

>**It ensures that data is read in its exact binary representation** without any text encoding conversions, which is crucial for maintaining data integrity when handling such files.

```python
image_file = open("ice_cream_img.jpg", "rb") # rb md for "reading binary"
image_data = image_file.read()
image_file.close()
```




<br>


###  🔶 Read and Write Mode ('r+' or 'w+')

Purpose: Opens a file for both reading and writing.


```python
# 'r+' Mode (Read and Write)
file = open('menu.txt', 'r+')

```

<br>

###  🔶 Exclusive Creation Mode ('x')

Purpose: Opens a file exclusively for writing. Raises an error if the file already exists.

```python
file = open('newfile.txt', 'x')

```

<br>

🍍 **'r+'**: Allows both reading and writing without truncating the file. Raises an error if the file does not exist.

🍍 **'w+'**: Allows both reading and writing, truncates the file if it exists or creates a new file if it doesn't.



<br>
<br>

###  🔶  Text Mode ('t') - Default mode in Python 3.x (optional).

Purpose: Opens a file in text mode (default). This is usually implied and not explicitly used.


 ```python
file = open('menu.txt', 'rt')
 ```


<br>


###  🔶  Exclusive Creation Mode ('x')

Purpose: Opens a file exclusively for writing. Raises an error if the file already exists.

```python
file = open('newfile.txt', 'x')

```
<br>
<br>
<br>
<br>


---

<br>
<br>


### 🟡 Some examples of file input and output (I/O) in Python using Spotify as a hypothetical example.

- We'll start with basic operations and gradually move towards more advanced scenarios.

<br>
<br>

#### 1. Basic FILE "r" READING & WRITING


- create a file and call it "tracks.txt" , then add this:

```bash
#tracks.txt
track_1: TEMPLEOFJOY 110 - IMMINENT
track_2: Kai Pattenberg - Obvilion

```

- example 1: reading from a file

```python
# import the tracks.txt
filename = "tracks_exe_0_.txt"

#open file in read mode
with open(filename, "r") as file:
    for line in file:
        # will show the content of the tracks.txt in your console
        print(line.strip())
```

- run the code, type the name of the file your code is, in my case it is: `tracks_exe_0/tracks_exe_0.py` , dont forget to **cd** into the folder (if you are in one)

#### output

```python
track_1: TEMPLEOFJOY 110 - IMMINENT
track_2: Kai Pattenberg - Obvilion
```