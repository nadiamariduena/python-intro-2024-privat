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

```python
data = ['Dave', 42, True]
#
users = ['Dave', 'John', 'Sara', 'Elsa', 'Robert', 'Jimmy']
#
#
# here i m inserting the data list within the user list
users.extend(data)
print(users)
#
# result
['Dave', 'John', 'Sara', 'Elsa', 'Jason', 'J', 'a', 's', 'o', 'n', 'Robert', 'Jimmy', 'Dave', 42, True]
```

<br>
<br>

## 🟡 insert item to a certain position, here below i want to insert "Bob" at position 0 which is the beginning

```python

users.insert(0, "Bob")
print(users)
#result
['Bob', 'Dave', 'John', 'Sara', 'Elsa', 'Jason', 'J', 'a', 's', 'o', 'n', 'Robert', 'Jimmy']
```

<br>

### Insert 2 values to an specific position

- I will add 2 new names to the second position

```python
users[2:2] = ["Eddie", "Alex"]
print(users)
#result
# ['Bob', 'Dave', 'Eddie', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'J', 'a', 's', 'o', 'n', 'Robert', 'Jimmy']
```

<br>

### replacing names at specific positions (similar to [SLICE in javascript](https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_slice_array))

```python
#it will replace the position 1 which is the second and then it will stop at pos 3 which is alex
users[1:3] = ['robert', 'JPJ']
print(users)
#RESULT
['Bob', 'robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'J', 'a', 's', 'o', 'n', 'Robert', 'Jimmy']
```

<br>
<br>

## REMOVE

- remove items from the list

```python
users.remove("Bob")
print(users)
#
# result
['robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'J', 'a', 's', 'o', 'n', 'Robert', 'Jimmy']
```

<br>
<br>

## [POP ](https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_pop)

- just like in JS **pop** will remove the last of the list

```python
print(users.pop())

# result
#['robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'J', 'a', 's', 'o', 'n', 'Robert', 'Jimmy']
# Jimmy # ✋ as you can see jimmy has been removed from the list and is now out
# print(users)
```

<br>
<br>

# DEL

#### i will delete the first item of the list

```python
del users[0]
print(users)
#result: robert has been deleted from the list ['JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'J', 'a', 's', 'o', 'n', 'Robert']
```

### deleting a list

```python
del data
print(data)
#
#result
```
