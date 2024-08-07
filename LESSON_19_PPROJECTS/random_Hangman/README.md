# 🟡 Hangman

#### 🫐 Course developed by Kylie Ying.

[min: 24:26 | 12 Beginner Python Projects - Coding Course](https://youtu.be/8ext9G7xspg?si=BSVIdjwSDysNzP_F&t=1466)


#### repo: https://github.com/kying18/hangman

<br>
<br>

# 🌴 Phase 1.

### 🟧 Structure

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

<br>

## 🫐 Alphabet

<br>


```python
    alphabet = set(string.ascii_uppercase) #`alphabet` is a `set` **of all uppercase letters**.
```

<br>

 The alphabet **set**, which contains all uppercase letters of the English alphabet `(set(string.ascii_uppercase))`, is **used to define** the **valid range** of **characters** that are **considered acceptable input** for **your application**.


<br>

 ### 🍰 In other words, it sets the boundaries for what is considered a valid letter.

<br>

 #### 🟣 QUESTION: So it controls that it s on proper British alphabet, and not (a example: sanskrit)?

 #### ✅  Chatgpt:

Yes, exactly! The alphabet set ensures that any letters or characters you're working with are within a predefined set of valid letters—in this case, the English alphabet.

#### Here's how it works in the context you described:

🔶 **Validating Against the English Alphabet:**

- -  By defining alphabet as `set(string.ascii_uppercase)`, **you**’re **explicitly specifying** that **only** the **uppercase English letters (A-Z)** are **considered valid**.

- - This is useful if your application is designed to work specifically with the English alphabet.


<br>

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


### 🟠 <u>Add Lives</u>  :


#### Begin by initializing the lives counter in your game. For example:

```python
lives = 0
```

- - 🟦  This line **sets up** a **variable** named **lives** to **keep track** of **how many attempts** the **player has left**.

<br>

- - ⚠️ You'll **need** to **update** this **counter** throughout the game **to reflect** the **number** of **incorrect guesses**.

<br>

### add it on top of the while loop

```python

    lives = 0

    #
    #
    # 10 while the  length of word_letters list/array is greater `>` than zero, I am going to keep iterating
    while len(word_letters) > 0:
```

<br>
<br>

## 🟠 Add a new conditional

#### TAKES AWAY a life, Track Lives:

- -  You’ll need to update the number of lives remaining based on the player's guesses. For instance:

```python
lives = lives - 1
# ✋ Decrements the lives counter by 1 for each incorrect guess

```

<br>

### Like so:

```python
         ## 8 If the user_letters is 'in' the word letters...
            if user_letters in word_letters:
                # 9 to the set of word_letters, remove( the user_letters)
                word_letters.remove(user_letters)

            # ✋ new conditional
            else:
                lives = lives - 1 # Takes away a life if wrong
                print("Letter is not in word")

```

<br>
<br>

### 🟠 Now modify the below line


#### Before

```python


  print("You have used these letters: ", ' '.join(used_letters))
# 11 `.join` will turn the list into a **string**, separated by whatever the string is `you can add , white spaces, etc...`
```
#### After

```python
# 16 - ✋ Shows Remaining Lives: It tells you how many lives (or chances) you have left.
print('You have', lives,  'lives left and you have used these letters: ', ' '.join(used_letters))
# The join part puts all the guessed letters together with spaces in between, so it’s easy to see which letters you’ve tried.
```

<br>
<br>

### 🟠 Now modify this




#### Before



```python
# 10 while the  length of word_letters list/array is greater `>` than zero, I am going to keep iterating
  while len(word_letters) > 0:
```

<br>

#### After

### the game will keep going as long as there are letters left to guess and you still have lives remaining.

- The game continues only if both conditions are true at the same time.


```python
 # 17 - the game will keep going as long as there are letters left to guess and you still have lives remaining.
    while len(word_letters) > 0 and lives > 0:
# The game continues only if both conditions are true at the same time.

```

<br>
<br>
<br>
<br>

# 🟡 Letter

#### This line of code will generate a new list where each letter of the random word is checked against a list of guessed letters.

- - If the letter is found in the guessed letters, it will be included as is; if not, it will be replaced with an underscore _. This allows you to see which letters you've guessed correctly and which ones are still hidden

-  the goal is to create a new list (word_list) based on whether each letter in a word should be shown or hidden

####  condition to filter items:

```python
word_list = [letter if letter in used_letters else "_" for letter in word]
# - Imagine you have a secret word generated by the computer,
# and you want to reveal some letters of this word based on whether they are in a list of "guessed" letters.
```
<br>

- - If letter is found in used_letters, it is added to the word_list.

- - If letter is not in used_letters, the character "_" is added instead.

<br>

### 🟦 Create a new variable

- I will start by creating a **NEW** variable, this variable **word_list** will enclose the logic for a scenario of not finding a letter within the random word choose by the computer

```python
word_list =
```

<br>

### 🟦 Assign to the variable the below logic

- - ✋ It is necessary to provide the alternative value when the condition  is not met, 🫴 🧶 **like when a letter isn't found/allowed or it's not the letter that the computer randomly used**

<br>

```python
# 🔶 "Check if the letter is allowed.
# - If yes, keep it; if no, put an underscore."
word_list = [letter if letter in used_letters else "_" for letter in word]
```

<br>

- So, you need to provide an alternative value (like `_`) **for** the case **when** the **letter isn’t allowed** or **isn’t what you’re looking for**. This way, the computer knows what to do whether the letter is allowed or not.


<br>
<br>

### 🔴 Why Not Just letter if?

### `letter if letter`

```python
letter if letter ...
```

- **If you only** write **letter if**...

- - 🔴 **it’s like saying:** ✋ <u>"Just give me the letter."</u>  **You haven’t said what to do if the letter isn’t allowed**.

#### 🌈 The code needs both parts (the condition and the alternative) to decide what to do in both cases.


```python
# 🔶 "Check if the letter is allowed.
# - If yes, keep it; if no, put an underscore."
word_list = [letter if letter in used_letters else "_" ...
```

<br>
<br>
<br>
<br>



## 🟠 Decreases  `lives by 1`

<br>

- `lives = lives - 1`: This line **decreases the player's number of lives by 1**.


#### 🔴 Each incorrect guess costs the player one life.

```python
if user_letters in alphabet - used_letters:
    used_letters.add(user_letters)
    if user_letters in word_letters:
        word_letters.remove(user_letters)
    else:
        lives = lives - 1
        print("Letter is not in word")
        print('\nYour letter,', user_letters, 'is not in the word.')
#________
```

<br>

- Add the prints, showing the **"`user_letters`, 'is not in the word.'"**



<br>
<br>
<br>
<br>

## 🟠 Last condition `if lives == 0`

- checks the player's remaining lives and provides feedback based on whether the player has won or lost the game:

```python

    # 18 Show the failure or succes messages
    if lives == 0:
        print("__💀__YOU Died. The word was", word )

    else:
        print("You Guessed the word🌈 ", word, "!!")



# ---- END ----
```

<br>
<br>
<br>


# 🟣 Testing:


- Run your code: `python main.py`

```python
#
# intro: imports
# import the random, string, and file containing the list of words
import random
import string
# when importing data from other files, keep in mind that the file type, is important
# because at the end of the first phase of this hangman exercise, i couldnt get the result i wanted  (no matter what word i used, it simply didnt get any word from the file of words), and was because the importing, i had this: "from file_withwords import words" and this file_withwords came from the file_withwords.py, so i ad the choice to either use the long name, or change the name to simply words, so to import it like "words" like here below(that is what i did)
from words import words




def function_1_(words):
    word = random.choice(words)
    while "_" in word or " " in words:
        word = random.choice(words)
    return word

#------------
#  2)  create the function to init the hangman game
def function_2_hangman():


    word =  function_1_(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()




    # ------💗
    lives = 10
    # ------💗

    while len(word_letters) > 0 and lives > 0:


        print('You have', lives,  '❤️‍🔥lives left and you have used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word:", ' '.join(word_list))



        # ----
        user_letters = input("GUESS A LETTER: " ).upper()

        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)


            # 15
            else:
                lives = lives - 1
                print("Letter is not in word")
                print('\nYour letter,', user_letters, 'is not in the word.')



        elif user_letters in used_letters:
            print("You have already used that character. Please try again")
        else:
            print("Invalid character. Please try again")



    # ____ 🟦  KEEP iterating until they find - all the letters

    if lives == 0:
        print("__💀__YOU Died. The word was", word )
    else:
        print("You Guessed the word🌈 ", word, "!!")



# ---- END ----
user_input = input("Type Something: ")
print(user_input)

if __name__ == '__main__':
    #
    # call the function with the condition logic
    function_2_hangman()


```


<br>
<br>
<br>

# 🔴 Issue:


- I **typed all** the **letters** of the **alphabet** and it didnt seem to find a match.


 >No matter what word I used, **the program didn't retrieve** any **words** from the file.

<br>

```bash
Letter is not in word

Your letter, O is not in the word.
You have 30 ❤️‍🔥lives left and you have used these letters:  O T E I U Z R
Current word: _ _ _ _ _ _ _
GUESS A LETTER: PP
Invalid character. Please try again
You have 30 ❤️‍🔥lives left and you have used these letters:  O T E I U Z R
Current word: _ _ _ _ _ _ _
GUESS A LETTER: P
Letter is not in word

Your letter, P is not in the word.
You have 29 ❤️‍🔥lives left and you have used these letters:  O T E I U Z R P
Current word: _ _ _ _ _ _ _
GUESS A LETTER: Y
Letter is not in word

Your letter, Y is not in the word.
You have 28 ❤️‍🔥lives left and you have used these letters:  O Y T E I U Z R P
Current word: _ _ _ _ _ _ _
GUESS A LETTER: X
Letter is not in word

Your letter, X is not in the word.
You have 27 ❤️‍🔥lives left and you have used these letters:  O Y T E I U Z X R P
Current word: _ _ _ _ _ _ _
GUESS A LETTER: C
Letter is not in word

Your letter, C is not in the word.
You have 26 ❤️‍🔥lives left and you have used these letters:  O Y T E I U Z C X R P
Current word: _ _ _ _ _ _ _
GUESS A LETTER: VB
Invalid character. Please try again
You have 26 ❤️‍🔥lives left and you have used these letters:  O Y T E I U Z C X R P
Current word: _ _ _ _ _ _ _
GUESS A LETTER: N
Letter is not in word

Your letter, N is not in the word.
You have 25 ❤️‍🔥lives left and you have used these letters:  O Y T E I U Z C N X R P
Current word: _ _ _ _ _ _ _
GUESS A LETTER: M
Letter is not in word

Your letter, M is not in the word.
You have 24 ❤️‍🔥lives left and you have used these letters:  O Y M T E I U Z C N X R P
Current word: _ _ _ _ _ _ _
GUESS A LETTER: M,
Invalid character. Please try again
You have 24 ❤️‍🔥lives left and you have used these letters:  O Y M T E I U Z C N X R P
Current word: _ _ _ _ _ _ _
GUESS A LETTER: M
You have already used that character. Please try again
You have 24 ❤️‍🔥lives left and you have used these letters:  O Y M T E I U Z C N X R P
Current word: _ _ _ _ _ _ _
GUESS A LETTER: L
Letter is not in word

Your letter, L is not in the word.
You have 23 ❤️‍🔥lives left and you have used these letters:  O Y M T E I U Z C N X L R P
Current word: _ _ _ _ _ _ _
GUESS A LETTER: D
Letter is not in word

Your letter, D is not in the word.
You have 22 ❤️‍🔥lives left and you have used these letters:  O D Y M T E I U Z C N X L R P
Current word: _ _ _ _ _ _ _
GUESS A LETTER: F
Letter is not in word

Your letter, F is not in the word.
You have 21 ❤️‍🔥lives left and you have used these letters:  O D Y F M T E I U Z C N X L R P
Current word: _ _ _ _ _ _ _
GUESS A LETTER: G
Letter is not in word

Your letter, G is not in the word.
You have 20 ❤️‍🔥lives left and you have used these letters:  O D Y F M T E G I U Z C N X L R P
Current word: _ _ _ _ _ _ _
GUESS A LETTER: H
Letter is not in word

Your letter, H is not in the word.
You have 19 ❤️‍🔥lives left and you have used these letters:  O D Y F M T E G H I U Z C N X L R P
Current word: _ _ _ _ _ _ _
```

<br>
<br>

## 🟫 The Problem

At the end of the second phase of the game, **I encounter** an issue where letters I typed do not seem to be recognized correctly, even though I receive messages about the **number of lives and chances remaining**.

<br>

- 🌈 The problem occurs because the **game is not correctly handling the case of the letters**. Specifically, if the chosen word is not **converted to uppercase**, your lowercase inputs will not match, and the game will not recognize them properly.

<br>


#### before

```python

 return word

```

#### after

```python
return word.upper()
```


<br>
<br>
<br>

# Le code


```python
#
# intro: imports
# import the random, string, and file containing the list of words
import random
import string
# when importing data from other files, keep in mind that the file type, is important
# because at the end of the first phase of this hangman exercise, i couldnt get the result i wanted  (no matter what word i used, it simply didnt get any word from the file of words), and was because the importing, i had this: "from file_withwords import words" and this file_withwords came from the file_withwords.py, so i ad the choice to either use the long name, or change the name to simply words, so to import it like "words" like here below(that is what i did)
from words import words



#  1
# create the function to grab the words from the list
def function_1_(words):

#   1.a grab the data coming from the 'words'
## Pick a random word from the list

    word = random.choice(words)

    # 1.b loop: add the condition in which you tell it:
    ## If the word has underscores or spaces...

    while "_" in word or " " in words:

        # 1.c # ... Pick a new word
        word = random.choice(words)


    # 1.d # Give back the chosen word

    # return word
    return word.upper() #🔴  if the chosen word is not **converted to uppercase**, your lowercase inputs will not match

#------------
#  2)  create the function to init the hangman game
def function_2_hangman():

    #1 make the connection to the first function
    word =  function_1_(words)

    #2 TAKES the 'word' and turns it into a special list where each letter is only listed

    word_letters = set(word)
    #3 This line creates a list of all the letters in the alphabet, from A to Z. It’s like having a list of all the letters you can use to guess the secret word.
    alphabet = set(string.ascii_uppercase)
    # 4 This line starts with an empty list where you can keep track of the letters you’ve already guessed. At first, it’s empty because you haven’t guessed any letters yet.
    used_letters = set()

    #14 This line "sets up" a "variable" named "lives" to "keep track" of "how many attempts" the "player has left".
    lives = 37
    # lives = 0 test it
    #
    #
    # 10 while the  length of word_letters list/array is greater `>` than zero, I am going to keep iterating
    # while len(word_letters) > 0:
    # 17 - the game will keep going as long as there are letters left to guess and you still have lives remaining.
    while len(word_letters) > 0 and lives > 0:
        # The game continues only if both conditions are true at the same time.


        #
        # 11 `.join` will turn the list into a **string**, separated by whatever the string is `you can add , white spaces, etc...`
        # print("You have used these letters: ", ' '.join(used_letters))
        #
        # 16 Shows Remaining Lives: It tells you how many lives (or chances) you have left.
        print('You have', lives,  'lives left and you have used these letters: ', ' '.join(used_letters))

        # -12 The code generates a new list, word_list,
        # - where each character in word is checked to see if it’s present in the collection used_letters.
        word_list = [letter if letter in used_letters else "_" for letter in word]
        # If the letter is in used_letters, it is included as-is in word_list, ELSE...
        # If the letter is not in used_letters, an underscore ("_") is included in its place.

        # 13 Now I am going to get this "new WORD list" and I am going to `.join()` it again(like i did it previously)
        print("Current word:", ' '.join(word_list))
        # This part converts the word_list from a list of characters into a single string with each character separated by a space. For example, if word_list is ['h', 'e', 'l', 'l', '_'], " ".join(word_list) will produce "h e l l _"


        # 5 add var, (this var will be the letter the user will type) and assign message input to "guess a letter:" , to uppercase()
        user_letters = input("GUESS A LETTER: " ).upper()

        # 6) Check if the user letter is 'in' the alphabet, and hasnt - ' been used yet (used_letters)
        if user_letters in alphabet - used_letters:
            # 7) to the set of used letters '.add' the ( the user letter)
            used_letters.add(user_letters)
            ## 8 If the user_letters is 'in' the word letters...
            if user_letters in word_letters:
                # 9 to the set of word_letters, remove( the user_letters)
                word_letters.remove(user_letters)


            # 15
            else:
                lives = lives - 1 # Takes away a life if wrong
                #This line of code subtracts 1 from the lives variable whenever the player makes an incorrect guess. It effectively reduces the number of remaining attempts.
                print("Letter is not in word")
                print('\nYour letter,', user_letters, 'is not in the word.')



        elif user_letters in used_letters:
            print("You have already used that character. Please try again")

        else:
            print("Invalid character. Please try again")



    # ____ 🟦  KEEP iterating until they find - all the letters



    # 18 Show the failure or succes messages
    if lives == 0:
        print("__💀__YOU Died. The word was", word )

    else:
        print("You Guessed the word🌈 ", word, "!!")



# ---- END ----
# user_input = input("Type Something: ")
# print(user_input)

if __name__ == '__main__':
    #
    # call the function with the condition logic
    function_2_hangman()

```

### 🟣 Test OUTPUT

```bash
Your letter, S is not in the word.
You have 17 lives left and you have used these letters:  G A I E V T O Y N Q X J M K Z F B S C R W H P U
Current word: _ R I N K
GUESS A LETTER: d
You Guessed the word🌈  DRINK !!
```


<br>
<br>
<br>

---


<br>
<br>


# 🌴 Phase 3.


# 🟡 Hangman Visual

### Third Phase: Implementing Visual Feedback for Hangman


- In the third phase of developing The Hangman game, I will focus on creating a visual representation to indicate the game's status.

- - This visual will provide feedback on the player's progress and the outcome of the game, enhancing the overall user experience.

#### Objective


I will develop a visual display that shows:

- - **The hangman figure:** A graphical representation that evolves as the player makes incorrect guesses.

- - **Success and Failure States:** Clear visuals to indicate whether the player has won or lost the game.

<br>



<br>
<br>

### 🟠 Create a file and add the following

```python

lives_visual_dict = {
        0: """
                ___________
               | /        |
               |/        ( )
               |          |
               |         / \\
               |
           """,
        1: """
                ___________
               | /        |
               |/        ( )
               |          |
               |         /
               |
            """,
        2: """
                ___________
               | /        |
               |/        ( )
               |          |
               |
               |
            """,
        3: """
                ___________
               | /        |
               |/        ( )
               |
               |
               |
            """,
        4: """
                ___________
               | /        |
               |/
               |
               |
               |
            """,
        5: """
                ___________
               | /
               |/
               |
               |
               |
            """,
        6: """
               |
               |
               |
               |
               |
            """,
        7: "",
    }
```



<br>
<br>

### 🟠 import the visuals file

```python
from hangman_visual import lives_visual_dict
```

<br>
<br>

### And use it here

```python
     # 19 hangman VISUAL
        print(lives_visual_dict[lives])

        # 13 Now I am going to get this "new WORD list" and I am going to `.join()` it again(like i did it previously)

```

### and here:

```python
    # 18 Show the failure or succes messages
    if lives == 0:
        # 20 🔴 hangman VISUAL
        print(lives_visual_dict[lives])
        print("__💀__YOU Died. The word was", word )

    else:
        print("You Guessed the word🌈 ", word, "!!")

```

<br>
<br>

### 🟣 Testing

- python main.py

```python


import random
from words import words
from hangman_visual import lives_visual_dict
import string



def function_1_(words):
    word = random.choice(words)
    while "_" in word or " " in words:
        word = random.choice(words)
    # return word
    return word.upper() #🔴  if the chosen word is not **converted to uppercase**, your lowercase inputs will not match

#------------
#  2)  create the function to init the hangman game
def function_2_hangman():

    #1 make the connection to the first function
    word =  function_1_(words)

    #2

    word_letters = set(word)
    #3
    alphabet = set(string.ascii_uppercase)
    # 4
    used_letters = set()

    #14 This line "sets up" a "variable" named "lives" to "keep track" of "how many attempts" the "player has left".
    lives = 7
    # lives = 0 test it
    #
    #
    # 10 while the  length of word_letters list/array is greater `>` than zero, I am going to keep iterating
    # while len(word_letters) > 0:
    # 17 -
    while len(word_letters) > 0 and lives > 0:
        # The game continues only if both conditions are true at the same time.


        #
        # 11 `.join` will turn the list into a **string**, separated by whatever the string is `you can add , white spaces, etc...`
        # print("You have used these letters: ", ' '.join(used_letters))
        #
        # 16 Shows Remaining Lives:
        print('You have', lives,  'lives left and you have used these letters: ', ' '.join(used_letters))

        # -12 If letter is found in used_letters, it is added to the word_list.
        word_list = [letter if letter in used_letters else "_" for letter in word]
        # If the letter is in used_letters, it is included as-is in word_list, ELSE...
        # If the letter is not in used_letters, an underscore ("_") is included in its place.


        # 19 hangman VISUAL
        print(lives_visual_dict[lives])

        # 13
        print("Current word:", ' '.join(word_list))


        # 5
        user_letters = input("GUESS A LETTER: " ).upper()

        # 6)
        if user_letters in alphabet - used_letters:
            # 7) to the set of used letters '.add' the ( the user letter)
            used_letters.add(user_letters)
            ## 8 If the user_letters is 'in' the word letters...
            if user_letters in word_letters:
                # 9 to the set of word_letters, remove( the user_letters)
                word_letters.remove(user_letters)


            # 15
            else:
                lives = lives - 1 # Takes away a life if wrong
                #This line of code subtracts 1 from the lives variable whenever the player makes an incorrect guess. It effectively reduces the number of remaining attempts.
                print("Letter is not in word")
                print('\nYour letter,', user_letters, 'is not in the word.')



        elif user_letters in used_letters:
            print("You have already used that character. Please try again")

        else:
            print("Invalid character. Please try again")



    # ____ 🟦  KEEP iterating until they find - all the letters



    # 18 Show the failure or succes messages
    if lives == 0:
        # 20 hangman VISUAL
        print(lives_visual_dict[lives])
        print("__💀__YOU Died. The word was", word )

    else:
        print("You Guessed the word🌈 ", word, "!!")



# ---- END ----
# user_input = input("Type Something: ")
# print(user_input)

if __name__ == '__main__':
    #
    # call the function with the condition logic
    function_2_hangman()

```

<br>
<br>

## 🔴 Error

```python
You have 37 lives left and you have used these letters:
Traceback (most recent call last):
  File "main.py", line 137, in <module>
    function_2_hangman()
  File "main.py", line 78, in function_2_hangman
    print(lives_visual_dict[lives])
KeyError: 37
```

<br>

<br>

## 🟫 Reason

- If your **game uses** a **variable number of lives (like 25)**, you need to **make sure** this value is a key in the dictionary. (value KEY?  🔴**if there are 7 keys** within the file of the visuals, you need to have **lives = 7**)

```python
lives_visual_dict = {
        0: """
                ___________
               | /        |
               |/        ( )
               |          |
               |         / \\
               |
           """,
        1: """
                ___________
               | /        |
               |/        ( )
               |          |
               |         /
               |
            """,
        2: """
                ___________
               | /        |
               |/        ( )
               |          |
               |
               |
            """,
        3: """
                ___________
               | /        |
               |/        ( )
               |
               |
               |
            """,
        4: """
                ___________
               | /        |
               |/
               |
               |
               |
            """,
        5: """
                ___________
               | /
               |/
               |
               |
               |
            """,
        6: """
               |
               |
               |
               |
               |
            """,
        7: "", # 🔴 seven KEYS
    }
```

<br>
<br>

## 🌈 Solution

### Adjust lives to Match Dictionary Keys:

- if you have something else in your code like `lives = 20` , change it to: `lives = 7`

```python
    #14
    lives = 7 # 🔴 seven keys


```

<br>
<br>

### 🟣 Test it

- Run your code: `python main.py`


### output


```bash
Current word: A _ _
GUESS A LETTER: r
Letter is not in word

Your letter, R is not in the word.
You have 6 lives left and you have used these letters:  A R

               |
               |
               |
               |
               |

Current word: A _ _
GUESS A LETTER: t
Letter is not in word

Your letter, T is not in the word.
You have 5 lives left and you have used these letters:  A T R

                ___________
               | /
               |/
               |
               |
               |

Current word: A _ _
GUESS A LETTER: z
Letter is not in word

Your letter, Z is not in the word.
You have 4 lives left and you have used these letters:  A T Z R

                ___________
               | /        |
               |/
               |
               |
               |

Current word: A _ _
GUESS A LETTER: u
Letter is not in word

Your letter, U is not in the word.
You have 3 lives left and you have used these letters:  A Z R U T

                ___________
               | /        |
               |/        ( )
               |
               |
               |

Current word: A _ _
GUESS A LETTER: i
Letter is not in word

Your letter, I is not in the word.
You have 2 lives left and you have used these letters:  A Z I R U T

                ___________
               | /        |
               |/        ( )
               |          |
               |
               |

Current word: A _ _
GUESS A LETTER: m
Letter is not in word

Your letter, M is not in the word.
You have 1 lives left and you have used these letters:  A Z I R U M T

                ___________
               | /        |
               |/        ( )
               |          |
               |         /
               |

Current word: A _ _
GUESS A LETTER: f
Letter is not in word

Your letter, F is not in the word.

                ___________
               | /        |
               |/        ( )
               |          |
               |         / \
               |

__💀__YOU Died. The word was ASK
```


<br>
<br>

### I will keep the clean version of this code on the main.py

```python
#
# intro: imports
# import the random, string, and file containing the list of words
import random

# when importing data from other files, keep in mind that the file type, is important
# because at the end of the first phase of this hangman exercise, i couldnt get the result i wanted  (no matter what word i used, it simply didnt get any word from the file of words), and was because the importing, i had this: "from file_withwords import words" and this file_withwords came from the file_withwords.py, so i ad the choice to either use the long name, or change the name to simply words, so to import it like "words" like here below(that is what i did)
from words import words
from hangman_visual import lives_visual_dict
import string


#  1
# create the function to grab the words from the list
def function_1_(words):

#   1.a grab the data coming from the 'words'
## Pick a random word from the list

    word = random.choice(words)

    # 1.b loop: add the condition in which you tell it:
    ## If the word has underscores or spaces...

    while "_" in word or " " in words:

        # 1.c # ... Pick a new word
        word = random.choice(words)


    # 1.d # Give back the chosen word

    # return word
    return word.upper() #🔴  if the chosen word is not **converted to uppercase**, your lowercase inputs will not match

#------------
#  2)  create the function to init the hangman game
def function_2_hangman():

    #1 make the connection to the first function
    word =  function_1_(words)

    #2 TAKES the 'word' and turns it into a special list where each letter is only listed

    word_letters = set(word)
    #3 This line creates a list of all the letters in the alphabet, from A to Z. It’s like having a list of all the letters you can use to guess the secret word.
    alphabet = set(string.ascii_uppercase)
    # 4 This line starts with an empty list where you can keep track of the letters you’ve already guessed. At first, it’s empty because you haven’t guessed any letters yet.
    used_letters = set()

    #14 This line "sets up" a "variable" named "lives" to "keep track" of "how many attempts" the "player has left".
    lives = 7
    # lives = 0 test it
    #
    #
    # 10 while the  length of word_letters list/array is greater `>` than zero, I am going to keep iterating
    # while len(word_letters) > 0:
    # 17 - the game will keep going as long as there are letters left to guess and you still have lives remaining.
    while len(word_letters) > 0 and lives > 0:
        # The game continues only if both conditions are true at the same time.


        #
        # 11 `.join` will turn the list into a **string**, separated by whatever the string is `you can add , white spaces, etc...`
        # print("You have used these letters: ", ' '.join(used_letters))
        #
        # 16 Shows Remaining Lives: It tells you how many lives (or chances) you have left.
        print('You have', lives,  'lives left and you have used these letters: ', ' '.join(used_letters))

        # -12 The code generates a new list, word_list,
        # - where each character in word is checked to see if it’s present in the collection used_letters.
        word_list = [letter if letter in used_letters else "_" for letter in word]
        # If the letter is in used_letters, it is included as-is in word_list, ELSE...
        # If the letter is not in used_letters, an underscore ("_") is included in its place.


        # 19 hangman VISUAL
        print(lives_visual_dict[lives])

        # 13 Now I am going to get this "new WORD list" and I am going to `.join()` it again(like i did it previously)
        print("Current word:", ' '.join(word_list))
        # This part converts the word_list from a list of characters into a single string with each character separated by a space. For example, if word_list is ['h', 'e', 'l', 'l', '_'], " ".join(word_list) will produce "h e l l _"


        # 5 add var, (this var will be the letter the user will type) and assign message input to "guess a letter:" , to uppercase()
        user_letters = input("GUESS A LETTER: " ).upper()

        # 6) Check if the user letter is 'in' the alphabet, and hasnt - ' been used yet (used_letters)
        if user_letters in alphabet - used_letters:
            # 7) to the set of used letters '.add' the ( the user letter)
            used_letters.add(user_letters)
            ## 8 If the user_letters is 'in' the word letters...
            if user_letters in word_letters:
                # 9 to the set of word_letters, remove( the user_letters)
                word_letters.remove(user_letters)


            # 15
            else:
                lives = lives - 1 # Takes away a life if wrong
                #This line of code subtracts 1 from the lives variable whenever the player makes an incorrect guess. It effectively reduces the number of remaining attempts.
                print("Letter is not in word")
                print('\nYour letter,', user_letters, 'is not in the word.')



        elif user_letters in used_letters:
            print("You have already used that character. Please try again")

        else:
            print("Invalid character. Please try again")



    # ____ 🟦  KEEP iterating until they find - all the letters



    # 18 Show the failure or succes messages
    if lives == 0:
        # 20 hangman VISUAL
        print(lives_visual_dict[lives])
        print("__💀__YOU Died. The word was", word )

    else:
        print("You Guessed the word🌈 ", word, "!!")



# ---- END ----
# user_input = input("Type Something: ")
# print(user_input)

if __name__ == '__main__':
    #
    # call the function with the condition logic
    function_2_hangman()

```