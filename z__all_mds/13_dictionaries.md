## Dictionaries

https://www.geeksforgeeks.org/python-dictionary/

- Think of a dictionary in Python as a collection of key-value pairs. It's similar to how words and their meanings are organized in a real-world dictionary.

### 🟡 Here's a simple breakdown:

<br>

**Definition:** A dictionary is a mutable, unordered collection of items. Each item in a dictionary is a pair consisting of a key and a value.

<br>

**Creation:** You can create a dictionary using curly braces `{}` and separating each key-value pair with a colon `:`. For example:

```python
my_dict = {'apple': 5, 'banana': 3, 'orange': 7}

```

<br>

### Other ways

```python
#1
band ={

"vocals": "Plant",
"guitar": "Page"

}
print(band)
#
#
#2 or
band2 = dict(
vocals="Plant",
guitar="Page"
)

print(band2)
#
#
print(type(band))
#result: <class 'dict'>
print(len(band))
#result: 2
```

<br>

**Accessing Values:** You can access the value associated with a particular key by using square brackets `[]`. For example:

```python
#1
my_dict = {'apple': 5, 'banana': 3, 'orange': 7}
#
# 2
print(my_dict['apple'])  # Output: 5
```

<br>
<br>

### Other ways to access the data

```python
#
# ----- ACCESSing the data ---
# band ={

# "vocals": "Plant",
# "guitar": "Page"

# }
print(band["vocals"])
print(band.get("guitar"))
#result:
# 🐖 i get plant and page on the terminal, because these are the values that are aligned to the dictionary in line 27
# Plant
# Page
```

<br>
<br>

## 🍒 ALL KEYS

#### what if i want to see all the keys

```python
# ----- print all keys ---
print(band.keys())
# result: dict_keys(['vocals', 'guitar'])
```

<br>

## 🍒 ALL VALUES

#### what if i want to see all values

```python
# ----- print all values ---
print(band.values())
#result
#dict_values(['Plant', 'Page'])
```

# 🍒 list of key/value pairs as tuples

```python
# --------
#list of key/value pairs as tuples
print(band.items())
#dict_items([('vocals', 'Plant'), ('guitar', 'Page')])
```

<br>

## 🍒 Verify if a key exists

```python
print("guitar" in band)
# True
print("triangle" in band)
# False because  triangle is not on the dictionnary

```

<br>

---

<br>

### 🟡 Adding or Modifying Items:

- You can add new items or modify existing ones in a dictionary by assigning a value to a **key**:

```python
#1
my_dict = {'apple': 5, 'banana': 3, 'orange': 7}
#
# 2
my_dict['grape'] = 4  # Adding a new item
my_dict['banana'] = 6  # Modifying an existing item
```

#### another way

```python
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)
```

<br>
<br>

## 🟥Removing Items:

- You can remove items from a dictionary using the del keyword or the `pop()` method:

```python
#1
my_dict = {'apple': 5, 'banana': 3, 'orange': 7}
#
# 2
del my_dict['orange']  # Deleting a specific item
my_dict.pop('apple')   # Removing 'apple' and its value
#

```

<br>

# 🧧remove the last item

```python
#---------------------------

#---------------------------
# - removes the last item added to a dictionnary
# 1 for that i will add a new item. the below is before i add the new item:
# dict_values(['Plant', 'Page'])
# ('guitar', 'Page')
#- add a new item
band["glow"] = "flower"
print(band)
# 2 result, after i added the new item:
# dict_values(['Plant', 'Page'])
# {'vocals': 'Plant', 'guitar': 'Page', 'glow': 'flower'}
# 3 now remove the last item added
print(band.popitem())
# 4 result, here you can see that the glow flower are outside the square brackets
# {'vocals': 'Plant', 'guitar': 'Page', 'glow': 'flower'}
# ('glow', 'flower')
#---------------------

```

<br>

## 🔴Delete and CLEAR

