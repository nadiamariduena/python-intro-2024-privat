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