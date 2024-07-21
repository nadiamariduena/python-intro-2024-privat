 ## 🟡 PICKLE


 <br>
 <br>

 ###  I came across the topic of Pickle while researching something else, and it piqued my interest. However, I must admit that I am a total beginner in Python, which makes using it comfortably quite challenging for me.

 <br>

#### ✅ chatgpt:

<br>

 - 🟦 **Pickle** is a Python **module** used **for serializing and deserializing** Python `objects{}`, essentially allowing you 🔴 [**TO CONVERT PYTHON OBJECTS**](#python_objects_to_convernt)
   INTO a byte stream (serialization) that can be easily stored or transmitted, and later reconstruct them back into their original form (deserialization). 🤔


  <br>

- Serialization is particularly **useful when you need to save the state of a Python object to disk or send it over a network** 💻 , as it converts complex Python objects into a format that can be easily stored or transmitted. On the other hand, deserialization reconstructs Python objects from the serialized byte stream.

<br>
<br>

🟫 As a complete **beginner in Python**, delving into **Pickle** might initially seem **overwhelming** due to its intricacies and potential pitfalls. **However, mastering its usage** can significantly **enhance** your ability to **work with** persistent **data** and facilitate **communication between different** parts of your Python programs.

<br>

>**If you're interested** in exploring **Pickle** further, it's beneficial to **familiarize** yourself with fundamental **concepts** such as **serialization, deserialization**, and the various methods provided by the Pickle module.

<br>


🔴 Additionally, **always ensure** you **understand** the **implications** of using **Pickle** in different **contexts**, particularly when handling **sensitive data** or in **distributed systems**.


<br>
<br>


#### 🟣 QUESTION: I've looked at the pickle documentation, but I don't understand where pickle is useful, What are some common use-cases for pickle?

[common-use-cases-for-pickle-in-python](https://stackoverflow.com/questions/3438675/common-use-cases-for-pickle-in-python)

<br>

- 🟧 Give examples for each of the **below:**

<br>

```bash
1) saving a program's state data to disk so that it can carry on where it left off when restarted (persistence)

2) sending python data over a TCP connection in a multi-core or distributed system (marshalling)

3) storing python objects in a database

4) converting an arbitrary python object to a string so that it can be used as a dictionary key (e.g. for caching & memoization).
```

<br>

🔴 I will include all the examples here. However, please note that they are all advanced. They are intended to provide you with an idea of what you can achieve in the future. For more details, refer to [Go to examples(advanced)](#common_use_cases_for_pickle) )

<br>
<br>

---




<br>
<br>

## 🎠 What is Serialization?

<br>

#### ✅ chatgpt:

Serialization is like packing up your toys 🧸 into a special box  📦 so you can easily send them to a friend who lives far away.

- It's a way to turn your toys (or data   in computers) into a special format 💾 that makes it easy to store, send, or even bring back exactly as they were.

<br>
<br>
<br>


## 🟠 Purpose of Serialization:

<br>

**Saving Things:** Just like you save your favorite drawings or toys in a box to keep them safe, computers save important information like **game levels, messages, or even pictures using serialization**. 🔴 This way, they can remember everything even after you turn off the computer.


**Sending Across the Internet:** Imagine sending a special message to a friend in another city. Serialization helps computers turn that message into a format that can be sent over the internet quickly and put back together when it arrives.


<br>
<br>

## 🟦How is Serialization Used?

**Saving Game Progress:** 👍 When you finish playing a game, serialization saves where you left off so you can start from the same spot next time.

**Sharing Data:** 🫐 It's used in apps and websites to share information like photos, videos, or messages between people or devices.

**Storing Information:** 👍 In big databases or files, serialization helps keep all kinds of important data organized and easy to find.

<br>
<br>

<br>


## 🟡 Sending Data


<br>

- let's break down how serialization helps in sending data, such as an object containing a fashion collection (like shoes with sizes), through email step by step, in simple terms:

### Step-by-Step Explanation for Sending Data:

<br>

### 🟦 1. the Object

 Imagine you have a special **box** (an `object{}`) that **holds** all your **favorite** **shoes**, <u>each with their sizes and colors</u> .

  🟧 This box (object) also remembers where each shoe came from and other details you like.

<br>
<br>


### 🟦 2. Serialization Process:


🔴 Serialization **is like taking a 📷 picture** of this **special shoe box** and **writing down** every **detail** about **each shoe and its sizes on a piece of paper** 🗒️ 🖊️.

#### 🟧 It's a way to capture all the information in a format that computers can easily understand and store.

<br>
<br>

### 🟦 3. Converting to Bytes:


After writing down all the details 🗒️ 🖊️ , serialization then **turns/converts** this **paper into** a special **code** made up of **numbers (bytes).**

🟧 These numbers represent everything about your shoes and their sizes, neatly packed together.

<br>
<br>

### 🟦 4. Sending Over Email:

Now, **you** want to **send** this special code **(bytes)** to your friend **through email**.

- - 🔴 **Computers** use serialization to **turn** these **bytes** into a **message** that can be **attached to an email**.

<br>
<br>

### 🟦 5. Receiving and Deserialization:

When your **friend gets** the **email**, their **computer** uses **deserialization** (the opposite of serialization) to **unpack** the special code **(bytes) back into a picture** of your shoe **box with all the details**.


- - 🟧 It's like **your friend** can **open** the **email**, see the picture of your shoe box, and **know exactly which shoes** are **inside**, their sizes, and everything else.

<br>
<br><br>

## 🟠 Exercises

#### [What is Pickling And Unpickling in Python?](https://stackabuse.com/how-to-pickle-and-unpickle-objects-in-python/)


#### Video [Python Pickle Module for saving objects (serialization)](https://youtu.be/2Tw39kZIbhs?si=uDzE3LpOxCG__we_)

<br>

<br>

<a name="python_objects_to_convernt"></a>

## 🟡 CONVERT PYTHON OBJECTS, INTO a byte stream (serialization)

<br>

## Exercise 1.

```python
import pickle

example_dict = {1:"6", 2:"2",3:"f"}


pickle_out = open("dict.pickle", "wb") # wb: write binary, this will create / generate the file
pickle.dump(example_dict, pickle_out)
pickle_out.close()

#https://youtu.be/2Tw39kZIbhs?si=uDzE3LpOxCG__we_
```

<br>

#### 🍭 1 Run the code, it will generate a binary file called "dict.pickle"



```bash
# ✋ This is the generated file, and this is what you have to deserialize to make the data human readable
\80\03\7D\71\00\28\4B\01\58\01\00\00\00\36\71\01\4B\02\58\01\00\00\00\32\71\02\4B\03\58\01\00\00\00fqu.
```

<br>

- check it here: https://hexed.it/

🌈 **Hexed.it** is a web-based hexadecimal (hex) **editor and viewer**. Hexadecimal is a base-16 numeral system often used in computing to represent **binary data in a human-readable format**. Hexed.it allows users to upload files and view their contents in hexadecimal format, providing tools to edit bytes directly.

<br>


#### 🍭 2 you will not be able to visualize it, but you can install the below extension:
#### 🍭 3 Within your extensions, Install: Hex Editor Extension


#### 🍭 4 Once installed, click on the generated "dict.pickle" , click on the blue button, it will offer you to options at the top bar, choose the option of Hex editor

<br>



<br>

#### 🟡 this generated binary file `dict.pickle` is the one you can send via email (like you do with images)

<br>

#### Deserialize

```python
import pickle

pickle_in = open("dict.pickle", "rb") # rb = readbinary
example_dict = pickle.load(pickle_in)
print(example_dict)
```

#### 🌟 output

```python
{1: '6', 2: '2', 3: 'f'}
```

<br>





<br>

<br>

## Exercise 2.

### 🟠 Serializing

#### 1 The purpose of the below code is to demonstrate <u>serialization</u>  of a collection of *Shoe* objects into a file using Python's pickle module.

<br>

- Later on, you will see how the data will be translated from binary to text.

```python
#0
import pickle
#The pickle module is imported (import pickle).



# 1 Defining the Shoe Class:
#A Shoe class is defined with attributes brand, size, and color.
class Shoe:
#Instances of this class represent individual shoes with specific attributes.

    def __init__(self, brand, size, color):
        #It contains instances of the Shoe class initialized with different brands, sizes, and colors.

        self.brand = brand
        self.size = size
        self.color = color

# 2 Creating a List of Shoe Objects:
shoes_collection = [
    Shoe("Nike", 9, "Black"),
    Shoe("Adidas", 8, "White"),
    Shoe("Puma", 7, "Red")

]

#
#
# 3 Serialize the shoes collection object to a file
#
# - file_path Definition: Specifies the path where the serialized data will be stored, with a ".pickle extension".
# - .pickle extension indicating it will be a pickled file.



#
file_path = "this_will_be_the_generated_shoes_collection.pickle"
with open(file_path, "wb") as file:
    #open() Function: Opens the file specified by file_path in binary write mode ("wb").

    ##The shoes_collection list is serialized and written to the file specified by file_path using the pickle.dump() function.
    #
    pickle.dump(shoes_collection, file)
    #dump() function: It takes two parameters - the object being “shoes_collection” (look at the shoes in line 11) and a File object (at the end of line 20) to write the data to.


#
# 4 Printing a Confirmation Message:
print(f"Serialized shoes collection to {file_path}")

```

<br>

### 2. Run the code:

- type the name of your file: `python test2_pickle_shoe.py` to run it.

- Once you run the code: it will generate a binary file called `this_will_be_the_generated_shoes_collection.pickle`


### 3. Visualization

 - you will not be able to visualize it, but you can install the below extension:

 -  Within your extensions, Install: Hex Editor Extension

-  Once installed, **click** on the generated `this_will_be_the_generated_shoes_collection.pickle` , **click** on the blue button, it will offer you two options at the top bar, choose the option of **Hex editor** (this will show you the binary version but not the actual object with the human readable data)

<br>

#### at this point i have this:

```python
project/
│
├── test2_pickle_shoe.py    # Contains definition of Shoe class
├── test2_pickle_deserialization.py    # Code to deserialize the generated code from the "test2_pickle_shoe.py"
│
├── this_will_be_the_generated_shoes_collection.pickle # the generated pickle (binary file)
#
#
└── README.md         # Documentation and usage instructions


```


<br>

## 🟠 Deserialize

### Deserialize (Unpickle) the Object:

- Use Python code to read the file and deserialize it back into Python objects.

- 🔴 This code below will give me an error

```python
# 1 once you have generated the pickle by using the code:
# 2 test2_pickle_shoe.py
# use the below code to convert the binary file that was generated on step 2 code


import pickle

# Assuming example.pickle is your pickled file
file_path = "this_will_be_the_generated_shoes_collection.pickle"

# Open the file in binary read mode
with open(file_path, "rb") as file:
    # Load (deserialize) the object from the file
    loaded_object = pickle.load(file)

# Now you can print or manipulate the loaded object
print("Loaded object:")
print(loaded_object)
```

<br>

### 🔴 THE ERROR:

```python
Traceback (most recent call last):
  File "test2_pickle_deserialization.py", line 14, in <module>
    loaded_object = pickle.load(file)
AttributeError: Can't get attribute 'Shoe' on <module '__main__' from 'test2_pickle_deserialization.py'>

```
<br>

### 🌈 REASON:

- The error you're encountering, AttributeError: Can't get attribute 'Shoe' on `<module '__main__' from 'test2_pickle_deserialization.py'>`, typically **occurs** when **Python tries to unpickle an object** that **has** a **class definition** that it **doesn't recognize**.

- - ✋ This happens because **Python needs** to **know about** the **class** (`Shoe` in this case) **before** it can properly **unpickle**  <u>instances of that class</u> .


<br>
<br>

### 🟣 QUESTION: why do i have to declare the `Shoe class` again?

#### ✅ chatgpt:

- ✋ **In Python**, when you **serialize** an **object** using **pickle**, you're essentially **saving its state and some metadata** necessary to reconstruct it later.

### Here’s why you encounter issues when trying to deserialize (unpickle) without redefining the class:


## Why Redefine the Class?

<br>

**Serialization and Metadata:**

When you use `pickle.dump()` to serialize an object (`shoes_collection` in your case), Python stores not only the object's data but also some metadata about its class and module.

This **metadata** includes **information about** where to find the **class** definition (**Shoe**) and **how to reconstruct objects** of that class when you unpickle them.


```python
class Shoe:
#Instances of this class represent individual shoes with specific attributes.

    def __init__(self, brand, size, color):
        #It contains instances of the Shoe class initialized with different brands, sizes, and colors.

        self.brand = brand
        self.size = size
        self.color = color

# 2 Creating a List of Shoe Objects:
shoes_collection = [
    Shoe("Nike", 9, "Black"),
    Shoe("Adidas", 8, "White"),
    Shoe("Puma", 7, "Red")

]

 ✋
file_path = "this_will_be_the_generated_shoes_collection.pickle"
with open(file_path, "wb") as file:

    pickle.dump(shoes_collection, file)

print(f"Serialized shoes collection to {file_path}")
```

<br>

## 🔴 Unpickling Requirements:

 🟠 When you unpickle (`pickle.load()`) an object, **Python needs to locate the class definition (Shoe)** to properly **reconstruct the objects** from the **serialized data**.


- - 🔴 If Python cannot find the class definition (**Shoe**), it raises an AttributeError because it doesn't know how to recreate instances of the Shoe class.

<br>
<br>

### 🟦 Module Scope:

**Python's pickle** module **stores references** to **class definitions** based on their module and name.

- - 🔶 **If you define Shoe** in a **script** (`test2_pickle_deserialization.py`, for example) and **then serialize objects of that class in the same script**, Python knows where to find Shoe when you unpickle them in the same script.

<br>

- - 🔶 **However**, if you attempt to unpickle in a different script or environment where Python doesn't have access to the original class definition, you must import or redefine the class (Shoe) to provide Python with the necessary information to reconstruct the objects correctly.

<br>

## 🫐 Key Points:

 🟠 **Class Definition Scope:**

- 🟥 You need to ensure that Python can access the class definition (Shoe) at the time of unpickling.

<br>

#### This can be done by:

- - Importing the class if it's defined in another module.

- - Redefining the class in the same module/script where you perform unpickling.

<br>


🟠  **Serialization Metadata:** pickle stores metadata about the class and module of serialized objects. This metadata is crucial for unpickling to work correctly.

<br>
<br>


## Solution

```python

# 1 once you have generated the pickle by using the code:
# 2 test2_pickle_shoe.py
# use the below code to convert the binary file that was generated on step 2 code


import pickle

# Define the Shoe class
class Shoe:
    def __init__(self, brand, size, color):
        self.brand = brand
        self.size = size
        self.color = color

# File path where the pickled data is stored
file_path = "this_will_be_the_generated_shoes_collection.pickle"

# Deserialize (unpickle) the objects from the pickle file
with open(file_path, "rb") as fdile:
    loaded_shoes_collection = pickle.load(fdile)

# Now you can work with the loaded objects
print("Deserialized shoes collection:")
for shoe in loaded_shoes_collection:
    print(f"Brand: {shoe.brand}, Size: {shoe.size}, Color: {shoe.color}")


```

#### output

```python
Deserialized shoes collection:
Brand: Nike, Size: 9, Color: Black
Brand: Adidas, Size: 8, Color: White
Brand: Puma, Size: 7, Color: Red
```


<br>
<br>
<br>

---

<br>
<br>
<br>

## 🟡 Common use cases for Pickle

<a name="common_use_cases_for_pickle"></a>

 <br>

```bash
1) saving a program's state data to disk so
that it can carry on where it left off when
restarted (persistence)

2) sending python data over a TCP connection
in a multi-core or distributed system
(marshalling)

3) storing python objects in a database

4) converting an arbitrary python object to a
string so that it can be used as a dictionary
key (e.g. for caching & memoization).

OTHER -----


- Game profile saves

- Game data saves like lives and health

- Previous records of say numbers inputed to
 a program
```

<br>

🔴 I will include all the examples here **below**. However, please note that they are all advanced. They are intended to provide you with an idea of what you can achieve in the future.

<br>

### 1) Saving a program's state data to disk (persistence)


#### Example:


- **Imagine** you have a Python **application** that **processes large** amounts of **data** and **needs** to be **able to save** its **state periodically** and **resume from where it left** off if it **crashes** or is **restarted**.

<br>


```python
import pickle

# Assume 'data' is a complex data structure holding program state
data = {
    'current_step': 75,
    'last_processed_item': 'item123',
    # ... other program state variables
}

# Save program state to a file using pickle
with open('program_state.pkl', 'wb') as f:
    pickle.dump(data, f)

# Later, to load the state back
with open('program_state.pkl', 'rb') as f:
    loaded_data = pickle.load(f)

# 'loaded_data' will now contain the program state as it was saved

```

<br>
<br>

- In this example, pickle is used to serialize the data dictionary to a file (`program_state.pkl`) which can then be loaded back to restore the program's state.


<br>
<br>

### 2) Sending Python data over a TCP connection (marshalling)

#### Example:

- **In a distributed system** where multiple **processes or machines** need to **exchange** Python **objects** over a **network connection** (e.g., **using TCP sockets**), pickle can serialize Python objects into a byte stream that can be sent over the network.

<br>


```python
import pickle
import socket

# Assume 'data' is a Python object to be sent over the network
data = {
    'command': 'process',
    'parameters': [1, 2, 3, 4]
}

# Serialize the data to a byte stream
serialized_data = pickle.dumps(data)

# Send the serialized data over a TCP connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('remote_host', 12345))
sock.sendall(serialized_data)
sock.close()

```

<br>
<br>

### 3) Storing Python objects in a database

#### Example:


- **If you need** to **store** Python **objects in a database** (particularly **NoSQL** databases **that support storing** complex **data** structures **directly**)**, pickle** can **serialize** Python **objects into a format** that **can be stored in the database**.

```python
import pickle
import pymongo

# Connect to MongoDB (assuming it's running locally)
client = pymongo.MongoClient('localhost', 27017)
db = client['mydatabase']
collection = db['mypicklecollection']

# Assume 'data' is a Python object to be stored in MongoDB
data = {
    'user_id': 123,
    'preferences': {'theme': 'dark', 'language': 'en'},
    # ... other user data
}

# Serialize and store data in MongoDB
serialized_data = pickle.dumps(data)
collection.insert_one({'serialized_data': serialized_data})

# Later, retrieve and deserialize the data
result = collection.find_one({'user_id': 123})
loaded_data = pickle.loads(result['serialized_data'])

# 'loaded_data' now contains the deserialized Python object


```

<br>

#### Here, pickle is used to serialize the data dictionary before storing it in MongoDB.

- - When retrieving the data, pickle is again used to deserialize the stored byte stream back into a Python object.

<br>
<br>

### 4) Converting an arbitrary Python object to a string for caching & memoization

#### Example:


- **When you** need to **use** a Python **object** (**or** a combination of **objects**) **as a dictionary key**, you can **serialize them** into a **string** representation **using pickle**.

```python
import pickle

# Example function with caching using pickle for key generation
cache = {}

def cached_function(arg1, arg2):
    # Create a tuple of arguments to use as cache key
    key = pickle.dumps((arg1, arg2))

    if key in cache:
        return cache[key]
    else:
        result = arg1 + arg2
        cache[key] = result
        return result

# Example usage
print(cached_function(3, 4))  # Output: 7
print(cached_function(3, 4))  # Output: 7 (retrieved from cache)


```

<br>

- In this example, `pickle.dumps()` is **used** to **serialize** a **tuple** (`arg1, arg2`) **into a byte** string **key**, ✋ which is then used as a key in the cache dictionary for memoization purposes.


<br>
<br>
<br>
<br>


### 🟡 This is an interesting question someone asked on Stack Overflow, especially if you are just starting out like me.

<br>

https://stackoverflow.com/questions/14509269/best-method-of-saving-data

#### 🟣 QUESTION: I've made a class in which I want to keep track of stats of students. I intend to make a GUI later to manipulate this data.



- 🟣 **My main question is:** what is the best way to save and later retrieve this data?

- 🟣I've read about pickle and **JSON, but I don't really get how they work** (especially about how they save the data, like in which format and where).

<br>

### ✅ stackoveflow:

<br>

#### If data is simple, use JSON:

- If your data are pretty simple, like just collections of collections of strings or numbers, I would use json.

 What JSON is, is a string representation of simple data types and combinations of simple data types. Once you use the json module to convert your data to a string, you write it to a file yourself.


<br>

#### If data is complicated, use PICKLE:

 If your **data** are more **complicated**, and involves `classes` **other than the built-in collection objects**, pickle is a better choice.


 - - 🔴 One very important thing to know about **pickle** is that there are **security vulnerabilities** in pickle, and
