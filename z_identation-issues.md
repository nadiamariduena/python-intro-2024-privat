## 🟧 Indentation issues

<br>

- 🔴 check the prettify for python results, its called **PPRINT** and you used instead of `print()` [Go to section](#pprint_to_prettifyhtecode)

<br>
<br>

### Read more about identation

https://www.askpython.com/python/python-indentation

<br>

# the issue

- when learning about the loops in python [loops](./15_loops.md) i couldn't get the same result the teacher was getting.

```python
#this code had the identation issues
# LOOP over the list and check if there is a specific name

thenames = ["Dave", "Sara", "John"]

for px in thenames:

    if px == 'Sara':
      continue
print(px)
# result: charless

#
#
# 👍 good
# notice the position of the  print(px)
thenames = ["Dave", "Sara", "John"]

for px in thenames:
    if px == 'Sara':
        continue
    print(px)
#
# result
Dave
John

```

# 🌈 reason

The issue you're encountering is due to indentation. Currently, **print(px) is outside of the loop**, so it only executes after the loop has finished iterating through all the elements in thenames. To print both the first and last elements, you need to adjust the indentation of the print(px) statement so it's inside the loop.

<br>
<br>

## 🔴 Indentation issues on loops

- ⚠️ Wrong

- 🌈 **REASON** the print statement is outside the loop. Thus, ✋ **it only prints the last person's information** because the variables name, age, and height are being overwritten in each iteration of the loop. To print all the people's information, you need to include the print statement inside the loop, like this:

```python
# list of "people" with their name, age, and height
# 1)
people = [
    # the 165.5 will be rounded
    {"name": "Alice", "age": 30, "height": 165.5},
    {"name": "Bob", "age": 25, "height": 180.0},
    {"name": "Charlie", "age": 35, "height": 175.2}
]

#
# 2) LOOP
# Loop through each person in the list
for person in people:
    # extract variables from the dictionary
    name = person["name"]
    age = person["age"]
    height = person["height"]



#
# 3) Format the string using f-string with formatting options
#
message_e = f"Name: {name}, Age:{age}, Height: {height:.2f} cm"
#🔴 In the context of the format specifier {:.2f}, the f indicates that the variable should be formatted as a floating-point number.

print(message_e)
#
#
#
# result
# Name: Charlie, Age:35, Height: 175.20 cm
```

# Corrected

```python

#----------
# LOOP
#----------
#
#
# list of "people" with their name, age, and height
# 1)
people = [
    # the 165.5 will be rounded
    {"name": "Alice", "age": 30, "height": 165.5},
    {"name": "Bob", "age": 25, "height": 180.0},
    {"name": "Charlie", "age": 35, "height": 175.2}
]

#
# 2) LOOP
# Loop through each person in the list
for person in people:
    # extract variables from the dictionary
    name = person["name"]
    age = person["age"]
    height = person["height"]



    #
    # 3) Format the string using f-string with formatting options
    #
    message_e = f"Name: {name}, Age:{age}, Height: {height:.2f} cm"
    #🔴 In the context of the format specifier {:.2f}, the f indicates that the variable should be formatted as a floating-point number.

    print(message_e)
#
# RESULT
# Name: Alice, Age:30, Height: 165.50 cm
# Name: Bob, Age:25, Height: 180.00 cm
# Name: Charlie, Age:35, Height: 175.20 cm
```


<br>
<br>

---


<br>
<br>


<a name="pprint_to_prettifyhtecode"></a>


# 🟠 PPRINT

- I used it for the first time in[ this weather app exercise ](./z_weather-API.md)

<br>

 Now lets import another **module**, its called **PPRINT**

<br>

**PPRINT** stands for **"pretty-print"**  💅and it is both a module and a function within Python.

- Its primary **purpose** is to **format** complex **Python** data **structures** in a more **readable** way,  **especially** when they are **nested** or contain multiple levels of **indentation** ✋.

<br>

### 🫐 Module and Function

**Module:** The  pprint module (pprint) in Python provides the pprint() function and related utilities.

 - - <u>It is used **to print data structures** such as **dictionaries and lists** in a visually appealing and readable format</u> , making it easier for humans to interpret.

- **Function:** The pprint() function within the module is the main tool used for this purpose.

- - It takes a Python data structure as input and outputs a formatted representation of that structure.

- - This can include **indenting** nested structures, **breaking** long **lines**, and generally presenting the data in a way that is easier to understand than the default print() function output.



<br>
<br>

## 🟧 Use it on the `weather.py`

 Now lets import the **PPRINT** within the weather app

 <br>


```python
from pprint import pprint
```

#### use it

- once imported , replace the default print by the pprint

```python
# before
 print(weather_data)

# after
pprint(weather_data)
```

<br>

- 🌈 RUN the code with the arrow at the top bar of your VS code


<br>

### Output

```javascript
// ✋ BEFORE PPRINT
{'coord': {'lon': -71.0598, 'lat': 42.3584}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}], 'base': 'stations', 'main': {'temp': 73.72, 'feels_like': 74.98, 'temp_min': 70.57, 'temp_max': 75.49, 'pressure': 1017, 'humidity': 89, 'sea_level': 1017, 'grnd_level': 1013}, 'visibility': 10000, 'wind': {'speed': 8.05, 'deg': 210}, 'clouds': {'all': 20}, 'dt': 1720930800, 'sys': {'type': 2, 'id': 2013408, 'country': 'US', 'sunrise': 1720948810, 'sunset': 1721002783}, 'timezone': -14400, 'id': 4930956, 'name': 'Boston', 'cod': 200}


#
#
// ✅ after PPRINT

*** Get Current Weather Conditions ***


Please enter a city name:
New Mexico
{'base': 'stations',
 'clouds': {'all': 1},
 'cod': 200,
 'coord': {'lat': 34.5003, 'lon': -106.0008},
 'dt': 1720985736,
 'id': 5481136,
 'main': {'feels_like': 88.54,
          'grnd_level': 812,
          'humidity': 13,
          'pressure': 1015,
          'sea_level': 1015,
          'temp': 92.98,
          'temp_max': 93.06,
          'temp_min': 91.33},
 'name': 'New Mexico',
 'sys': {'country': 'US',
         'id': 2003420,
         'sunrise': 1720958529,
         'sunset': 1721009837,
         'type': 2},
 'timezone': -21600,
 'visibility': 10000,
 'weather': [{'description': 'clear sky',
              'icon': '01d',
              'id': 800,
              'main': 'Clear'}],
 'wind': {'deg': 109, 'gust': 13.11, 'speed': 8.57}}
```