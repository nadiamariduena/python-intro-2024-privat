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

## 🟡 Explanation

#### Imagine you have a number and you want to keep adding **1** to it until you reach a certain point. In this case, that point is **9**. Let's look at the code step by step:

### Start with the number 0:

- You call the function add_one(0).

```python
add_one(0)
```

### Check if the number is 9 or more:

- The first thing the function does is check if the number is 9 or more:

```python
if (num >= 9):
    return num + 1

```
