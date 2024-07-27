# 🟡 Hangman

<br>
<br>

# 🌴 Phase 1.

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

 - - **Checks** if the **guess** is **valid and unused**.

- - **Updates** the **state** based on **whether** the **guess** is **correct or not**.

- - **Provides feedback** to the **user** if the **guess** has **already** been **used or is invalid**


<br>


```python
def hangman():
    word = get_valid_word(words) # the get_valid_word is the first function. the ones that handles (selects a random word from the words list, **ensuring** it **doesn't contain hyphens or spaces**.)


    #
    #
    word_letters = set(word) #`word_letters` is a `set` of **unique letters** in the `word` to be **guessed**
    alphabet = set(string.ascii_uppercase) #`alphabet` is a `set` **of all uppercase letters**.
    used_letters = set() #`used_letters` keeps **track of letters** that the **user has guessed** so far.

```

<br>

 - - 🟢 `word` is `set` to a valid **random word**.

 - - 🟢 `word_letters` is a `set` of **unique letters** in the `word` to be **guessed**.


 - - 🟢 `alphabet` is a `set` **of all uppercase letters**.


 - - 🟢 `used_letters` keeps **track of letters** that the **user has guessed** so far.



<br>
<br>

 ### 🟡 9. Prompts the user to guess a letter

- Prompts the user to guess a letter and converts their input to uppercase for consistency with the game logic.

 <br>

```python
user_letter = input("Guess a letter: ").upper()
```


<br>
<br>


 ### 🟡 10. Handle User Input: Prompts the user to guess a letter and processes the guess:


<br>



```python

# If it is, add it to used_letters.
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)

        if user_letter in word_letters: # If the letter is in word_letters,
            word_letters.remove(user_letter) # it means the guess was correct, so remove it from word_letters.

```

<br>
<br>


### 🟠  at this point

- You can use the **INPUT**: `input()`

- But You won't receive any error messages at this stage; those will be addressed in the **next phase**.

```python
import random
from file_withwords import words
import string


#1
def get_valid_word(words):

    word = random.choice(words)
    while '_' in word or ' ' in words:
        word = random.choice(words)

    return word


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    #
    #
    #
    user_letter = input("Guess a letter: ").upper()

    #
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)

        if user_letter in word_letters:
            word_letters.remove(user_letter)

# I am going to add this block here below, but it s not going to show the messages yet
# -------------
    # elif user_letter in used_letters:
    #     print("You have already used that character. PLEASE try again.")


    # else:
    #     print("Invalid character. Please try again")
# -------------



user_input = input("Type Something: ")
print(user_input)

if __name__ == '__main__':
    hangman()
```

<br>

#### Run the code `python main.py`

<br>



- you will be requested to type a letter **twice**

```bash
Type Something: e
e
GUESS A LETTER: f
```

### 🟢 output

>It will not do anything (because we need to implement the next phase)

<br>
<br>

## 🟠 Another `WHILE` Loop

<br>

```python
while len(word_letters) > 0:
```

- - Now that we can get the user **INPUT**, I want the **user** to be able to keep guessing **UNTIL** they the **get the WORD**

<br>

- -  >Every time I am removing a letter from **word letters**, which is a **set()** of the letters of the **word** (list/Array) that we haven't seen yet, I am just keep decrementing that


- - So the condition that I have to satisfy for when the user gets all the letters in the words in the word, is:


🟧 **while** the **length** of **word_letters** list/array is greater `>` than zero, I am going to keep iterating

```python
# similar to js but different syntax len for length
while len(word_letters) > 0:
# react
#if (wordLetters.length > 0) {
```
<br>

- 🔴 You have to indent the previous code, as this new **while** loop will be position at the top of the **previous condition**

<br>


```python
 # 4
  used_letters = set()
     #           __|**|__   WHILE    __ |**|_
    #
    # 10 while the  length of word_letters list/array is greater `>` than zero, I am going to keep iterating
    while len(word_letters) > 0:

    # |**| KEEP iterating until they find - all the letters
        # 5 the letters the user will be adding
        user_letters = input("GUESS A LETTER: " ).upper()
```
<br>
<br>

### Like so

```python
 # 4
  used_letters = set()
     #           __|**|__   WHILE    __ |**|_
    #
    # 10 while the  length of word_letters list/array is greater `>` than zero, I am going to keep iterating
    while len(word_letters) > 0:

    # |**| KEEP iterating until they find - all the letters
        # 5 the letters the user will be adding
        user_letters = input("GUESS A LETTER: " ).upper()
            # 6)
        if user_letters in alphabet - used_letters:
```

<br>
<br>

## 🟠 `Join` the word

- `.join` will turn the list into a **string**, separated by whatever the string is.

-  you can add **white spaces, symbols, letters** , example:

-  `' '.join` or `', '.join` or `'/ '.join` etc...


```python
print("You have used these letters: ", ' '.join(used_letters))
#output
"a", "b",
```

<br>
<br>

## 🟠 Create a NEW LIST of words

#### Purpose:

