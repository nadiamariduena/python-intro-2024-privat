# 🟡 Hangman

<br>
<br>

### 🟦 Structure

```javascript
project_folder/
     └── file_withwords.py
     └── helper.py
     └── main.py
```

<br>

## Explanation

- You can explain this by using an analogy of picking toys from a box. Initially, you pick a toy (**first** `random.choice(words)`), but **if the 🧸 toy has a mark** or is **broken** 🧶 *(like a word with underscores or spaces)*, you **put it back** and **pick another** toy 🧸 (**second** `random.choice(words)`) **until you find a toy** (word) that's perfect (no marks or broken parts).

<br>
<br>

## 🟠  0. import

- import the **random** module, then import the file with the words

```python
import random
from file_withwords import words
```

<br>
<br>

## 🟠 1. Retrieve the `words` from the `file_withwords`

- pass the parameter **words**

```python
def get_valid_word(words):
```

<br>
<br>

## 🟠 2. Initialization:

####  Retrieve the words from the `file_withwords.py`

-  - This is the first random selection which picks a word to start with.

<br>

```python
#1
def get_valid_word():
    #
    # 🔸 Initialization:
    #  This is the first random selection which picks a word to start with.
    word = random.choice(words)


```


<br>
<br>

## 🟠 3.  Validation Loop:

####  - The while loop checks the selected word (word) to ensure it does not contain underscores ('_') or spaces (' ').

<br>


- -  `while _ or space ''` **is in the word**,  **keep choosing a word** (If the selected word contains either an underscore or a space, the loop continues to randomly select another word from words until a valid word (without underscores or spaces) is found.)


<br>

```python
  # 🔸 Validation Loop

    while '_' in word or ' ' in words:
```
<br>

<br>

## 🟠 4.  Second `random.choice(words)`:

### Second Random Selection (random.choice(words) within the loop):

<br>

- - Inside the while loop, when word is found to contain an underscore or a space, random.choice(words) is used again to pick another random word from the list words.

<br>

- - 🧶  This process repeats until a word is selected that meets the condition of not containing underscores or spaces.


```python
word = random.choice(words)
```

<br>

<br>

## 🟠 5.  `return word`:

### Once a valid word (one that does not contain underscores or spaces) is found, the function returns this word.


```python
return word
```


<br>

<br>

 ### 🟡 6. Select a random word from the words list

<br>

- This function selects a random word from the words list, **ensuring** it **doesn't contain hyphens or spaces**.


- - 🔶 If a word with these characters is chosen, it keeps selecting until it finds a valid word.

<br>

```python
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

```

<br>
<br>
<br>
<br>


 ### 🟡 7.


 -  Import `string` ,  to **access** the uppercase **alphabet**



```python
import random
from file_withwords import words
import string ✋ # import this
#
```
<br>
<br>

 ### 🟡 8. Initialize the Game:

 -  - 🟠 It selects a valid word for the game, initializes the sets for the letters in the word, the alphabet, and used letters.

 - - #### 🟦 Purpose:

 <br>
