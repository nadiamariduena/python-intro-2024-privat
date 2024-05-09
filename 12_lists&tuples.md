## IN the following code i will check if 'Dave' is found within the users, data or emptyList, then i will run the code and see the type of bool i will get

```python
users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptyList = []

print("Dave" in data) #  True
#print("Dave" in users) # True
#print("Dave" in emptyList) #True
```

## Get an specific item from a LIST

```python
users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptyList = []

#----------
print("Dave" in data)
# get an element from a list
print(users[0])
print(users[-1]) # will get the last item
print(users[-2]) # will get the penultimo/second-last
#
# RESULT
True
Dave
Sara
John
```

## 🍨 Now find the Position INDEX of an item within a LIST

```python
users = ['Dave', 'John', 'Sara']

print(users.index('Sara'))
#result
2 # position 2 on the list
```

<br>
<br>

### Now get the length

- here we will get the first 2 items of the list

```python
users = ['Dave', 'John', 'Sara']

print(users[0:2])
#
#result
Dave
John
```

<br>
<br>

## Pick up the item at position 1 and all after that

```python
print(users[1:]) # it will pick up the item at position 1 and all after that, the reason for that is because arent specifing a second value after the:colons
```
