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

>However, various languages and frameworks might have similar functionality or libraries that offer similar capabilities for string formatting and interpolation.

#### Here’s a brief overview across different languages:

<br>

### 🟧 Languages and Frameworks with String Formatting Methods:

<br>

#### Python:

`.format()` method: Used for string formatting. Python also introduced f-strings (f"...") starting from Python 3.6, which offer a more concise and readable way to format strings.



#### JavaScript:

Template literals (ES6): Introduced with ECMAScript 6 (ES6), template literals provide a way to embed expressions inside strings using `${}` placeholders.

- - This is the primary method for string interpolation and formatting in modern JavaScript and React applications.

<br>

```javascript
import React from 'react';

const youtuber = "Dorothea Ernst";

const MyComponent = () => {
  return (
    <div>
      <p>{`Subscribe to ${youtuber}`}</p>
    </div>
  );
}

export default MyComponent;

```

<br>

#### C#:

`String.Format()` method: In C#, String.Format() is used for composite formatting of strings, where placeholders like {0}, {1}, etc., are replaced with values provided in subsequent arguments.

<br>

#### Java:

`String.format()` method: In Java, String.format() allows for string formatting similar to C#'s String.Format(). It uses placeholders like %s, %d, etc., to format strings with corresponding values.

<br>

#### PHP:

`sprintf()` function: PHP provides sprintf() for formatted string output. It supports placeholders similar to C#'s and Java's formatting methods.


<br>

#### Swift (iOS development):

`String(format:)` constructor: In Swift, String(format:) allows for string interpolation and formatting using placeholders like %@, %d, etc.


<br>
<br>

## Continue

```python
print("---- 🍀 ----")

adj = input("Adjetive: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \ I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person} "

# Print THE RESULT
print(madlib)
```

<br>

#### Run the code

- Run the arrow (top bar) , you will have to fill the questions:

```bash
Adjetive: interesting
Verb: learn
Verb: eat healthy
famous Person: Tilda S.

```
#### output

```bash
Computer programming is si interesting! It makes me so excited all the time because \ I love to learn. Stay hydrated and eat healthy like you are Tilda S.
```