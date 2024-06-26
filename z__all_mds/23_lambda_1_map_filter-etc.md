## Python lambda, map, filter, & reduce - Higher Order Functions for Beginners

https://youtu.be/YIOYJgLQYiY?feature=shared

<br>

- to test any example, **CD** into the folder you have stored the **py** file , for example, i have my py file within a folder called **LESSON_13_lambda_map_etc**, so if i want to test my examples, i need to cd on that folder and then type this:

```javascript
python3 lambda_and_other_functions.py
```

<br>
<br>

### 🍭 Lambda

- [LAMBDA functions](https://youtu.be/KR22jigJLok?feature=shared)

##### chatgpt

- Lambda typically refers to the lambda function in Python, which is a small anonymous function defined using the lambda keyword. Lambda functions can take any number of arguments, but can only have one expression.

```python
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8
# 3 +5 = 8
```

<br>

### 🍭 In Python, a lambda function is a way to create small, anonymous functions. They are similar to regular functions defined using the def keyword, but with a few key differences:

<br>

- **Anonymous:** Lambda functions are anonymous, meaning they don't have a name like regular functions do. They are defined using the lambda keyword followed by parameters and an expression.

```python
# Anonymous lambda function to calculate the square of a number
square = lambda x: x**2
print(square(5))  # Output: 25
#
#
# ✋ another example
# a) we cannot do this
lambda num : num * num
# b) we can assign the lambda anony function to a variable, in this case will be 'squared'
squared = (lambda num : num * num)
```

## 🔴 Reformating issue

```python
#🖐️ here you have to be careful, if you dont add parenthesis to the lambda like here (lambda num : num * num), it will reformat it, and you wont get the result 4
squared = (lambda num1 : num1 * num1)
print(squared(2))
#result: 4 // num + num or 2 + 2 = 4
# the reformat happens in line 8, when typing (squared(2))
```

### this is what you get if ou dont add the parenthesis

```python
def squared(num): return num + num
print(squared(2))
#result
#4 // num + num or 2 + 2 = 4
```

<br>

#### another anonym function

```python
# ------- another example
def addTwo(num): return num + 2

print(addTwo(12))
#result
# 14
```

<br>
<br>

**Small:** Lambda functions are typically used for small tasks and simple operations. They are often used where a function is needed for a short period of time and creating a named function would be overkill.

```python
# Using lambda function to add two numbers
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

```

<br>

**Expression-based:** Lambda functions can only contain a single expression. This means they are limited in what they can do compared to regular functions, which can contain multiple statements and have more complex logic.

```python
# Using lambda function to check if a number is even
is_even = lambda x: x % 2 == 0
print(is_even(4))  # Output: True
# Examples of odd numbers are 3, 5, 7, 9, 11, 13, 15,…
# Examples of even numbers are 2, 4, 6, 8, 10, 12, 14,…
```

#### another function expression

```python
def sum(a, b): return a + b
print(sum(2, 2))
```

<br>

---

<br>

#### Lambda functions are often used in Python in situations where a function is required as an argument to higher-order functions (functions that take other functions as arguments), such as `map()`, `filter()`, and `sorted()`.

They are a convenient way to define simple functions inline without the need for a full function definition.

<br>
<br>

## ALSO:

-In mathematics, lambda (λ) often denotes a parameter or variable in functions or calculus.

- ✋ In computer science and distributed systems, ["Lambda"](https://aws.amazon.com/pm/lambda/?gclid=Cj0KCQjwsPCyBhD4ARIsAPaaRf3S1nW6pAbjQs9UkM1QB0OQYXuuzn5CBnmUqHWFRJDXD2KDAMC5msYaAvVVEALw_wcB&trk=c8019b8a-d2f2-4ec8-ac50-7bdc0dbe1996&sc_channel=ps&ef_id=Cj0KCQjwsPCyBhD4ARIsAPaaRf3S1nW6pAbjQs9UkM1QB0OQYXuuzn5CBnmUqHWFRJDXD2KDAMC5msYaAvVVEALw_wcB:G:s&s_kwcid=AL!4422!3!651612391322!e!!g!!lambda%20aws!19828205892!147081379877) can refer to AWS Lambda, which is a serverless computing service provided by Amazon Web Services.

- courses [AWS Lambda y Python | Guía PRÁCTICA aprende con un EXPERTO](https://www.udemy.com/course/aws-lambda-y-python-el-futuro-es-serverless/?utm_source=adwords&utm_medium=udemyads&utm_campaign=DSA-WebIndex_la.ES_cc.LATAM&campaigntype=Search&portfolio=LATAM&language=ES&product=Course&test=&audience=DSA&topic=&priority=&utm_content=deal4584&utm_term=_._ag_120316893258_._ad_504879908808_._kw__._de_c_._dm__._pl__._ti_dsa-93451758763_._li_9077251_._pd__._&matchtype=&gad_source=1&gclid=Cj0KCQjwsPCyBhD4ARIsAPaaRf1aMPZkWxqBwRmqiRF6xZCnNpGTxjewd0wr389S8o2rJFYA7buTV-kaAtISEALw_wcB)

[Intro to AWS Lambda with Python | AWS Lambda Python Tutorial](https://www.youtube.com/watch?v=-8L4OxotXlE)

<br>
<br>

- In functional programming languages like Lisp, lambda denotes an anonymous function.

<br>
<br>

---

<br>

# ADDITION > Concatenation

- First check this example below, then in the second example you will see another way of doing it (with concatenation) and why you have to add **str**

```python
# ✋ example 1)
# notice what is happening here
def funcBuilder(x):
    return lambda num: num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

# result
#17
# 27

```

The **funcBuilder** function returns a lambda function that takes a parameter num and adds it to x, which is provided when calling funcBuilder. This pattern is known as closure, where the returned function retains access to the variables in the scope where it was defined.

In this case, **addTen** and addTwenty are both functions created by calling funcBuilder with different values for `x`. They are essentially functions that add **10 and 20** respectively to whatever number is passed to them.

So, the type of function being created here is a closure, specifically a closure that adds a specified **number** `(x)` to another number **(num)**.

<br>
<br>

# 🍭 Concatenation

- Regarding concatenation instead of addition, if you want the function to concatenate instead of adding numbers, you would need to modify the lambda function returned by funcBuilder to perform string concatenation instead of addition. Here's how you can do it:

## ✋ example 2

```python
def funcBuilder(x):
    # specify the str
    return lambda num: str(num) + str(x)

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))      # Output: '710'
print(addTwenty(7))   # Output: '720'

```

#### my question:

- Is it similar to JavaScript, where errors can sometimes occur due to omitting the quotation marks `""`, in the way that mixing data types in Python without specifying the appropriate conversions may lead to errors?"

#### chatgpt answer:

- 🔴 Yes, in a way, it's similar to JavaScript in that context. In JavaScript, if you try to add a number to a string without explicitly converting one of them, it will perform type coercion, resulting in concatenation. Similarly, in Python, if you try to add a string and a number, it will raise a TypeError.

#### javascript error example

```javascript
// WITH ERROR
for (let i = 1; i <= 5; i++) {
  console.log("Number " + i); // Error: Implicit conversion of number to string
}
// #Explanation: In this example, the number i is implicitly converted into a string when concatenated with the string "Number ", which may lead to unexpected behavior if arithmetic addition was intended.
//
//  ----------
//
// WITHOUT err
for (let i = 1; i <= 5; i++) {
  console.log("Number " + i.toString()); // Outputs: "Number 1", "Number 2", ..., "Number 5"
}
// Explanation: To avoid the error, explicitly convert the number i to a string using the toString() method before concatenation.
```

#### python error example

```python
for i in range(1, 6):
    print("Number " + i)  # Error: TypeError: can only concatenate str (not "int") to str
    #
#Explanation: In this example, the integer i is attempted to be concatenated with the string "Number ", causing a TypeError due to the attempt to concatenate incompatible types.
#
#
# --------
# without error
#
for i in range(1, 6):
    print("Number " + str(i))  # Outputs: "Number 1", "Number 2", ..., "Number 5"
    #
    #
# Explanation: To avoid the error, explicitly convert the integer i to a string using the str() function before concatenation.
```

<br>
<br>

## Spotify example

```python
# ---------- read the '23_lambda_1_etc.md'

def playlistBuilder(songs):
    #
    #
    return lambda playlist_name: f"Adding songs to {playlist_name} playlist: {', '.join(songs)}"

# List of songs for the "Chill Vibes" playlist
chill_vibes_songs = ["Song 1", "Song 2", "Song 3"]
# List of songs for the "Summer Hits" playlist
summer_hits_songs = ["Song A", "Song B", "Song C"]


# Here you are assigning the value of chill_vibes_songs to addChillVibesSongs, then the addChillVibesSongs will be appending a new song "Song 4"
# Look ath the scope of the playlistBuilder
addChillVibesSongs = playlistBuilder(chill_vibes_songs)
addSummerHitsSongs = playlistBuilder(summer_hits_songs)

# Add a new song to the "Chill Vibes" playlist
chill_vibes_songs.append("Song 4")

print(addChillVibesSongs("Chill Vibessss"))
print(addSummerHitsSongs("Summer Hits"))


```

<br>
<br>

### explanation

**QUESTION:**

- so all the below is out of the **scope** of the playlistBuilder, that is why i can use the playlistBuilder when assigning the value to the addChillVibesSongs and eventually appending a new song ?

```python
# List of songs for the "Chill Vibes" playlist
chill_vibes_songs = ["Song 1", "Song 2", "Song 3"]
# List of songs for the "Summer Hits" playlist
summer_hits_songs = ["Song A", "Song B", "Song C"]

addChillVibesSongs = playlistBuilder(chill_vibes_songs)
addSummerHitsSongs = playlistBuilder(summer_hits_songs)

# Add a new song to the "Chill Vibes" playlist
chill_vibes_songs.append("Song 4")

print(addChillVibesSongs("Chill Vibes"))
print(addSummerHitsSongs("Summer Hits"))
```

<br>

#### chatgpt:

- Yes, you've got it. The creation and modification of the chill_vibes_songs and summer_hits_songs lists are indeed outside the scope of the playlistBuilder function.

The **playlistBuilder** function itself doesn't interact with these lists directly. It simply takes a list of **songs** (`def playlistBuilder(songs):`) as an argument and returns a lambda function that generates a message indicating the songs being added to a playlist.

So, you can use playlistBuilder to create functions like addChillVibesSongs and addSummerHitsSongs and then manipulate the lists independently. In your example, chill_vibes_songs.append("Song 4") is entirely separate from the playlistBuilder function and has no impact on the function addChillVibesSongs.

<br>
<br>

# 🍭 FILTER & MAP

```python
# SPOTIFY map example

# We want to filter out songs that are shorter than 200 seconds
# Let's assume we have a list of tuples where each tuple represents a song in the format (song_name, duration_in_seconds)
playlist = [("Song 1", 180), ("Song 2", 240), ("Song 3", 200), ("Song 4", 300), ("Song 5", 150)]


# 🖐️ We want to filter out songs that are shorter than 200 seconds
filtered_playlist = list(filter(lambda song: song[1] >= 200, playlist))


print("Filtered Playlist:")
print(filtered_playlist)

# 🤚 Now, let's say we want to convert the duration of the remaining songs from seconds to minutes
# We can use map and a lambda function to achieve this
converted_playlist = list(map(lambda song: (song[0], song[1] // 60), filtered_playlist))

print("\nConverted Playlist (in minutes):")
print(converted_playlist)
```

<br>
<br>

# MAP

```python
strings = [ "apple", "banana", "cherry", "date", "elderberry"]

reversed_strings = list(map(lambda s: s[::-1], strings))
#[::-1] is a slicing notation used to reverse a sequence (string, list, tuple, etc.).

print(reversed_strings)
#RESULT

#['elppa', 'ananab', 'yrrehc', 'etad', 'yrrebredle']
```

<br>

### explanation:

- `[::-1]` is a slicing notation used to reverse a sequence (string, list, tuple, etc.).

- The first colon `:` indicates the **start** of the slicing operation.

- The second colon `:` indicates the **end** of the slicing operation. If not specified, it defaults to the beginning or end of the sequence.

- The `-1` indicates the step size, which in this case is `-1`, meaning it reverses the sequence.

### more:

```python
# ✋ Positive step size ([::1]):
sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
positive_step = sequence[::1]
print(positive_step)
#result
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# - - With a positive step size (1), the sequence is traversed from left to right, selecting every element.
# - - So, sequence[::1] returns the original sequence as it selects every element in the original order.
#--------
#
#
# ✋ Negative step size ([::-1]):

sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
negative_step = sequence[::-1]
print(negative_step)
# result:
#[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# -- With a negative step size (-1), the sequence is traversed from right to left, selecting every element in reverse order.
#
# - - So, sequence[::-1] returns the reversed sequence, selecting each element from the end to the beginning.
```

<br>
<br>

#### 🌈 So, `[::-1]` essentially means

- **"start from the end, go to the beginning, stepping backwards by one element,"** resulting in the reversal of the sequence.

### result

```python
 ['elppa', 'ananab', 'yrrehc', 'etad', 'yrrebredle']
```

<br>
<br>

---

<br>

## 🟠 REDUCE

```python

# ** REDUCE
#reduce: reduce() is a function from the functools module in Python. It applies a function of two arguments cumulatively to the items of an iterable (such as a list), from left to right, so as to reduce the iterable to a single value.
#
#
#

# ** 1)--- sum up the list
#---------------------------
from functools import reduce
#----------------------------
# accumulator
# current
numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr: acc + curr, numbers)

print(total)

# result
# 16
# it s doing an addition of 1 + 2 + 3 + 4 + 5 +1
# THE BELOW is the equivalent but without the rreduce
def sum_total(a,b): return  a + b
print(sum_total(10,19))
#result
#29
```

<br>
<br>

```python

numbers_0 = [2, 4,6, 6]

# Using lambda function to sum up the values of the list

sum_0 = reduce(lambda x, y: x + y, numbers_0)

print("Sum of numbers", sum_0)

# result
#Sum of numbers 18
```

<br><br>

```python

# ** 2)--- Finding the maximum number in a list using reduce and a lambda function:

numbers_2 = [10, 20, 5]

# Using lambda function to find the maximum number
#lambda x, y: x if x > y else y: This is a lambda function that takes two arguments, x and y, representing two elements from the list numbers. It compares these two elements and returns the greater one.
max_number = reduce(lambda x, y: x if x > y else y, numbers_2)
#If x is greater than y, it returns x.
# Otherwise, it returns y.

print("Maximum number:", max_number)

# result
#Maximum number: 20
```

<br>
<br>

```python

# ** SPOTIFY
# ------------
# FIND THE DURATION OF A List
# ------------

playlist_durations = [180, 240, 200, 300, 210] # duration of songs in seconds

# find the total duration
total_duration = reduce(lambda x, y: x + y, playlist_durations)

print("Total duration of the playlist:", total_duration, "seconds")

# result
#Total duration of the playlist: 1130 seconds
#
#
```

<br>
<br>

```python

# ** Shoes ESHOP
# ------------
#  find the total revenue generated from selling these shoes.add()
# -We can use reduce along with a lambda function to calculate the total revenue.
# ------------

shoe_prices = [50, 70, 90, 60] # prices of shoes in dollars

# we want to find the total revenue generated from selling these shoes. We can use "reduce" and a lambda function like this:
#
#
total_revenue = reduce(lambda x, y: x + y, shoe_prices)

print("Total revenue from selling shoes", total_revenue, "dollars")
# result
# Total revenue from selling shoes 270 dollars
#
#
```

<br>
<br>

```python

# ** Shoes ESHOP
# ------------
# Suppose we have a list of tuples where each tuple represents a shoe sale. Each tuple contains the shoe size and its corresponding price. We want to find the total revenue generated from selling these shoes across all sizes.
# ------------

from functools import reduce

shoe_sales = [(8, 50), (9, 70), (7, 90), (8, 60), (10, 80)]  # (size, price) tuples

# Now we want to calculate the total revenue. We can still use `reduce` along with a lambda function, but this time, we need to extract the price from each tuple and accumulate it to find the total revenue

total_revenue = reduce(lambda acc, sale: acc + sale[1], shoe_sales, 0)

# In this example, the lambda function lambda acc, sale: acc + sale[1] takes two arguments: acc (the accumulated revenue so far) and sale (the current sale tuple). It extracts the price (the second element) from each sale tuple and adds it to the accumulated revenue. The reduce function applies this lambda function cumulatively to the list shoe_sales, starting with an initial value of 0 for the accumulated revenue, resulting in the total revenue generated from selling shoes.

print("Total revenue from selling shoes:", total_revenue, "dollars")

# result
# Total revenue from selling shoes: 350 dollars


```

<br>
<br>

---

<br>

```python

#
#
# ** pizza resto
# ------------
# pizza restaurant where we have a list of orders. Each order is represented by a tuple containing the pizza size and its corresponding price. We want to find the total revenue generated from these orders.

#
# from functools import reduce
#
pizza_orders = [("medium", 12), ("large", 15), ("small",10), ("largeXl", 18), ("mediumXl", 14 )]

# - Now we want to calculate the total revenue.
# - We can use `reduce` along with a lambda function, similar to the previous example.
#
# - This time, we need to extract the price from each order TUPLE and accumulate it to find the total revenue.

total_revenue = reduce(lambda acc, order: acc + order[1], pizza_orders, 0)
# ** in this example, the lambda function 'lambda acc, order: acc + order[1]' takes 2 arguments 'acc' (the accumulated revenue so far) and 'order (the current tuple).
#
# - It extracts the price (the second element) from each order tuple and adds it to the accumulated revenue.

# - The 'reduce function applies this lambda function cumulatively to the list 'pizza_orders', starting with an initial value of 0 for the accumulated revenue, resulting in the total revenue generated from pizza orders.
print("total revenue from pizza orders:", total_revenue, "dollars")
#
# result
# total revenue from pizza orders: 69 dollars

```

<br>
<br>

```python

#
# ** pizza resto 2
# ------------
# from functools import reduce
# 25 total of pizza & salad
#
order__s = [
    ("Alice", ["Pizza", "Salad", 25]),
    ("Bob", ["Burguer", "Fries", "Soda"], 20),
    ("Charlie", ["Pizza", "Wings", "Soda", 30]),
    ("David", ["Salad", "Soup"], 15)

]

# Now we want to calculate the total revenue
# We can use 'reduce' along with a LAMBDA function to achieve this.

# This time, we need to EXTRACT the TOTAL price from each order TUPLE and accumulate it to find the TOTAL revenue.

total__revenue = reduce(lambda acc, order: acc + order[2], order__s, 0 )

# going down on the branch to reach the order[2]
# ** BY going down the branch i mean this: david is pos 0, pizza etc is pos 1, and 25 is position 2
# order[0]: Customer's name
# order[1]: Items ordered (a list of strings)
# order[2]: Total price of the order
print("Total revenue from orders:", total_revenue, "dollars")

# Total revenue from orders: 125 dollars

```

<br>
<br>

## 💳 payment service that accepts different types of cards to handle the total of the order.

- We'll define a dictionary mapping card types to their respective processing fees, and then we'll calculate the total revenue after deducting the processing fees.

<br>

```python

```
