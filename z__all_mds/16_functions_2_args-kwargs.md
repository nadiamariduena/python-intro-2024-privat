## 🍭 `*args` in Python

[source/ geeksforgeeks.org/](https://www.geeksforgeeks.org/args-kwargs-python/)

In this article, we will cover what `**` (double star/asterisk) and **(star/asterisk)** do for parameters in Python, Here, we will also cover args and **kwargs** examples in Python.

- We can pass a variable number of arguments to a function using special symbols.

<br>

### Special Symbols Used for passing arguments in Python:

`*args` (Non-Keyword Arguments)
`**kwargs` (Keyword Arguments)

<br>

### There are two special symbols:

<br>

- The `*args` parameter allows you to write a function that can accept a varying number of individual positional arguments in each call

<br>

#### example 1:

```python
##  -------
# ** ARGS
# ----------
# args will work like in javascript
# ** The *args parameter allows you to write a function that can accept a varying number of individual positional arguments in each call

def multiple_items(*args):
    # as you can see i am not adding names like in the num1 & num2, instead i grab the various values within the multiple_items("Dave"...
        print(args)
        print(type(args))

multiple_items("Dave", "John", "Noaln")
# -----------------  REMEMBER: -----------
#  TUPLES -----
# #tuples can't be changed after they're created, but lists can be modified
# Typically use parentheses (), but can also be created without them by simply separating items with commas.
#my_tuple = (1, 2, 3)  # Using parentheses
#my_tuple = 1, 2, 3    # Without parentheses (still a tuple)
#  LISTS -------
# Use square brackets [].
#my_list = [1, 2, 3]  # Using square brackets
```

<br>

### Example 2:

- Python program to illustrate `*args` with a first extra argument

```python
# EXAMPLE 2

def myFun(arg1, *argv):
    print('First argument :', arg1)
    for arg in argv:
        print('Next argument through *argv :', arg)

myFun('Hello', 'Welcome', 'to', 'Paradisse')
# RESULT:
# First argument : Hello
# Next argument through *argv : Welcome
# Next argument through *argv : to
# Next argument through *argv : Paradisse


```

<br>
<br>

## `**kwargs` in Python

<br>

- Using `**kwargs` in Python **allows you to pass a variable number of keyword arguments to a function**. Here's a breakdown of how it works along with additional examples to help you understand its usage better.

```python
def myFunny(**kwargs):
    for key, value in kwargs.items():
        print('%s == %s' % (key,value))
        #The syntax "%s == %s" % (key, value) in Python uses the old-style string formatting (also known as printf-style string formatting). Here, the % operator is used to format a string. Let's break down the components:

myFunny(first='Geeks', mid='for', last='Geeks')

```

### Output

```python
first == Geeks
mid == for
last == Geeks

```

<br>

# 🔴 the old way

### 👾The syntax `"%s == %s"` %

The syntax "%s == %s" % (key, value) in Python uses the old-style string formatting (also known as printf-style string formatting). Here, the % operator is used to format a string. Let's break down the components:

<br>

# Explanation

### Format Specifiers:

`%s`: This is a placeholder for a string. When the string is formatted, %s will be replaced by the corresponding value.

#### example 1

```python
name = "Alice"
age = 30

# Using %s as a placeholder for strings
# alice will be raplaced by the %s which is at the end alice, because alice is within the string and that is the purpose of the %s, to replace the string
print("Name: %s, Age: %s" % (name, age))
#
#Here, the %s in "Name: %s, Age: %s" is replaced by the
# values of name and age.

# OUTPUT:
Name: Alice, Age: 30

```

<br>
<br>

## 2. String with Placeholders

#### example 2

- A string with placeholders (%s) can be designed to include multiple placeholders which will be replaced by corresponding values provided later.

```python
# ✋ as you can see below, Bon IS REPLACED BY THE string which is the %s
template = "Hello, %s! You have %s new messages."

# Placeholder string with two %s placeholders
name = "Bob"
messages = 5

print(template % (name, messages))
# OUTPUT:
Hello, Bob! You have 5 new messages.

```

<br>

In this example, the template "Hello, `%s!` You have %s new messages." contains two `%s` placeholders. When formatted, the first %s is replaced by name and the second `%s` is replaced by messages.

<br>
<br>

## 3. % Operator

The `%` operator is used to provide the actual values that replace the placeholders in the format string. The % operator takes a tuple of values, and each value corresponds to a `%s` in the format string.

<br>

```python
def myFunny(**kwargs):
    for key, value in kwargs.items():
    # Using % operator to replace placeholders with actual values
    print("%s == %s" % (key, value))

#
myFun(first="Geeks", mid="for", last="Geeks")
```

#### output

```python
first == Geeks
mid == for
last == Geeks
```

Here, for each key-value pair in the kwargs dictionary, the string "%s == %s" contains two %s placeholders. The % operator then takes a tuple (key, value) and replaces the placeholders with the actual values of key and value.

<br>
<br>

## COMBINED

```python
#---------
# ++KWARGS
# ----------

def myFune(**kwargs):
    for key, value in kwargs.items():
    #String with placeholders and format specifiers
        format_string = "%s == %s"
        #Using % operator to provide values that replace the placeholders
        print(format_string % (key, value))
#The % operator takes a tuple (key, value) and substitutes each %s with the respective elements of the tuple.




myFune(first="my", mid="beautiful", last="life")


# OUTPUT:
#first == my
# mid == beautiful
# last == life
```

<br>
<br>

## 🌈 THE new way

- This approach using %s and the % operator is a classic way of string formatting in Python. However, for modern Python code, you might prefer using str.format or f-strings for better readability and flexibility:

#### Using str.format

```python
name = "Alice"
age = 30
# ✋ as you can see the string goes before the .format
formatted_string = "Name: {}, Age: {}".format(name, age)
print(formatted_string)

```

### Using f-strings (Python 3.6+)

```python
name = "Alice"
age = 30
# here i use the f
formatted_string = f"Name: {name}, Age: {age}"
print(formatted_string)

```

## Both methods will produce the same output:

```python
Name: Alice, Age: 30

```

## My Question:

- its more or less like in react?

````javascript
<Prop contentOfThevariable="hello"

`${contentOfTheVariable}`

output: hello```
````

### Chatgpt:

- Yes, it's a similar concept! In both Python and React (JavaScript/JSX), you are inserting or interpolating variable values into strings. Let's compare the two approaches directly to highlight the similarities and differences.

#### In React (JavaScript/JSX)

In React (or JavaScript in general), you often use template literals (also known as template strings) to interpolate variables within strings. Template literals are enclosed by backticks (`) and use the ${}` syntax to include variables.

#### React example

```javascript
const contentOfTheVariable = "hello";

