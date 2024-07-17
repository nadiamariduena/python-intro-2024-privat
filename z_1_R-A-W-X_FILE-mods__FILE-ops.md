# 🟡 FILE Operations

<br>

### File operations include methods for reading, writing, managing positions, and handling file closures:


<br>

### open():

- Function to open a file and return a corresponding file object.

#### Takes the file path and mode as arguments.


```python
file = open('example.txt', 'r')
```

<br>

### close():

- Method to close an opened file.

#### Ensures resources associated with the file are freed.


```python
file = open('example.txt', 'r')
file.close()

```
<br>

### `read(size=-1)`:

Method to read and return the entire file content or specified number of bytes (size).


```python
with open('example.txt', 'r') as file:
    content = file.read()
```
<br>

#### Example 3: Handling Large Files in Chunks

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