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

# subscribe to Dorothea Ernst
# subscribe to Dorothea Ernst
# subscribe to Dorothea Ernst
```