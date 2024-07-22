# 🟡 Concatenation

### Two of the methods I'll use here can more or less be applied in JavaScript and React



```python
# string concatenation (aka how to put strings together)
# # suppose we want to create a string that says "subscribe to ____"
youtuber = "Dorothea Ernst" # some string variable


# # a few ways to do this
print("subscribe to " + youtuber) # ✋ you can use it in JS & react
print("subscribe to {}". format(youtuber))
print(f"subscribe to {youtuber}") # ✋ you can use it in JS & react BUT, you dont use the f"", you will use the template literals: console.log(`subscribe to ${youtuber}`);

#Template literals, introduced in ECMAScript 6 (ES6), provide a powerful way to embed expressions inside strings using ${} placeholders. This is quite similar to Python's f-strings and is now widely used in modern JavaScript and React applications.


#🟧 OUTPUT:
# subscribe to Dorothea Ernst
# subscribe to Dorothea Ernst
# subscribe to Dorothea Ernst
```

<br>
<br>

## 🫐 `.format()`

The **.format()** method as seen in Python **does not exist** as a built-in method in **JavaScript or React*.

>However, various languages and frameworks might have similar functionality or libraries that offer similar capabilities for string formatting and interpolation. Here’s a brief overview across different languages: