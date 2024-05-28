# 📙 Scope

<br>
<br>

### Different type of scopes in Python

- local Scope

- Enclosing Scope (Nonlocal)

- Global Scope

- Built in Scope

<br>
<br>

### Similarities with ReactJS

ReactJS is a JavaScript handles variable scope differently. **However**, some conceptual **similarities** exist (I will add the similarities at the bottom )

<br>
<br>

## LOcal SCOPE

```python

def my_function():
    x = 10  # x is local to my_function
    print(x)

my_function()  #  Outputs: 10
print(x)  # ✋Error: x is not defined outside the function

```

<br>

---

<br>

## Enclosing Scope (Nonlocal):

**Definition:** Variables in the local scope of enclosing functions. Useful in nested functions.

```python
def outer_function():
    x = 5
    def inner_function():
        nonlocal x
        x = 10
        print(x)
    inner_function()  # Outputs: 10
    print(x)  # Outputs: 10 (modified by inner_function)✋

outer_function()

```

- 🔴 🔴 **nonlocal** `nonlocal x` tells Python that inner_function intends to modify the x variable defined in outer_function's scope. Without nonlocal, inner_function would create a new local variable x within its own scope.

<br>

---

<br>
