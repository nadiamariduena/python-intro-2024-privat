 ## 🟡 PICKLE


 <br>
 <br>

 ### ⚠️ I came across the topic of Pickle while researching something else, and it piqued my interest. However, I must admit that I am a total beginner in Python, which makes using it comfortably quite challenging for me.

 <br>

#### ✅ chatgpt:



 - 🟦 **Pickle** is a Python **module** used **for serializing and deserializing** Python `objects{}`, essentially allowing you to convert Python objects into a byte stream (serialization) that can be easily stored or transmitted, and later reconstruct them back into their original form (deserialization). 🤔

- - Serialization is particularly **useful when you need to save the state of a Python object to disk or send it over a network** 💻 , as it converts complex Python objects into a format that can be easily stored or transmitted. On the other hand, deserialization reconstructs Python objects from the serialized byte stream.

<br>

🟧 As a complete **beginner in Python**, delving into **Pickle** might initially seem **overwhelming** due to its intricacies and potential pitfalls. **However, mastering its usage** can significantly **enhance** your ability to **work with** persistent **data** and facilitate **communication between different** parts of your Python programs.

<br>

>**If you're interested** in exploring **Pickle** further, it's beneficial to **familiarize** yourself with fundamental **concepts** such as **serialization, deserialization**, and the various methods provided by the Pickle module.

<br>


🔴 Additionally, **always ensure** you **understand** the **implications** of using **Pickle** in different **contexts**, particularly when handling **sensitive data** or in **distributed systems**.


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

## 🟣  Exercises




### 1 The purpose of the below code is to demonstrate <u>serialization</u>  of a collection of *Shoe* objects into a file using Python's pickle module.

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

### 2. Run the code

- type the name of your file: `python test2_pickle_shoe.py`

#### 3 Once you run the code

- You will see that you have a new file within your project, this is a pickle (binary) file `this_will_be_the_generated_shoes_collection.pickle`