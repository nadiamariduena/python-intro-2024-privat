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
