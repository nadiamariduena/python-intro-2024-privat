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

### 1) Start with the number 0:

- You call the function add_one(0).

```python
add_one(0)
```

### 2) Check if the number is 9 or more:

- The first thing the function does is check if the number is 9 or more:

```python
if (num >= 9):
    return num + 1

```

#### 👾 If the number is 9 or more, the function stops and returns that number plus 1. But since we start with 0, this check is false and we move to the next part.👾

- Let's see what happens step by step:

Step 1: **add_one(0)** adds 1 to 0 (total = 1) and calls add_one(1).

 <br>

Step 2: add_one(1) adds 1 to 1 (total = 2) and calls add_one(2).
Step 3: add_one(2) adds 1 to 2 (total = 3) and calls add_one(3).
Step 4: add_one(3) adds 1 to 3 (total = 4) and calls add_one(4).
Step 5: add_one(4) adds 1 to 4 (total = 5) and calls add_one(5).
Step 6: add_one(5) adds 1 to 5 (total = 6) and calls add_one(6).
Step 7: add_one(6) adds 1 to 6 (total = 7) and calls add_one(7).
Step 8: add_one(7) adds 1 to 7 (total = 8) and calls add_one(8).

<br>

Step 9: **add_one(8)** adds 1 to 8 (total = 9) and calls add_one(9).

<br>
<br>

### 3) Add 1 to the number and print it:

Next, the function adds 1 to the number and prints the new total:

```python

total = num + 1
print(total)
```