### 🔴 The code generates a new LIST, `word_list`, where each character in word is checked to see if it’s present in the collection `used_letters`.

<br>


- - **If** the **letter** is **in** `used_letters`, it is **included as-is** in `word_list`.

- - **If** the **letter** is **not** in `used_letters`, an **underscore** ("_") is **included** in its place.


- -  By using **dashes** (you can use other symbols), the **user will know** what are the **words they haven't** guessed. example: `'h', 'e', 'l', 'l', '_'`

<br>

```python
 #- The code generates a new list, word_list,
 # - where each character in word is checked to see if it’s present in the collection used_letters.
word_list = [letter if letter in used_letters else "_" for letter in word]
# If the letter is in used_letters, it is included as-is in word_list, ELSE...
# If the letter is not in used_letters, an underscore ("_") is included in its place.
```

<br>
<br>

### 🟠 Now I am going to get this "new WORD list" and I am going to `.join()` it again, so to convert it and to have this result: `"h e l l _"`


```python
    # 13
        print("Current word:", " ".join(word_list))
        # This part converts the word_list from a list of characters into a single string with each character separated by a space. For example, if word_list is ['h', 'e', 'l', 'l', '_'], " ".join(word_list) will produce "h e l l _"
```

<br><br>

## 🟣 Testing:
- Run your code: `python main.py`

```python

import random
import string
from words import words




def function_1_(words):

    word = random.choice(words)
    while "-" in word or " " in words:
        word = random.choice(words)
    return word.upper()



def function_2_hangman():


    word =  function_1_(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what user has guessed





    while len(word_letters) > 0:

        print("You have used these letters: ", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in word]

        print("Current word:", " ".join(word_list))



        user_letters = input("GUESS A LETTER: " ).upper()

        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)


            if user_letters in word_letters:
                word_letters.remove(user_letters)

            else:
                print('\nYour letter, ', user_letters, 'is not in the word.')



        elif user_letters in used_letters:
            print("You have already used that character. Please try again")
        else:
            print("Invalid character. Please try again")



# ---- END ----
user_input = input("Type Something: ")
print(user_input)

if __name__ == '__main__':

    function_2_hangman()


```

<br>
<br>
<br>

# 🔴 Issue:

#### 🟠 At the end of the first phase of this **Hangman** exercise, I encountered an issue where I couldn't get the desired result.

<br>

- I **typed all** the **letters** of the **alphabet** and it didnt seem to find a match.


 >No matter what word I used, **the program didn't retrieve** any **words** from the file.

<br>

```bash
Type Something: a
a
You have used these letters:
Current word: _ _ _ _
GUESS A LETTER: s
You have used these letters:  S
Current word: _ _ _ _
GUESS A LETTER: e
You have used these letters:  S E
Current word: _ _ _ _
GUESS A LETTER: r
You have used these letters:  R S E
Current word: _ _ _ _
GUESS A LETTER: t
You have used these letters:  R T S E
Current word: _ _ _ _
GUESS A LETTER: z
You have used these letters:  Z S R E T
Current word: _ _ _ _
GUESS A LETTER: u
You have used these letters:  Z U S R E T
Current word: _ _ _ _
GUESS A LETTER: i
You have used these letters:  Z U S R E I T
Current word: _ _ _ _
GUESS A LETTER: o
You have used these letters:  Z U S O R E I T
Current word: _ _ _ _
GUESS A LETTER: o
You have already used that character. Please try again
You have used these letters:  Z U S O R E I T
Current word: _ _ _ _
GUESS A LETTER: p
You have used these letters:  Z U S P O R E I T
Current word: _ _ _ _
GUESS A LETTER: a
You have used these letters:  A Z U S P O R E I T
Current word: _ _ _ _
GUESS A LETTER: s
You have already used that character. Please try again
You have used these letters:  A Z U S P O R E I T
Current word: _ _ _ _
GUESS A LETTER: d
You have used these letters:  A Z U S P O R D E I T
Current word: _ _ _ _
GUESS A LETTER: f
You have used these letters:  A Z U S P O R F D E I T
Current word: _ _ _ _
GUESS A LETTER: g
You have used these letters:  A Z U S P O G R F D E I T
Current word: _ _ _ _
GUESS A LETTER: h
You have used these letters:  A Z U S P O G R F H D E I T
Current word: _ _ _ _
GUESS A LETTER: j
You have used these letters:  A Z U S P O G J R F H D E I T
Current word: _ _ _ _
GUESS A LETTER: k
You have used these letters:  A Z U S P O K G J R F H D E I T
Current word: _ _ _ _
GUESS A LETTER: l
You have used these letters:  A Z U S P L O K G J R F H D E I T
Current word: _ _ _ _
GUESS A LETTER: l
You have already used that character. Please try again
You have used these letters:  A Z U S P L O K G J R F H D E I T
Current word: _ _ _ _
GUESS A LETTER: y
You have used these letters:  A Z U S P L O K G J R F H D E I Y T
Current word: _ _ _ _
GUESS A LETTER: x
You have used these letters:  L J F E Z S X K R D I Y U T A P G H O
Current word: _ _ _ _
GUESS A LETTER: c
You have used these letters:  L J F E Z S C X K R D I Y U T A P G H O
Current word: _ _ _ _
GUESS A LETTER: v
You have used these letters:  L J F E Z S C X K R D I Y U T A P V G H O
Current word: _ _ _ _
GUESS A LETTER: b
You have used these letters:  L J F E B Z S C X K R D I Y U T A P V G H O
Current word: _ _ _ _
GUESS A LETTER: n
You have used these letters:  L J F E B Z S C X K R D I Y U T A P V G N H O
Current word: _ _ _ _
GUESS A LETTER: m
You have used these letters:  L J F E B Z S C X K R D I Y U T A M P V G N H O
Current word: _ _ _ _
GUESS A LETTER:

```

<br>
<br>

## 🔴 Reason:

### ✅: the import



#### ⚠️ When importing data from other files, it's important to consider the `file type`.




<br>

#### The problem:

 This problem was due to the import statement I used:

`from file_withwords import words`, where `file_withwords` referred to `file_withwords.py`.

>🤚 I think i already had a similar issue when retrieving **data** from either a `json or js` **file** to use in a **.map** operation


<br>

#### Solution:

-  - I had the **choice to either use** the **long name** or **rename** the **file** to simply `words`. I chose the latter:

```python
# ✋
from words import words
```

<br>
<br>

### Test it again

#### output

```bash
Type Something: a
a
You have used these letters:
Current word: - - - - - - - -
GUESS A LETTER: b

Your letter,  B is not in the word.
You have used these letters:  B
Current word: - - - - - - - -
GUESS A LETTER: p

Your letter,  P is not in the word.
You have used these letters:  B P
Current word: - - - - - - - -
GUESS A LETTER: h
You have used these letters:  B H P
Current word: H - - - - - - -
GUESS A LETTER: a
You have used these letters:  B H A P
Current word: H - - - - A - -
GUESS A LETTER: e
You have used these letters:  E B H P A
Current word: H E - - - A - -
GUESS A LETTER: r

Your letter,  R is not in the word.
You have used these letters:  E B H P R A
Current word: H E - - - A - -
GUESS A LETTER: t
You have used these letters:  E B H T P R A
Current word: H E - - T A - T
GUESS A LETTER: s
You have used these letters:  E B H T P R S A
Current word: H E S - T A - T
GUESS A LETTER: m

Your letter,  M is not in the word.
You have used these letters:  E B M H T P R S A
Current word: H E S - T A - T
GUESS A LETTER: h
You have already used that character. Please try again
You have used these letters:  E B M H T P R S A
Current word: H E S - T A - T
GUESS A LETTER: o

Your letter,  O is not in the word.
You have used these letters:  E B M H T O P R S A
Current word: H E S - T A - T
GUESS A LETTER: p
You have already used that character. Please try again
You have used these letters:  E B M H T O P R S A
Current word: H E S - T A - T
GUESS A LETTER: q

Your letter,  Q is not in the word.
You have used these letters:  E Q B M H T O P R S A
Current word: H E S - T A - T
GUESS A LETTER: d

Your letter,  D is not in the word.
You have used these letters:  E D Q B M H T O P R S A
Current word: H E S - T A - T
GUESS A LETTER: c

Your letter,  C is not in the word.
You have used these letters:  E D Q B M C H T O P R S A
Current word: H E S - T A - T
GUESS A LETTER: v

Your letter,  V is not in the word.
You have used these letters:  E D Q B M C H T O P R V S A
Current word: H E S - T A - T
GUESS A LETTER: b
You have already used that character. Please try again
You have used these letters:  E D Q B M C H T O P R V S A
Current word: H E S - T A - T
GUESS A LETTER: n
You have used these letters:  N E D Q B M C H T O P R V S A
Current word: H E S - T A N T
GUESS A LETTER:
Invalid character. Please try again
You have used these letters:  N E D Q B M C H T O P R V S A
Current word: H E S - T A N T
GUESS A LETTER: i
```

### 🌈 Now it works!!1


<br>
<br>
<br>

---


<br>
<br>


# 🌴 Phase 2.

### 🌞 Implementing Lives and Success Message


 This will make the game more interactive and rewarding as players work to complete the word while managing their lives.

<br>

<br>

#### 1.  Add Lives:

- -   Introduce a **mechanism to track** and display the **number** of remaining **lives**. Each incorrect guess should decrement the count of lives.

<br>

#### 2. Success Message:

-  - When the user successfully completes the word by finding all the letters, the game should display a congratulatory message or visual to indicate their victory.


<br>
<br>


### 🟧 <u>Add Lives</u>  :


#### Begin by initializing the lives counter in your game. For example:

```python
lives = 0
```

- - 🟦  This line **sets up** a **variable** named **lives** to **keep track** of **how many attempts** the **player has left**.

- - 🫐 You'll need to update this counter throughout the game to reflect the number of incorrect guesses.


