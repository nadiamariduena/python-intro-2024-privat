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
#It doesnt reach the 10, because the condition tells that "WHILE" its less than 10. if you want to show the 10, you can change the condition from < 10 to <= 10 (less or equal to 10)
value = 1
while value <= 10:
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
10
```

### Another WAY to break the LOOP

```python
value = 1
while value <= 10:
    print(value)
    if value == 5:
        break #if the condition is met, it will stop the loop at 5
    value += 1
```

<br>
<br>

# ELSE

### 🖐️ USING the else

- You can use it once the loop is completed and the condition is no longer TRUE

```python
while value <= 10:
  value += 1
  if value == 5:
     continue  # If value is 5, the loop skips the remaining code in this iteration and continues to the next iteration
  print(value)
  #
  # ELSE: You can use it once the loop is completed and the condition is no longer TRUE
  #
else:
    print("Value is now equal to " + value) #🧧 You will get an error if you try to print this, so convert the TYPE

```

## 🔴 the error

```python
    print("Value is now equal to " +  value)
          ~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~
TypeError: can only concatenate str (not "int") to str
```

<br>

### 🌈 convert the TYPE to str (string)

```python
else:
    print("Value is now equal to " + str(value))
```

<br>
<br>

---

<br>
<br>

## 🟡 FOR loop (sequence)

<br>

#### chatgpt basict doc about the topic:

<br>

- In Python, a for **loop is used to iterate over a sequence (such as a list, tuple, string, or range) or any other iterable object.**

> The basic syntax of a for loop in Python is:

```python

for item in sequence:
    # do something with item

```

#### The `for` keyword indicates the start of the loop.

- **item** is a variable that will take on the value of each element in the sequence during each iteration of the loop.

**sequence** is the collection of items over which the loop will iterate.

```python

fruits = ["apple", "banana", "cherry"]
#
# fruit will represent the content within the fruits list/ array(js)
for fruit in fruits:
    print(fruit)

```

<br>

### In this example, the for loop iterates over the fruits list.

✋ **During each iteration**, the variable fruit takes on the value of each element in the list ("apple", "banana", and "cherry" in sequence), and it prints each fruit.

You can also use the `range()` function to generate a sequence of numbers:

<br>

```python
for i in range(5):
    print(i)

    # The for loop continues iterating until it has gone through all the elements in the sequence or until a break statement is encountered, which exits the loop prematurely.

# result
# 0
# 1
# 2
# 3
# 4
```

#### The for loop continues iterating until it has gone through all the elements in the sequence or until a break statement is encountered, which exits the loop prematurely.

<br>
<br>

### How can I use the `range()` for a real scenario?

<br>

- Let's imagine you're building a program that simulates a **Spotify** playlist, and you want to display the track numbers along with their titles.

- You can use the range() function to generate track numbers dynamically, especially if your playlist can have a variable number of tracks.
