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

- first i will show you how to delete the entire list, then i will show you to only **clear** the list without deleting it all

```python
# --- del a lst
del data
print(data)
# it will tell you the following because the list no longer exists
# line 102, in <module>
#     print(data)
#           ^^^^
# NameError: name 'data' is not defined
```

### deleting a list

- clear the content of the list

```python
data = ['Dave', 42, True]
# --- del a lst
# del data
data.clear()
print(data)
#
# result
['Dave', 42, True]
[]
```

<br>
<br>

## 🟡[SORT ](https://www.w3schools.com/js/tryit.asp?filename=tryjs_array_sort)

- just like in javascript The **sort()** method sorts an array alphabetically:

```python
users.sort()
print(users)
# result
#['Alex', 'Elsa', 'J', 'JPJ', 'Jason', 'John', 'Robert', 'Sara', 'a', 'n', 'o', 's']
```

<br>
<br>

## Lowercase

```python

users.sort(key=str.lower)
print(users)
#result
```

<br>
<br>

## 🟧 REVERSE (Numbers)

```python

# -- numbers
nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)
# result: [5, 1, 78, 42, 4]
```

#

#

#

# reverse it again

```python
nums.sort(reverse=True)
print(nums)
# result: as you can noticem the its the biggest showing first and so on [78, 42, 5, 4, 1]
```

# bring it back to the original list

- hide the previous test

```python
#hide this:
# nums.sort(reverse=True)
# print(nums)
# result: as you can noticem the its the biggest showing first and so on [78, 42, 5, 4, 1]
#
nums = [4, 42, 78, 1,5]
#
print(sorted(nums, reverse=True))
print(nums)
#result
```

<br>
<br>

## List copies

```python
nums = [4, 42, 78, 1,5]
#
print(sorted(nums, reverse=True))
print(nums)
#result
#[78, 42, 5, 4, 1]
# [4, 42, 78, 1, 5]
print(".----.")
#
# --- list copies

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
print(mycopy)
print(nums)
```
