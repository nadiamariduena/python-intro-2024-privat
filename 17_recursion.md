# 🍭 Recursion

- read the explanation below the code

```python
# check the explanation on 17 recursion
def add_one(num):
    if (num >= 9):
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)

add_one(0)

#1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
```

<br>

## Explanation
