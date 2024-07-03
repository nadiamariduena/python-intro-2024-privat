## 🟧 indentation issues

<br>
<br>

### Read more about identation

https://www.askpython.com/python/python-indentation

<br>

# the issue

- when learning about the loops in python [loops](./15_loops.md) i couldn't get the same result the teacher was getting.

```python
#this code had the identation issues
# LOOP over the list and check if there is a specific name

thenames = ["Dave", "Sara", "John"]

for px in thenames:

    if px == 'Sara':
      continue
print(px)
# result: charless

#
#
# 👍 good
# notice the position of the  print(px)
thenames = ["Dave", "Sara", "John"]

for px in thenames:
    if px == 'Sara':
        continue
    print(px)
#
# result
Dave
John

```

# 🌈 reason

The issue you're encountering is due to indentation. Currently, **print(px) is outside of the loop**, so it only executes after the loop has finished iterating through all the elements in thenames. To print both the first and last elements, you need to adjust the indentation of the print(px) statement so it's inside the loop.

<br>
<br>

## 🔴 Indentation issues on loops

- ⚠️ Wrong

- 🌈 **REASON** the print statement is outside the loop. Thus, ✋ **it only prints the last person's information** because the variables name, age, and height are being overwritten in each iteration of the loop. To print all the people's information, you need to include the print statement inside the loop, like this:

```python
# list of "people" with their name, age, and height
# 1)
people = [
    # the 165.5 will be rounded
    {"name": "Alice", "age": 30, "height": 165.5},
    {"name": "Bob", "age": 25, "height": 180.0},
    {"name": "Charlie", "age": 35, "height": 175.2}
]

#
# 2) LOOP
# Loop through each person in the list
for person in people:
    # extract variables from the dictionary
    name = person["name"]
    age = person["age"]
    height = person["height"]



#
# 3) Format the string using f-string with formatting options
#
message_e = f"Name: {name}, Age:{age}, Height: {height:.2f} cm"
#🔴 In the context of the format specifier {:.2f}, the f indicates that the variable should be formatted as a floating-point number.

print(message_e)
#
#
#
# result
# Name: Charlie, Age:35, Height: 175.20 cm
```

# Corrected

```python

#----------
# LOOP
#----------
#
#
# list of "people" with their name, age, and height
# 1)
people = [
    # the 165.5 will be rounded
    {"name": "Alice", "age": 30, "height": 165.5},
    {"name": "Bob", "age": 25, "height": 180.0},
    {"name": "Charlie", "age": 35, "height": 175.2}
]

#
# 2) LOOP
# Loop through each person in the list
for person in people:
    # extract variables from the dictionary
    name = person["name"]
    age = person["age"]
    height = person["height"]



    #
    # 3) Format the string using f-string with formatting options
    #
    message_e = f"Name: {name}, Age:{age}, Height: {height:.2f} cm"
    #🔴 In the context of the format specifier {:.2f}, the f indicates that the variable should be formatted as a floating-point number.

    print(message_e)
#
# RESULT
# Name: Alice, Age:30, Height: 165.50 cm
# Name: Bob, Age:25, Height: 180.00 cm
# Name: Charlie, Age:35, Height: 175.20 cm
```
