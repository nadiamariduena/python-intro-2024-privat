## 🟨 [Loops](https://youtu.be/23vCap6iYSs?feature=shared&t=36)

- while loops

- for loops

<br>
<br>

### WHILE loop

- Just like in javascript

- careful with the never ending loop that will crash your browser, so dont **print** the below

```python
value = 1
while value < 10:
    print(value) # :stop_sign: DONT!!!

    #result
    # infinite loop
```

<br>
<br>

### Do this:

- add the `+= 1` its going to increment everytime it goes through the LOOP, until it reaches the 9 (as we are incrementing 1), which is the end point `< 10`

```python
value = 1
while value < 10:
    print(value)
    value += 1
#result
1
2
3
4
5
6
7
8
9
# it doesnt reach the 10, because the conditions tells that "WHILE" its less than 10, if you want to show the 10 you can change the condition from < 10 to <= 10 (less or equal to 10)
```
