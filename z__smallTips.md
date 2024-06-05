## INdentation

- to move a piece of code use the **tab key** to indent the code

- to reverse the indentation use **Shift+Tab**

https://www.computerhope.com/jargon/s/shift-tab.htm#:~:text=Shift%2BTab%20is%20a%20keyboard,line%20in%20most%20text%20editors.

<br>

other

https://defkey.com/what-means/shift-tab

<br>
<br>

### If you have many of this `print("")` on your code, you can remove all of them depending on the situation

- If you remove them add this `\n`

```python
#  print("")
   print("\nYou choose " + str(RPS(player)).
```

<br>

## DEF

- to start with a function you will use the **def** that stands for **defining**

```python
def hello():
   print('Hello World')
#
#
# just like in js, you call the function like here below: name + parentheses
hello()
```

## NONE

- IN python **none** is neither true or false

<br>

---

<br>

### 🍭 `__name__ == "__main__"`

- in other words this code, will check if i am importing it in another component, or if i am running the code from the same component, in this case will be the **modules_3_kansas.py**

```python

if __name__ == "__main__":
    randomfunfact3()
```

#### chatgpt

- The if `__name__ == "__main__"`: block at the end of a Python script is a common idiom used to control whether the script should be executed when it's run directly or when it's imported as a module into another script.

#### 🔴 Here's what it does:

`__name__` is a special variable in Python that holds the name of the current module. If the script is being run directly (i.e., it's the main program), Python sets `__name__` to "`__main__`".
When the script is imported as a module into another script, `__name__` is set to the name of the script.

<br>

In the example you provided, the randomfunfact3() function is defined, and then the script checks if it's being run directly (**name** == "**main**"). If so, it calls the randomfunfact3() function, printing a random fun fact about Kansas. If the script were imported into another Python script, the randomfunfact3() function would still be available for use, but the code inside the if **name** == "**main**": block would not be executed unless explicitly called.

<br>
<br>

% is the modulo operator, not a percentage calculation. The % operator returns the remainder of the division operation. So, x % 2 returns 0 if x is even (because it's divisible by 2 with no remainder), and it returns a non-zero value if x is odd.

For example:

4 % 2 equals 0 because 4 is evenly divisible by 2.
5 % 2 equals 1 because 5 divided by 2 leaves a remainder of 1.
So, x % 2 == 0 checks if x is divisible by 2 with no remainder, which is true for even numbers.
