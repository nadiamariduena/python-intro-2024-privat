## IF ELSE & indentation

```javascript
meaning = 42
print("")


// In javascript you have the curly brackets, here you use colons
if meaning > 10:
   print("Right on!")

```

<br>
<br>

# 🔴 indentation

https://www.askpython.com/python/python-indentation

```javascript
// without indentation
if meaning > 10:
print("Right on!")
// if you add the print() from the beginning of the line, you will notice that the colons will show you an error, and the reason for that is because you are telling it, that the logic ends there and you wont continue
//

//  with identation
//
if meaning > 10:
   print("Right on!")
// here the print() starts after
```

<br>

[<img src="./img/python-indentation.png.webp"/>](https://www.askpython.com/python/python-indentation)

<br>
<br>

```python

meaning = 42
print("")

if meaning > 10:
    print("Right on!")
#if you see a yellow underline , and when hovering it tells you that you are wrongly indentating, launch the server at the top
else:
    print('not today')

```

<br>
<br>

## Ternary operator

```python
meaning = 42
print("")

# if meaning > 10:
#     print("Right on!")
# else:
#     print('not today')

#
print('Right on 🦄!') if meaning > 10 else print("Not today")
```
