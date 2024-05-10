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
users = ['Dave', 'John', 'Sara']
#
#
print(users[1:]) # it will pick up the item at position 1 and all after that, the reason for that is because arent specifing a second value after the:colons
#
# RESULT
# John and Sara
#
#
# or
print(users[-3:-1])
#result
['Dave', 'John']
```

<br>
<br>

## Length of a list

- check how many items i have

```python
users = ['Dave', 'John', 'Sara']
data = ['Dave', 42, True]
#
#
print(len(data))
print(len(users)) # also contains 3 items
# result
3
```

<br>
<br>

### 🟡 Add a new item to the list

- for that i will use **append**, this append works like **push** in javascript https://www.w3schools.com/jsref/jsref_push.asp

```python
users.append('Elsa')
print(users)
#
# result
# ['Dave', 'John', 'Sara', 'Elsa']
```

#### another wax to do it

```python
users += ['Jason']
print(users)
#
# result
['Dave', 'John', 'Sara', 'Elsa', 'Jason']
```

### but be careful when you use this method, compare the examples

- wrapped on array & only strings

```python
# wrapped on array
users += ['Jason']
print(users)
# result
['Dave', 'John', 'Sara', 'Elsa', 'Jason']
#
#
#
#---
# wrapped on strings
users += 'Jason'
print(users)
# result
'J', 'a', 's', 'o', 'n'
#
#
# like so
['Dave', 'John', 'Sara', 'Elsa', 'Jason', 'J', 'a', 's', 'o', 'n']
```

<br>
<br>

## 🟡 EXTEND

- this also will **push** more items to the list

```python
# original list
users = ['Dave', 'John', 'Sara']
#
#
users.extend(['Robert', 'Jimmy'])
print(users)
#
# result

['Dave', 'John', 'Sara', 'Elsa', 'Robert', 'Jimmy']
```

<br>

### insert another list within a list using EXTEND