```python
# ---- deleting
# 1 create a new item
band["drums"] = "Bonita"
#result: {'vocals': 'Plant', 'guitar': 'Page', 'drums': 'Bonita'}
# 2 delete the new item
del band["drums"]
#result after deleting
# {'vocals': 'Plant', 'guitar': 'Page'}
print(band)
#
#
#
#
#
#------ CLEAR
# 1. for this example, i will create a new dic

animals ={
"anim1": "dog",
"anim2": "cat"
}
#result
# {'anim1': 'dog', 'anim2': 'cat'}
print(animals)
# now i will delete it
animals.clear()
print(animals)
# result: {}  its empty because its cleared of its content
# DEL
# if i want to delete it entirely use this:
del animals
#result
print(animals)
#result: you will get the below once its entirely deleted
# print(animals)
# ^^^^^^^
# NameError: name 'animals' is not defined
```

<br>
<br>

### 🟡 Iterating Over a Dictionary:

- You can loop through a dictionary using a for loop. By default, **looping through a dictionary will give you its keys**:

```python
#
 my_dict = {'apple': 5, 'banana': 3, 'orange': 7}
#
#
for key in my_dict:
    print(key)  # This will print each key in the dictionary

```

<br>
<br>

## Checking for Key Existence: You can check if a key exists in a dictionary using the in keyword:

```python
#
 my_dict = {'apple': 5, 'banana': 3, 'orange': 7}
#
#
#
if 'apple' in my_dict:
    print("Yes, 'apple' is a key in the dictionary.")

```

<br>

### Dictionary Methods:

- Python dictionaries have several useful **methods** such as `keys(), values(), and items()` which return views of the dictionary's keys, values, and key-value pairs respectively.

<br>
<br>

---

<br>

## 🟡 COPY

### bad copy

- ⛔ First I will see **"how not to copy dictionaries"**

```python
# 1. for this example, i will create a new dic

animalss ={
"anim1": "parrot",
"anim2": "eagle"
}
fishes ={
"anim1": "dorada",
"anim2": "espadon"
}
print(animalss)
print(fishes)
#result
# {'anim1': 'parrot', 'anim2': 'eagle'}
# {'anim1': 'dorada', 'anim2': 'espadon'}
#
#
# ---- copy -------
# it s not a good thing to create a copy in such way, because here we are not creating a copy but a reference, and it means that they are both referring to the same place in memory or the same dictionary, so if i add or remove something to animalss , the fishes will be affected, by also adding or remove to the fishes, SO that IS WHY i dont want to do it.
animalss = fishes # create a reference
```

<br>
<br>

## ✅ Copy (the correct way)

### Example 1

<br>

- i corrected it (i will be addding another examples below this one)

```python
# 1. for this example, i will create a new dic

animalss = {
    "anim1": "parrot",
    "anim2": "eagle"
}
fishes = animalss.copy()  # Create a copy of animalss
fishes["anim3"] = "turtle"
print(animalss)
print(fishes)


# result
#{'anim1': 'parrot', 'anim2': 'eagle'}
# {'anim1': 'parrot', 'anim2': 'eagle', 'anim3': 'turtle'}

```

<br>
<br>

## Example 2

🌟 in other words ITS IS LIKE ( an array) when creating a new variable and assigning to it a new value, then merging the original variable with the new one (which contains the new value)

```python
# Original dictionary
original_dict = {'a': 1, 'b': 2}

# Making a copy using the copy() method
copied_dict = original_dict.copy()

# Modifying the copied dictionary
copied_dict['c'] = 3

# Printing both dictionaries
print("Original Dictionary:", original_dict)
print("Copied Dictionary:", copied_dict)

```

<br>

- When you create a new variable and assign it a new value, you're essentially creating a separate instance of that value. Then, when you "merge" the original variable with the new one, you're combining the values from both variables into a single variable, typically by concatenation or some other form of combination.

<br>

- In Python, this concept applies not just to arrays but also to dictionaries, lists, sets, etc. For example, when you create a copy of a dictionary and modify it, you're essentially creating a new dictionary with the modified values. When you merge it with the original dictionary, you're effectively combining the key-value pairs from both dictionaries into one.

<br>

