## indentation issues

- when learning about the loops in python [loops](./15_loops.md) i couldnt get the same result the teacher was getting.

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
