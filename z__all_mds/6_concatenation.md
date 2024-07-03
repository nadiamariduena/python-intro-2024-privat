## 🟡 CONCATENATION

- Basic concatenation

- Number to string concatenation

<br>
<br>

---

<br>

#### Basic concatenation

```python
first = 'Laure'
last = "Blaz"

fullname = first + " " + last
print(fullname)
#
#result
#its like in js, it concatenate the 2 variables into 1
Laure Blaz
```

### in addition

```python
first = 'Laure'
last = "Blaz"
##its like in js, it concatenate the 2 variables into 1
fullname = first + " " + last
print(fullname)
# ✋ in addition you can also add this below, it will add the exclamation to the full name
fullname += "!"
print(fullname)
```

<br>
<br>

## Number to String

- I need to convert the number to a string to concatenate it to the fullname

```python
#🟥 number to string
#I need to convert the number to a string to concatenate it to the fullname

decade = str(1982)
print(type(decade))
print(decade)
```

### like so

```python
first = 'Laure'
last = "Blaz"
##its like in js, it concatenate the 2 variables into 1
fullname = first + " " + last
print(fullname)
# in addition you can also add this below, it will add the exclamation to the full name
fullname += "!"
print(fullname)

#🟥 number to string
#I need to convert the number to a string to concatenate it to the fullname

decade = str(1982)
# assigning the type
print(type(decade))
print(decade)
```

#### result

```python
Laure Blaz
Laure Blaz!
<class 'str'>
1982
```

<br>
<br>

### Another example

```python
## Another example
# add another variable that will contain the previous information
statement = 'I like rock music ' + decade + 's.'
print(statement)

# result
I like rock music 1982s.
```

<br>

### like so

```python
first = 'Laure'
last = "Blaz"
##its like in js, it concatenate the 2 variables into 1
fullname = first + " " + last
print(fullname)
# in addition you can also add this below, it will add the exclamation to the full name
fullname += "!"
print(fullname)

#🟥 number to string
#I need to convert the number to a string to concatenate it to the fullname

decade = str(1982)
print(type(decade))
print(decade)

## Another example
# add another variable that will contain the previous information
statement = 'I like rock music ' + decade + 's.'
print(statement)
#
#
Laure Blaz
Laure Blaz!
<class 'str'>
1982
I like rock music 1982s.
```