- So, yes, in a way, creating a new variable, modifying it, and then merging it with the original one is conceptually similar to working with arrays, especially when considering the idea of creating, modifying, and combining data structures.

<br>
<br>

## :yellow_circle: NESTED dictionaries

<br>

#### example 1) : https://youtu.be/zdVdqTLk8O0?feature=shared&t=1056

```python
# example : https://youtu.be/zdVdqTLk8O0?feature=shared&t=1056
#
#dictio 1
member1 = {
    'name': 'Robert Plant',
    'instrument': 'vocals'
}
#---------
#dictio 2
member2 = {
    'name': 'Jimmy Page',
    'instrument': 'guitar'
}
#---------
#dictio 3
# here we will nest the 2 dictios from above
band = {
    "member1": member1,
    "member2": member2
}
#
# show the content

print(band)
# result, the band contains the following:
# {'member1': {'name': 'Robert Plant', 'instrument': 'vocals'}, 'member2': {'name': 'Jimmy Page', 'instrument': 'guitar'}}
#
# -- level down
print(band['member1']['name'])

```

<br>
<br>

## Example 2)

#### Chatgpt examples

```python


user_tastes = {
# 🤚 Each user has a username as the key.
    "username1": {
        "pop": ["Taylor Swift", "Ariana Grande", "Ed Sheeran"],
        "rock": ["Foo Fighters", "Led Zeppelin", "Red Hot Chili Peppers"],
        "hip_hop": ["Kendrick Lamar", "Drake", "Cardi B"]
    },
    "username2": {
    # 🤚 Each username maps to a dictionary where keys are music genres (e.g., "pop", "rock", "hip_hop").

        "pop": ["Billie Eilish", "Dua Lipa", "Justin Bieber"],
        "rock": ["Queen", "The Beatles", "Nirvana"],
        "hip_hop": ["Jay-Z", "Kanye West", "Nicki Minaj"]
    },
    "username3": {
        "pop": [
    # 🤚 Each genre key maps to a list of artists that the user likes in that genre.

            "Shawn Mendes", "Bruno Mars", "Lady Gaga"],
        "rock": ["AC/DC", "Metallica", "Linkin Park"],
        "hip_hop": ["Eminem", "Post Malone", "Lil Nas X"]
    }
}


```

### You can access a user's tastes by username and then by genre. For example:

```python
# Get the tastes of username1 in pop music
username1_pop_tastes = user_tastes["username1"]["pop"]
print(username1_pop_tastes)
# Output: ['Taylor Swift', 'Ariana Grande', 'Ed Sheeran']

```

<br>
<br>

### Example 3

```python
ecommerce_shop = {
# ✋ Each top-level key represents a product category (e.g., "electronics", "clothing").

    "electronics": {
        "phones": [
           # ✋ Each category key maps to a dictionary where keys are subcategories (e.g., "phones", "laptops" under "electronics").
           #
            {"name": "iPhone 13", "price": 999},
            {"name": "Samsung Galaxy S21", "price": 899},
            {"name": "Google Pixel 6", "price": 699}
        ],
        "laptops": [
            {"name": "MacBook Pro", "price": 1499},
            {"name": "Dell XPS 15", "price": 1299},
            {"name": "HP Spectre x360", "price": 1199}
        ]
    },
    "clothing": {

        "men": [
            {"name": "T-shirt", "price": 20},
            {"name": "Jeans", "price": 50},
            {"name": "Jacket", "price": 80}
        ],
        "women": [
            {"name": "Dress", "price": 60},
            {"name": "Skirt", "price": 40},
            {"name": "Blouse",

            # ✋ Each subcategory key maps to a list of dictionaries, each representing a product with keys "name" and "price".
            "price": 30}
        ]
    }
}

```

## You can access products by navigating through categories and subcategories. For example:

```python

# Get the laptops available in the electronics category

laptops = ecommerce_shop["electronics"]["laptops"]
for laptop in laptops:
print(laptop["name"], "-", laptop["price"])

# Output:

# MacBook Pro - 1499

# Dell XPS 15 - 1299

# HP Spectre x360 - 1199
```
