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

my_function()  # Outputs: 10
print(x)  # Error: x is not defined outside the function

```
