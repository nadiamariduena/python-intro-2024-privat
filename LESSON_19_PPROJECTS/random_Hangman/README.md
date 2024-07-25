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
<br>

## 🟠  1. import

- import the **random** module, then import the file with the words

```python
import random
from file_withwords import words
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
