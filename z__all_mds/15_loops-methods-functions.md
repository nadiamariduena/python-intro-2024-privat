## 🟡 LOOPS methods and functions

### Iterating over a list directly:

```python
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)
    #result
    # 1, 2, 3, 4, 5
```

<br>
<br>

### Iterating over a tuple:

```python
my_tuple = (1, 2, 3, 4, 5)
for item in my_tuple:
    print(item)
#result
# 1, 2, 3, 4, 5
```

### Iterating over a set:

```python
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)

```

### Iterating over a dictionary (keys):

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key)
#result:  a b c
```

### Using enumerate() to iterate over a sequence with indices:

```python
my_list = ['a', 'b', 'c', 'd', 'e']
for index, item in enumerate(my_list):
    print(index, item)
#result
0 a
1 b
2 c
3 d
4 e
```

### Using zip() to iterate over multiple sequences simultaneously:

```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for item1, item2 in zip(list1, list2):
    print(item1, item2)
#result
#1 a
# 2 b
# 3 c
#
#
# ✋ ZIP
# Lists of songs and corresponding artists
songs = ['Song 1', 'Song 2', 'Song 3']
artists = ['Artist A', 'Artist B', 'Artist C']

# Using zip to iterate over both lists simultaneously
for song, artist in zip(songs, artists):
    print(f"{song} by {artist}")
# result
Song 1 by Artist A
Song 2 by Artist B
Song 3 by Artist C

```

## 👾 is zip used a lot?

<br>

### ChatGPT:

Yes, zip is a commonly used function in Python, especially when working with multiple lists or sequences simultaneously. It's a versatile tool that allows you to iterate over multiple iterables in parallel, making it useful for a variety of tasks such as:

Pairing corresponding elements from multiple lists for processing.
Combining data from different sources for analysis or visualization.
Generating combinations or permutations of elements from multiple iterables.
Simplifying code by avoiding nested loops when dealing with multiple sequences.
Overall, zip provides a convenient way to work with data that is organized into multiple related sequences.