// Using template literals for string interpolation
const output = `${contentOfTheVariable}`;

console.log(output); // Output: hello
```

#### python example

```python
content_of_the_variable = "hello"

# Using str.format for string interpolation
output = "{}".format(content_of_the_variable)

print(output)  # Output: hello

```

<br>
<br>

## Real scenario (SPOTFY)

```python
def update_playlist(playlist_id, **kwargs):
    """
    Update a Spotify-like playlist with provided details.

    :param playlist_id: ID of the playlist to update.
    :param kwargs: Dictionary of playlist details to update.
    """
    print(f"Updating playlist with ID: {playlist_id}")
    for key, value in kwargs.items():
        print(f"{key.replace('_', ' ').capitalize()}: {value}")

    # Simulate sending updated data to a Spotify-like service
    # For example, sending a request to an API endpoint
    # response = requests.post(f"https://api.spotify.com/playlists/{playlist_id}", json=kwargs)
    # print(f"Response: {response.status_code}")

# Driver code
update_playlist(
    playlist_id="12345",
    name="My Favorite Songs",
    description="A collection of my favorite songs from various genres.",
    tracks=["Track1", "Track2", "Track3"],
    public=True
)

```

<br>

- `update_playlist(playlist_id, **kwargs)`: The function takes a playlist_id and any number of additional keyword arguments (\*\*kwargs).

- The playlist_id is a required argument, while `**kwargs` allows passing optional details like **name, description, tracks, and public**.
