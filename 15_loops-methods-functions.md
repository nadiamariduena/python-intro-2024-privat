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
